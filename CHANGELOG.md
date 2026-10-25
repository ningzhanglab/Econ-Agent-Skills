# Change Log

A short, chronological summary of meaningful changes to the Econ Agent Skills repository. Newest changes appear first. Detailed records explain rationale and validation in [logs/](logs/README.md). Exact diffs and commit history are preserved by Git.

## Unreleased

_No uncommitted planned changes are represented as completed here._

## 2026-10-24

### Professor — Visual-first teaching, Figure Index and test expansion

- Replaced new-image-as-last-resort wording with proactive visual teaching alongside exact mathematics; no arbitrary figure quotas.
- Added an original figure locator and [Figure Index template](skills/econ-phd-professor/templates/figure-index.md); when a TeX figure asset is missing, check the corresponding rendered handout PDF before declaring the figure unseen.
- Simplified the Professor's core rules from 12 to six priorities, while preserving exact notation, Homework and private TeX/PDF cloud delivery.
- Added teaching evaluation cases 38–44 and Python tests for provenance and nested TeX figure sources.
- Details: [2026-10-24-professor-visual-first-figure-index](logs/2026-10-24-professor-visual-first-figure-index.md).


### Test — ECONS 509 Volume III, source-grounded DSDP + PS1 teaching

- Added a 15-page Chinese DSDP teaching companion grounded in the original Lecture and PS1, including Bellman contraction, policy-induced Markov distribution, Howard=Newton, residual-gradient and Euler/KKT derivations, with explicit PS1(a)--(h) mapping.
- Uploaded and verified TeX/PDF in the exact private `Agent Outputs/`; SHA-256 of both downloaded formats matched local sources; clean-directory XeLaTeX rebuild matched PDF page count and text.
- Lecture rendered overlays, numerical solver runs and independent economics grading remain outside this test.
- Details: [2026-10-24-professor-dsdp-ps1-lecture-handbook.md](logs/2026-10-24-professor-dsdp-ps1-lecture-handbook.md).


### Test — ECONS 509 detailed quantitative methods (Volume II)

- Added a 20-page Chinese deep-dive companion to the existing 22-page course Handbook, with detailed DSDP/CSDP/DLDP/SE derivations and PS1–PS3 learning links.
- Saved TeX and PDF in the verified private `Agent Outputs/`; re-downloaded both; cloud TeX SHA matched local and compiled again to a 20-page PDF with identical extracted text to cloud PDF.
- Missing source visual assets and independent teaching review remain untested; no raw course materials or handbook contents committed to this public repository.
- Details: [2026-10-24-professor-econs509-deep-dive-volume-ii.md](logs/2026-10-24-professor-econs509-deep-dive-volume-ii.md).


### Test — ECONS 509 end-to-end whole-course handbook

- Built a 22-page Chinese course handbook from eight real Lecture TeX sources, the Syllabus and PS1--PS3; compiled XeLaTeX into PDF.
- Verified both TeX and PDF uploads into the correct course `Agent Outputs/`, round-trip SHA-256 equality and clean-directory TeX recompilation.
- Source figure inspection and independent pedagogical blind grading remain outside the test.
- Details: [2026-10-24-professor-econs509-handbook-e2e](logs/2026-10-24-professor-econs509-handbook-e2e.md).


### CI — Validate all active Markdown reference links

- Added standard-library CI tests for local links in README, active Skill references, templates, policies and manual test guidance.
- The check excludes immutable dated history logs and does not attempt to validate external websites.
- Details: [2026-10-24-active-link-validation](logs/2026-10-24-active-link-validation.md).


### Course-file metadata — Group matching TeX, PDF and Word safely

- Added read-only exact-parent, same-stem file grouping and tests for cross-course collisions and presenter variants.
- Updated Course State example to track available format representations as provisional, not confirmed identical.
- Details: [2026-10-24-group-course-file-formats](logs/2026-10-24-group-course-file-formats.md).


### Fix — TeX asset recursion and safe partial cloud delivery

- Fixed TeX/PDF validation so binary figure assets are copied without attempting UTF-8 decoding, and nested `\\input` dependencies are checked recursively.
- Added a real figure-bearing LaTeX scratch-compilation regression and fail-closed handling for dynamic `\\graphicspath` / bibliographies.
- Clarified that a generated file is not saved to Google Drive until a supported file-reference upload is verified; partial `.tex`/`.pdf` uploads are reported as incomplete.
- Details: [2026-10-24-tex-bundle-and-upload-validation](logs/2026-10-24-tex-bundle-and-upload-validation.md).


### econ-phd-professor — Treat same-basename TeX/PDF/Word as one logical source

- Files with matching stems in the same course folder are grouped as representations of a **single lecture** by default, avoiding inflated lecture counts and unnecessary confirmation.
- The Professor chooses the most reliable readable source (often TeX or Word), consulting PDF for diagrams and rendered notation as needed; material inconsistencies remain explicit.
- Added regression cases 35–37 and a Python contract test.
- Details: [2026-10-24-professor-multiformat-sources](logs/2026-10-24-professor-multiformat-sources.md).


### econ-phd-professor — Course recovery and reproducible-output hardening

- Distinguished lecture source roles (student handout PDF, presenter PDF and LaTeX), verified instructor revisions, and added private Course State JSON for source-version checks when resuming.
- Added Lecture ↔ Homework mapping, version annotations in course and lecture indexes, and explicit handling of untrusted operational instructions embedded in course files.
- Added a minimal Chinese `ctexart` template, a TeX asset/scratch-compile checker and Python contract tests to the GitHub Actions workflow.
- The first expanded CI run exposed a source-rule wording mismatch; fixed this and resource warnings. End-to-end Google Drive paired-file upload remains a separate acceptance test.
- Details: [2026-10-24-professor-recovery-hardening](logs/2026-10-24-professor-recovery-hardening.md).


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
