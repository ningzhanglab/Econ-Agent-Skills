# 2026-10-24 — Add Cloud Drive Sources and Outputs Convention

- **Date:** 2026-10-24
- **Component:** `econ-phd-professor`
- **Change type:** Changed / Added / Test planning / Documentation
- **Status:** Skill instructions implemented; end-to-end cloud-file delivery not yet tested
- **Related commits:** See Git history for this log and associated source edits.

## Motivation

The user will keep full-course lecture slides and other materials in a cloud drive. Whenever the Professor is asked to create a file, the final artifact must be saved to the cloud's `outputs/` folder rather than remaining as a local attachment or being committed to the public skills repository.

## Changes made

- Added `references/cloud-drive-workflow.md` with a source-and-output storage contract, evidence-based course folder resolution, exact `outputs/` selection, file formats, safe versioning, uploads and mandatory metadata verification.
- Updated `SKILL.md`, `course-navigation.md`, and `large-file-strategy.md` to read original course files from the authorized cloud and put requested generated study materials, course maps, lecture indexes, and notation registries in the course's `outputs/`.
- Updated three reusable templates to point completed course artifacts to cloud `outputs/` while keeping template source in GitHub.
- Updated `AGENTS.md` and `README.md`; added four manual evaluation cases for correct destination, similar folder names, upload failures and safe version handling.
- Retained the previous instruction to preserve all original slide notation.

## Cloud discovery evidence

The connected Google Drive was searched for output folders. Three similar folder names were found: `agent outputs`, `Agent output`, and `agent output` (in separate parent folders). These are not the exact folder name `outputs` requested by the user, and there was no grounded current course folder. **No cloud folder was created, selected as destination, or modified** in this change. Once the user supplies or identifies a course folder, an Agent should find its `outputs/` child or create it when permitted and when a file is actually requested.

## Files affected

- `skills/econ-phd-professor/references/cloud-drive-workflow.md` (new)
- `skills/econ-phd-professor/SKILL.md`
- `skills/econ-phd-professor/references/course-navigation.md`
- `skills/econ-phd-professor/references/large-file-strategy.md`
- `skills/econ-phd-professor/templates/course-map.md`
- `skills/econ-phd-professor/templates/lecture-index.md`
- `skills/econ-phd-professor/templates/notation-registry.md`
- `tests/professor-evaluation.md`
- `AGENTS.md`, `README.md`, `CHANGELOG.md`, `logs/README.md`, and this dated log

## Behavior and compatibility

Normal chat explanations stay in chat. A requested deliverable must be saved to the verified `outputs/` folder in the active course cloud workspace, with read-back and a user-visible cloud link. The exact output folder explicitly designated by the user takes precedence; otherwise choose a verified course folder's `outputs` child, or the verified drive-root `outputs` for source files actually at root. Never silently substitute `agent outputs` or another fuzzy match. The Skill does not create or manage folders without supported host connector actions.

## Verification and evidence

| Check | Result | Evidence or reason |
| --- | --- | --- |
| Existing GitHub Skill and logging rules | Pass | Fetched target source files and their metadata before changes. |
| Connected Drive folder discovery | Pass (read-only) | Retrieved names and parent identifiers of three similar output folders; no exact active course destination yet. |
| GitHub write actions | Pass (individual files) | API updates returned new commit SHAs for policy, routing, docs, templates and tests; final read-back still needed. |
| End-to-end cloud output upload | Not run | No new course-specific file to generate or grounded target workspace in this turn. |
| Manual evaluation cases 15–18 | Not run | Defined as future acceptance checks. |
| Python validator CLI | Not run | GitHub text updates alone do not execute a local Python validation run. |
| GitHub Actions | Not verified | No CI result inspected yet. |

## Limitations and next steps

Instruction-level output routing depends on Google Drive/other cloud access, permissions and actual creation actions exposed by the running Agent. The first real course upload should resolve the course workspace, create or reuse the exact `outputs/`, save a requested output, verify its destination and add a separate test log **without posting private course files to public GitHub**.
