#!/usr/bin/env python3
"""Check a TeX/PDF deliverable copied from cloud Agent Outputs.

- Verify every simple relative \input, \include and \includegraphics dependency.
- Reject references outside the bundle: a PDF is not sufficient if .tex cannot
  be compiled after downloading the files.
- Optionally compile with latexmk, choosing XeLaTeX for ctexart and PDFLaTeX
  for plain article. Compilation always runs from a scratch copy.
- Verify the PDF header and nonempty content.

Usage:
  python scripts/check_tex_bundle.py /path/to/AgentOutputs/LectureNotes.tex --compile

Requires only Python stdlib for dependency validation. --compile requires
latexmk and the appropriate TeX packages. Handles simple, literal paths only:
complex \graphicspath, TeX macro expansion, imported subfiles, or shell-escape
workflows require manual/TeX-engine validation.
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
EXTENSIONS = {"input": (".tex",), "include": (".tex",), "includegraphics": (".pdf", ".png", ".jpg", ".jpeg", ".eps")}


def missing_dependencies(tex: Path) -> list[str]:
    """Return missing, outside-bundle, or unresolvable simple TeX dependencies."""
    root = tex.parent.resolve()
    source = tex.read_text(encoding="utf-8")
    errors: list[str] = []
    for line_number, line in enumerate(source.splitlines(), 1):
        # Skip full-line comments and comments following a non-escaped %.
        active = re.split(r"(?<!\\)%", line, maxsplit=1)[0]
        for match in DEP_RE.finditer(active):
            cmd, raw = match.groups()
            for token in raw.split(","):
                name = token.strip()
                if not name or "\\" in name or "#" in name:
                    errors.append(f"line {line_number}: dynamic {cmd} reference {name!r}; manual check required")
                    continue
                ref = Path(name)
                candidate = root / ref
                attempts = [candidate] if ref.suffix else [candidate.with_suffix(ext) for ext in EXTENSIONS[cmd]]
                if not all(p.resolve().is_relative_to(root) for p in attempts):
                    errors.append(f"line {line_number}: {cmd} path outside deliverable bundle: {name}")
                elif not any(p.is_file() for p in attempts):
                    errors.append(f"line {line_number}: missing {cmd} dependency: {name}")
    return errors


def is_pdf(path: Path) -> bool:
    return path.is_file() and path.stat().st_size > 1024 and path.open("rb").read(5) == b"%PDF-"


def choose_engine(source: str) -> str:
    # A Chinese-character TeX document should not silently compile with PDFLaTeX.
    if re.search(r"\\documentclass(?:\[[^]]+\])?\{ctexart\}", source) or re.search(r"[\u3400-\u9fff]", source):
        return "-xelatex"
    return "-pdf"


def compile_in_scratch(tex: Path) -> tuple[bool, str]:
    exe = shutil.which("latexmk")
    if not exe:
        return False, "latexmk not installed"
    source = tex.read_text(encoding="utf-8")
    engine = choose_engine(source)
    with tempfile.TemporaryDirectory(prefix="econ-tex-check-") as temp:
        destination = Path(temp)
        shutil.copytree(tex.parent, destination / "bundle", dirs_exist_ok=True)
        run_dir = destination / "bundle"
        target = run_dir / tex.name
        cmd = [exe, engine, "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", tex.name]
        try:
            result = subprocess.run(cmd, cwd=run_dir, capture_output=True, text=True, timeout=120, check=False)
        except (subprocess.TimeoutExpired, OSError) as exc:
            return False, str(exc)
        compiled = run_dir / (tex.stem + ".pdf")
        if result.returncode != 0 or not is_pdf(compiled):
            return False, (result.stdout + "\n" + result.stderr)[-3500:]
        return True, "scratch compilation OK (" + ("XeLaTeX" if engine == "-xelatex" else "PDFLaTeX") + ")"


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
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("tex", type=Path, help="TeX file downloaded along with its figures and matching PDF")
    p.add_argument("--compile", action="store_true", help="compile a fresh copy in a temporary directory")
    args = p.parse_args()
    errors = validate(args.tex, args.compile)
    if errors:
        for error in errors:
            print("FAIL:", error, file=sys.stderr)
        return 1
    print("PASS: matched TeX/PDF and accessible relative dependencies")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
