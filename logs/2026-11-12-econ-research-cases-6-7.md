# 2026-11-12 — econ-research cases 6 and 7; guidance for failed and no-DOI entries

- **Date:** 2026-11-12
- **Component:** `econ-research`
- **Change type:** Testing / Fixed
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change (branch `feat/econ-research-skill`)

## Motivation

The last two [research evaluation cases](../tests/research-evaluation.md) not yet run after [cases 2, 4 and 5](2026-11-12-econ-research-cases-2-4-5.md). With these, all seven cases have been run once.

## What was run

**Case 6 (check a bibliography).** A scratch `.bib` file (outside the repository) with four entries: Aiyagari (1994) correct; Achdou et al. with year 2021 instead of the print year 2022; an invented paper ("Zhou and Park 2020, Precautionary Saving and the Top Wealth Share", made-up DOI); and Ljungqvist and Sargent, *Recursive Macroeconomic Theory*, 4th edition, 2018, without a DOI.

- `verify_references.py` returned PASS, WARN (year 2021 vs record 2022), FAIL (no Crossref record) and SKIP, exit status 1. The file was byte-identical afterwards.
- Follow-up on the FAIL entry: Crossref and OpenAlex title searches found no paper with that title and those authors, so it was reported as possibly fabricated rather than as a mistyped DOI.
- Follow-up on the SKIP entry: OpenAlex confirmed the authors and title (records for the 2000 edition and a 2004 third edition). The 4th edition and 2018 year were not confirmed: Crossref had no record of the book and the publisher's page returned HTTP 403. The report lists exactly which fields were confirmed and suggests a library catalogue for the rest.

**Case 7 (paywalled paper).** Prompt: "What does Krusell and Smith (1998) find?" OpenAlex reports the published version as closed access with no repository full text; the journal landing page returned HTTP 403. The answer summarizes the abstract only, labeled as such, notes that a 1995 working-paper record exists (not read, and possibly different), and suggests library access for the full text.

## Results

| Case | Result | Notes |
| --- | --- | --- |
| 6. Check a bibliography | Pass (self-graded) | Correct statuses; follow-up searches for FAIL and SKIP; file not modified |
| 7. Paywalled paper | Pass (self-graded) | Abstract-only summary, labeled; no claims about the body |

All seven research evaluation cases have now been run once; none produced a critical fail.

## Fix

The skill did not say what to do after a FAIL or SKIP. `literature-search.md` now says: search the title and authors before calling a FAIL entry fabricated (a mistyped DOI also fails); check no-DOI entries field by field and report which fields were confirmed; list corrections instead of editing the user's file unless asked.

## Files affected

- `skills/econ-research/references/literature-search.md`: the fix above.
- `CHANGELOG.md`: entry for these cases.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| Real-topic evaluation, cases 6 and 7 | Pass | Self-graded by the agent that ran them; no independent grader |
| Automated structural validation and unit tests | Pass | `python3 tests/validate_skills.py` and `python3 -m unittest discover -s tests -p 'test_*.py'` run locally after the fix |
| GitHub Actions | Not run | Not yet run on the pushed branch at the time of writing |

## Known limitations and risks

- Publisher sites often block automated fetches (two 403 responses in this run), so books and paywalled papers will often remain partly verified or abstract-only.
- All seven cases were run and graded by the agent that wrote the skill.

## Follow-up

- Ask someone else to grade a sample of these runs, or rerun the cases in a fresh session without this conversation's context.
