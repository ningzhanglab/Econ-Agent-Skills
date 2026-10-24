#!/usr/bin/env python3
"""Validate this repository's portable Agent Skills metadata and local reference paths.

Only uses Python standard library. This is a structural check, not pedagogical QA.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)#]+)(?:#[^)]*)?\)")


def validate(skill_dir: Path) -> list[str]:
    problems: list[str] = []
    file = skill_dir / "SKILL.md"
    if not file.is_file():
        return [f"{skill_dir}: missing SKILL.md"]

    text = file.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return [f"{file}: missing YAML frontmatter"]
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return [f"{file}: unterminated YAML frontmatter"]
    frontmatter, body = parts[1], parts[2]
    fields = {}
    # Only parse simple one-line key-value metadata; complex YAML needs a YAML parser.
    for line in frontmatter.splitlines():
        if re.match(r"^[A-Za-z][A-Za-z0-9_-]*\s*:", line):
            k, v = line.split(":", 1)
            fields[k.strip()] = v.strip().strip('"').strip("'")
    name = fields.get("name", "")
    description = fields.get("description", "")
    if not name or not NAME_RE.fullmatch(name) or len(name) > 64:
        problems.append(f"{file}: invalid name")
    if name != skill_dir.name:
        problems.append(f"{file}: name must match skill folder")
    if not description or len(description) > 1024:
        problems.append(f"{file}: description missing or too long")
    if not body.strip():
        problems.append(f"{file}: empty instructions")
    for path in LINK_RE.findall(body):
        if "://" in path or path.startswith("#"):
            continue
        if not (skill_dir / path).is_file():
            problems.append(f"{file}: broken reference {path}")
    return problems


def main() -> int:
    if not SKILLS.is_dir():
        print("ERROR: missing skills directory")
        return 1
    dirs = [p for p in sorted(SKILLS.iterdir()) if p.is_dir()]
    if not dirs:
        print("ERROR: no skill folders")
        return 1
    issues = [problem for folder in dirs for problem in validate(folder)]
    for problem in issues:
        print("ERROR:", problem)
    if issues:
        return 1
    print(f"OK: {len(dirs)} skill(s) passed basic structural checks.")
    print("Note: Teaching quality, semantic correctness and PDF fidelity require manual evaluation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
