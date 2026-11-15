"""Offline checks for the link editions used by the paste-a-link method."""
import importlib.util
import re
import tempfile
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

    def test_index_page_is_current_and_names_every_skill(self):
        # If this fails after editing a skill description: python tools/build_link_editions.py
        names = le.bz.skill_names()
        target = ROOT / "link" / f"{le.INDEX_NAME}.md"
        self.assertTrue(target.is_file(), f"missing {target}")
        text = target.read_text(encoding="utf-8")
        self.assertEqual(text, le.render_index(names))
        for name in names:
            self.assertIn(f"{le.RAW_BASE}/link/{name}.md", text)
            self.assertTrue((ROOT / "link" / f"{name}.md").is_file(), name)
            self.assertIn(le.skill_description(ROOT / "skills" / name), text)
            # Codes appear only on the skill pages, so reporting one shows the page was opened.
            self.assertNotIn(le.edition_code(ROOT / "skills" / name), text, name)

    def test_edition_code_is_shown_and_follows_every_file(self):
        for name in le.bz.skill_names():
            code = le.edition_code(ROOT / "skills" / name)
            self.assertRegex(code, r"^[0-9a-f]{6}$")
            text = le.render(ROOT / "skills" / name)
            self.assertIn(f"Edition code: `{code}`", text)
            self.assertIn(f"Skill edition: {code}", text)
        with tempfile.TemporaryDirectory() as tmp:
            skill = Path(tmp) / "demo-skill"
            (skill / "references").mkdir(parents=True)
            (skill / "SKILL.md").write_text("---\nname: demo-skill\n---\nBody\n", encoding="utf-8")
            ref = skill / "references" / "a.md"
            ref.write_text("one\n", encoding="utf-8")
            first = le.edition_code(skill)
            self.assertEqual(first, le.edition_code(skill))
            ref.write_text("two\n", encoding="utf-8")
            self.assertNotEqual(first, le.edition_code(skill))


if __name__ == "__main__":
    unittest.main()
