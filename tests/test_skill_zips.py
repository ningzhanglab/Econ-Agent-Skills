"""Offline checks for the per-skill zip builder used by the release workflow."""
import importlib.util
import shutil
import subprocess
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("build_skill_zips", ROOT / "tools" / "build_skill_zips.py")
bz = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bz)


class SkillZipTests(unittest.TestCase):
    def test_every_real_skill_builds_with_folder_at_top(self):
        with tempfile.TemporaryDirectory() as tmp:
            for name in bz.skill_names():
                target = bz.build_zip(ROOT / "skills" / name, Path(tmp))
                with zipfile.ZipFile(target) as zf:
                    names = zf.namelist()
                self.assertIn(f"{name}/SKILL.md", names)
                self.assertTrue(all(n.startswith(f"{name}/") for n in names), names)
                self.assertFalse(any(".DS_Store" in n or "__pycache__" in n for n in names))
                self.assertFalse(any(n.split("/")[1] in {"logs", "tests"} for n in names))

    def test_junk_is_skipped_and_other_skills_are_not_included(self):
        with tempfile.TemporaryDirectory() as tmp:
            skills = Path(tmp) / "skills"
            one = skills / "one"
            (one / "references").mkdir(parents=True)
            (one / "SKILL.md").write_text("---\nname: one\n---\n", encoding="utf-8")
            (one / "references" / "a.md").write_text("a", encoding="utf-8")
            (one / ".DS_Store").write_bytes(b"x")
            (one / "__pycache__").mkdir()
            (one / "__pycache__" / "m.cpython-312.pyc").write_bytes(b"x")
            (one / "notes.aux").write_text("x", encoding="utf-8")
            (skills / "two").mkdir()
            (skills / "two" / "SKILL.md").write_text("---\nname: two\n---\n", encoding="utf-8")

            target = bz.build_zip(one, Path(tmp) / "dist")
            with zipfile.ZipFile(target) as zf:
                self.assertEqual(sorted(zf.namelist()), ["one/SKILL.md", "one/references/a.md"])
            self.assertEqual(bz.skill_names(skills), ["one", "two"])

    def test_build_is_reproducible(self):
        with tempfile.TemporaryDirectory() as a, tempfile.TemporaryDirectory() as b:
            first = bz.build_zip(ROOT / "skills" / "econ-learn", Path(a)).read_bytes()
            second = bz.build_zip(ROOT / "skills" / "econ-learn", Path(b)).read_bytes()
            self.assertEqual(first, second)

    def test_folder_without_skill_md_is_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                bz.build_zip(Path(tmp), Path(tmp) / "dist")

    @unittest.skipUnless(shutil.which("git"), "git not available")
    def test_untracked_files_are_left_out_inside_a_git_checkout(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = Path(tmp) / "repo" / "skills" / "one"
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text("---\nname: one\n---\n", encoding="utf-8")
            (skill / "private-notes.txt").write_text("not for sharing", encoding="utf-8")
            repo = Path(tmp) / "repo"
            subprocess.run(["git", "init", "-q", str(repo)], check=True)
            subprocess.run(["git", "-C", str(repo), "add", "skills/one/SKILL.md"], check=True)
            target = bz.build_zip(skill, Path(tmp) / "dist")
            with zipfile.ZipFile(target) as zf:
                self.assertEqual(zf.namelist(), ["one/SKILL.md"])

    @unittest.skipUnless(shutil.which("git"), "git not available")
    def test_git_checkout_with_nothing_tracked_is_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = Path(tmp) / "repo" / "one"
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text("---\nname: one\n---\n", encoding="utf-8")
            subprocess.run(["git", "init", "-q", str(Path(tmp) / "repo")], check=True)
            with self.assertRaises(ValueError):
                bz.build_zip(skill, Path(tmp) / "dist")

    def test_unknown_skill_name_fails(self):
        self.assertEqual(bz.main(["--skill", "no-such-skill", "--out", tempfile.gettempdir()]), 1)


vspec = importlib.util.spec_from_file_location("validate_skills", ROOT / "tests" / "validate_skills.py")
vs = importlib.util.module_from_spec(vspec)
vspec.loader.exec_module(vs)


class SelfContainedSkillTests(unittest.TestCase):
    def test_real_skills_link_only_inside_their_folder(self):
        for name in bz.skill_names():
            self.assertEqual(vs.links_leaving_folder(ROOT / "skills" / name), [], name)

    def test_link_out_of_the_folder_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = Path(tmp) / "skills" / "x"
            (skill / "references").mkdir(parents=True)
            (skill / "SKILL.md").write_text("[ok](references/r.md)\n", encoding="utf-8")
            (skill / "references" / "r.md").write_text("[bad](../../../README.md) [web](https://example.org)\n", encoding="utf-8")
            problems = vs.links_leaving_folder(skill)
            self.assertEqual(len(problems), 1)
            self.assertIn("../../../README.md", problems[0])

    def test_other_link_forms_out_of_the_folder_are_reported(self):
        forms = {
            "angle brackets": "[a](<../../../README.md>)",
            "image with empty label": "![](../../../x.png)",
            "reference style": "[a][r]\n\n[r]: ../../../README.md",
            "html": '<a href="../../../README.md">a</a>',
            "file url": "[a](file:///etc/hosts)",
        }
        for label, body in forms.items():
            with tempfile.TemporaryDirectory() as tmp:
                skill = Path(tmp) / "skills" / "x"
                skill.mkdir(parents=True)
                (skill / "SKILL.md").write_text(body + "\n", encoding="utf-8")
                self.assertEqual(len(vs.links_leaving_folder(skill)), 1, label)

    def test_inside_links_with_title_or_anchor_are_not_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = Path(tmp) / "skills" / "x"
            (skill / "references").mkdir(parents=True)
            (skill / "references" / "r.md").write_text("r", encoding="utf-8")
            (skill / "SKILL.md").write_text(
                '[a](references/r.md "title") [b](references/r.md#part) [c](#top) [w](https://example.org)\n',
                encoding="utf-8",
            )
            self.assertEqual(vs.links_leaving_folder(skill), [])

    def test_plain_text_pointer_to_a_repository_file_is_reported(self):
        # The real bug fixed on 2026-11-14 was plain text, not a link.
        with tempfile.TemporaryDirectory() as tmp:
            skill = Path(tmp) / "skills" / "x"
            (skill / "agents").mkdir(parents=True)
            (skill / "SKILL.md").write_text("follow the storage policy (`STORAGE_POLICY.md`)\n", encoding="utf-8")
            (skill / "agents" / "a.yaml").write_text("note: see AGENTS.md\n", encoding="utf-8")
            (skill / "blob.bin").write_bytes(b"\xff\xfe\x00")
            problems = vs.repo_file_mentions(skill)
            self.assertEqual(len(problems), 2)
            self.assertEqual(vs.links_leaving_folder(skill), [])

    def test_real_skills_do_not_name_repository_files(self):
        for name in bz.skill_names():
            self.assertEqual(vs.repo_file_mentions(ROOT / "skills" / name), [], name)


if __name__ == "__main__":
    unittest.main()
