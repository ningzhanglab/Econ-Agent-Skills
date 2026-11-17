#!/usr/bin/env python3
"""Print every "## Defaults" section in the skills: all adjustable preferences in one view.

Usage:
  python tools/list_defaults.py

Read-only. To change a preference, edit the line in the file named above it
(for the shared lines, edit shared/defaults.md and run tools/build_all.py).
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    for doc in sorted((ROOT / "skills").rglob("*.md")):
        text = doc.read_text(encoding="utf-8")
        match = re.search(r"^## Defaults\n(.*?)(?=^## |\Z)", text, re.S | re.M)
        if not match:
            continue
        body = re.sub(r"<!-- /?shared:\w+ -->\n", "", match.group(1)).strip()
        print(f"=== {doc.relative_to(ROOT)}\n{body}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
