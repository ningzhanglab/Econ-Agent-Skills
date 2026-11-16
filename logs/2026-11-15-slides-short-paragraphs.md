# 2026-11-15 — Slides: short paragraphs allowed

- **Date:** 2026-11-15
- **Component:** `econ-teaching` (slides reference)
- **Change type:** Changed
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

After the fixed bullet count was removed ([2026-11-15 — Slides: no fixed bullet count](2026-11-15-slides-no-bullet-cap.md)), the **Text** item in `references/slides.md` still said "no paragraphs." The user said slides may also have paragraphs, but not very long ones.

## Changes made

- "Each slide", **Text:** a slide may use a short paragraph of two or three sentences where prose carries the point better than bullets, for example an intuition, an analogy or a figure's message. Long paragraphs are still not allowed. Bullets remain the default form, with no fixed count and with sub-bullets allowed.

## Files affected

- `skills/econ-teaching/references/slides.md` — the **Text** item.
- `link/econ-teaching.md` — regenerated with `tools/build_link_editions.py`.
- `CHANGELOG.md`, this log.

## Behavior and compatibility

New decks may mix bullets with a short paragraph. "Two or three sentences" gives a concrete bound for "not very long." The content file needs no change: a paragraph is written as plain text, as figure messages already are. The bundle checker does not inspect text and is unaffected.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| File / syntax inspection | Pass | Read the edited item; searched the skill, template and tests for other statements against paragraphs and found none |
| Automated structural validation | Pass | `python tests/validate_skills.py` |
| Unit tests | Pass | `python -m unittest discover -s tests -p 'test_*.py'` |
| Real slide / domain evaluation | N/A | Wording change requested by the user; no deck rebuilt for it |
| GitHub Actions or other CI | Not run | Not pushed at the time of writing |

## Known limitations and risks

The "two or three sentences" bound is a judgment call, not a check; the rendered-page review for small type remains the practical guard.

## Follow-up

None planned.
