# 2026-11-16 — Slides: no default talk length

- **Date:** 2026-11-16
- **Component:** `econ-teaching` (`references/slides.md`)
- **Change type:** Removed
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

The user asked whether slides default to a 20-minute talk and, if so, to remove that: the deck should tell the story fully, with no length limit. `references/slides.md` did default to "a 20-minute reading-group talk ... about 12–15 main slides (1.5–2 minutes each)".

## Changes made

- Plan step 1 is now "Purpose and audience": default is a reading-group talk to PhD students with no default length or slide count; use as many main slides as telling the story clearly needs. A length or slide count the user states is still followed.
- Removed "Recheck that the slide count still fits the time" from revision step 3 and "the slide count fits the time" from the delivery check.
- The final check now says a length or timing the user stated is met (instead of "overrides the default slide count").

## Files affected

- `skills/econ-teaching/references/slides.md` — the four sentences above.

## Behavior and compatibility

Decks are no longer sized to 12–15 main slides by default; the story decides the count. User-stated lengths behave as before. The template has no length rule and is unchanged.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| File / syntax inspection | Pass | Searched `skills/` for "20-minute", "minute" and "fits the time"; no remaining hits |
| Automated structural validation | Pass | `python tests/validate_skills.py`: 3 skills passed |
| Real slide / domain evaluation | Not run | Editorial change; no deck built |
| GitHub Actions or other CI | Not run | Runs on push |

## Known limitations and risks

Without a length anchor, a deck can run long; the story-first planning and Appendix rules remain the only check on that.

## Follow-up

None planned.
