# 2026-11-15 — One index link for all three skills

- **Date:** 2026-11-15
- **Component:** link editions (all skills), README, tools, tests
- **Change type:** Added
- **Status:** Implemented; not yet tried in a real chat
- **Related commit / PR:** See Git history for this change

## Motivation

The user keeps the `econ-teaching` paste link in a claude.ai Project's instructions. In that setup the agent cannot use `econ-research`, so a request such as "explain this paper, then place it in its literature" stops at the teaching boundary (observed in the paper session recorded in [2026-11-15 — Paper assessment boundary](2026-11-15-teaching-paper-assessment-boundary.md)). The user asked for one link that covers all three skills and asked to keep the three single-skill paste prompts.

## Decisions

- **An index page, not a merged page.** Concatenating three `SKILL.md` files would make a long page that fetch tools truncate or summarize, would place conflicting rules side by side (for example, teaching's "all math in LaTeX" against writing's "keep the writer's form"), and would load irrelevant rules. The index lists each skill's description and link-edition address and tells the agent to open the page or pages the request needs.
- **Not a new skill.** The index is a generated page, not a top-level skill, so the v1 stability rule and each skill's independence are unchanged.
- **No edition codes on the index.** The codes stay only on the skill pages, so an agent can report a code only by opening the skill page itself.

## Changes made

- `tools/build_link_editions.py`: new `skill_description`, `render_index` and `INDEX_NAME`. `main` also writes and checks `link/econ-skills.md`. The index text comes from each skill's frontmatter description, so it stays in step with the skills.
- `link/econ-skills.md`: generated index.
- `tests/test_link_editions.py`: one new test. The committed index matches the builder, names every skill and its link edition, includes each description and contains no edition code.
- `README.md`: a fourth paste prompt for the index, placed after the three single-skill prompts, which are unchanged. The repository tree line for `link/` mentions the index.

## Files affected

`tools/build_link_editions.py`, `tests/test_link_editions.py`, `link/econ-skills.md`, `README.md`, `CHANGELOG.md`, this log.

## Behavior and compatibility

- The three single-skill pages and prompts are unchanged, and their edition codes did not change.
- Installed and zipped skills are unchanged.
- With the index prompt, the agent opens one more page than with a single-skill prompt.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| Link editions and index rebuilt | Pass | `python3 tools/build_link_editions.py --check`: all four pages up to date |
| Unit tests | Pass | `python3 -m unittest discover -s tests -p 'test_*.py'`: 58 tests OK |
| Structural validation | Pass | `python3 tests/validate_skills.py` |
| Real chat with the index prompt | Not run | Not tried in a claude.ai Project |
| GitHub Actions or other CI | Not run | `gh` is not installed on the maintainer machine |

## Known limitations and risks

- The agent may open only one skill when a request needs two, or open all three to be safe.
- One extra fetch per answer adds another chance for a fetch tool to summarize or drop a page.
- The edition-code line now lists one code per opened page; whether agents follow that format is untested.

## Follow-up

In the user's Project, replace the teaching line with the index prompt and ask about the Jones paper twice: once about the paper only, once adding its place in the literature. Record which pages were opened and whether the codes came back.
