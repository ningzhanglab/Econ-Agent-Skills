#!/usr/bin/env python3
"""Copy the text every skill shares from shared/ into the skill folders.

Usage:
  python tools/sync_shared.py           # write the copies
  python tools/sync_shared.py --check   # fail if a copy is out of date

A skill must work when its folder is installed alone, so it cannot link to a
file outside itself. Text that several skills need is therefore written once
in shared/ and copied in:

- whole files (FILES): the copy is byte-for-byte the shared file;
- blocks (BLOCKS): the text between `<!-- shared:NAME -->` and
  `<!-- /shared:NAME -->` in every SKILL.md is replaced by shared/NAME.md.

Edit the file in shared/, never the copy, then run this and
tools/build_link_editions.py (or tools/build_all.py for both).

Standard library only. Reads shared/; writes only the listed copies.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHARED = ROOT / "shared"
SKILLS = ROOT / "skills"

FILES = {
    "deliver-file.md": ["econ-learn/tasks/deliver-file.md", "econ-present/tasks/deliver-file.md"],
    "scripts/check_tex_bundle.py": ["econ-learn/scripts/check_tex_bundle.py", "econ-present/scripts/check_tex_bundle.py"],
    "templates/simple-handout.tex": [
        "econ-learn/templates/simple-notes.tex",
        "econ-present/templates/simple-handout.tex",
        "econ-write/templates/simple-report.tex",
    ],
}
BLOCKS = ("guarantees", "defaults")


def block_re(name: str) -> re.Pattern:
    return re.compile(rf"(<!-- shared:{name} -->\n).*?(<!-- /shared:{name} -->)", re.S)


def with_blocks(text: str) -> str:
    for name in BLOCKS:
        body = (SHARED / f"{name}.md").read_text(encoding="utf-8").strip("\n")
        text = block_re(name).sub(lambda m, body=body: f"{m.group(1)}{body}\n{m.group(2)}", text)
    return text


def planned() -> list[tuple[Path, bytes]]:
    out: list[tuple[Path, bytes]] = []
    for source, targets in FILES.items():
        data = (SHARED / source).read_bytes()
        out += [(SKILLS / target, data) for target in targets]
    for skill_md in sorted(SKILLS.glob("*/SKILL.md")):
        text = skill_md.read_text(encoding="utf-8")
        for name in BLOCKS:
            if not block_re(name).search(text):
                raise ValueError(f"{skill_md.relative_to(ROOT)} has no shared:{name} block")
        out.append((skill_md, with_blocks(text).encode("utf-8")))
    return out


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="do not write; fail if a copy is out of date")
    args = parser.parse_args(argv)
    stale = 0
    for target, wanted in planned():
        rel = target.relative_to(ROOT)
        if target.is_file() and target.read_bytes() == wanted:
            continue
        if args.check:
            stale += 1
            print(f"ERROR: {rel} differs from shared/; run python tools/sync_shared.py")
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(wanted)
            print(f"WROTE: {rel}")
    if not stale:
        print("OK: shared text is in sync")
    return 1 if stale else 0


if __name__ == "__main__":
    sys.exit(main())
