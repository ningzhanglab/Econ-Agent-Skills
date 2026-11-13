# 2026-11-12 — Fixes from the Independent econ-research Rerun

- **Date:** 2026-11-12
- **Component:** `econ-research` (v0.1)
- **Change type:** Fixed
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change (not committed at the time of writing)

## Motivation

The [independent rerun](2026-11-12-econ-research-independent-rerun.md) graded all seven cases Pass but recorded ten findings. The user asked to fix all of them. Findings 1–3 were observed checker failures on real Crossref records; findings 4–10 were wording gaps in which an agent following the skill could plausibly go wrong.

## Changes made

| Finding | Fix |
| --- | --- |
| 1 Year rule and checker reject a correct volume year | Checker: `check_year` compares the entry's year with every date in the record (print, online, issued, published, journal-issue). A year one after the latest date passes **with a note** when that date is in November or December; any other mismatch is still WARN. Literature Search: cite the volume/issue year; Crossref dates are evidence |
| 2 Renamed journal gives a false WARN | Checker: compares against `container-title` and `short-container-title`; a remaining venue difference is a note, not a WARN, since DOI and title already identify the paper. Literature Search: "The journal was renamed" case |
| 3 Failed lookup exits 0 | Checker: exit status 2 if any ERROR, then 1 if any FAIL, else 0. ERROR, SKIP and notes documented in the script, Literature Search and README |
| 4 "Abstract only" can be false | Literature Search, Read: check that an abstract is real authors' text, name where it came from, otherwise label metadata only |
| 5 "Most important" undefined; citation sort returns noise | Literature Search, Query design: sort by citations only with a title/abstract filter; rank "most important" by relevance then influence, naming the count's source |
| 6 Published version missing from Crossref/OpenAlex | Literature Search, Common cases: check RePEc/IDEAS, JSTOR or the journal before citing the working paper |
| 7 Aggregator years differ | Literature Search, Common cases: take year, volume and pages from Crossref or the publisher |
| 8 Scoping wording differs | Research Questions: for broad brainstorming, stating assumptions and proceeding is allowed; explains how this fits the one-question rule in `SKILL.md` |
| 9 Reading PDFs not operationalised | Literature Search, Read: say when a reachable PDF could not be read; keep the lower read label; ask before downloading where required |
| 10 One article, two DOIs | Literature Search, Screen: always apply the title step because a publisher DOI and a JSTOR DOI can coexist |

`tests/research-evaluation.md` case 6 gains optional harder fixture entries (late-December print year, former journal name) and a pass condition that the agent must not tell the user to change either.

## Files affected

- `skills/econ-research/scripts/verify_references.py`: year and venue checks, exit status, docstring.
- `skills/econ-research/references/literature-search.md`: findings 1–7, 9, 10.
- `skills/econ-research/references/research-questions.md`: finding 8.
- `tests/test_research_contracts.py`: five regression tests.
- `tests/research-evaluation.md`: case 6 fixture and pass condition.
- `README.md`: checker statuses include ERROR.
- `CHANGELOG.md`: entry for the rerun and these fixes.

## Behavior and compatibility

- Checker output: a correct volume year after a late-year print date now gives PASS with a note instead of WARN; a venue difference gives PASS (or the status set by other fields) with a note instead of WARN. Scripts that relied on exit status 0 after network failures now get 2.
- A wrong year that is one after a November/December print date is no longer a WARN; the note asks the user to confirm with the issue. This is the trade-off for not flagging correct volume years.
- A genuinely wrong venue with a correct DOI and title is now a note rather than a WARN; the reference tells the agent to report notes.
- No change to the core guarantees in `SKILL.md`.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| File / syntax inspection | Pass | Reviewed the diff of all touched files |
| Automated structural validation | Pass | `python3 tests/validate_skills.py` and the full unittest suite; results recorded below |
| Unit tests | Pass | `python3 -m unittest tests.test_research_contracts -v`: 11 tests OK (5 new) |
| Live checker on the rerun's fixture | Pass | Against Crossref on 2026-11-12: Dustmann et al. 2022 → `PASS` with volume-year note (was WARN); Kaplan et al. 2016 → `WARN year 2016 vs record 2018`; fake DOI → FAIL; no-DOI → SKIP; Card (1990) with correct DOI and former journal name → `PASS` with venue note (was WARN); blocked network → `ERROR`, exit 2 (was 0) |
| Real domain evaluation | Not run | Wording changes only; the seven cases were not rerun after the fix |
| GitHub Actions or other CI | Not run | Not committed or pushed by this session |

## Known limitations and risks

- The late-year rule is a heuristic based on one observed pattern (OUP issue-1 print dates); other publishers may use other conventions.
- Venue differences are now softer; an agent that ignores notes would miss a wrong venue.

## Follow-up

- Rerun case 6 with the harder entries through an agent, not only the script.
- If other publishers show volume-year mismatches outside November/December, widen the rule with a test for each.
