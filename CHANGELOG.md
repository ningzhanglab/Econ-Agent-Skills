# Change Log

A short, chronological summary of meaningful changes to the Econ Agent Skills repository. Newest changes appear first. Detailed records explain rationale and validation in [logs/](logs/README.md). Exact diffs and commit history are preserved by Git.

## Unreleased

_No uncommitted planned changes are represented as completed here._

## 2026-10-24

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
