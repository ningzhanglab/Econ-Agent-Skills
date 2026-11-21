# 2026-11-20 — Shorter Project router

- **Date:** 2026-11-20
- **Component:** Link editions, README router block
- **Change type:** Changed
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

The user found the router block for the Project instructions too long (2,153 bytes).

## Changes made

- The preamble is cut to three sentences. It keeps the rule from the [per-message fix](2026-11-20-route-every-message.md): every message, including later ones, opens its page unless that page was already opened in this chat. It also keeps the `Skill:` line, the report when a page fails to open, and LaTeX for all math. The pointer to the index page is dropped; the per-skill pages remain the fallback named on each route page.
- The nine route descriptions in `ROUTES` are shortened, for example "Homework, a past exam, or exam prep". The index page uses the same descriptions.
- The full URLs stay. A chat app's fetch tool may open only addresses written out in full, so the router does not build them from a shared base address.
- The test limit for the router drops from 2,500 to 1,600 bytes, and the test still checks for the per-message wording.

## Files affected

`tools/build_link_editions.py`, `tests/test_link_editions.py`, regenerated `link/` pages and the README router block, `CHANGELOG.md`.

## Behavior and compatibility

The router is 1,575 bytes, of which about 860 are the nine URLs. The page addresses are unchanged, so the old block keeps working, but the new block must be pasted to get the shorter text. The route pages themselves change only in their edition code.

## Verification and evidence

| Check | Result | Evidence or reason |
| --- | --- | --- |
| Generators, validation, unit tests, whitespace | Pass | `python3 tools/check_all.py`: all PASS. |
| Routing with the shorter descriptions in the user's Project | Not run | Case 6 and the other cases in `tests/link-route-evaluation.md` cover it. |

## Known limitations and risks

Shorter descriptions leave the model less text to choose a page from. The likeliest confusions are "Why something holds" against "A research paper" for a question about one paper's mechanism, and "Editing my own writing" against homework for "make the solution shorter". Either page links the other.
