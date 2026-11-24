#!/usr/bin/env python3
r"""Validate a downloaded TeX/PDF bundle.

Check all *static* \input, \include and \includegraphics dependencies, including
nested TeX inputs. Distinguish binary image/PDF assets from readable .tex files.
Optionally rebuild from an isolated copy. Compare the supplied PDF with that
build's rendered pages, or write the fresh PDF beside the source. To verify a
download of a checked bundle, compare the files by SHA-256 without rebuilding.

Usage (from the skill's folder):
  python3 scripts/check_tex_bundle.py "/path/Agent Outputs/Notes.tex" --compile
  python3 scripts/check_tex_bundle.py "/path/Agent Outputs/Notes.tex" --build-pdf
  python3 scripts/check_tex_bundle.py "/path/Agent Outputs/Notes.tex" --verify-copy /path/download

Rebuilding needs latexmk and TeX packages. Page comparison uses Poppler's
pdftoppm when PDF bytes differ; it checks appearance, not interactive links.
This is a conservative check: dynamic TeX macros, \graphicspath, external
bibliographies, custom classes and shell escape require independent verification.
It does not interact with Google Drive or prove visual/economic accuracy.

For a Beamer deck with a "<name>_content.md" beside it, also check that the
Markdown has one "## Slide N: Title" section per frame, numbered 1..n, with
titles in the same order. Body text is not compared.
"""
from __future__ import annotations

import argparse
import filecmp
import hashlib
import re
import shutil
import subprocess
import sys
import tempfile
from bisect import bisect_right
from pathlib import Path

DEP_RE = re.compile(
    r"\\(?:(?P<command>input|include|includegraphics\*?)(?:\s*\[[^\]]*\])?\s*\{(?P<braced>[^{}]+)\}"
    r"|input\s+(?P<unbraced>[^\s{}\\]+))"
)
EXTENSIONS = {
    "input": (".tex",),
    "include": (".tex",),
    "includegraphics": (".pdf", ".png", ".jpg", ".jpeg", ".eps"),
}
UNSUPPORTED_RE = re.compile(r"\\(?:graphicspath|bibliography|addbibresource)\b")
DOCUMENT_CLASS_RE = re.compile(r"\\documentclass\s*(?:\[[^]]*\]\s*)?\{([^{}]+)\}")


def _active_lines(source: str):
    for line_number, line in enumerate(source.splitlines(), 1):
        # This intentionally handles simple comments, not a full TeX tokenizer.
        yield line_number, re.split(r"(?<!\\)%", line, maxsplit=1)[0]


def _resolve_dependencies(tex: Path) -> tuple[list[str], set[Path]]:
    root = tex.parent.resolve()
    errors: list[str] = []
    included: set[Path] = set()
    pending = [tex.resolve()]
    seen_tex: set[Path] = set()

    while pending:
        current = pending.pop()
        if current in seen_tex:
            continue
        seen_tex.add(current)
        try:
            source = current.read_text(encoding="utf-8")
        except (UnicodeError, OSError) as exc:
            errors.append(f"{current.name}: cannot read TeX source: {exc}")
            continue
        included.add(current)

        active_lines = [line for _, line in _active_lines(source)]
        for line_number, line in enumerate(active_lines, 1):
            if UNSUPPORTED_RE.search(line):
                errors.append(
                    f"{current.name}:{line_number}: unsupported dynamic bibliography/"
                    "graphicspath; manually verify the complete bundle"
                )
        active = "\n".join(active_lines)
        line_starts = [newline.end() for newline in re.finditer("\n", active)]
        for match in DEP_RE.finditer(active):
            command = (match["command"] or "input").rstrip("*")
            name = match["braced"] or match["unbraced"]
            line_number = bisect_right(line_starts, match.start()) + 1
            for part in (item.strip() for item in name.split(",")):
                if not part or any(ch in part for ch in ("\\", "#", "~")):
                    errors.append(
                        f"{current.name}:{line_number}: dynamic {command} reference "
                        f"{part!r}; manual verification required"
                    )
                    continue
                ref = Path(part)
                raw = root / ref
                choices = ([raw] if ref.suffix else
                           [raw.with_suffix(ext) for ext in EXTENSIONS[command]])
                if not all(p.resolve().is_relative_to(root) for p in choices):
                    errors.append(
                        f"{current.name}:{line_number}: {command} path outside bundle: {part}"
                    )
                    continue
                found = next((p.resolve() for p in choices if p.is_file()), None)
                if found is None:
                    errors.append(
                        f"{current.name}:{line_number}: missing {command} dependency: {part}"
                    )
                    continue
                included.add(found)
                # Binary figure assets must remain out of the source queue.
                if command in ("input", "include"):
                    pending.append(found)
    return errors, included


