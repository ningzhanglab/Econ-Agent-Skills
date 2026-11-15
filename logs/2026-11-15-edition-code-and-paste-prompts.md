# 2026-11-15 — Edition code in link editions; stronger paste prompts

- **Date:** 2026-11-15
- **Component:** all skills (link editions), README, tools, tests
- **Change type:** Added
- **Status:** Implemented; not yet tried in a real chat
- **Related commit / PR:** See Git history for this change

## Motivation

Two failures were observed by the user with the paste-a-link method: the agent did not write math in LaTeX unprompted, and it sometimes answered from its own knowledge without reading the repository files. Five wording changes to `SKILL.md` on this date did not settle the first. The analysis in the session was that a page fetched from a link is tool content, weaker than the user's own message, and that the existing "list the files you read" line can be written by an agent that read nothing. The user asked for the two requirements to go into the paste prompts and for a code that shows whether the page was read (item 3 of the list given in the session).

## Changes made

- `tools/build_link_editions.py`: new `edition_code(skill_dir)`, the first six hex characters of a SHA-256 over the path and bytes of every file the skill ships (the same file list as the zip builder). Each link edition now opens with "Edition code: `xxxxxx`", and rule 4 of its note reads: begin your first answer with the line `Skill edition: xxxxxx`, and end it with one line listing the skill files you read.
- `README.md`, the three paste prompts: added "Start your answer with the edition code shown at the top of that page. If you cannot open the page or a file it names, say so and stop; do not answer from memory." The `econ-teaching` prompt also says "Write all math in LaTeX, including single symbols in sentences." `econ-writing` and `econ-research` do not get the LaTeX sentence: the first keeps the writer's own form, the second has little math.
- `README.md`: the Limits paragraph explains how to check the code (open the link and compare), and the maintainer note says to rebuild after changing any file of a skill.
- `tests/test_link_editions.py`: one new test. The code is six hex characters, appears in both places on each page, is stable for unchanged files and changes when a reference file changes.
- `link/*.md` regenerated.

## Files affected

`tools/build_link_editions.py`, `tests/test_link_editions.py`, `README.md`, `link/econ-teaching.md`, `link/econ-writing.md`, `link/econ-research.md`, `CHANGELOG.md`.

## Behavior and compatibility

- Installed and zipped skills are unchanged; skill folders still contain no repository address and no edition code.
- **Maintenance effect:** the code covers every file, so the committed link edition is now out of date after an edit to any reference, template, example or script, not only `SKILL.md`. The existing test `test_committed_link_editions_match_the_skills` fails until `python tools/build_link_editions.py` is run.
- The builder lists only files tracked by Git, so a new skill file must be added to Git (`git add`) before rebuilding, or it is missing from the index and the code. This was already true of the index; it was met again in this session with the two new examples.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| Link editions rebuilt | Pass | `python3 tools/build_link_editions.py`; `--check` reports all three up to date |
| Unit tests | Pass | `python3 -m unittest discover -s tests`, 57 tests, including the new one |
| Structural validation | Pass | `python3 tests/validate_skills.py` |
| Real chat with the new prompts | Not run | Not tried in any chat app |

## Known limitations and risks

- The code shows that the link page was read, not that the reference files were. The closing list of files read is still self-reported.
- An agent can invent a six-character code. The check works only if the user compares it with the page.
- The user has to open the link to see the right code; the README cannot show it because it changes with every skill edit.
- `raw.githubusercontent.com` caches for a few minutes, so a code read just after a push can be the previous one.
- A fetch tool that summarizes pages may drop the code.

## Follow-up

Try each prompt once in a new chat and record whether the code comes back and whether the first answer uses LaTeX.
