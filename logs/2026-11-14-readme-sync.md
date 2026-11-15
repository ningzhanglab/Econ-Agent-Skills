# 2026-11-14 — README brought up to date

- **Date:** 2026-11-14
- **Component:** `README.md` (documentation only)
- **Change type:** Documentation
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

After the review fixes in commit 85366b4, the user asked for the README to be updated. Several README passages described the skills as they were before today's changes.

## Changes made

- "Share a skill": a paragraph saying a single installed skill works on its own, and what it does when a request needs a skill that is not installed.
- "How the Professor teaches": a "Reading a paper" paragraph (short map first, depth where stuck, says what was read; a named but unsent paper gets a labeled outline and a request for the PDF).
- "Getting started": step 2 points to the zip download as well as copying or linking the folder.
- Untrusted-content sentence: adds papers, screenshots and web pages, matching `econ-teaching`.
- "Change history, contributing and testing": CI also checks that skills are self-contained and tests the zip builder; a missing comma fixed.
- "Try a skill without installing": the three paste prompts shortened to one line each (the skill's `SKILL.md` link, "its files are in the same folder; fetch only what my request needs", then the request), at the user's request.
- "Roadmap": run evaluation cases 57–60; publish the first release and test one Claude.ai upload.

## Files affected

`README.md`, `CHANGELOG.md`.

## Behavior and compatibility

None; documentation only.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| README statements checked against the skill files | Pass | Compared with `skills/econ-teaching/SKILL.md`, `references/teaching-design.md`, the three scope lines and `tests/validate_skills.py` at 85366b4 |
| Structural validation and unit tests | Pass | Run before committing |
| Real use | N/A | Documentation only |

## Known limitations and risks

The roadmap item about the first release becomes outdated once it is published.

## Follow-up

Remove the release roadmap item after the first release.
