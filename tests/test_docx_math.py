"""Offline checks for the Word equation reader (standard library only)."""
import importlib.util
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "econ-teaching" / "scripts" / "read_docx_math.py"
spec = importlib.util.spec_from_file_location("read_docx_math", SCRIPT)
reader = importlib.util.module_from_spec(spec)
spec.loader.exec_module(reader)

NS = (
    'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
    'xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" '
    'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
    'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
    'xmlns:v="urn:schemas-microsoft-com:vml"'
)


def run(text):
    return f"<m:r><m:t>{text}</m:t></m:r>"


def sub(base, index):
    return f"<m:sSub><m:e>{run(base)}</m:e><m:sub>{run(index)}</m:sub></m:sSub>"


# A hypothetical line, not from any course: "Model: x_t = (a)/(1-b) + \hat{c}^2 . End"
EQUATION = (
    "<m:oMath>"
    + sub("x", "t")
    + run("=")
    + f"<m:f><m:num>{run('a')}</m:num><m:den>{run('1-b')}</m:den></m:f>"
    + run("+")
    + "<m:sSup><m:e><m:acc><m:accPr><m:chr m:val=\"̂\"/></m:accPr>"
    + f"<m:e>{run('c')}</m:e></m:acc></m:e><m:sup>{run('2')}</m:sup></m:sSup>"
    + "</m:oMath>"
)
NARY = (
    "<m:oMath><m:nary><m:naryPr><m:chr m:val=\"∑\"/></m:naryPr>"
    f"<m:sub>{run('j=1')}</m:sub><m:sup>{run('q')}</m:sup><m:e>{sub('b', 'j')}</m:e></m:nary></m:oMath>"
)
DOCUMENT = (
    f'<?xml version="1.0" encoding="UTF-8"?><w:document {NS}><w:body>'
    f"<w:p><w:r><w:t>Model: </w:t></w:r>{EQUATION}<w:r><w:t> . End</w:t></w:r></w:p>"
    f"<w:p><m:oMathPara>{NARY}</m:oMathPara></w:p>"
    '<w:p><w:r><w:drawing><a:blip r:embed="rId1"/></w:drawing></w:r></w:p>'
    '<w:p><w:r><w:pict><v:shape><v:imagedata r:id="rId2"/></v:shape></w:pict></w:r></w:p>'
    "<w:tbl><w:tr><w:tc><w:p><w:r><w:t>Lag</w:t></w:r></w:p></w:tc>"
    "<w:tc><w:p><w:r><w:t>0.5</w:t></w:r></w:p></w:tc></w:tr></w:tbl>"
    "</w:body></w:document>"
)
RELS = (
    '<?xml version="1.0" encoding="UTF-8"?>'
    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
    '<Relationship Id="rId1" Type="image" Target="media/image1.png"/>'
    '<Relationship Id="rId2" Type="image" Target="media/image2.wmf"/>'
    "</Relationships>"
)


def make_docx(folder):
    path = Path(folder) / "sample.docx"
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("word/document.xml", DOCUMENT)
        archive.writestr("word/_rels/document.xml.rels", RELS)
    return path


class DocxMathReader(unittest.TestCase):
    def test_equations_keep_subscripts_fractions_accents_and_sums(self):
        with tempfile.TemporaryDirectory() as folder:
            text, counts = reader.read_docx(make_docx(folder))
        self.assertIn("Model:  $x_t=(a)/(1-b)+\\hat{c}^2$  . End", text)
        self.assertIn("$∑_{j=1}^q b_j$", text)
        self.assertEqual(counts["equations"], 2)

    def test_equation_text_is_not_duplicated_outside_the_math(self):
        with tempfile.TemporaryDirectory() as folder:
            text, _ = reader.read_docx(make_docx(folder))
        self.assertEqual(text.count("1-b"), 1)

    def test_images_and_embedded_objects_are_marked_unread(self):
        with tempfile.TemporaryDirectory() as folder:
            text, counts = reader.read_docx(make_docx(folder))
        self.assertIn("[IMAGE media/image1.png]", text)
        self.assertIn("[EMBEDDED OBJECT media/image2.wmf]", text)
        self.assertEqual((counts["images"], counts["embedded_objects"]), (1, 1))

    def test_table_rows_are_joined_in_order(self):
        with tempfile.TemporaryDirectory() as folder:
            text, _ = reader.read_docx(make_docx(folder))
        self.assertIn("Lag | 0.5", text)

    def test_command_line_reports_what_was_not_read_and_leaves_source_unchanged(self):
        with tempfile.TemporaryDirectory() as folder:
            path = make_docx(folder)
            before = path.read_bytes()
            result = subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("x_t=", result.stdout)
            self.assertIn("NOT read", result.stderr)
            self.assertEqual(path.read_bytes(), before)

    def test_a_file_that_is_not_a_docx_fails_cleanly(self):
        with tempfile.TemporaryDirectory() as folder:
            bad = Path(folder) / "bad.docx"
            bad.write_text("not a zip")
            result = subprocess.run([sys.executable, str(SCRIPT), str(bad)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn("ERROR", result.stderr)

    def test_skill_documents_the_reader_and_its_limit(self):
        fidelity = (ROOT / "skills/econ-teaching/references/slide-fidelity.md").read_text(encoding="utf-8")
        self.assertIn("read_docx_math.py", fidelity)
        self.assertIn("count as unread", fidelity)
        self.assertIn("read_docx_math.py", (ROOT / "skills/econ-teaching/SKILL.md").read_text(encoding="utf-8"))

    def test_skill_requires_a_formula_reread_before_delivery(self):
        fidelity = (ROOT / "skills/econ-teaching/references/slide-fidelity.md").read_text(encoding="utf-8")
        outputs = (ROOT / "skills/econ-teaching/references/latex-outputs.md").read_text(encoding="utf-8")
        self.assertIn("Re-read every displayed formula against the source before delivering", fidelity)
        self.assertIn("Re-read each displayed formula against its source", outputs)


if __name__ == "__main__":
    unittest.main()
