"""Verify active repository Markdown links, not only SKILL.md references.

Historical dated logs are intentionally excluded because they are append-only
records. External HTTP(S) links aren't network-checked in this test.
"""
from __future__ import annotations

import re
import unittest
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def active_docs():
    paths = [
        ROOT / "README.md",
        ROOT / "AGENTS.md",
        ROOT / "STORAGE_POLICY.md",
        ROOT / "CHANGELOG.md",
        ROOT / "logs/README.md",
        ROOT / "tests/professor-evaluation.md",
    ]
    paths.extend((ROOT / "skills").rglob("*.md"))
    return paths


class ActiveMarkdownLinkTests(unittest.TestCase):
    def test_all_local_links_have_real_targets(self):
        for file in active_docs():
            self.assertTrue(file.is_file(), f"missing required doc: {file}")
            text = file.read_text(encoding="utf-8")
            for match in MARKDOWN_LINK.finditer(text):
                url = match.group(1).split("#", 1)[0].strip()
                if not url or url.startswith(("https://", "http://", "mailto:")):
                    continue
                target = (file.parent / unquote(url)).resolve()
                with self.subTest(source=file.relative_to(ROOT), target=url):
                    self.assertTrue(target.is_relative_to(ROOT),
                                    f"link escapes repository: {url}")
                    self.assertTrue(target.exists(), f"missing target: {url}")


if __name__ == "__main__":
    unittest.main()
