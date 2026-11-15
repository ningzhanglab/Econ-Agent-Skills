"""Offline checks for the per-skill zip builder used by the release workflow."""
import importlib.util
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
            first = bz.build_zip(ROOT / "skills" / "econ-teaching", Path(a)).read_bytes()
            second = bz.build_zip(ROOT / "skills" / "econ-teaching", Path(b)).read_bytes()
            self.assertEqual(first, second)

    def test_folder_without_skill_md_is_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                bz.build_zip(Path(tmp), Path(tmp) / "dist")

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


if __name__ == "__main__":
    unittest.main()
