# 2026-11-15 — Slides: revising, figures and the bundle check

- **Date:** 2026-11-15
- **Component:** `econ-teaching`
- **Change type:** Changed
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

The user asked to audit the slide-making workflow after the Jones and Tonetti deck. Auditing `references/slides.md` against that session found gaps beyond source handling ([2026-11-15 — Source before building](2026-11-15-slides-source-before-building.md)):

- Nothing described revising an existing deck, which is how the stale version surfaced.
- Nothing said how to get a paper's figures (crop from the PDF page) or where to keep them. The revised deck used `\graphicspath`, and the skill's own `check_tex_bundle.py` rejected it; the slides reference never mentioned that checker.
- "Look at each rendered page" had no fallback when no renderer is installed.

## Changes made

- `references/slides.md`: new section "Revising an existing deck" (keep a copy, re-verify the source version, put additions in Backup first, list old versus new numbers in the handover); figures are cropped from the inspected PDF page into a folder beside the deck and called by relative path; pre-delivery checks add the bundle checker with `--compile` and a handover note for any pages not viewed.
- `templates/simple-slides.tex`: comment on loading `graphicx` and using relative figure paths.
- `link/econ-teaching.md` rebuilt.

## Files affected

`skills/econ-teaching/references/slides.md`, `skills/econ-teaching/templates/simple-slides.tex`, `link/econ-teaching.md`, `CHANGELOG.md`, this log.

## Behavior and compatibility

Only deck requests change. Decks that already use relative figure paths are unaffected.

## Verification and evidence

| Check | Result | Evidence or reason |
| --- | --- | --- |
| File / syntax inspection | Pass | Re-read the edited sections |
| Bundle checker on the real deck | Pass after fix | Failed on `\graphicspath` and 7 figures, passed with relative paths and `--compile` |
| Automated structural validation | Pass | `python3 tests/validate_skills.py` |
| Unit tests | Pass | `python3 -m unittest discover -s tests -p 'test_*.py'` |
| Real slide / domain evaluation | Not run | Not retried in a fresh chat |
| GitHub Actions or other CI | Not run | Not checked |

## Known limitations and risks

- The rules are in a reference file and rely on the agent opening it.
- The checker verifies files and compilation, not whether a figure is the right one.

## Follow-up

Regenerate a paper deck in a fresh chat from only a link and check the version statement, the request for the PDF, and the bundle check.
