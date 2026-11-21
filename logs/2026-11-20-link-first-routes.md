# 2026-11-20 — Link-first: one self-contained page per kind of request

- **Date:** 2026-11-20
- **Component:** Link editions, README, AGENTS.md
- **Change type:** Changed / Testing / Documentation
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

The user said they mainly use the skills by pasting links into a chat Project, not by installing them. The v2 design assumes an installed skill that reads `SKILL.md`, then a task page, then guides as needed. Over links, each of those reads is a separate web fetch that can fail or return a stale page. Earlier logs recorded both failures. Before this change, a request needed 2–4 fetches: the index, then a skill page or one of two combined pages, then task pages or guides. 49 of the 95 logs dealt with this link layer.

## Changes made

- **Route pages.** `tools/build_link_editions.py` now builds pages from one `ROUTES` table: nine pages in `link/route/`, one per kind of request. Each page holds the skill's `SKILL.md` followed by every task page, guide and template that request needs. Links between those files become anchors on the same page; other files keep full addresses as fallbacks. The two old special-case combined pages (`link/econ-learn/term-or-screenshot.md`, `homework-exam.md`) now point to their routes.
- **Router in the Project instructions.** The same table generates a router block (2.1 KB) inside `<!-- link-router -->` markers in the README. The user pastes it into the Project instructions, so each request goes straight to its page: one fetch instead of two or more. Page addresses are stable, so the block needs re-pasting only when the block itself changes. The index page `link/econ-skills.md` lists the same routes plus the four skill pages as fallbacks.
- **Fewer reply lines.** The instruction to end replies with the list of files read is removed. With one page per request, the page name already says what was read. The `Skill edition:` line stays, to detect a stale cached page.
- **Homework includes file delivery.** Submissions are often files, so the homework page also holds `tasks/deliver-file.md`.
- **Manual cases.** `tests/link-route-evaluation.md` has five requests to run in the user's Project. For each, it records the page expected, the pages fetched, the edition code and answer quality.

## Files affected

- `tools/build_link_editions.py`: `ROUTES`, `render_route`, `render_router`, `readme_with_router`, the route note; the per-task special case is removed.
- `link/`: nine new route pages, regenerated skill and index pages, two moved-page notices.
- `tests/test_link_editions.py`: route content, size budget, every task and guide on some route, router current in the README, moved pages.
- `README.md` (paste-a-link section, router block, status line, evaluation links), `AGENTS.md` (the router block is generated), `CHANGELOG.md`, `tests/link-route-evaluation.md`.

## Behavior and compatibility

| Route | Page size |
| --- | --- |
| term | 16,259 bytes |
| paper | 17,214 |
| explain (with derive) | 25,431 |
| writing | 26,035 |
| research | 27,115 |
| slides (with the template) | 28,661 |
| lecture | 36,904 |
| course | 43,345 |
| homework (four field guides and file delivery) | 47,158 |

- A test keeps every route under 50,000 bytes.
- Compared with before, the term request reads about the same bytes in one fetch instead of two. A homework request reads more bytes (47 KB against about 31 KB), but in one fetch instead of three: it now carries all four field guides and file delivery, so the agent never has to pick or fetch a guide.
- Installed skills are unaffected: no file under `skills/` changed.
- Old addresses keep working: the index, the four skill pages, the renamed-skill redirects and the two old combined pages, which now point to their routes.
- The user's current Project instructions still work, through the index, but need two fetches per request until the new router block is pasted.

## Verification and evidence

| Check | Result | Evidence or reason |
| --- | --- | --- |
| Generators, validation, unit tests, whitespace | Pass | `python3 tools/check_all.py`: all four steps PASS. |
| Route content | Pass | Tests assert that each route page contains its `SKILL.md` body and every listed file verbatim, apart from the link rewriting. They also check that no included file is linked as a separate fetch, and that every task page and guide of every skill is on some route. |
| Spot read | Pass | In `route/homework.md`, the skill's routing table and the homework procedure link to the included guides and file delivery by anchor. The slides template appears in a `tex` code block. |
| Fetch and answers in the user's Project | Not run | Needs the user's chat client; the cases are in `tests/link-route-evaluation.md`. |
| GitHub Actions | Not run | Not pushed when this log was written. |

## Known limitations and risks

- The router depends on the model choosing the right row from a one-line description. A misread sends it to a page without the procedure it needs. That page still links everything else, at the cost of another fetch.
- Larger pages may be truncated by a web reader with a low size limit. 47 KB is within common limits, but this has not been measured in the user's client.
- Anchors such as `#defaults` can match more than one heading on a combined page. A model reading the raw text sees the surrounding section, but the anchor alone is ambiguous.

## Follow-up

Paste the new router block into the Project and run the five cases in `tests/link-route-evaluation.md`. If they pass, the per-skill pages and the index can be described as fallbacks only.
