# 2026-11-15 — Cleanup after the LaTeX-rule iterations; maintainer notes out of references

- **Date:** 2026-11-15
- **Component:** `econ-teaching`, README, logs
- **Change type:** Fixed / Documentation
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

A read of the day's five LaTeX-rule logs, at the user's request, found four places that still described wording removed later the same day. A full read of the `econ-teaching` references then found sentences addressed to repository maintainers inside files the agent reads at run time. The user asked for both to be cleaned up (items 1 and 2 of the list given in the session).

## Changes made

Leftovers from the LaTeX-rule iterations:

- `README.md`, Claude Code install note: it promised that saying "use plain text for math" switches the format "for the rest of the conversation". That exception was removed from the skill in commit 6f896c4. The note now says a terminal shows LaTeX as code and the user may ask for plain text.
- `skills/econ-teaching/examples/bellman-teaching-example.md`, line 3: no longer prescribes `$...$` and `$$...$$`; it says math is written in LaTeX, including single symbols in sentences. Delimiters are left to the agent, as the reduced rule decided.
- `logs/2026-11-15-latex-rule-prominent.md`: appended a correction; the separate rule line it added was later removed.
- `logs/2026-11-15-latex-math-in-chat.md`: appended a second correction; its first correction pointed to a state that did not last.
- `CHANGELOG.md`: one italic line at the top of the 2026-11-15 section quoting the wording now in force. No older entry was edited.

Maintainer notes removed from run-time references (no rule changed):

- `cloud-drive-workflow.md`: "It supersedes historical instructions naming `outputs/`." Step 6 of the same file still says a folder named `outputs` does not qualify.
- `course-state-and-sources.md`: "This rule replaces the overly rigid assumption that every PDF/TeX/Word variant must be indexed as a separate source document." The sentence that grouping does not permit inferring identical content is kept.
- `time-series.md`: "inside the existing `econ-teaching` Skill, not a separate course Skill or a fixed STAT 516 teaching script" became "not a fixed teaching script".
- `latex-outputs.md`: "The standard CI job tests the Latin template" was dropped; the instruction to check Chinese compilation on the host is kept.

Left in place on purpose: the line in `learning-log.md` saying GitHub `logs/` is the development log, not a learning diary. It is a rule an agent working inside this repository must follow.

## Files affected

`README.md`; `skills/econ-teaching/examples/bellman-teaching-example.md`; `skills/econ-teaching/references/cloud-drive-workflow.md`, `course-state-and-sources.md`, `time-series.md`, `latex-outputs.md`; `CHANGELOG.md`; appended corrections in two logs.

## Behavior and compatibility

No rule changes. The README no longer promises behavior the skill does not state.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| Old logs only appended to | Pass | `git diff --numstat -- logs` shows additions only for existing logs |
| Structural validation | Pass | `python3 tests/validate_skills.py` |
| Unit tests | Pass | `python3 -m unittest discover -s tests`, 57 tests (run after all of the session's changes) |
| Real chat | N/A | No behavior change |

## Known limitations and risks

`econ-writing` and `econ-research` references were not searched for maintainer notes.

## Follow-up

None.
