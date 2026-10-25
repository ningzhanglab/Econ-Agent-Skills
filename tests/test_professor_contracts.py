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

    def test_equivalent_multiformat_lecture_grouping(self):
        doc = (SKILL / "references/course-state-and-sources.md").read_text(encoding="utf-8").lower()
        for term in (".tex", ".docx", ".pdf", "filename stem", "one logical", "ask a brief clarification"):
            self.assertIn(term, doc)
        nav = (SKILL / "references/course-navigation.md").read_text(encoding="utf-8")
        self.assertIn("Group same-basename", nav)
        idx = (SKILL / "templates/lecture-index.md").read_text(encoding="utf-8")
        self.assertIn("Grouped formats", idx)

    def test_group_multiformat_files_with_verified_parents(self):
        path = ROOT / "scripts/group_course_sources.py"
        spec_group = importlib.util.spec_from_file_location("course_grouping", path)
        grouper = importlib.util.module_from_spec(spec_group)
        spec_group.loader.exec_module(grouper)
        cases = [
            {"id": "a", "name": "L07.tex", "parent_id": "course1"},
            {"id": "b", "name": "l07.pdf", "parent_id": "course1"},
            {"id": "c", "name": "l07.docx", "parent_id": "course1"},
            {"id": "d", "name": "l07_presenter.pdf", "parent_id": "course1"},
            {"id": "e", "name": "l07.pdf", "parent_id": "course2"},
            {"id": "f", "name": "l07.docx"},
        ]
        grouped = grouper.group_sources(cases)
        self.assertEqual(len(grouped["logical_documents"]), 3)
        self.assertEqual(len(grouped["ungrouped"]), 1)
        doc = next(x for x in grouped["logical_documents"]
                   if x["parent_id"] == "course1" and x["basename"] == "l07")
        self.assertEqual({x["format"] for x in doc["files"]}, {".tex", ".pdf", ".docx"})
        self.assertEqual(doc["equivalence"], "provisional")

    def test_identical_pdf_names_flag_for_review(self):
        path = ROOT / "scripts/group_course_sources.py"
        spec_group = importlib.util.spec_from_file_location("course_grouping", path)
        grouper = importlib.util.module_from_spec(spec_group)
        spec_group.loader.exec_module(grouper)
        result = grouper.group_sources([
            {"id": "v1", "name": "notes.pdf", "parent_id": "course"},
            {"id": "v2", "name": "notes.PDF", "parent_id": "course"},
        ])
        self.assertTrue(result["logical_documents"][0]["needs_review"])

    def test_visual_first_policy_and_figure_index(self):
        skill = (SKILL / "SKILL.md").read_text(encoding="utf-8").lower()
        visual = (SKILL / "references/visuals-and-homework.md").read_text(encoding="utf-8").lower()
        expert = (SKILL / "references/expert-teaching.md").read_text(encoding="utf-8").lower()
        index = (SKILL / "templates/figure-index.md").read_text(encoding="utf-8")
        self.assertIn("visuals as a first-class", skill)
        self.assertIn("do not wait for prose", skill)
        self.assertIn("visual-first", visual)
        self.assertIn("rendered lecture handout pdf", visual)
        self.assertIn("proactively", expert)
        self.assertIn("RENDERED_PDF_VISUALLY_REVIEWED", index)
        self.assertIn("ASSET_LOCATED_NOT_VISUALLY_REVIEWED", index)

    def test_figure_inventory_honestly_tracks_assets_and_nested_tex(self):
        path = ROOT / "scripts/inventory_tex_figures.py"
        spec_fig = importlib.util.spec_from_file_location("figure_inventory", path)
        figure_module = importlib.util.module_from_spec(spec_fig)
        spec_fig.loader.exec_module(figure_module)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "figures").mkdir()
            (root / "chapters").mkdir()
            (root / "figures/policy.pdf").write_bytes(b"%PDF-" + b"\xff" * 1500)
            main = root / "lecture.tex"
            main.write_text(
                "\\section{Savings}\n"
                "\\includegraphics{figures/policy}\n"
                "\\input{chapters/methods}\n", encoding="utf-8"
            )
            (root / "chapters/methods.tex").write_text(
                "\\frametitle{Numerical errors}\n"
                "\\includegraphics{figures/missing}\n"
                "% \\includegraphics{commented}\n"
                "\\begin{tikzpicture}\n", encoding="utf-8"
            )
            result = figure_module.inventory(main)
            records = result["figure_references"]
            self.assertEqual(len(records), 3)
            self.assertEqual(records[0]["asset_status"], "ASSET_LOCATED_NOT_VISUALLY_REVIEWED")
            self.assertEqual(records[0]["asset"], "figures/policy.pdf")
            self.assertEqual(records[1]["asset_status"], "ASSET_NOT_FOUND")
            self.assertEqual(records[2]["asset_status"], "INLINE_FIGURE_NOT_VISUALLY_REVIEWED")
            self.assertTrue(all(not x["visually_inspected"] for x in records))
            self.assertEqual(len(result["source_files"]), 2)

    def test_figure_inventory_blocks_parent_traversal(self):
        path = ROOT / "scripts/inventory_tex_figures.py"
        spec_fig = importlib.util.spec_from_file_location("figure_inventory", path)
        figure_module = importlib.util.module_from_spec(spec_fig)
        spec_fig.loader.exec_module(figure_module)
        with tempfile.TemporaryDirectory() as tmp:
            main = Path(tmp) / "lecture.tex"
            main.write_text("\\includegraphics{../private/graph}\n", encoding="utf-8")
            result = figure_module.inventory(main)
            self.assertEqual(
                result["figure_references"][0]["asset_status"],
                "OUTSIDE_SOURCE_FOLDER"
            )

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

    def test_binary_figure_is_not_decoded_as_utf8(self):
        # The previous compiler walked every asset as text, failing on binary PDFs.
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            tex = folder / "notes.tex"
            figures = folder / "figures"
            figures.mkdir()
            (figures / "image.pdf").write_bytes(b"%PDF-" + b"\xff" * 2048)
            tex.write_text(r"\includegraphics{figures/image.pdf}", encoding="utf-8")
            self.assertEqual(bundle.missing_dependencies(tex), [])
            errors, dependencies = bundle._resolve_dependencies(tex)
            self.assertEqual(errors, [])
            self.assertEqual(len(dependencies), 2)

    def test_nested_input_missing_figure_is_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            tex = folder / "notes.tex"
            chapters = folder / "chapters"
            chapters.mkdir()
            tex.write_text(r"\input{chapters/part}", encoding="utf-8")
            (chapters / "part.tex").write_text(
                r"\includegraphics{figures/missing}", encoding="utf-8"
            )
            errors = bundle.missing_dependencies(tex)
            self.assertTrue(any("missing includegraphics" in msg for msg in errors), errors)

    def test_nested_asset_relative_to_main_and_external_blocked(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            (folder / "chapters").mkdir()
            (folder / "figures").mkdir()
            tex = folder / "notes.tex"
            tex.write_text(r"\input{chapters/part}", encoding="utf-8")
            (folder / "chapters/part.tex").write_text(
                r"\includegraphics{figures/plot.png}", encoding="utf-8"
            )
            (folder / "figures/plot.png").write_bytes(b"\x89PNG\r\n\x1a\n" + b"\xff" * 128)
            problems, files = bundle._resolve_dependencies(tex)
            self.assertEqual(problems, [])
            self.assertEqual(len(files), 3)
            (folder / "chapters/part.tex").write_text(r"\input{../outside}", encoding="utf-8")
            self.assertTrue(any("outside bundle" in x for x in bundle.missing_dependencies(tex)))

    def test_dynamic_graphicspath_cannot_pass_silently(self):
        with tempfile.TemporaryDirectory() as tmp:
            tex = Path(tmp) / "notes.tex"
            tex.write_text(r"\graphicspath{{figures/}}", encoding="utf-8")
            self.assertTrue(any("unsupported" in x for x in bundle.missing_dependencies(tex)))

    @unittest.skipUnless(shutil.which("latexmk") and shutil.which("pdflatex"),
                         "TeX engine not available")
    def test_figure_pdf_and_nested_input_compile_together(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "figures").mkdir()
            (root / "chapters").mkdir()
            fig_tex = root / "figures/figure.tex"
            fig_tex.write_text(
                r"\documentclass{article}\pagestyle{empty}\begin{document}"
                r"\rule{2cm}{1cm}\end{document}", encoding="utf-8"
            )
            comp = subprocess.run(
                ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", fig_tex.name],
                cwd=fig_tex.parent, capture_output=True, text=True, timeout=90,
            )
            self.assertEqual(comp.returncode, 0, comp.stdout[-1500:])
            tex = root / "notes.tex"
            tex.write_text(
                "\\documentclass{article}\n"
                "\\usepackage{graphicx}\n"
                "\\begin{document}\n"
                "\\input{chapters/part}\n"
                "\\end{document}\n", encoding="utf-8"
            )
            (root / "chapters/part.tex").write_text(
                r"\includegraphics[width=2cm]{figures/figure.pdf}", encoding="utf-8"
            )
            result = subprocess.run(
                ["latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error", tex.name],
                cwd=root, capture_output=True, text=True, timeout=120,
            )
            self.assertEqual(result.returncode, 0, result.stdout[-1500:])
            self.assertEqual(bundle.validate(tex, compile_requested=True), [])

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
