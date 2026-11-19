# 2026-11-19 — Follow-up audit of link routing and skill helpers

- **Date:** 2026-11-19
- **Component:** Link editions, `econ-learn`, `econ-present`, `econ-research`, packaging and CI
- **Change type:** Changed / Fixed / Testing
- **Status:** Implemented locally
- **Related commit / PR:** See Git history for this change

## Motivation

The [combined link change](2026-11-19-combined-link-and-review-fixes.md) reduced the work for the first request. Its table still offered the same combined pages after the teaching skill was already loaded. The follow-up review also reproduced missing TeX dependencies going unreported, a reordered bibliographic title receiving PASS, and an untracked fixture entering a ZIP when Git could not list the checkout. The last published CI run passed. Its package download took 49 minutes and 5 seconds, which delayed checks that can run without TeX.

## Changes made

- **Combined link.** Offer a direct task page when the main teaching rules have already been read in the same chat. If a combined page is unavailable on a first request, the index names the main skill page and separate task page as an alternative. Both homework routes still provide the required field-guide links.
- **TeX checks.** The bundle checker and figure inventory recognize line-wrapped commands, starred graphics and literal unbraced inputs. They preserve the source line where the command starts. The bundle checker uses XeLaTeX for active `ctexbeamer` declarations and recognizes explicit frame overlays and relative overlay specifications. The content-file task explains when to compare with compiled PDF pages.
- **Reference checks.** A title with similar vocabulary and a different normalized word sequence now receives WARN. The task explains which fields the automated check covers and points to the existing ranking default for the reading list.
- **Distribution.** A Git checkout with an unavailable tracked-file list stops packaging before opening a ZIP for writing. A plain copy outside Git still packages its non-junk files. CI checks generated links before installing TeX. The README now points to the completed homework and slides evaluations.

## Files affected

- `tools/build_link_editions.py`, generated `link/` pages and `tests/test_link_editions.py`.
- `shared/scripts/check_tex_bundle.py` and its two generated copies, `skills/econ-learn/scripts/inventory_tex_figures.py`, `skills/econ-present/tasks/content-file.md` and `tests/test_professor_contracts.py`.
- `skills/econ-research/scripts/verify_references.py`, `skills/econ-research/tasks/literature-search.md` and `tests/test_research_contracts.py`.
- `tools/build_skill_zips.py`, `tests/test_skill_zips.py`, `.github/workflows/validate-skills.yml`, `README.md` and `CHANGELOG.md`.

## Behavior and compatibility

The existing combined and per-skill addresses remain valid. A local comparison measured the pages named by the combined entry after the main teaching rules had been read. Other guides and course sources are outside the byte counts.

| Next request | Previous combined link | Revised task-only link |
| --- | --- | --- |
| Explain a standalone term | 16,300 bytes | 2,497 bytes |
| Explain or solve homework | 21,614 bytes | 7,895 bytes |

The first-use routes retain their consolidated pages. Without a skill, the baseline uses zero skill pages and none of these checks. The route comparison measured downloaded rule bytes, with no estimate of token counts or client speed.

## Verification and evidence

| Check | Result | Evidence |
| --- | --- | --- |
| Build and validation | Pass | Ran the generators, their freshness check, four-skill structural validation and the Git whitespace check. |
| Unit tests and TeX execution | Pass | 78 tests, zero skips. The nested-figure fixture compiled using the supported multiline and unbraced forms. The missing-file fixture produced two diagnostics, up from zero. |
| Public reference metadata | Pass | Checked the published title at the [American Economic Association](https://www.aeaweb.org/articles?id=10.1257/aer.20190623). Its correct title passes both checks. The intentionally reordered version moves from PASS to WARN. The comparison used the publisher title as the fixture. |
| ZIP build and degraded Git | Pass | Built all four ZIPs. With simulated Git failure, the previous tool included the untracked fixture. The revised tool refused to package it, and a regression test confirmed an existing archive stays intact. |
| Published links and CI | Previous commit only | The previous [CI run](https://github.com/ningzhanglab/Econ-Agent-Skills/actions/runs/44494091245) passed. On this recheck, the web reader fetched the published index while missing the combined homework page. This revision was tested locally. |
| Fresh model comparison in the user's Project | Not run | The route, metadata and executable comparisons do not measure generated answer quality or the user's client's ability to fetch a page. |

## Known limitations and risks

The fallback links help only when the client can read an alternative page. The early CI check catches stale link files before installation. It does not change Ubuntu's package download time. The TeX helpers continue to require manual review for dynamic dependencies.

## Follow-up

Compare the two routes in a fresh Project chat before expanding the combined pages to more tasks. A future CI run can show whether the slow package downloads recur.

## Correction (2026-11-19, after publication)

- The task-only route described under "Combined link" was removed in a later change; see [Drop the task-only route](2026-11-19-drop-task-only-route.md). The fallback links remain.
- "Behavior and compatibility" left out that the index grew from 2,060 to 2,486 bytes, which every first-use route reads.
- The "Published links and CI" row mixed two results. The CI run for the previous commit (4d211ea) passed. The web reader's fetch of the published combined homework page failed.
- The public GitHub API gives 50 minutes and 15 seconds for the whole TeX and Poppler installation step of that run. The 49 minutes and 5 seconds in "Motivation" could not be confirmed from public data.