def missing_dependencies(tex: Path) -> list[str]:
    if not tex.is_file():
        return [f"TeX source not found: {tex}"]
    problems, _ = _resolve_dependencies(tex)
    return problems


def is_pdf(path: Path) -> bool:
    if not path.is_file() or path.stat().st_size <= 1024:
        return False
    with path.open("rb") as fh:
        return fh.read(5) == b"%PDF-"


def sha256_file(path: Path) -> bytes:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.digest()


def verify_copy(root: Path, files: set[Path], copy_dir: Path) -> list[str]:
    copy_dir = copy_dir.resolve()
    if not copy_dir.is_dir():
        return [f"downloaded bundle directory not found: {copy_dir}"]
    if copy_dir == root:
        return ["use a separate directory for the downloaded bundle"]
    errors = []
    for original in sorted(files):
        if not original.is_relative_to(root):
            errors.append(f"{original}: local file outside the bundle")
            continue
        rel = original.relative_to(root)
        downloaded = copy_dir / rel
        if not downloaded.resolve().is_relative_to(copy_dir):
            errors.append(f"{rel}: downloaded path outside the bundle")
            continue
        try:
            if not downloaded.is_file():
                errors.append(f"{rel}: missing from downloaded bundle")
            elif sha256_file(original) != sha256_file(downloaded):
                errors.append(f"{rel}: SHA-256 mismatch with downloaded copy")
        except OSError as exc:
            errors.append(f"{rel}: cannot compare files: {exc}")
    return errors


def choose_engine(source: str) -> str:
    # Never silently compile Chinese prose using a plain PDFLaTeX configuration.
    active = "\n".join(line for _, line in _active_lines(source))
    document_class = DOCUMENT_CLASS_RE.search(active)
    if document_class and document_class[1] in ("ctexart", "ctexbeamer"):
        return "-xelatex"
    if re.search(r"[\u3400-\u9fff]", active):
        return "-xelatex"
    return "-pdf"


def compare_pdf_pages(reference: Path, compiled: Path, scratch: Path) -> tuple[bool, str]:
    if filecmp.cmp(reference, compiled, shallow=False):
        return True, "supplied PDF equals the scratch build"
    renderer = shutil.which("pdftoppm")
    if not renderer:
        return False, "PDF match unchecked: install Poppler (pdftoppm) or use --build-pdf"
    pages = []
    for pdf, name in ((reference, "supplied"), (compiled, "fresh")):
        result = subprocess.run(
            [renderer, "-r", "120", "-png", str(pdf), str(scratch / name)],
            capture_output=True, text=True, timeout=120, check=False,
        )
        rendered = sorted(scratch.glob(f"{name}-*.png"))
        if result.returncode != 0 or not rendered:
            return False, f"cannot render {name} PDF: {result.stderr.strip()}"
        pages.append(rendered)
    supplied, fresh = pages
    if len(supplied) != len(fresh):
        return False, f"supplied PDF has {len(supplied)} pages, scratch build has {len(fresh)}"
    for number, (old, new) in enumerate(zip(supplied, fresh), 1):
        if not filecmp.cmp(old, new, shallow=False):
            return False, f"supplied PDF differs from the scratch build on page {number}"
    return True, f"rendered pages match the scratch build ({len(fresh)} pages)"


