# 2026-10-24 — Add Course Navigation and Large-File Strategy

- **Date:** 2026-10-24
- **Component:** `econ-phd-professor`
- **Change type:** Added / Changed / Testing instructions / Documentation
- **Status:** Implemented; real multi-file end-to-end evaluation pending
- **Related commit:** See Git history for this change.

## Motivation

The user wants the Professor to understand an **entire economics PhD course** in a sensible sequence even if many lecture slides, notes, homework files and linked images are too large to read in one context. The Professor must maintain precise lecturer notation, meaningful lecture connections and truthful source coverage.

## Changes made

- Added optional Course Onboarding: inventory, syllabus-aware instructor sequence, separate conceptual prerequisite graph, lecture-scoped symbols, coverage and blocked assets.
- Added bounded three-pass processing (discovery, indexing, deep reading) and source reopening when teaching; no false assumption upload means permanent access or complete reading.
- Added course-specific private templates for course map, per-lecture index and notation registry. New artifacts stay in the authorized private course workspace, not this public repository.
- Added six manual evaluation scenarios about syllabus ordering, missing syllabus, long TeX/figure dependencies, symbol collisions, targeted slide questions and changed lecture versions.
- Clarified activation: a narrow question does **not** require whole-course indexing.

## Files affected

- `skills/econ-phd-professor/SKILL.md` — route full-course tasks and add coverage integrity rule.
- `skills/econ-phd-professor/references/course-navigation.md` — syllabus order, prerequisites, indexing and retrieval.
- `skills/econ-phd-professor/references/large-file-strategy.md` — staged large-material processing and uncertainty.
- `skills/econ-phd-professor/templates/course-map.md` — reusable private course outline.
- `skills/econ-phd-professor/templates/lecture-index.md` — bounded per-lecture locating/indexing.
- `skills/econ-phd-professor/templates/notation-registry.md` — lecture-scoped symbol disambiguation.
- `tests/professor-evaluation.md` — added qualitative coverage and six test scenarios.
- `README.md` — user workflow and template links.
- `CHANGELOG.md`, `logs/README.md` and this dated record — change tracking.

## Behavior and compatibility

Existing one-slide explanations remain supported, with no forced full-course scan. Whole-course instructions are only operational when the Agent can access the source files and optionally write course artifacts in authorized storage. No new code dependencies or host permissions are introduced. The future Research Agent is still planned, not implemented.

## Verification and evidence

| Check | Result | Evidence or reason |
| --- | --- | --- |
| Source file and link consistency | Reviewed in authoring | Relative links, names and coverage states checked against intended tree; post-commit GitHub read-back to follow. |
| SKILL metadata and required paths | Reviewed in authoring | Portable frontmatter preserved; references and templates link to new files. |
| `python tests/validate_skills.py` | Not run | GitHub write tools do not execute the repository's Python script; must run via CI or local checkout. |
| GitHub Actions | Not verified | No workflow execution result examined. |
| Real entire-course onboarding | Not run | No complete multi-lecture course workspace provided and indexed through a host Agent. |
| Manual evaluation cases 9–14 | Not run | Added as acceptance tests for future regression evaluation. |

## Limitations and risks

These files define an explicit workflow and output templates; they are **not** a search index, persistent course database or automatic loader. Accurate ordering depends on accessible syllabi and filenames. Some hosts omit images, enforce file limits or cannot persist course artifacts. Coverage states must remain honest; even an indexed course requires primary-slide verification for each proof or graph.

## Follow-up

1. Trial whole-course onboarding with a real multi-lecture Macro or Econometrics folder in the user's private workspace.
2. Inspect generated course order, coverage and symbol conflicts and record gaps.
3. Verify exact slides/figures on retrieval and test cases 9–14.
4. If repeated indexing becomes costly, prototype a host-specific tool-backed index without weakening source fidelity.
