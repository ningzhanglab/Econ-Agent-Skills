#!/usr/bin/env python3
r"""Locate TeX lecture figure references; do not claim visual inspection.

Usage: python skills/econ-phd-professor/scripts/inventory_tex_figures.py lecture.tex [--output index.json]
Handles simple literal includegraphics/input/include references relative to main
TeX folder. For complex macros/graphicspath, manual or rendered-PDF review is
required. Does not access Drive, inspect graph pixels, or reconstruct figures.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

COMMANDS = re.compile(
    r"\\(?P<kind>includegraphics|input|include|section|subsection|frametitle)"
    r"(?:\s*\[[^\]]*\])?\s*\{(?P<name>[^{}]+)\}"
)
IMAGE_EXT = (".pdf", ".png", ".jpg", ".jpeg", ".eps", ".svg")


def inventory(tex: Path) -> dict:
    tex = tex.resolve()
    if tex.suffix.lower() != ".tex" or not tex.is_file():
        raise ValueError("expected an existing TeX file")
    root = tex.parent
    visited: set[Path] = set()
    figures: list[dict] = []
    warnings: list[str] = []

    def resolve(name: str, extensions: tuple[str, ...]) -> tuple[str, Path | None]:
        if any(c in name for c in ("\\", "#", "~")):
            return "DYNAMIC_REFERENCE", None
        candidate = root / name
        choices = [candidate] if candidate.suffix else [
            candidate.with_suffix(ext) for ext in extensions
        ]
        if not all(p.resolve().is_relative_to(root) for p in choices):
            return "OUTSIDE_SOURCE_FOLDER", None
        found = next((p.resolve() for p in choices if p.is_file()), None)
        return ("ASSET_LOCATED_NOT_VISUALLY_REVIEWED", found) if found else (
            "ASSET_NOT_FOUND", None
        )

    def scan(path: Path, section: str = "") -> None:
        path = path.resolve()
        if path in visited:
            return
        visited.add(path)
        rel = str(path.relative_to(root))
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except (UnicodeError, OSError) as exc:
            warnings.append(f"{rel}: cannot read TeX: {exc}")
            return
        for lineno, line in enumerate(lines, 1):
            active = re.split(r"(?<!\\)%", line, maxsplit=1)[0]
            if r"\graphicspath" in active:
                warnings.append(f"{rel}:{lineno}: graphicspath requires manual lookup")
            for m in COMMANDS.finditer(active):
                kind, name = m.group("kind"), m.group("name").strip()
                if kind in ("section", "subsection", "frametitle"):
                    section = name
                elif kind == "includegraphics":
                    status, asset = resolve(name, IMAGE_EXT)
                    figures.append({
                        "source_tex": rel, "line": lineno, "section": section,
                        "reference": name,
                        "asset": str(asset.relative_to(root)) if asset else None,
                        "asset_status": status,
                        "visually_inspected": False,
                        "rendered_pdf_page_reviewed": None,
                    })
                else:
                    status, target = resolve(name, (".tex",))
                    if target is None:
                        warnings.append(f"{rel}:{lineno}: {kind} {name}: {status}")
                    else:
                        scan(target, section)
            if r"\begin{tikzpicture}" in active or r"\begin{axis}" in active:
                figures.append({
                    "source_tex": rel, "line": lineno, "section": section,
                    "reference": "inline TikZ/PGFPlots", "asset": None,
                    "asset_status": "INLINE_FIGURE_NOT_VISUALLY_REVIEWED",
                    "visually_inspected": False,
                    "rendered_pdf_page_reviewed": None,
                })

    scan(tex)
    return {
        "main_tex": tex.name, "source_files": sorted(str(p.relative_to(root)) for p in visited),
        "figure_references": figures, "warnings": warnings,
        "note": "References are NOT inspected figures. Open an actual image or matching rendered PDF page before describing graph content.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tex", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    output = json.dumps(inventory(args.tex), ensure_ascii=False, indent=2) + "\n"
    if args.output is not None:
        args.output.write_text(output, encoding="utf-8")
    else:
        print(output, end="")


if __name__ == "__main__":
    main()
