# 2026-11-15 — Settle the paper's source before building a deck

- **Date:** 2026-11-15
- **Component:** `econ-teaching`
- **Change type:** Changed
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

A deck for a Jones and Tonetti paper was built from a link. The download failed and the paper was read as fetched text, version 0.5 (May 2026). The paper the user meant was version 1.0 (November 2026), and its headline numbers, equation numbers and figures differed. The existing rules already said to report the version and the unseen equations, but only in the handover, after the deck existed. The handover also named a compiled PDF that was not in the output folder, and the later revision put first-person labels on slides.

## Changes made

- `references/slide-fidelity.md`, "Papers and screenshots": new bullet "Source given as a link", for any material (paper, notes, handout, homework): say what was retrieved (version or date; file or only text), treat a link as provisional, and ask the student to attach the file when figures or typeset equations matter, not a one-page screenshot. Added after the user pointed out the problem is not specific to slides.
- `references/slides.md`: new short section "Settle the source before building" that applies that rule and says what the handover records if the PDF is not attached.
- `references/slides.md`, "Format and checks": confirm every file the handover names exists in the output folder; search the `.tex` for "my ", "Paper states" and "Derived"; a user-stated length overrides the default slide count and the handover says so.
- `link/econ-teaching.md` rebuilt.

## Files affected

- `skills/econ-teaching/references/slides.md`, `link/econ-teaching.md`, `CHANGELOG.md`, this log.

## Behavior and compatibility

Any answer or deck based on a source sent as a link is affected. `econ-research` already requires naming the version and what was read, and `econ-writing` works on text the user pastes, so neither changed. No other skill changed.

## Verification and evidence

| Check | Result | Evidence or reason |
| --- | --- | --- |
| File / syntax inspection | Pass | Re-read the edited sections |
| Automated structural validation | Pass | `python3 tests/validate_skills.py`: 3 skills passed |
| Unit tests | Pass | `python3 -m unittest discover -s tests -p 'test_*.py'`: 60 tests OK |
| Real slide / domain evaluation | Not run | Not retried with a link in a real chat |
| GitHub Actions or other CI | Not run | Not checked |

## Known limitations and risks

- The rule sits in a reference file, so it applies when the agent opens `slides.md`.
- An agent can still misjudge whether a fetched copy is the current version; the rule asks it to state the version and ask when unsure.

## Follow-up

Re-run the Jones paper request with only the link and check that the agent states the version and asks for the PDF before building.
