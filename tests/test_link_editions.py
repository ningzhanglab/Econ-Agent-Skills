"""Offline checks for the link editions used by the paste-a-link method."""
import importlib.util
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("build_link_editions", ROOT / "tools" / "build_link_editions.py")
le = importlib.util.module_from_spec(spec)
spec.loader.exec_module(le)

URL_RE = re.compile(re.escape(le.RAW_BASE) + r"/skills/([a-z0-9-]+)/([^\s)`]+)")
ANY_LINK_RE = re.compile(r"\]\(([^)\s]+)")


class LinkEditionTests(unittest.TestCase):
    def test_committed_link_editions_match_the_skills(self):
        # If this fails after editing a skill: python tools/build_link_editions.py
        for name in le.bz.skill_names():
            target = ROOT / "link" / f"{name}.md"
            self.assertTrue(target.is_file(), f"missing {target}")
            self.assertEqual(target.read_text(encoding="utf-8"), le.render(ROOT / "skills" / name), name)

    def test_no_relative_link_is_left(self):
        for name in le.bz.skill_names():
            text = le.render(ROOT / "skills" / name)
            for link in ANY_LINK_RE.findall(text):
                self.assertTrue(link.startswith(("https://", "http://", "#")), f"{name}: {link}")

    def test_every_skill_address_points_to_a_real_file(self):
        for name in le.bz.skill_names():
            text = le.render(ROOT / "skills" / name)
            found = URL_RE.findall(text)
            self.assertTrue(found, name)
            for skill, rel in found:
                self.assertEqual(skill, name)
                self.assertTrue((ROOT / "skills" / skill / rel).is_file(), f"{name}: {rel}")

    def test_every_linked_reference_and_every_file_is_in_the_index(self):
        for name in le.bz.skill_names():
            text = le.render(ROOT / "skills" / name)
            body, index = text.split("## File index", 1)
            indexed = {rel for _, rel in URL_RE.findall(index)}
            for _, rel in URL_RE.findall(body):
                self.assertIn(rel, indexed, f"{name}: {rel}")
            on_disk = {
                p.relative_to(ROOT / "skills" / name).as_posix()
                for p in le.bz.included_files(ROOT / "skills" / name)
            } - {"SKILL.md"}
            self.assertEqual(indexed, on_disk, name)

    def test_note_and_description_are_present(self):
        for name in le.bz.skill_names():
            text = le.render(ROOT / "skills" / name)
            self.assertIn("reading this skill from a link", text)
            self.assertIn(f"name: {name}", text)


if __name__ == "__main__":
    unittest.main()
