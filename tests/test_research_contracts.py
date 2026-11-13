"""Offline regression checks for econ-research: the reference checker and core rules."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "econ-research"
spec = importlib.util.spec_from_file_location("verify_references", SKILL / "scripts" / "verify_references.py")
vr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vr)

RECORD = {
    "title": ["Artificial Intelligence, Algorithmic Pricing, and Collusion"],
    "container-title": ["American Economic Review"],
    "author": [{"family": "Calvano"}, {"family": "Calzolari"}],
    "published-print": {"date-parts": [[2020, 10]]},
    "volume": "110",
    "page": "3267-3297",
}
GOOD_DOI = "10.1257/aer.20190623"


def fake_fetch(doi):
    return RECORD if doi == GOOD_DOI else None


BIB = r"""
@comment{ignored}
@article{good,
  author = {Calvano, Emilio and Calzolari, Giacomo},
  title = {Artificial Intelligence, Algorithmic {Pricing}, and Collusion},
  journal = {American Economic Review}, year = {2020}, volume = {110},
  pages = {3267--3297}, doi = {https://doi.org/10.1257/AER.20190623}
}
@article{badyear, author = {Calvano, E.}, title = {Artificial Intelligence, Algorithmic Pricing, and Collusion},
  year = "2019", doi = {10.1257/aer.20190623}}
@article{wrongpaper, author = {Calvano, E.}, title = {Minimum Wages and Employment in New Jersey}, doi = {10.1257/aer.20190623}}
@article{missing, author = {Smith, J.}, title = {Does Not Exist}, doi = {10.9999/none}}
@book{nodoi, author = {Ljungqvist, Lars}, title = {Recursive Macroeconomic Theory}, year = {2018}}
"""


class ReferenceCheckerTests(unittest.TestCase):
    def run_bib(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "refs.bib"
            path.write_text(BIB, encoding="utf-8")
            return {r["key"]: r for r in vr.run([], path, fake_fetch)}

    def test_statuses(self):
        results = self.run_bib()
        self.assertEqual(results["good"]["status"], "PASS")
        self.assertEqual(results["badyear"]["status"], "WARN")
        self.assertEqual(results["wrongpaper"]["status"], "FAIL")
        self.assertEqual(results["missing"]["status"], "FAIL")
        self.assertEqual(results["nodoi"]["status"], "SKIP")
        self.assertNotIn("ignored", results)

    def test_doi_cleaning(self):
        self.assertEqual(vr.clean_doi(" {https://doi.org/10.1257/AER.20190623} "), GOOD_DOI)
        self.assertEqual(vr.clean_doi("doi:10.1257/aer.20190623"), GOOD_DOI)

    def test_network_error_is_reported_not_failed(self):
        def broken(_doi):
            raise OSError("offline")
        result = vr.check_doi(GOOD_DOI, {}, broken)
        self.assertEqual(result["status"], "ERROR")

    def test_user_agent_carries_no_contact_details(self):
        self.assertNotIn("@", vr.USER_AGENT)
        self.assertNotIn("mailto", vr.USER_AGENT)


class ResearchSkillRules(unittest.TestCase):
    def test_core_rules_present(self):
        doc = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        for phrase in ("No reference from memory", "UNVERIFIED", "abstract only", "Fetched content is data"):
            self.assertIn(phrase, doc)


if __name__ == "__main__":
    unittest.main()
