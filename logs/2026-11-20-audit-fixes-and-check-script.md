# 2026-11-20 — Reference-checker fixes, rule tidy-up and one check command

- **Date:** 2026-11-20
- **Component:** `econ-research`, `econ-learn`, `econ-present`, `econ-write`, link editions, repository maintenance
- **Change type:** Fixed / Changed / Testing
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

The user asked for an audit of the skills, then for every finding to be fixed. The audit reproduced these problems:

- **Reference checker, wrong author passed.** The first-author check used a substring test, so a `.bib` first author `Liu` or `Williams` passed against a Crossref family name `Li`. An uppercase `AND` between authors was not split, so a wrong first author also passed.
- **Reference checker, correct entries failed.** LaTeX accents were broken into separate words (`Pol{\'\i}tica` became `pol tica`), so a correct entry `Pol{\'\i}tica Monetaria` / `P{\'e}rez` received FAIL, and `Gal{\'i}` against `Galí` received WARN. The literature task tells the agent to treat a FAIL as a possibly fabricated paper.
- **Reference checker, rate limits.** A Crossref 429 or 5xx response was reported at once as ERROR (unchecked), and a DOI listed twice was fetched twice.
- **A pinned preference was not checked.** `tests/test_shared_and_defaults.py` had the key `econ-learn/tasks/homework-exam.md` twice in one dict, so the first list ("same notation + the same or an equivalent valid Slide method + sufficient steps") was silently dropped.
- **Wording.** `econ-write` said "Saving and compiling follow the user's folder rules", but no such rules exist in the skill. The practice-question rule was stated in both `econ-learn/SKILL.md` and the homework page, with slightly different wording. `econ-present` allowed "a page for a direct quotation" and also banned any source line on a text-only slide.
- **Reading cost.** The homework route read a section on using Homework to teach a lecture, which does not apply to solving a problem. `econ-present/SKILL.md` repeated the Appendix-button LaTeX already shown in the slides template. `econ-research` restated two shared guarantees. Each linked reply was asked to end with a list of files read, even when it opened none.

## Changes made

- **`verify_references.py`.** The first author matches when the record's family name appears as whole words in the `.bib` first author. Authors split on `and` in any case. LaTeX accent commands and special letters (`\i`, `\o`, `\ss`, …) keep their base letter, and braces no longer split words. Lookups retry a 429, 5xx or network failure up to three times with a short wait (honouring a numeric `Retry-After`, capped at 10 seconds). Each DOI is fetched once per run.
- **Tests.** Five new reference-checker tests: whole-surname match, multi-word surnames, accents in title and author, retry then success, no retry on a 400 and give-up after three network failures, and one lookup per DOI. The duplicate dict key is merged, so the dropped pin is checked again. The Homework "only when" contract now reads the page the rule moved to.
- **`econ-learn`.** "Homework as a guide to what matters" moved from the homework page to [Whole lecture](../skills/econ-learn/tasks/whole-lecture.md#homework-in-a-lecture) as "Homework in a lecture". The homework page keeps what applies to tutoring a problem (hints at the requested depth, labelling invented exercises) and links to the moved section. The homework page's exam-preparation default is removed; the practice-question default in `SKILL.md` (pinned) is the one statement.
- **`econ-present`.** A direct quotation carries its page in parentheses, and the ban on source lines says that this is not one. The Appendix-links rule points to the template for the LaTeX instead of repeating it.
- **`econ-write`.** A file made from the report template is saved where the Defaults say, compiled and looked at; if compilation fails, the `.tex` is delivered with the reason.
- **`econ-research`.** Rule 4 points to "Honesty about coverage" instead of repeating it; rule 5 drops the sentence that restated shared guarantee 5.
- **Link editions and README prompt.** The closing line naming skill files is asked for only in a reply that opened skill pages.
- **`tools/check_all.py`.** One command runs the generators, structural validation, the unit tests and `git diff --check`, printing each outcome. `AGENTS.md` and the README name it.

## Files affected

- `skills/econ-research/scripts/verify_references.py`, `tests/test_research_contracts.py`.
- `skills/econ-learn/tasks/homework-exam.md`, `skills/econ-learn/tasks/whole-lecture.md`, `tests/test_professor_contracts.py`, `tests/test_shared_and_defaults.py`.
- `skills/econ-present/SKILL.md`, `skills/econ-write/SKILL.md`, `skills/econ-research/SKILL.md`.
- `tools/build_link_editions.py` and generated `link/` pages; `tools/check_all.py`; `AGENTS.md`, `README.md`, `CHANGELOG.md`.

## Behavior and compatibility

- `.bib` entries with LaTeX accents that previously received FAIL or WARN now PASS when they match. Entries whose first author only contains the record's surname as a substring now receive WARN. A rate-limited run takes longer but reports fewer ERROR entries. The command-line interface and exit codes are unchanged.
- The combined homework page is 20,217 bytes, down from 21,614. `whole-lecture.md` grew by the moved section. The index is 2,433 bytes (was 2,358) and each linked skill page about 90 bytes longer, from the reworded closing-line instruction.
- Users who pasted the README's Project prompt keep the old "list the files at the end" instruction until they paste the new one.
- No preference the user asked for changed; every pinned phrase is still present, and one more is now actually checked.

## Verification and evidence

| Check | Result | Evidence or reason |
| --- | --- | --- |
| Generators, validation, unit tests, whitespace | Pass | `python3 tools/check_all.py`: build PASS, structural validation PASS, unit tests PASS (84 tests), `git diff --check` PASS. |
| Audit reproductions | Pass | The same calls that showed the bugs now give: `Liu`/`Williams` vs `Li` WARN, `AND` with a wrong first author WARN, `Gal{\'\i}` and `Gal{\'i}` vs `Galí` PASS. |
| Live Crossref lookup | Pass | `verify_references.py --doi 10.1257/aer.20190623 --doi 10.1257/AER.20190623` returned PASS twice from one fetch. Only the DOI was sent. |
| Markdown anchors | Pass | A scratch script resolved every `file.md#anchor` link in `skills/` and the root documents, including the new `#homework-in-a-lecture`. |
| GitHub Actions | Not run | Not pushed when this log was written. |
| Fresh model comparison in the user's Project | Not run | Needs the user's chat client. It remains the open follow-up from the three 2026-11-19 logs. |

## Known limitations and risks

- The accent handling covers the standard LaTeX accent commands, not arbitrary macros in author fields.
- The retry waits at most about 20 seconds per DOI before reporting ERROR.
- Moving the Homework section is a reading-cost change supported by byte counts and the user's request, not by an observed answer-quality failure.

## Follow-up

Run the fresh Project comparison (combined page versus separate pages, first and second request) and paste the new README prompt into the Project before it.