def compile_in_scratch(tex: Path, included: set[Path], *, reference: Path | None = None,
                       output: Path | None = None) -> tuple[bool, str]:
    exe = shutil.which("latexmk")
    if not exe:
        return False, "latexmk not installed"
    root = tex.parent.resolve()
    engine = choose_engine(tex.read_text(encoding="utf-8"))

    with tempfile.TemporaryDirectory(prefix="econ-tex-check-") as temp:
        run_dir = Path(temp) / "bundle"
        run_dir.mkdir()
        for source in included:
            rel = source.relative_to(root)
            dest = run_dir / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, dest)
        cmd = [
            exe, engine, "-interaction=nonstopmode", "-halt-on-error",
            "-file-line-error", tex.name,
        ]
        try:
            result = subprocess.run(
                cmd, cwd=run_dir, capture_output=True, text=True,
                timeout=120, check=False,
            )
            compiled = run_dir / (tex.stem + ".pdf")
            if result.returncode != 0 or not is_pdf(compiled):
                return False, (result.stdout + "\n" + result.stderr)[-3500:]
            label = "XeLaTeX" if engine == "-xelatex" else "PDFLaTeX"
            print(f"PASS: scratch compilation ({label})")
            log = compiled.with_suffix(".log")
            if log.is_file():
                for line in log.read_text(encoding="utf-8", errors="replace").splitlines():
                    if line.startswith((r"Overfull \hbox", r"Overfull \vbox")):
                        print(f"WARNING: {line}")
            if reference is not None:
                return compare_pdf_pages(reference.resolve(), compiled, Path(temp))
            if output is not None:
                # Publish only after a successful build. Stage on the same filesystem.
                with tempfile.TemporaryDirectory(prefix=".econ-pdf-", dir=output.parent) as stage:
                    ready = Path(stage) / output.name
                    shutil.copyfile(compiled, ready)
                    ready.replace(output)
                return True, f"fresh PDF written: {output}"
        except (subprocess.TimeoutExpired, OSError) as exc:
            return False, str(exc)
        return True, "scratch build completed"


FRAME_RE = re.compile(r"\\begin\{frame\}")
SLIDE_HEADING_RE = re.compile(r"^## Slide (\d+)(?::\s*(.*))?$")
UNCOUNTABLE_RE = re.compile(
    r"\\(?:AtBeginSection|AtBeginSubsection|pause|onslide|input|include)\b"
    r"|\\(?:only|uncover)\s*<|\\begin\{frame\}\s*<"
)


def _braced(text: str, start: int) -> tuple[str, int] | None:
    """Return the content of the {...} group opening at text[start], and its end."""
    if start >= len(text) or text[start] != "{":
        return None
    depth = 0
    for pos in range(start, len(text)):
        if text[pos] == "{" and (pos == 0 or text[pos - 1] != "\\"):
            depth += 1
        elif text[pos] == "}" and text[pos - 1] != "\\":
            depth -= 1
            if depth == 0:
                return text[start + 1:pos], pos + 1
    return None


def frame_titles(source: str) -> list[str | None]:
    """Titles of the frames in order; None for a frame without a title."""
    active = "\n".join(line for _, line in _active_lines(source))
    starts = [m.end() for m in FRAME_RE.finditer(active)]
    titles: list[str | None] = []
    for index, pos in enumerate(starts):
        end = starts[index + 1] if index + 1 < len(starts) else len(active)
        rest = active[pos:end]
        head = re.match(r"[ \t]*(?:<[^>]*>)?[ \t]*(?:\[[^\]]*\])?[ \t]*", rest)
        group = _braced(rest, head.end())
        if group is None:
            marker = re.search(r"\\frametitle\s*", rest)
            group = _braced(rest, marker.end()) if marker else None
        titles.append(group[0] if group else None)
    return titles


