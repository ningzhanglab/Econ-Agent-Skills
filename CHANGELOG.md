# Change Log

A short, chronological summary of meaningful changes to the Econ Agent Skills repository. Newest changes appear first. Detailed records explain rationale and validation in [logs/](logs/README.md). Exact diffs and commit history are preserved by Git.

## Unreleased

_No uncommitted planned changes are represented as completed here._

## 2026-10-24

### econ-phd-professor — Optional added charts, Homework integration and simple TeX/PDF default

- Relevant **original Slide figures can be used freely**; new illustrative charts are added **only when pedagogically needed**, with clear sourcing.
- Linked relevant Homework/Problem Sets to the lecture models and learning objectives, respecting the lecturer's notation and assignment AI-use rules.
- Added a minimal `article` LaTeX template and default **paired `.tex` + compiled `.pdf`** output for unspecified-format file requests; the verified cloud destination remains `Agent Outputs/`.
- Template compiled and rendered locally; course-specific paired cloud delivery remains untested.
- Details: [2026-10-24-professor-visuals-homework-texpdf](logs/2026-10-24-professor-visuals-homework-texpdf.md).


### Repository storage policy — Exact Agent Outputs folder

- Corrected the default cloud folder name from `outputs/` to **`Agent Outputs/`** for the Professor and future skills, with exact capitalization and spacing.
- Reused the existing Econs 509 `Agent Outputs` folder and moved the prior Course Map there; verified the Google Drive file parent.
- Introduced repository-wide [STORAGE_POLICY.md](STORAGE_POLICY.md), updated teaching/reference/templates, and added a regression case for coexistence with legacy `outputs`.
- Prior dated change logs remain historical records; this change supersedes their older output-folder convention.
- Details: [2026-10-24-agent-outputs-convention](logs/2026-10-24-agent-outputs-convention.md).


### econ-phd-professor — Cloud sources and mandatory cloud outputs

- Defined connected cloud drive (Google Drive when available) as the source of course Slides and supporting files.
- Required generated files to be saved to the **exact `outputs/` folder** of the verified active course workspace, with file metadata/read-back verification and a cloud link.
- Added safe destination resolution, naming/versioning and permission-failure behavior, with manual acceptance tests; kept private material out of the public GitHub repository.
- Details: [2026-10-24-professor-cloud-outputs](logs/2026-10-24-professor-cloud-outputs.md).


### econ-phd-professor — Add whole-course navigation and large-file handling

- Added syllabus-aware onboarding, separate instructor and prerequisite orders, lecture-level indexing, scoped notation registry and honest DISCOVERED / INDEXED / REVIEWED / BLOCKED coverage.
- Added bounded ingestion and source-reopening strategy for large courses, PDFs, TeX dependencies and missing graphics.
- Created private-workspace course map, lecture index and notation templates; expanded manual regression cases for course sequencing, revisions, scale and notation conflicts.
- No lecture/course data were committed to this public repository.
- Details: [2026-10-24-professor-course-navigation](logs/2026-10-24-professor-course-navigation.md).


### econ-phd-professor — Manual smoke test on a dynamic-programming lecture

- Tested expert economic interpretation, mathematical reasoning, notation fidelity, borrowing-limit constraints, and appropriate handling of unavailable visual assets.
- Sample explanations passed **self-review**, but this was not an independently evaluated or installed-host Skill run; six linked PDF figures were missing.
- No teaching instructions changed. Detailed limitations and future tests are recorded.
- Details: [2026-10-24-professor-dldp-smoke-test](logs/2026-10-24-professor-dldp-smoke-test.md).


### Repository maintenance — Add change logging

- Added repository-level agent instructions for documenting meaningful changes.
- Introduced dated detailed logs, a reusable log template and this summary file.
- Updated the README to direct future contributors to the logging workflow.
- Details: [2026-10-24-logging-system](logs/2026-10-24-logging-system.md).

### econ-phd-professor — Initial v0.1 implementation

- Introduced one adaptive Professor Skill for macroeconomics, microeconomics and econometrics.
- Required faithful preservation of lecture-slide notation and explicit separation of lecture claims from supplementary explanations.
- Added expert teaching, mathematical reasoning, domain references, a hypothetical Bellman teaching example, manual evaluation cases and structural validation.
- Initial commits: [catalog](https://github.com/ningzhanglab/Econ-Agent-Skills/commit/0fcce9cef2b955cf418f1b7704dce9b4ee27db62) and [Professor Skill](https://github.com/ningzhanglab/Econ-Agent-Skills/commit/30b089491cc552cf51844b8acabf1b4da5785f8c).
- Details: [2026-10-24-professor-v0.1](logs/2026-10-24-professor-v0.1.md).

## Logging policy

Add a dated record and update this document for meaningful edits to a Skill, its supporting materials or repository workflows. Use [the template](logs/TEMPLATE.md), and follow [AGENTS.md](AGENTS.md). Do not mistake automated structure checks for pedagogical validation.
