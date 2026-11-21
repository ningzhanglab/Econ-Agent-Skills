# 2026-11-20 — Pick a page for every message, and show it on every reply

- **Date:** 2026-11-20
- **Component:** Link editions, README, manual evaluation cases
- **Change type:** Changed / Fixed
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

The user reported that the agent sometimes forgets to use the skills when requests come in sequence in one chat. Two parts of the [link-first routes](2026-11-20-link-first-routes.md) allowed this:

- The router said "For each request, open the one page below". A model that had opened one page earlier in the chat could treat it as covering a later request of another kind, or skip the pages altogether.
- The `Skill edition:` line was asked for only the first time a skill was used. Later replies carried no sign of whether a page had been followed, so neither the model nor the user could see a lapse.

## Changes made

- **Router (README block and index).** "For every message, including later ones in the same chat, pick the page below that matches it and follow it. Open it if it has not been opened in this chat, even when another page was; reuse it if it has."
- **Every reply carries one line.** Route pages ask for `Skill: <route> · <code>` at the start of every reply that follows them. Skill pages ask for `Skill: <skill> · <code>`. This replaces the first-use-only `Skill edition:` line. A missing line shows the user that the page was not used.
- **Route pages say their scope.** Each page states that it covers one kind of request, and that a later message of another kind needs that kind's page first.
- **Evaluation.** `tests/link-route-evaluation.md` adds case 6: three requests of different kinds in one chat. It checks the page and the `Skill:` line on each reply.
- **Test.** `test_link_editions.py` checks the per-reply line on every page, the scope sentence on route pages, and the per-message wording in the router.

## Files affected

`tools/build_link_editions.py`, regenerated `link/` pages, `README.md` (router block, "Checking what loaded"), `tests/test_link_editions.py`, `tests/link-route-evaluation.md`, `CHANGELOG.md`.

## Behavior and compatibility

Every skill-based reply now starts with one short line instead of only the first. The router block changed, so it must be pasted into the Project instructions again; it is 2,153 bytes. No skill rule changed.

## Verification and evidence

| Check | Result | Evidence or reason |
| --- | --- | --- |
| Generators, validation, unit tests, whitespace | Pass | `python3 tools/check_all.py`: all PASS. |
| Sequence behavior in the user's Project | Not run | Needs the user's chat client; this is case 6 of `tests/link-route-evaluation.md`. |

## Known limitations and risks

Instructions cannot force a fetch: a model can still skip one. The per-reply line makes a lapse visible but does not prevent it. The line also adds a little text to every reply.

## Follow-up

Run case 6. If later messages still skip their page while showing the `Skill:` line, the router's row descriptions need work. If they also drop the line, the instruction itself is not followed, and a stronger mechanism (for example, installing the skills) is the remaining option.
