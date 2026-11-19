# 2026-11-19 — Combined skill link and review fixes

- **Date:** 2026-11-19
- **Component:** Link editions, `econ-present`, `econ-research`, CI
- **Change type:** Changed / Fixed / Testing
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

The user keeps one link in a chat Project for all four skills. A public-link simulation found that GitHub returned the current index, skill pages and required task pages. A separate web reader missed some downstream pages and returned the previous edition of the slides skill. The audit also reproduced Poppler crop and filename failures, two reference-checker failures and a GitHub Actions failure compiling the English notes template.

## Changes made

- The existing `link/econ-skills.md` URL now serves a concise task table. It routes standalone terms and screenshots, and homework and exams, directly to generated pages that include both the main teaching instructions and the task procedure. Homework continues to link to the required field guide. Cross-skill routing and the edition and file-read lines are explicit.
- Each linked Markdown page gets a generated copy with complete URLs for downstream pages and assets. Skill entry pages no longer need a full file index. The edition code now also covers the generator, so a change to the link wrapper or routing can be distinguished from a cached copy.
- Poppler now renders the PDF's visible page when it differs from the media box and resolves output names such as `figure.v2.png` and `figure.v3.PNG` correctly.
- The BibTeX checker reads parenthesized entries. Crossref date comparison handles records that mix a year-only date with a dated month in the same year.
- The GitHub Actions runner installs the Latin Modern and additional TeX packages used by the default English notes template.

## Files affected

- `tools/build_link_editions.py` and generated `link/` pages.
- `skills/econ-present/scripts/crop_figure.py` and `skills/econ-research/scripts/verify_references.py`.
- `.github/workflows/validate-skills.yml`, regression tests for link generation, Poppler and the reference checker, plus `README.md` and `CHANGELOG.md`.

## Behavior and compatibility

The combined URL, four direct skill URLs and renamed-skill redirects keep their existing addresses. Installed skill instructions and templates keep their existing text. The consolidated pages are generated from the same skill and task sources. Downloadable releases follow the existing release workflow.

A local traversal used the same requests for the previous and revised routes. Each next URL appeared in a page already opened. The no-skill baseline opens zero skill pages. The comparison measured navigation, with no grading of model answers or timing.

| Request | Previous | Revised |
| --- | --- | --- |
| Explain a standalone term | 3 pages, 27,555 bytes | 2 pages, 18,360 bytes |
| Solve a time-series homework question | 4 pages, 39,427 bytes | 3 pages, 31,116 bytes |

The total index went from 4,812 to 2,060 bytes. Course sources, optional examples and output resources are outside these counts.

## Verification and evidence

| Check | Result | Evidence |
| --- | --- | --- |
| Generation, structure and whitespace | Pass | `python3 tools/build_all.py`, `python3 tools/build_all.py --check`, `python3 tests/validate_skills.py` (4 skills), and `git diff --check`. |
| Unit tests | Pass | `python3 -m unittest discover -s tests` ran 75 tests with no skips. The Poppler regression compared PNG bytes to the visible-page render and covered both dotted filenames. |
| Prior CI failure | Confirmed | [The previous run](https://github.com/ningzhanglab/Econ-Agent-Skills/actions/runs/44491043736) failed with `File lmodern.sty not found`. |
| Revised GitHub Actions and published URLs | Not run before push | The new workflow and public URLs can be checked once the commit reaches `main`. |
| Fresh model comparison in the user's Project | Not run | The local route traversal and regression tests exercise mechanics. They do not measure how a particular chat client follows the page or the quality of the resulting economics answer. |

## Known limitations and risks

A web reader may still return an older page or fail to fetch a required page. The two consolidated pages reduce the number of required requests but are longer than their individual task pages.

## Follow-up

In a fresh Project chat, compare the edition code, file list and answer for one plain term and one homework question. Keep additional bundled routes contingent on that evidence.