def _title_key(title: str) -> str:
    """Words of a title, ignoring math, TeX commands, punctuation and case."""
    title = re.sub(r"\$[^$]*\$", " ", title)
    title = re.sub(r"\\[A-Za-z]+", " ", title)
    return "".join(ch for ch in title.lower() if ch.isalnum())


def content_file_problems(tex: Path) -> list[str]:
    """Check "<stem>_content.md" against the frames of a Beamer deck, if it exists."""
    content = tex.with_name(tex.stem + "_content.md")
    if not content.is_file():
        return []
    try:
        source = tex.read_text(encoding="utf-8")
        markdown = content.read_text(encoding="utf-8")
    except (UnicodeError, OSError) as exc:
        return [f"{content.name}: cannot read: {exc}"]
    active = "\n".join(line for _, line in _active_lines(source))
    document_class = DOCUMENT_CLASS_RE.search(active)
    if not document_class or document_class[1] not in ("beamer", "ctexbeamer"):
        return []
    if UNCOUNTABLE_RE.search(active):
        print(f"NOTE: {content.name} not checked: the deck uses overlays, section "
              "frames or nested inputs, so frames cannot be counted from the source")
        return []
    titles = frame_titles(source)
    headings = [m.groups() for m in map(SLIDE_HEADING_RE.match, markdown.splitlines()) if m]
    numbers = [int(number) for number, _ in headings]
    if numbers != list(range(1, len(numbers) + 1)):
        return [f"{content.name}: slide sections are not numbered 1..{len(numbers)} in order"]
    if len(headings) != len(titles):
        return [f"{content.name}: {len(headings)} slide sections but {tex.name} has "
                f"{len(titles)} frames"]
    problems = []
    for number, (title, (_, heading)) in enumerate(zip(titles, headings), 1):
        if title is not None and _title_key(title) != _title_key(heading or ""):
            problems.append(f"{content.name}: Slide {number} is titled {heading!r} "
                            f"but frame {number} is {title!r}")
    return problems


def validate(tex: Path, compile_requested: bool = False, *, build_pdf: bool = False,
             copy_dir: Path | None = None) -> list[str]:
    if not tex.is_file() or tex.suffix.lower() != ".tex":
        return [f"TeX source not found: {tex}"]
    errors, included = _resolve_dependencies(tex)
    errors.extend(content_file_problems(tex))
    pdf = tex.with_suffix(".pdf")
    if not build_pdf and not is_pdf(pdf):
        errors.append(f"PDF missing or invalid: {pdf.name}")
    if errors:
        return errors
    if copy_dir is not None:
        root = tex.parent.resolve()
        files = included | {root / pdf.name}
        errors = verify_copy(root, files, copy_dir)
        if not errors:
            print(f"PASS: SHA-256 match for {len(files)} bundle files against the downloaded copy")
    elif compile_requested or build_pdf:
        ok, message = compile_in_scratch(
            tex, included, reference=pdf if compile_requested else None,
            output=pdf if build_pdf else None,
        )
        if not ok:
            errors.append(message)
        else:
            print(f"PASS: {message}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tex", type=Path, help="TeX source file beside its figures")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--compile", action="store_true", help="compare the existing PDF with a scratch build")
    mode.add_argument("--build-pdf", action="store_true", help="write or replace the sibling PDF after a successful scratch build")
    mode.add_argument("--verify-copy", type=Path, metavar="DIR",
                      help="compare a checked local bundle with its downloaded copy by SHA-256")
    args = parser.parse_args()
    errors = validate(args.tex, args.compile, build_pdf=args.build_pdf, copy_dir=args.verify_copy)
    if errors:
        for error in errors:
            print("FAIL:", error, file=sys.stderr)
        return 1
    print("PASS: static nested dependencies and PDF presence")
    if not (args.compile or args.build_pdf or args.verify_copy):
        print("NOTE: PDF content unchecked; use --compile to compare it with a fresh build")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
