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

URL_RE = re.compile(re.escape(le.RAW_BASE) + r"/(?:skills|link)/[^\s)`]+")
ANY_LINK_RE = re.compile(r"\]\(([^)\s]+)")


class LinkEditionTests(unittest.TestCase):
    def test_committed_link_editions_match_the_skills(self):
        generated = le.generated_pages()
        self.assertEqual(set((ROOT / "link").rglob("*.md")), set(generated))
        for target, text in generated.items():
            with self.subTest(page=target.relative_to(ROOT)):
                self.assertEqual(target.read_text(encoding="utf-8"), text)

    def test_no_relative_link_is_left(self):
        for target, text in le.generated_pages().items():
            for link in ANY_LINK_RE.findall(text):
                self.assertTrue(link.startswith(("https://", "http://", "#")), f"{target}: {link}")

    def test_every_skill_address_points_to_a_real_file(self):
        for target, text in le.generated_pages().items():
            for url in URL_RE.findall(text):
                path = ROOT / url.removeprefix(le.RAW_BASE + "/")
                self.assertTrue(path.is_file(), f"{target}: {url}")

    def test_homework_links_to_its_guide_and_example_directly(self):
        page = ROOT / "link" / "econ-learn" / "tasks" / "homework-exam.md"
        text = page.read_text(encoding="utf-8")
        self.assertIn(f"{le.RAW_BASE}/link/econ-learn/guides/time-series.md", text)
        self.assertIn(f"{le.RAW_BASE}/link/econ-learn/examples/omitted-variable-homework-example.md", text)

    def test_link_reading_note_is_present(self):
        for name in le.bz.skill_names():
            text = le.render(ROOT / "skills" / name)
            self.assertIn("reading this skill from a link", text)

    def test_index_page_is_current_and_names_every_skill(self):
        names = le.bz.skill_names()
        target = ROOT / "link" / f"{le.INDEX_NAME}.md"
        self.assertTrue(target.is_file(), f"missing {target}")
        text = target.read_text(encoding="utf-8")
        self.assertEqual(text, le.render_index())
        for name in names:
            self.assertIn(f"{le.RAW_BASE}/link/{name}.md", text)
            self.assertTrue((ROOT / "link" / f"{name}.md").is_file(), name)
            # Codes appear only on the skill pages, so reporting one shows the page was opened.
            self.assertNotIn(le.edition_code(ROOT / "skills" / name), text, name)

    def test_frequent_requests_include_the_task_and_skill_in_one_page(self):
        skill = ROOT / "skills" / "econ-learn"
        index = le.render_index()
        for task in le.LEARN_TASKS:
            with self.subTest(task=task):
                source = Path("tasks") / f"{task}.md"
                bundle = le.render(skill, task)
                self.assertIn(f"{le.RAW_BASE}/link/econ-learn/{task}.md", index)
                self.assertIn(f"{le.RAW_BASE}/link/econ-learn/tasks/{task}.md", index)
                self.assertIn("](#included-task-procedure)", bundle)
                self.assertIn("## How to teach", bundle)
                self.assertIn(le.absolute_links((skill / source).read_text(), skill / source, skill), bundle)
                self.assertIn(f"Edition code: `{le.edition_code(skill)}`", bundle)

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
