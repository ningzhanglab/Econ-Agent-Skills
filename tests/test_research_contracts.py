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

    def test_parenthesized_entry_is_checked(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "refs.bib"
            path.write_text(
                '@article(grouped, note = "Contains a closing parenthesis )", '
                'title = {Artificial Intelligence, Algorithmic {Pricing}, and Collusion}, '
                f'doi = {{{GOOD_DOI}}})\n',
                encoding="utf-8",
            )
            results = vr.run([], path, fake_fetch)
        self.assertEqual([(result["key"], result["status"]) for result in results], [("grouped", "PASS")])

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

    def test_title_word_order_matters_but_punctuation_and_case_do_not(self):
        fields = {"title": "Algorithmic Intelligence, Artificial Pricing, and Collusion"}
        status, notes = vr.compare(fields, RECORD)
        self.assertEqual(status, "WARN")
        self.assertIn(RECORD["title"][0], notes[0])
        punctuation_only = {"title": "ARTIFICIAL INTELLIGENCE: Algorithmic Pricing and Collusion"}
        self.assertEqual(vr.compare(punctuation_only, RECORD), ("PASS", []))

    def test_subtitle_ampersand_and_markup_differences_pass(self):
        split = dict(RECORD, title=["Artificial Intelligence"], subtitle=["Algorithmic Pricing and Collusion"])
        self.assertEqual(vr.compare({"title": "Artificial Intelligence: Algorithmic Pricing and Collusion"}, split),
                         ("PASS", []))
        colon = dict(RECORD, title=["Artificial Intelligence: Algorithmic Pricing &amp; Collusion"])
        self.assertEqual(vr.compare({"title": "Artificial Intelligence"}, colon), ("PASS", []))
        self.assertEqual(vr.compare({"title": "Artificial Intelligence: Algorithmic Pricing and Collusion"}, colon),
                         ("PASS", []))
        markup = dict(RECORD, title=["Artificial <i>Intelligence</i>, Algorithmic Pricing, and Collusion"])
        self.assertEqual(vr.compare({"title": RECORD["title"][0]}, markup), ("PASS", []))

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

    def test_crossref_dates_of_mixed_precision_in_the_same_year(self):
        record = dict(RECORD, **{"published-print": {"date-parts": [[2021]]},
                                 "published-online": {"date-parts": [[2021, 12]]}})
        status, notes = vr.compare({"year": "2022"}, record)
        self.assertEqual(status, "PASS")
        self.assertTrue(any("volume year" in note for note in notes))

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

    def test_first_author_matches_whole_surname_only(self):
        rec = {"title": ["Growth and Trade"], "author": [{"family": "Li"}]}
        for author in ("Liu, Wei and Li, Hong", "Williams, Ann", "Smith, A AND Li, H"):
            status, notes = vr.compare({"title": "Growth and Trade", "author": author}, rec)
            self.assertEqual(status, "WARN", author)
        for author in ("Li, Hong and Liu, Wei", "Hong Li"):
            self.assertEqual(vr.compare({"title": "Growth and Trade", "author": author}, rec)[0], "PASS", author)
        multi = {"title": ["Growth and Trade"], "author": [{"family": "Van Reenen"}]}
        self.assertEqual(vr.compare({"title": "Growth and Trade", "author": "Van Reenen, John"}, multi)[0], "PASS")

    def test_latex_accents_match_unicode_record(self):
        rec = {"title": ["Política Monetaria y Ciclo"], "author": [{"family": "Galí"}]}
        for title, author in ((r"Pol{\'\i}tica Monetaria y Ciclo", r"Gal{\'\i}, Jordi"),
                              (r"Pol\'{\i}tica Monetaria y Ciclo", r"Gal\'{i}, Jordi"),
                              (r"Pol{\'i}tica Monetaria y Ciclo", r"Gal\'i, Jordi")):
            self.assertEqual(vr.compare({"title": title, "author": author}, rec), ("PASS", []), title)
        rec2 = {"title": ["Trade"], "author": [{"family": "Acemoğlu"}]}
        self.assertEqual(vr.compare({"title": "Trade", "author": r"Acemo{\u{g}}lu, Daron"}, rec2)[0], "PASS")

    def test_rate_limit_is_retried_then_succeeds(self):
        calls, waits = [], []

        class Response(io.BytesIO):
            def __enter__(self):
                return self
            def __exit__(self, *exc):
                return False

        def opener(req, timeout):
            calls.append(req.full_url)
            if len(calls) < 3:
                raise vr.urllib.error.HTTPError(req.full_url, 429 if len(calls) == 1 else 503,
                                                "busy", {"Retry-After": "1"}, None)
            return Response(b'{"message": {"title": ["X"]}}')

        self.assertEqual(vr.fetch_crossref(GOOD_DOI, opener=opener, sleep=waits.append), {"title": ["X"]})
        self.assertEqual(len(calls), 3)
        self.assertEqual(waits, [1.0, 1.0])

    def test_client_error_is_not_retried_and_gives_up_after_three_tries(self):
        calls = []

        def bad_request(req, timeout):
            calls.append(1)
            raise vr.urllib.error.HTTPError(req.full_url, 400, "bad", {}, None)
        with self.assertRaises(vr.urllib.error.HTTPError):
            vr.fetch_crossref(GOOD_DOI, opener=bad_request, sleep=lambda s: None)
        self.assertEqual(len(calls), 1)

        calls.clear()
        def offline(req, timeout):
            calls.append(1)
            raise OSError("offline")
        with self.assertRaises(OSError):
            vr.fetch_crossref(GOOD_DOI, opener=offline, sleep=lambda s: None)
        self.assertEqual(len(calls), vr.ATTEMPTS)

    def test_each_doi_is_looked_up_once(self):
        calls = []

        def counting(doi):
            calls.append(doi)
            return fake_fetch(doi)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "refs.bib"
            path.write_text(BIB, encoding="utf-8")
            vr.run([GOOD_DOI], path, counting)
        self.assertEqual(calls.count(GOOD_DOI), 1)

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
