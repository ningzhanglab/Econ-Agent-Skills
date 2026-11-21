#!/usr/bin/env python3
"""Rebuild the generated files, then run every repository check in order.

Usage:
  python3 tools/check_all.py          # rebuild, validate, unit tests, git diff --check
  python3 tools/check_all.py --check  # same, but fail instead of rewriting stale copies (CI)

Each step's outcome is printed; the exit status is nonzero if any step failed.
Standard library only.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def steps(check_only: bool) -> list[tuple[str, list[str]]]:
    build = [sys.executable, "tools/build_all.py"] + (["--check"] if check_only else [])
    return [
        ("build generated files" if not check_only else "generated files up to date", build),
        ("structural validation", [sys.executable, "tests/validate_skills.py"]),
        ("unit tests", [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-q"]),
        ("whitespace", ["git", "diff", "--check"]),
    ]


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    check_only = "--check" in args
    failed = []
    for name, cmd in steps(check_only):
        result = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
        ok = result.returncode == 0
        print(f"{'PASS' if ok else 'FAIL'}  {name}")
        if not ok:
            failed.append(name)
            print((result.stdout + result.stderr).rstrip()[-4000:])
    print("All checks passed." if not failed else f"Failed: {', '.join(failed)}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
