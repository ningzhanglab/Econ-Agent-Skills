"""Offline regression checks for econ-research: the reference checker and core rules."""
import contextlib
import importlib.util
import io
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

    def test_html_entities_in_record_are_decoded(self):
        record = dict(RECORD, **{"container-title": ["Journal of Economic Behavior &amp; Organization"]})
        self.assertIn("Behavior & Organization", vr.describe(record))
        status, _ = vr.compare({"journal": "Journal of Economic Behavior & Organization"}, record)
        self.assertEqual(status, "PASS")

    def test_volume_year_after_late_december_print_date_passes_with_note(self):
        # Shape of Crossref's record for QJE 137(1) (2022 volume): print date 2021-12-24, no 2022 date.
        record = dict(RECORD, **{"published-print": {"date-parts": [[2021, 12, 24]]},
                                 "published-online": {"date-parts": [[2021, 8, 20]]},
                                 "issued": {"date-parts": [[2021, 8, 20]]}})
        status, notes = vr.compare({"year": "2022"}, record)
        self.assertEqual(status, "PASS")
        self.assertTrue(any("volume year" in n for n in notes))
        self.assertEqual(vr.compare({"year": "2021"}, record), ("PASS", []))
        self.assertEqual(vr.compare({"year": "2023"}, record)[0], "WARN")

    def test_year_one_after_mid_year_print_date_still_warns(self):
        self.assertEqual(vr.compare({"year": "2021"}, RECORD)[0], "WARN")  # record printed 2020-10
        record = dict(RECORD, **{"published-print": {"date-parts": [[2020, 6]]}})
        self.assertEqual(vr.compare({"year": "2021"}, record)[0], "WARN")

    def test_online_year_is_accepted(self):
        record = dict(RECORD, **{"published-online": {"date-parts": [[2019, 11, 3]]}})
        self.assertEqual(vr.compare({"year": "2019"}, record), ("PASS", []))

    def test_renamed_journal_is_a_note_not_a_warn(self):
        record = dict(RECORD, **{"container-title": ["ILR Review"], "short-container-title": ["ILR Review"]})
        status, notes = vr.compare({"journal": "Industrial and Labor Relations Review"}, record)
        self.assertEqual(status, "PASS")
        self.assertTrue(any("venue differs" in n and "ILR Review" in n for n in notes))

    def test_lookup_error_gives_nonzero_exit(self):
        original = vr.fetch_crossref
        def broken(_doi):
            raise OSError("offline")
        vr.fetch_crossref = broken
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(vr.main(["--doi", GOOD_DOI]), 2)
        finally:
            vr.fetch_crossref = original

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
