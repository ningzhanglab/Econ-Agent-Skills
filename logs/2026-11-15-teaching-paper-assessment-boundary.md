# 2026-11-15 — Teaching may judge a paper on its own terms

- **Date:** 2026-11-15
- **Component:** `econ-teaching`
- **Change type:** Changed
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

The user read a published paper with `econ-teaching` alone, through the link edition. The answer said it "did not assess the paper's evidence," because that "belongs to the separate econ-research skill," which was not available in that session. The rule behind this (`SKILL.md`, "judging its evidence ... belongs to `econ-research`") handed away all assessment of a paper. That included assessment needing no outside literature, such as which assumption drives the result or which numbers are chosen rather than estimated. A user with only `econ-teaching` installed therefore got no assessment at all, and only a bare "not installed" line with no pointer to what to do next.

## Changes made

- `SKILL.md`: judging a paper on its own terms (assumptions that drive the result, sensitivity to a parameter, chosen versus estimated numbers) now belongs to `econ-teaching`. It is labeled as the agent's judgment and names no outside paper. Literature placement, comparison with other papers and reference verification stay with `econ-research`.
- `SKILL.md`: when `econ-research` is not installed, the one-line notice now points to the Econ-Agent-Skills README for installing it or pasting its link.
- `references/teaching-design.md`: the matching sentence under "Questions outside a course" was updated the same way. The existing rule "Critique only when the purpose calls for it" is unchanged, so this changes which skill owns the assessment, not how often it appears.
- `link/econ-teaching.md` was rebuilt (edition code `4c1df5`).

## Files affected

- `skills/econ-teaching/SKILL.md`: boundary sentence and missing-skill notice.
- `skills/econ-teaching/references/teaching-design.md`: same boundary, for consistency.
- `link/econ-teaching.md`: generated link edition.
- `CHANGELOG.md`, this log.

## Behavior and compatibility

With only `econ-teaching`, a reader of a paper can now get labeled internal assessment and is told where to find `econ-research`. With both skills, the split is unchanged in practice: `econ-research` still owns literature work and was not edited. `econ-teaching` still reads and depends on no file of another skill, and the "no papers, years or findings from memory" rule is unchanged.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| File / syntax inspection | Pass | Re-read both edited sentences; searched the repo for the old wording outside `logs/` |
| Automated structural validation | Pass | `python3 tests/validate_skills.py`: 3 skills passed |
| Unit tests | Pass | `python3 -m unittest discover -s tests -p 'test_*.py'`: 57 tests OK (pytest is not installed locally) |
| Real slide / domain evaluation | Not run | Not retried with the paper in a real chat |
| GitHub Actions or other CI | Not run | Not pushed at the time of writing |

## Known limitations and risks

- Whether an agent now offers internal assessment unprompted still depends on the existing "purpose calls for it" judgment. It may still omit it in a plain reading request.
- The README pointer names the repository but gives no URL in `SKILL.md`, so a user in a chat without web access has to find it themselves.

## Follow-up

Re-run the same paper request with the link edition and check that the answer labels internal assessment and points to `econ-research` correctly.
