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

    def test_every_route_page_holds_its_files_and_fits_one_fetch(self):
        for name, _, skill_name, files in le.ROUTES:
            with self.subTest(route=name):
                skill = ROOT / "skills" / skill_name
                page = (ROOT / "link" / "route" / f"{name}.md").read_text(encoding="utf-8")
                included = {(skill / rel).resolve(): le.anchor_for(rel) for rel in ("SKILL.md", *files)}
                self.assertLessEqual(len(page.encode("utf-8")), le.ROUTE_BUDGET)
                self.assertIn(f"`Skill: {name} · {le.edition_code(skill)}`", page)
                self.assertIn("when a later message in the chat asks for another kind", page)
                self.assertIn(le.absolute_links(le.skill_body(skill), skill / "SKILL.md", skill, included), page)
                for rel in files:
                    text = (skill / rel).read_text(encoding="utf-8")
                    if rel.endswith(".md"):
                        self.assertIn(le.absolute_links(text, skill / rel, skill, included), page)
                        # A file on this page is never sent to another fetch.
                        self.assertNotIn(le.link_url(le.link_path(skill_name, Path(rel))), page)
                    else:
                        self.assertIn(text.rstrip(), page)

    def test_routes_keep_local_defaults_and_delivery_on_the_page(self):
        lecture = (ROOT / "link/route/lecture.md").read_text(encoding="utf-8")
        course = (ROOT / "link/route/course.md").read_text(encoding="utf-8")
        homework = (ROOT / "link/route/homework.md").read_text(encoding="utf-8")
        self.assertIn('[requested documents default](#defaults)', lecture)
        self.assertIn('[Deliver a file](#included-tasks-deliver-file-md)', course)
        self.assertLess(len(homework.encode("utf-8")), 48_000)
        self.assertNotIn('## Included: templates/simple-notes.tex', homework)

    def test_every_task_page_and_guide_is_on_some_route(self):
        for name in le.bz.skill_names():
            skill = ROOT / "skills" / name
            routed = {rel for _, _, s, files in le.ROUTES if s == name for rel in files}
            for folder in ("tasks", "guides"):
                for path in sorted((skill / folder).glob("*.md")):
                    self.assertIn(path.relative_to(skill).as_posix(), routed, f"{name}: add it to a route")

    def test_index_and_readme_router_list_every_route(self):
        index = le.render_index()
        router = le.render_router()
        self.assertLess(len(router.encode("utf-8")), 1600, "the router is pasted into Project instructions; keep it short")
        # Later messages in a chat must pick their page again (observed: agents skipped the skill mid-chat).
        self.assertIn("For every message, later ones included", router)
        for name, *_ in le.ROUTES:
            self.assertIn(le.route_url(name), index)
            self.assertIn(le.route_url(name), router)
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertEqual(readme, le.readme_with_router(readme), "run python3 tools/build_link_editions.py")
        self.assertIn(router, readme)

    def test_readme_one_link_prompt_keeps_the_every_message_rule(self):
        # The main setup is one link to the index; the rule against skipping skills on
        # later messages must be in the pasted prompt and on the index page itself.
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index_url = le.link_url(Path(f"{le.INDEX_NAME}.md"))
        self.assertIn(f"Use the Econ Agent Skills: {index_url}. For every message, later ones included", readme)
        self.assertIn("Pick the page again for every message", le.render_index())

    def test_old_combined_pages_point_to_their_route(self):
        for old, name in le.MOVED.items():
            text = (ROOT / "link" / old).read_text(encoding="utf-8")
            self.assertIn(le.route_url(name), text)

    def test_edition_code_is_shown_and_follows_every_file(self):
        for name in le.bz.skill_names():
            code = le.edition_code(ROOT / "skills" / name)
            self.assertRegex(code, r"^[0-9a-f]{6}$")
            text = le.render(ROOT / "skills" / name)
            self.assertIn(f"Edition code: `{code}`", text)
            self.assertIn(f"`Skill: {name} · {code}`", text)
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
