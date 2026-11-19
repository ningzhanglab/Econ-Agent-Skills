#!/usr/bin/env python3
"""Save one figure from a PDF page as a PNG, for use on a slide.

Usage (from the skill's folder):
  python3 scripts/crop_figure.py paper.pdf 14 --out figures/page14.png
      renders the whole page, so you can look at it and choose the box
  python3 scripts/crop_figure.py paper.pdf 14 --box 0.08 0.12 0.92 0.55 --out figures/fig5.png
      saves only the box: left, top, right, bottom as fractions of the page
      width and height, measured from the top-left corner

The saved image holds only the cropped area. Trimming a PDF page inside TeX
(`\\includegraphics[trim=..., clip]`) hides the rest of the page but still
embeds all of it, so its text can be selected and copied from the slide.

Rendering uses PyMuPDF (`import fitz`) when it is installed, otherwise
`pdftoppm` and `pdfinfo` from Poppler. With neither, the script says so and
exits with status 2. It only reads the PDF and writes the one output file.
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path


def parse_box(values: list[float] | None) -> tuple[float, float, float, float]:
    """The crop box as fractions of the page; the whole page when none is given."""
    if values is None:
        return (0.0, 0.0, 1.0, 1.0)
    x0, y0, x1, y1 = values
    if not (0 <= x0 < x1 <= 1 and 0 <= y0 < y1 <= 1):
        raise ValueError("--box needs 0 <= left < right <= 1 and 0 <= top < bottom <= 1")
    return (x0, y0, x1, y1)


def pixel_window(box, width_pt: float, height_pt: float, dpi: int) -> tuple[int, int, int, int]:
    """Left, top, width and height in pixels of the box on a page rendered at dpi."""
    scale = dpi / 72.0
    left = round(box[0] * width_pt * scale)
    top = round(box[1] * height_pt * scale)
    right = round(box[2] * width_pt * scale)
    bottom = round(box[3] * height_pt * scale)
    return left, top, max(1, right - left), max(1, bottom - top)


def page_size_from_pdfinfo(text: str, page: int) -> tuple[float, float]:
    """Width and height in points of one page, from `pdfinfo -f N -l N` output."""
    match = re.search(rf"Page\s+{page}\s+size:\s*([\d.]+)\s*x\s*([\d.]+)", text)
    if not match:
        raise ValueError(f"pdfinfo did not report the size of page {page}")
    width, height = float(match.group(1)), float(match.group(2))
    rotated = re.search(rf"Page\s+{page}\s+rot:\s*(\d+)", text)
    if rotated and int(rotated.group(1)) % 180 == 90:
        width, height = height, width
    return width, height


def crop_with_pymupdf(pdf: Path, page: int, box, dpi: int, out: Path) -> tuple[int, int]:
    import fitz  # PyMuPDF

    with fitz.open(pdf) as doc:
        if not 1 <= page <= doc.page_count:
            raise ValueError(f"page {page} is outside 1-{doc.page_count}")
        pg = doc[page - 1]
        r = pg.rect
        clip = fitz.Rect(r.x0 + box[0] * r.width, r.y0 + box[1] * r.height,
                         r.x0 + box[2] * r.width, r.y0 + box[3] * r.height)
        pix = pg.get_pixmap(dpi=dpi, clip=clip)
        pix.save(str(out))
        return pix.width, pix.height


def crop_with_poppler(pdf: Path, page: int, box, dpi: int, out: Path) -> tuple[int, int]:
    info = subprocess.run(["pdfinfo", "-f", str(page), "-l", str(page), str(pdf)],
                          capture_output=True, text=True)
    if info.returncode != 0:
        raise ValueError(info.stderr.strip() or "pdfinfo could not read the PDF")
    width_pt, height_pt = page_size_from_pdfinfo(info.stdout, page)
    x, y, w, h = pixel_window(box, width_pt, height_pt, dpi)
    stem = out.with_suffix("")
    command = ["pdftoppm", "-cropbox", "-f", str(page), "-l", str(page), "-r", str(dpi),
               "-x", str(x), "-y", str(y), "-W", str(w), "-H", str(h),
               "-png", "-singlefile", str(pdf), str(stem)]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        raise ValueError(result.stderr.strip() or "pdftoppm failed")
    written = stem.parent / f"{stem.name}.png"
    if written != out:
        written.replace(out)
    return w, h


def choose_backend():
    try:
        import fitz  # noqa: F401
        return crop_with_pymupdf
    except ImportError:
        pass
    if shutil.which("pdftoppm") and shutil.which("pdfinfo"):
        return crop_with_poppler
    return None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Save one figure from a PDF page as a PNG.")
    parser.add_argument("pdf", type=Path)
    parser.add_argument("page", type=int, help="page number, starting at 1")
    parser.add_argument("--box", type=float, nargs=4, metavar=("LEFT", "TOP", "RIGHT", "BOTTOM"),
                        help="crop box as fractions of the page, from the top-left corner")
    parser.add_argument("--dpi", type=int, default=200)
    parser.add_argument("--out", type=Path, required=True, help="output .png path")
    args = parser.parse_args(argv)

    try:
        box = parse_box(args.box)
    except ValueError as error:
        parser.error(str(error))
    if args.out.suffix.lower() != ".png":
        parser.error("--out must end in .png")
    if not args.pdf.is_file():
        print(f"FAIL: {args.pdf} not found")
        return 1

    backend = choose_backend()
    if backend is None:
        print("FAIL: no PDF renderer. Install PyMuPDF (pip install pymupdf) or Poppler "
              "(pdftoppm and pdfinfo), or crop the figure by hand and say so in the handover.")
        return 2

    args.out.parent.mkdir(parents=True, exist_ok=True)
    try:
        width, height = backend(args.pdf, args.page, box, args.dpi, args.out)
    except ValueError as error:
        print(f"FAIL: {error}")
        return 1
    print(f"Saved {args.out} ({width} x {height} px). Open it and check that every panel "
          "is whole and no neighbouring text or panel label is left in.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
