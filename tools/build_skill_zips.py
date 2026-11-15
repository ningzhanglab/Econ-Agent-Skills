#!/usr/bin/env python3
"""Build one installable zip per skill, for sharing a single skill.

Usage:
  python tools/build_skill_zips.py [--out dist] [--skill econ-teaching ...]

Each zip holds only that skill's folder at its top level
(econ-teaching.zip -> econ-teaching/SKILL.md, econ-teaching/references/...),
which is the layout Claude.ai skill upload and skills folders expect.
Repository maintenance files (logs, tests, CHANGELOG) are never included.
Local junk such as .DS_Store, __pycache__ and LaTeX build files is skipped.

Standard library only. Read-only on skills/; writes only into --out.
"""
from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"

SKIP_NAMES = {".DS_Store", "__pycache__", "Thumbs.db"}
SKIP_SUFFIXES = {".pyc", ".pyo", ".aux", ".log", ".fls", ".fdb_latexmk", ".out", ".synctex.gz"}
FIXED_TIME = (2020, 1, 1, 0, 0, 0)  # fixed timestamps make the zip reproducible


def skill_names(skills_dir: Path = SKILLS) -> list[str]:
    return sorted(p.name for p in skills_dir.iterdir() if (p / "SKILL.md").is_file())


def included_files(skill_dir: Path) -> list[Path]:
    files = []
    for path in sorted(skill_dir.rglob("*")):
        rel = path.relative_to(skill_dir)
        if any(part in SKIP_NAMES for part in rel.parts):
            continue
        if path.is_symlink() or not path.is_file():
            continue
        if any(path.name.endswith(s) for s in SKIP_SUFFIXES):
            continue
        files.append(path)
    return files


def build_zip(skill_dir: Path, out_dir: Path) -> Path:
    if not (skill_dir / "SKILL.md").is_file():
        raise ValueError(f"{skill_dir} has no SKILL.md")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / f"{skill_dir.name}.zip"
    with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in included_files(skill_dir):
            arcname = f"{skill_dir.name}/{path.relative_to(skill_dir).as_posix()}"
            info = zipfile.ZipInfo(arcname, date_time=FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zf.writestr(info, path.read_bytes())
    return target


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--out", default=str(ROOT / "dist"), help="output folder (default: dist/)")
    parser.add_argument("--skill", action="append", help="skill folder name; repeat for several (default: all)")
    args = parser.parse_args(argv)

    available = skill_names()
    wanted = args.skill or available
    unknown = [s for s in wanted if s not in available]
    if unknown:
        print(f"ERROR: unknown skill(s): {', '.join(unknown)}; available: {', '.join(available)}")
        return 1
    for name in wanted:
        target = build_zip(SKILLS / name, Path(args.out))
        with zipfile.ZipFile(target) as zf:
            count = len(zf.namelist())
        print(f"OK: {target} ({count} files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
