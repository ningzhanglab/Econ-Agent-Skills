# 2026-11-16 — Slides: content file and speaker notes only on request

- **Date:** 2026-11-16
- **Component:** `econ-teaching` (`references/slides.md`)
- **Change type:** Changed
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

The user asked that the `_content.md` file and speaker notes not be delivered by default. The reply may offer them, but not every time.

## Changes made

- The content file (`<deck>_content.md`) is now produced only on request. Its format and sync rules are unchanged for when it is requested.
- Speaker notes were already on request only; unchanged.
- New rule: default delivery is `.tex` and `.pdf`. The reply may mention once, in one line, that a content file or speaker notes are available. Offer at most once per conversation, and not again after the user declined or did not take it up.

## Files affected

- `skills/econ-teaching/references/slides.md` — the content-file bullet and a new "Offering them" bullet.

## Behavior and compatibility

Decks no longer come with a `_content.md` by default. The bundle checker already checks the content file only if it exists, so no script change was needed.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| File / syntax inspection | Pass | Read the edited bullets in `slides.md` |
| Automated structural validation | Pass | `python tests/validate_skills.py`; `python -m unittest discover -s tests` |
| Real slide / domain evaluation | Not run | Editorial change; no deck built |
| GitHub Actions or other CI | Not run | Runs on push |

## Known limitations and risks

"Once per conversation" is guidance an agent follows within one chat. It cannot carry over between chats.

## Follow-up

None planned.
