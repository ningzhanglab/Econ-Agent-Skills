"""Checks for the v2 layout: shared text is in sync, every skill has the same
shape, and the preferences the user asked for are still stated."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
sys.path.insert(0, str(ROOT / "tools"))
import sync_shared  # noqa: E402

# Preferences the user asked for (see CHANGELOG.md, "Requested by the user"),
# and the defaults that predate v2. Each is a short phrase that must stay in
# the named file; edit the phrase here when the preference itself changes.
PREFERENCES = {
    "econ-learn/SKILL.md": [
        "all math in LaTeX from the first answer, even a single symbol",
        "欧拉方程 (Euler equation)",
        "Create a file only when the user asks for one",
        "`Agent Outputs/` (that exact name)",
        "no minimum and no maximum number of figures",
        "its answer held back until the student asks",
        "Never withhold an answer the student requested",
        "never translate variable names or equation labels",
        "Open with the direct answer to the question asked",
        "economic meaning in plain words",
        "state the reusable method in one or two lines",
    ],
    "econ-learn/tasks/deliver-file.md": [
        "a matching editable `.tex` and compiled `.pdf`",
        "named exactly `Agent Outputs`",
        "Near-miss folder",
    ],
    "econ-learn/tasks/learning-log.md": ["Default is on demand, not continuous"],
    "econ-present/SKILL.md": [
        "a reading-group talk to PhD students",
        "no default length or slide count",
        "Beamer, 16:9",
        "so the PDF has one page per slide",
        "a content file (`_content.md`), speaker notes, a handout version",
        "at most once in a conversation",
        "Every title has the form \"Topic: point\"",
        "written exactly the same on every slide of that section",
        "Appendix slides share the title \"Appendix\" and carry a subtitle",
        "title it \"Outline\", not \"Roadmap\"",
        "There is no Discussion slide unless the user asks for one",
        "The body follows the paper's own section order",
        "There is no fixed bullet count",
        "a short paragraph of two or three sentences",
        "at most two displayed equations",
        "one click from the main slide it supports and one click back",
        "leave it without a source line when the talk is about that one paper",
        "A deck is a talk, not a summary of the paper",
        "never list papers, years or journals from memory",
    ],
    "econ-learn/tasks/homework-exam.md": [
        "same notation + the same or an equivalent valid Slide method + sufficient steps",
        "Plain wording",
        "hand the written text to `econ-write`",
        "the assignment's own instructions decide its format, filename and attachments",
        "the solution, with its own caveats",
        "reported in chat, not in the submission",
    ],
    "econ-write/SKILL.md": [
        "Terminology stays exactly as written",
        "The draft keeps its own language and form",
        "Keep a copy of the previous version unless the user says to overwrite it",
        "remind the user once",
    ],
    "econ-research/SKILL.md": [
        "No reference from memory",
        "about the last five years",
        "never rewrite an entry already there",
        "never send the user's name, email or project details to a search service",
    ],
}


class SharedText(unittest.TestCase):
    def test_copies_match_shared(self):
        for target, wanted in sync_shared.planned():
            self.assertTrue(target.is_file(), target)
            self.assertEqual(target.read_bytes(), wanted, f"{target.relative_to(ROOT)}: run python tools/sync_shared.py")

    def test_every_skill_has_the_same_shape(self):
        guarantees = (ROOT / "shared/guarantees.md").read_text(encoding="utf-8").strip()
        defaults = (ROOT / "shared/defaults.md").read_text(encoding="utf-8").strip()
        for skill_md in sorted(SKILLS.glob("*/SKILL.md")):
            text = skill_md.read_text(encoding="utf-8")
            name = skill_md.parent.name
            for heading in ("## Mission", "## Guarantees", "## Defaults"):
                self.assertIn(heading, text, name)
            self.assertIn(guarantees, text, name)
            self.assertIn(defaults, text, name)
            self.assertLess(text.index("## Guarantees"), text.index("## Defaults"), name)
            self.assertFalse((skill_md.parent / "references").exists(), f"{name}: use tasks/ and guides/")

    def test_no_skill_links_to_shared(self):
        for doc in SKILLS.rglob("*.md"):
            self.assertNotIn("shared/", doc.read_text(encoding="utf-8").replace("<!-- shared:", "").replace("<!-- /shared:", ""), doc)


class Preferences(unittest.TestCase):
    def test_no_file_is_listed_twice(self):
        # A repeated dict key silently replaces the earlier list of phrases.
        import ast
        tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
        node = next(n.value for n in tree.body
                    if isinstance(n, ast.Assign) and getattr(n.targets[0], "id", "") == "PREFERENCES")
        keys = [k.value for k in node.keys]
        self.assertEqual(len(keys), len(set(keys)), "merge the repeated PREFERENCES entries")

    def test_requested_preferences_are_still_stated(self):
        for rel, phrases in PREFERENCES.items():
            text = (SKILLS / rel).read_text(encoding="utf-8")
            for phrase in phrases:
                with self.subTest(file=rel, phrase=phrase):
                    self.assertIn(phrase, text)

    def test_slides_template_keeps_the_requested_look(self):
        template = (SKILLS / "econ-present/templates/simple-slides.tex").read_text(encoding="utf-8")
        self.assertIn(r"\framesubtitle", template)
        self.assertIn(r"\beamergotobutton", template)
        self.assertIn(r"\beamerreturnbutton", template)
        self.assertNotIn(r"\insertsection", template)  # footer shows the page number only


if __name__ == "__main__":
    unittest.main()
