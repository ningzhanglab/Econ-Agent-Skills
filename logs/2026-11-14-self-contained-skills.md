# 2026-11-14 — Self-contained skill folders

- **Date:** 2026-11-14
- **Component:** all three skills, `README.md`, `tests/validate_skills.py`
- **Change type:** Fixed / Changed / Removed
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

The user asked to stop agents from reading outside a skill, to save tokens, and then asked twice to rethink the result on general merit, setting aside the original request where it did not help.

## Decisions, in the order they were reached

1. **A rule against reading outside the folder.** First drafted as a ban on the repository's README, changelog, logs, tests and other skills' folders, placed at the top of each `SKILL.md`.
2. **Other skills are handed off to, not banned.** The user questioned the ban on other skills. A full ban would make the agent do literature or writing work inside the wrong skill, for example listing papers from memory, which `econ-research` forbids. Changed to: do not pre-read other skills; switch when the request becomes their job.
3. **The rule does not save tokens.** An installed or zipped skill does not contain logs, tests or other skills, so there is nothing to avoid; the note itself is read on every use (about 130 tokens). The real fixed costs are `SKILL.md` (about 3,400 tokens for `econ-teaching`), `references/teaching-design.md` (about 5,300) and above all the user's own papers and slides. The routing tables already say to load only the references a task needs.
4. **Final design: no note at the top of `SKILL.md`.** The restriction was dropped. The link note added earlier the same day (commit 9f3fde6) was also removed: it hard-coded this repository's GitHub address into every portable skill and was read by every user, though only paste-a-link users need it. Their prompts in the README now carry the folder address. The only behavior kept from the discussion is one sentence in each skill's existing scope line: if the needed skill is not installed, say so and do not do its job without its rules.

## Changes made

- `skills/*/SKILL.md`: top note removed; scope sentence extended with the not-installed rule.
- `skills/econ-writing/SKILL.md`: storage rule stated inline instead of pointing to the root `STORAGE_POLICY.md` (a real bug for a zipped skill).
- `skills/econ-teaching/references/cloud-drive-workflow.md`: no longer mentions the root policy file.
- `README.md`: one paste-a-link prompt per skill, each with that skill's raw folder address.
- `tests/validate_skills.py`: `links_leaving_folder` fails the build if any Markdown link in a skill leaves its folder. `tests/test_skill_zips.py`: two tests for it.

## Behavior and compatibility

Installed and zipped skills read slightly less than before (no top note). Paste-a-link users must use the README prompts, which now say where the files are; pasting a bare `SKILL.md` link still works if the agent resolves relative links itself.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| Search for outside pointers in `skills/` | Pass | Only the two `STORAGE_POLICY.md` mentions found; both fixed |
| Outside-link check | Pass | Probed with a temporary skill linking to `../../../README.md`; reported |
| Structural validation and unit tests | Pass | `python tests/validate_skills.py` and `python -m unittest discover -s tests -p 'test_*.py'`, run before committing |
| Real use of the not-installed rule | Not run | Not tried with a single installed skill |

## Known limitations and risks

Token estimates use about 4 characters per token and are approximate.

## Follow-up

If real sessions show `SKILL.md` or `teaching-design.md` length hurting answers or cost, slim them carefully, keeping every rule.

## Correction (2026-11-14, after a review of commits 898730a..c1c6c28)

- The sentence "if the needed skill is not installed, say so and do not do its job without its rules" was replaced: the skill now says so in one line and helps only as far as its own rules allow.
- The outside-link check described above could not have caught the `STORAGE_POLICY.md` pointers, which were plain text; a separate check for repository-only file names was added.
- This log omitted a "Files affected" list and a CI row. Files: the three `SKILL.md` files, `skills/econ-teaching/references/cloud-drive-workflow.md`, `README.md`, `CHANGELOG.md`, `tests/validate_skills.py`, `tests/test_skill_zips.py`, `logs/2026-11-14-share-skills-per-skill.md`. GitHub Actions on `c1c6c28`: Pass, read from the public GitHub API during the review.

See [Review fixes](2026-11-14-review-fixes-papers-and-tooling.md).
