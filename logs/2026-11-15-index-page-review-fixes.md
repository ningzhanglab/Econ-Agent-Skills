# 2026-11-15 — Review fixes for the index page and missing-skill notices

- **Date:** 2026-11-15
- **Component:** link index, `econ-research`, `econ-writing`, README
- **Change type:** Fixed
- **Status:** Implemented; not yet tried in a real chat
- **Related commit / PR:** See Git history for this change

## Motivation

The user asked for a recheck of the day's changes ([paper assessment boundary](2026-11-15-teaching-paper-assessment-boundary.md), [paper equations not seen](2026-11-15-paper-equations-not-seen-upfront.md), [link index page](2026-11-15-link-index-page.md)). Reading the diffs together found three problems, all found by reading the text, not seen in a chat:

1. **Index mode against "not installed".** With the index in a Project's instructions, every skill is reachable. But a skill page opened through it still says what to do when another skill "is not installed". A follow-up later in the chat (for example, a literature question after a teaching answer) could hit that rule and stop, which is the case the index was built for.
2. **Two edition-line formats.** Each skill page asks for its own `Skill edition: CODE` line, while the index asks for one line with a code per page. With two pages opened, the instructions conflict.
3. **README accuracy.** The README said a skill handles a missing skill "in one line", but only `econ-teaching` gave a pointer to the README; `econ-research` and `econ-writing` did not. The Limits paragraph described only the single-code line.

## Changes made

- Index note (`tools/build_link_editions.py`, generated `link/econ-skills.md`), two new rules. Rule 5: later in the chat, open any listed skill from the index when a request needs it; while the index is in use, a skill's "not installed" instruction does not apply. Rule 6: the index's single `Skill edition:` line replaces each page's own line, and one closing line lists all files read.
- `econ-research` and `econ-writing` `SKILL.md`: the missing-skill notice now points to the Econ-Agent-Skills README, matching `econ-teaching`.
- `README.md`: the "Installing only one skill" paragraph mentions the pointer; the Limits paragraph describes the index's multi-code line.
- Link editions rebuilt: `econ-research` `32cf74`, `econ-writing` `fb53ad`; `econ-teaching` unchanged at `2555e6`.

## Files affected

`tools/build_link_editions.py`, `link/econ-skills.md`, `link/econ-research.md`, `link/econ-writing.md`, `skills/econ-research/SKILL.md`, `skills/econ-writing/SKILL.md`, `README.md`, `CHANGELOG.md`, this log.

## Behavior and compatibility

The single-skill prompts work as before. Rule 5 applies only when the index page has been read. No guarantee of any skill changed.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| Diff review of the day's changes | Pass | Read `git diff dcccb4b..HEAD` for skills, README and tools |
| Link editions and index rebuilt | Pass | `python3 tools/build_link_editions.py`; all pages written or up to date |
| Unit tests | Pass | `python3 -m unittest discover -s tests -p 'test_*.py'`: 58 tests OK |
| Structural validation | Pass | `python3 tests/validate_skills.py` |
| Real chat | Not run | Not tried in a claude.ai Project |
| GitHub Actions | Not run | `gh` is not installed on the maintainer machine |

## Known limitations and risks

Rule 5 relies on the agent remembering the index across turns. In a long chat it may fall back to a skill page's own wording.

## Follow-up

The real-chat test in the [link index log](2026-11-15-link-index-page.md) now also covers rule 5: ask the literature question as a second message, not in the first.
