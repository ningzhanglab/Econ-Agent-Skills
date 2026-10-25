"""Standard-library regression checks for the Professor's repository contracts."""
import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "econ-phd-professor"
checker_path = ROOT / "scripts" / "check_tex_bundle.py"
spec = importlib.util.spec_from_file_location("check_tex_bundle", checker_path)
bundle = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bundle)


class CourseContracts(unittest.TestCase):
    def test_state_example_is_valid_scoped_json(self):
        state = json.loads((SKILL / "templates/course-state.example.json").read_text(encoding="utf-8"))
        self.assertEqual(state["schema_version"], 1)
        self.assertFalse(state["course_folder"]["verified"])
        self.assertIn("lectures", state)
        self.assertIn("coverage", state["lectures"][0])
        self.assertIn("preferred_source", state["lectures"][0])
        self.assertIn("unresolved_conflicts", state)

    def test_course_map_includes_homework(self):
        doc = (SKILL / "templates/course-map.md").read_text(encoding="utf-8")
        self.assertIn("Homework", doc)
        self.assertIn("Source locator", doc)
        self.assertIn("Conceptual dependency", doc)

    def test_source_selection_and_prompt_boundary(self):
        doc = (SKILL / "references/course-state-and-sources.md").read_text(encoding="utf-8")
        for token in ("LaTeX", "handout", "Presenter", "Untrusted material", "reopen", "Agent Outputs"):
            self.assertIn(token.lower(), doc.lower())
        self.assertIn("course-state.example.json", doc)

    def test_template_defaults_and_encoding(self):
        latin = (SKILL / "templates/simple-notes.tex").read_text(encoding="utf-8")
        chinese = (SKILL / "templates/simple-notes-cn.tex").read_text(encoding="utf-8")
        self.assertIn(r"\documentclass[11pt]{article}", latin)
        self.assertIn(r"\documentclass[11pt]{ctexart}", chinese)
        self.assertIn(r"\usepackage{amsmath,amssymb}", latin)
        self.assertEqual(bundle.choose_engine(chinese), "-xelatex")
        self.assertEqual(bundle.choose_engine(latin), "-pdf")

    def test_missing_asset_and_directory_escape(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            file = base / "notes.tex"
            file.write_text(r"\includegraphics{figures/missing-plot}", encoding="utf-8")
            self.assertTrue(any("missing" in s for s in bundle.missing_dependencies(file)))
            fig = base / "figures" / "missing-plot.pdf"
            fig.parent.mkdir()
            fig.write_bytes(b"%PDF-" + b"x" * 1200)
            self.assertEqual(bundle.missing_dependencies(file), [])
            file.write_text(r"\input{../secret}", encoding="utf-8")
            self.assertTrue(any("outside" in s for s in bundle.missing_dependencies(file)))

    def test_no_extra_chart_or_homework_without_source(self):
        doc = (SKILL / "references/visuals-and-homework.md").read_text(encoding="utf-8").lower()
        self.assertIn("only when", doc)
        self.assertIn("homework", doc)
        self.assertIn("untrusted", (SKILL / "references/course-state-and-sources.md").read_text(encoding="utf-8").lower())

    @unittest.skipUnless(shutil.which("latexmk") and shutil.which("pdflatex"), "TeX engine not available")
    def test_default_english_template_compiles_cleanly(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / "simple-notes.tex"
            shutil.copy2(SKILL / "templates/simple-notes.tex", dest)
            command = ["latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error", dest.name]
            result = subprocess.run(command, cwd=dest.parent, capture_output=True, text=True, timeout=120)
            self.assertEqual(result.returncode, 0, result.stdout[-2000:])
            self.assertTrue(bundle.is_pdf(dest.with_suffix(".pdf")))
            self.assertEqual(bundle.validate(dest, compile_requested=True), [])


if __name__ == "__main__":
    unittest.main()
