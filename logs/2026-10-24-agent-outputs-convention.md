# 2026-10-24 — Default Cloud Folder Renamed to Agent Outputs

- **Date:** 2026-10-24
- **Component:** Repository-wide storage policy and `econ-phd-professor`
- **Change type:** Changed / Fixed / Testing instructions / Documentation
- **Status:** Implemented; cloud migration verified
- **Related commits:** Consult GitHub history for this log.

## Motivation

The user corrected the target folder name from `outputs` to **`Agent Outputs`**. All new files that an Agent is asked to create must use that exact folder name (capital A, capital O, space), unless an alternative destination is explicitly selected.

## Changes made

- Added `STORAGE_POLICY.md` as a shared rule for current and future Agent Skills.
- Updated `README.md`, `AGENTS.md`, the Professor `SKILL.md`, cloud workflow, course navigation, large-file strategy, and the three course-index templates.
- Updated manual Professor evaluation cases 15–18 and added case 19, which ensures legacy `outputs` is not chosen over an existing `Agent Outputs`.
- Added this dated change log and a summary to `CHANGELOG.md` / the log index. **Historical logs were preserved unchanged**.

## Actual cloud workspace action

- Verified the existing exact `Agent Outputs` folder belongs to the user-provided Econs 509 course workspace.
- Moved the previously generated multi-file Course Map Google Doc from the accidentally created legacy `outputs` folder to the already existing `Agent Outputs` folder.
- Re-read the file's parent metadata and the destination folder's contents; both confirmed the new location.
- The old `outputs` folder was left unchanged, as the user did not request deletion. No source slides or assignment files were modified.
- The public repository does not contain the private course files or identifiers.

## Verification and evidence

| Check | Result | Evidence |
| --- | --- | --- |
| Existing exact destination and its course parent | Pass | Google Drive folder metadata returned the expected exact name and parent. |
| Course Map moved to new location | Pass | File metadata and direct destination folder listing matched. |
| Professor instructions, references and templates | Updated | GitHub file updates were accepted; final read-back/check pending. |
| End-to-end new generated deliverable | Not run | This task changes destination policy and migrates a previously generated document. |
| Regression case 19 | Not run | Added as a future agent acceptance check. |
| CI / Python validation | Not verified | No successful CI run is claimed. |

## Behavior, limitations and follow-up

Use `Agent Outputs` for all newly requested files by default, reusing a verified course-specific folder. Never treat `outputs` or `agent outputs` as equivalent. Explicit user-selected alternate destinations take priority. A future real generation run should confirm format, file name, correct parent and cloud link after writing.
