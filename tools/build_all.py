#!/usr/bin/env python3
"""Run every generator in order: shared text first, then the link editions.

Usage:
  python tools/build_all.py           # write
  python tools/build_all.py --check   # fail if anything is out of date

The link editions carry a hash of each skill's files, so they must be built
after the shared copies. New files must be `git add`ed first: only files Git
tracks are part of a skill.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_link_editions  # noqa: E402
import sync_shared  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    status = sync_shared.main(args)
    return build_link_editions.main(args) or status


if __name__ == "__main__":
    sys.exit(main())
