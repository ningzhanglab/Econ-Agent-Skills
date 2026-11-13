# 2026-11-12 — econ-research cases 2, 4 and 5; two checker fixes

- **Date:** 2026-11-12
- **Component:** `econ-research` (reference checker and tests)
- **Change type:** Testing / Fixed
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change (branch `feat/econ-research-skill`)

## Motivation

After the [first topic test](2026-11-12-econ-research-first-topic-test.md), the user asked to run the fake-paper case and a research-idea case. For the idea, the user chose "a second-year-paper idea building on the Aiyagari literature" rather than a private project, so this log contains only public literature.

## What was run

**Case 2 (fake paper).** Prompt used: a summary of "the 2021 AER paper by Mehta and Lindqvist on gig-economy income risk and precautionary saving", which was invented for the test. Crossref (author and title query, 2020–2022) and OpenAlex (topic and author queries) returned no such paper. The correct response is to say that no such paper was found, give no summary, and offer the closest verified paper: Orland and Rostam-Afschar (2021, *JEBO*, 10.1016/j.jebo.2021.09.015, metadata only because OpenAlex had no abstract).

**Case 4 (vague interest to a question).** Ten OpenAlex searches across five candidate directions. Three candidates were kept and tested for closest papers, contribution, approach, main threat and feasibility:

1. Uninsured disaster (flood) risk to housing wealth in an Aiyagari-type model with housing: effects on precautionary saving and wealth inequality. Recommended.
2. Self-employment or platform income risk and precautionary saving. Judged largely covered: Audoly (2024, NY Fed Staff Report 1085, 10.59576/sr.1085) calibrates a search model with precautionary savings and self-employment risk, per its abstract.
3. Student debt and young households' wealth. Search results addressed student-loan repayment and default (Lochner and Monge-Naranjo 2015; Ionescu and Ionescu 2014; Dinerstein, Earnest, Koustas and Yannelis 2025) rather than general-equilibrium wealth inequality; judged provisional because the queries were few.

**Case 5 (is it done?) for candidate 1.** One more OpenAlex query. No paper found in these sources combines uninsured idiosyncratic disaster risk with a stationary Aiyagari-type equilibrium and the wealth distribution. Closest verified papers: Favilukis, Ludvigson and Van Nieuwerburgh (NBER w15988; general-equilibrium housing with idiosyncratic and aggregate risk and a realistic wealth distribution; its abstract does not mention disaster risk), Bakkensen and Barrage (NBER w23854; flood-risk beliefs and coastal home prices), Bagliano, Fugazza and Nicodano (2024, *IREF*; personal disaster risk over the life cycle; metadata only) and Beltrán, Kuralbayeva and Tipoe (2026, *JEG*; nearby floods and housing markets in England). The paper a referee would most likely raise is Favilukis et al. The main modeling threat: disaster risk is spatially correlated and partly insured (private insurance, public aid), so treating it as idiosyncratic and uninsured needs justification.

All eight papers named in cases 4 and 5 returned PASS from `verify_references.py`.

## Results

| Case | Result | Notes |
| --- | --- | --- |
| 2. Plausible but fake paper | Pass (self-graded) | No summary produced; closest real paper offered with read status |
| 4. Vague interest to a question | Pass (self-graded) | Three candidates tested; one recommended; one judged largely done; one flagged as provisional |
| 5. Is my idea done? | Pass (self-graded) | Closest papers named with what each does; likely referee objection and main threat stated; "open" claim limited to the sources searched |

No critical fail observed.

## Fixes

1. **HTML entities in Crossref records.** Crossref returned "Journal of Economic Behavior &amp; Organization". `verify_references.py` now decodes HTML entities in record fields. A unit test covers it.
2. **Records without a venue.** NBER working-paper records have no container title, which produced output such as "Going Under Water?. ". The record description now joins only the parts that exist.

## Files affected

- `skills/econ-research/scripts/verify_references.py`: the two fixes.
- `tests/test_research_contracts.py`: test for decoded entities.
- `CHANGELOG.md`: entry for these cases.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| Real-topic evaluation, cases 2, 4, 5 | Pass | Self-graded by the agent that ran them; no independent grader |
| Reference checker on live Crossref | Pass | 9 of 9 DOIs PASS (8 in cases 4–5, 1 in case 2) |
| Automated structural validation and unit tests | Pass | `python3 tests/validate_skills.py` and `python3 -m unittest discover -s tests -p 'test_*.py'` run locally after the fixes |
| GitHub Actions | Not run | Not yet run on the pushed branch at the time of writing |

## Known limitations and risks

- Self-graded; the same agent wrote the skill and ran the tests.
- The "open" judgment for candidate 1 rests on about a dozen queries in two sources and abstracts only; it is provisional, as stated in the answer.
- Case 6 (bibliography check through the agent) and case 7 (paywalled paper) remain unrun as conversations, although the checker itself was tested on a `.bib` file in the build log.

## Follow-up

- Run cases 6 and 7, and repeat cases 4–5 on the user's own project when one exists.
