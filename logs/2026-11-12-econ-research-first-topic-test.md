# 2026-11-12 — First real-topic test of econ-research; three guidance fixes

- **Date:** 2026-11-12
- **Component:** `econ-research`
- **Change type:** Testing / Fixed
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change (branch `feat/econ-research-skill`)

## Motivation

First run of [econ-research v0.1](2026-11-12-econ-research-skill.md) on a real topic chosen by the user: **precautionary saving and wealth inequality in Aiyagari-type heterogeneous-agent models**. The run corresponds to [evaluation case 1](../tests/research-evaluation.md) (known literature), with part of case 3 (working-paper coverage). The topic is public economics literature; no private course material is recorded here.

## What was run

- **Search:** ten OpenAlex keyword queries covering the core model, wealth inequality, precautionary saving, skewed distributions, calibration, sources of inequality, return heterogeneity and Pareto tails; one Semantic Scholar query; five Crossref title lookups for seed papers known in advance (Huggett 1993, De Nardi and Fella 2017, Benhabib, Bisin and Luo 2019, Krueger, Mitman and Perri 2016, Bewley 1986).
- **Screening:** seventeen papers kept, scored 3–5 for relevance.
- **Verification:** `verify_references.py` returned PASS for all seventeen DOIs against Crossref.
- **Reading:** abstracts fetched from OpenAlex for twelve; five had no abstract available and were reported as metadata only. No full texts were read.

## Results

| Case | Result | Notes |
| --- | --- | --- |
| 1. Known literature | Pass (self-graded) | Every listed paper verified; read status and version given; splits described with candidate explanations taken from abstracts; coverage line given |
| 3. Thin or new topic | Partial | Working-paper versions appeared through OpenAlex (NBER, SSRN), but RePEc/IDEAS and NBER were not queried directly |
| 2, 4–7 | Not run | Not part of this topic test |

No critical fail was observed: no invented paper, no finding described beyond an abstract, no personal details sent (queries contained only topic words and DOIs; OpenAlex was used without a key).

### Observations that led to fixes

1. **Seed papers from prior knowledge.** Five candidates were looked up by title because they were known in advance. The skill did not say whether this is allowed. Fix: `literature-search.md` now allows known papers as search seeds only, kept only if a source confirms them, and asks for this to be stated in the coverage line.
2. **Year disagreement across sources.** Achdou, Han, Lasry, Lions and Moll is listed as 2021 by OpenAlex and 2022 by the Crossref print record. Fix: cite the print year and note the online year.
3. **Incomplete records and pre-DOI work.** The Crossref record for the Krueger, Mitman and Perri *Handbook of Macroeconomics* chapter has no authors (the NBER working-paper record has them). Bewley's 1986 chapter, a founding paper of the model class, could not be found in Crossref or OpenAlex. Fix: fill missing fields from another record of the same work and name the source; for older work without a DOI, check RePEc or a catalogue, otherwise cite only as UNVERIFIED.

## Files affected

- `skills/econ-research/references/literature-search.md`: the three fixes above.
- `CHANGELOG.md`: entry for this test.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| Real-topic evaluation | Pass (case 1), Partial (case 3) | Self-graded by the agent that ran it; no independent grader |
| Reference checker on live Crossref | Pass | 17 of 17 DOIs PASS, exit status 0 |
| Automated structural validation and unit tests | Pass | `python3 tests/validate_skills.py` and `python3 -m unittest discover -s tests -p 'test_*.py'` run locally after the fixes |
| GitHub Actions | Not run | Not yet run on the pushed branch at the time of writing |

## Known limitations and risks

- Grading was done by the same agent that ran the test.
- Abstracts only: the run cannot show how the skill handles full-text reading.
- OpenAlex's keyless daily budget is shared and small; heavier use may need the user's own key.

## Follow-up

- Run cases 2 (fake paper) and 4–5 (question development, "is it done?") on a topic from the user's own research.
- Query RePEc/IDEAS directly in a future run to close the working-paper gap.
