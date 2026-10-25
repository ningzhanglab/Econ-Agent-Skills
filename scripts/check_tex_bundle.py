#!/usr/bin/env python3
r"""Validate a downloaded TeX/PDF bundle.

Check all *static* \input, \include and \includegraphics dependencies, including
nested TeX inputs. Distinguish binary image/PDF assets from readable .tex files.
Optionally compile an isolated copy containing only required source/assets.

Usage:
  python scripts/check_tex_bundle.py "/path/Agent Outputs/Notes.tex" --compile

Stdlib only for dependency checking; --compile needs latexmk and TeX packages.
This is a conservative check: dynamic TeX macros, \graphicspath, external
bibliographies, custom classes and shell escape require independent verification.
It does not interact with Google Drive or prove visual/economic accuracy.
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

DEP_RE = re.compile(r"\\(input|include|includegraphics)(?:\s*\[[^\]]*\])?\s*\{([^{}]+)\}")
EXTENSIONS = {
    "input": (".tex",),
    "include": (".tex",),
    "includegraphics": (".pdf", ".png", ".jpg", ".jpeg", ".eps"),
}
UNSUPPORTED_RE = re.compile(r"\\(?:graphicspath|bibliography|addbibresource)\b")


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

        for line_number, active in _active_lines(source):
            if UNSUPPORTED_RE.search(active):
                errors.append(
                    f"{current.name}:{line_number}: unsupported dynamic bibliography/"
                    "graphicspath; manually verify the complete bundle"
                )
            for match in DEP_RE.finditer(active):
                command, name = match.groups()
                names = [part.strip() for part in name.split(",")]
                for part in names:
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
                    # Crucial: binary .pdf/.png/.jpg/.eps assets must NOT be decoded as TeX.
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


def choose_engine(source: str) -> str:
    # Never silently compile Chinese prose using a plain PDFLaTeX configuration.
    if re.search(r"\\documentclass(?:\[[^]]+\])?\{ctexart\}", source) or re.search(r"[\u3400-\u9fff]", source):
        return "-xelatex"
    return "-pdf"


def compile_in_scratch(tex: Path) -> tuple[bool, str]:
    exe = shutil.which("latexmk")
    if not exe:
        return False, "latexmk not installed"
    problems, included = _resolve_dependencies(tex)
    if problems:
        return False, "; ".join(problems)
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
        except (subprocess.TimeoutExpired, OSError) as exc:
            return False, str(exc)
        compiled = run_dir / (tex.stem + ".pdf")
        if result.returncode != 0 or not is_pdf(compiled):
            return False, (result.stdout + "\n" + result.stderr)[-3500:]
        label = "XeLaTeX" if engine == "-xelatex" else "PDFLaTeX"
        return True, f"scratch compilation OK ({label})"


def validate(tex: Path, compile_requested: bool = False) -> list[str]:
    if not tex.is_file() or tex.suffix.lower() != ".tex":
        return [f"TeX source not found: {tex}"]
    errors = missing_dependencies(tex)
    pdf = tex.with_suffix(".pdf")
    if not is_pdf(pdf):
        errors.append(f"matching compiled PDF not found or invalid: {pdf.name}")
    if not errors and compile_requested:
        ok, message = compile_in_scratch(tex)
        if not ok:
            errors.append("scratch compile failed: " + message)
        else:
            print(message)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tex", type=Path, help="TeX file downloaded along with its figures and matching PDF")
    parser.add_argument("--compile", action="store_true", help="compile a fresh copy in a temporary directory")
    args = parser.parse_args()
    errors = validate(args.tex, args.compile)
    if errors:
        for error in errors:
            print("FAIL:", error, file=sys.stderr)
        return 1
    suffix = " and scratch compilation" if args.compile else ""
    print(f"PASS: TeX/PDF pair, static nested dependencies{suffix}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
