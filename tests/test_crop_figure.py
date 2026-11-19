"""Checks for econ-present's figure cropper (standard library only)."""
import importlib.util
import io
import struct
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "crop_figure", ROOT / "skills" / "econ-present" / "scripts" / "crop_figure.py")
crop = importlib.util.module_from_spec(spec)
spec.loader.exec_module(crop)


def one_page_pdf(width: int = 612, height: int = 792) -> bytes:
    """A minimal valid PDF: one page with a filled rectangle in its upper half."""
    stream = b"0 0 0 rg 100 400 200 200 re f"
    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {width} {height}] /Contents 4 0 R >>".encode(),
        b"<< /Length %d >>\nstream\n" % len(stream) + stream + b"\nendstream",
    ]
    out = bytearray(b"%PDF-1.4\n")
    offsets = []
    for number, body in enumerate(objects, 1):
        offsets.append(len(out))
        out += b"%d 0 obj\n" % number + body + b"\nendobj\n"
    xref = len(out)
    out += b"xref\n0 %d\n0000000000 65535 f \n" % (len(objects) + 1)
    for offset in offsets:
        out += b"%010d 00000 n \n" % offset
    out += b"trailer\n<< /Size %d /Root 1 0 R >>\nstartxref\n%d\n%%%%EOF\n" % (len(objects) + 1, xref)
    return bytes(out)


def png_size(path: Path) -> tuple[int, int]:
    data = path.read_bytes()
    assert data[:8] == b"\x89PNG\r\n\x1a\n", "not a PNG"
    return struct.unpack(">II", data[16:24])


class CropFigure(unittest.TestCase):
    def test_box_defaults_to_whole_page_and_rejects_bad_boxes(self):
        self.assertEqual(crop.parse_box(None), (0.0, 0.0, 1.0, 1.0))
        self.assertEqual(crop.parse_box([0.1, 0.2, 0.9, 0.5]), (0.1, 0.2, 0.9, 0.5))
        for bad in ([0.5, 0.2, 0.4, 0.6], [0.1, 0.6, 0.9, 0.5], [-0.1, 0, 1, 1], [0, 0, 1.2, 1]):
            with self.assertRaises(ValueError):
                crop.parse_box(bad)

    def test_pixel_window_scales_points_to_pixels(self):
        # A US-letter page at 144 dpi is 1224 x 1584 px; the top half's left half:
        self.assertEqual(crop.pixel_window((0, 0, 0.5, 0.5), 612, 792, 144), (0, 0, 612, 792))
        self.assertEqual(crop.pixel_window((0.25, 0.5, 0.75, 1), 612, 792, 72), (153, 396, 306, 396))

    def test_page_size_reads_pdfinfo_and_swaps_for_rotation(self):
        text = "Pages:          20\nPage   14 size: 612 x 792 pts (letter)\nPage   14 rot:  0\n"
        self.assertEqual(crop.page_size_from_pdfinfo(text, 14), (612.0, 792.0))
        self.assertEqual(crop.page_size_from_pdfinfo(text.replace("rot:  0", "rot:  90"), 14), (792.0, 612.0))
        with self.assertRaises(ValueError):
            crop.page_size_from_pdfinfo(text, 3)

    def test_no_renderer_fails_clearly(self):
        with tempfile.TemporaryDirectory() as tmp:
            pdf = Path(tmp) / "paper.pdf"
            pdf.write_bytes(one_page_pdf())
            out = Path(tmp) / "figures" / "fig.png"
            buffer = io.StringIO()
            with mock.patch.object(crop, "choose_backend", return_value=None), redirect_stdout(buffer):
                status = crop.main([str(pdf), "1", "--out", str(out)])
            self.assertEqual(status, 2)
            self.assertIn("no PDF renderer", buffer.getvalue())
            self.assertFalse(out.exists())

    @unittest.skipUnless(crop.choose_backend(), "no PDF renderer (PyMuPDF or Poppler) installed")
    def test_crop_saves_only_the_box(self):
        with tempfile.TemporaryDirectory() as tmp:
            pdf = Path(tmp) / "paper.pdf"
            pdf.write_bytes(one_page_pdf())
            whole = Path(tmp) / "figures" / "page.png"
            part = Path(tmp) / "figures" / "fig.png"
            with redirect_stdout(io.StringIO()):
                self.assertEqual(crop.main([str(pdf), "1", "--dpi", "72", "--out", str(whole)]), 0)
                self.assertEqual(crop.main([str(pdf), "1", "--dpi", "72", "--box", "0", "0", "0.5", "0.5",
                                            "--out", str(part)]), 0)
            self.assertEqual(png_size(whole), (612, 792))
            self.assertEqual(png_size(part), (306, 396))


if __name__ == "__main__":
    unittest.main()
