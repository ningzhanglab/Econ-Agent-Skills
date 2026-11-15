# 2026-11-15 — Say upfront when a paper's equations were not seen

- **Date:** 2026-11-15
- **Component:** `econ-teaching`
- **Change type:** Changed
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

In the same paper-reading session recorded in [2026-11-15 — Paper assessment boundary](2026-11-15-teaching-paper-assessment-boundary.md), the PDF download failed and the paper was read through a fetch tool. The answer presented six displayed equations, labeled E1–E6, and said only in its closing section that it had "not read the equations on the PDF pages themselves." Some equations were therefore partly rebuilt from text, and the reader learned this only after reading the explanation. Exact notation is a core guarantee of `econ-teaching`, so a reader needs to know before the first equation whether that notation was actually seen.

## Changes made

- `references/slide-fidelity.md`, "Papers and screenshots": new bullet. If a paper was read only as fetched or extracted text, or its equations could not be read as typeset, say so before the first equation, and mark any equation rebuilt from the text as reconstructed.
- `link/econ-teaching.md` rebuilt (edition code `2555e6`).

## Files affected

- `skills/econ-teaching/references/slide-fidelity.md`: the new rule.
- `link/econ-teaching.md`: generated link edition.
- `CHANGELOG.md`, this log.

## Behavior and compatibility

Answers about a paper read without typeset equations now carry the caveat before the math, and rebuilt equations are labeled. Papers read as a PDF with visible equations are unaffected. No other skill or interface changed.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| File / syntax inspection | Pass | Re-read the edited section |
| Automated structural validation | Pass | `python3 tests/validate_skills.py`: 3 skills passed |
| Unit tests | Pass | `python3 -m unittest discover -s tests -p 'test_*.py'`: 57 tests OK |
| Real slide / domain evaluation | Not run | Not retried with the paper in a real chat |
| GitHub Actions or other CI | Not run | `gh` is not installed on the maintainer machine; not checked |

## Known limitations and risks

- The rule is in a reference file, not `SKILL.md`, so it applies only when the agent opens Slide Fidelity. `SKILL.md` already routes paper notation questions there.
- An agent may not know that a fetch tool summarized or dropped equations. The rule depends on it noticing.

## Follow-up

Re-run the Jones paper request through the link edition and check that the caveat appears before E1.
