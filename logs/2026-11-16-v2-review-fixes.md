# 2026-11-16 — v2 review fixes: narrower guide routing and leftovers

- **Date:** 2026-11-16
- **Component:** `econ-learn`, `shared`, tools, repository documents
- **Change type:** Changed / Fixed
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

The user asked for a full check of the repository after the v2 merge. The first comparison run had shown agents opening two guides beyond the task page in every case, including a field guide and the figures guide for a bare term. The check also found wording left from v1.

## Changes made

- **Guide routing in `econ-learn/SKILL.md`.** The guide table now opens with "A guide is opened only for its situation. A bare term, a quick step, or a question answered from text already in view needs none", and each row states its situation more narrowly (field guides for a Homework solution, a derivation or a whole lecture where a field's traps matter; reading sources for a PDF, TeX or Word file read with care). `tasks/term-or-screenshot.md` says a bare term needs that page only.
- **`econ-learn/SKILL.md`:** the lists of helper scripts and worked examples are gone, because the task pages and guides that use them already link them. With the added routing sentences the file is about the same length (1,935 to 1,920 words).
- **Defaults sections** added to `tasks/course.md` (with a clearer title and a pointer to the cross-lecture page) and named in `tasks/learning-log.md`.
- **Shared default example** changed from "no footer", which only fits slides, to "shorter answers".
- **Leftovers:** "reference files" in the link index note and the builder's docstring; "references that use them" in `econ-research`; a stray blank line that split a list in `guides/large-files.md`; old skill names in `logs/TEMPLATE.md` and the title of `tests/writing-evaluation.md`; an old link label in `STORAGE_POLICY.md`; `python` written as `python3` in the README's commands.
- `DESIGN_V2.md` records the guide finding. The merged local branch `rebuild-v2` was deleted.

## Files affected

`skills/econ-learn/SKILL.md`, `tasks/term-or-screenshot.md`, `tasks/course.md`, `tasks/learning-log.md`, `guides/large-files.md`, `guides/sources-and-versions.md`; `skills/econ-research/SKILL.md`; `shared/defaults.md` and the four `SKILL.md` copies; `tools/build_link_editions.py`; `tests/test_docx_math.py`; `link/`; `README.md`, `DESIGN_V2.md`, `STORAGE_POLICY.md`, `logs/TEMPLATE.md`, `tests/writing-evaluation.md`, `CHANGELOG.md`.

## Behavior and compatibility

Agents should open fewer guides for small requests. No rule about teaching, notation, files or storage changed. `tests/test_docx_math.py` no longer requires the Word reader to be named in `SKILL.md`; it is still required in `guides/reading-sources.md`.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| File / syntax inspection | Pass | Searched the skills, tools and documents for v1 names and wording; read `tasks/course.md` and the end of `guides/large-files.md` |
| Automated structural validation | Pass | `python3 tools/build_all.py`, `python3 tests/validate_skills.py` (4 skills), `python3 -m unittest discover -s tests` (66 tests) |
| Real slide / domain evaluation | Not run | Whether the narrower routing reduces the guides opened was not re-run |
| GitHub Actions or other CI | Not run | Not checked |

## Known limitations and risks

The narrower wording may also keep an agent from opening a guide when it would have helped. `tests/professor-evaluation.md` still words its cases for v1. `econ-present` remains untested on a real paper.

## Follow-up

Re-run the three comparison cases and count the files read.
