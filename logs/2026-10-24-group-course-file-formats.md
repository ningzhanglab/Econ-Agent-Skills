# 2026-10-24 — Add Tested Grouping for Same-Name Lecture Formats

- **Date:** 2026-10-24
- **Component:** Course inventory and Course State
- **Status:** Implemented; check final CI separately

## Purpose and change

A same-stem lecture often appears as PDF, Word and TeX. Previous guidance specified grouping but did not provide an executable repeatable check. Added scripts/group_course_sources.py, a read-only JSON metadata helper grouping only by the same normalized stem and verified parent folder. It does not read file contents or imply exact equality.

Added regression tests for one logical three-format lecture, a presenter variant, another course with identical stem, an unknown parent, and two PDFs with colliding names. Added representations and provisional equivalence to the example course state; updated reference/README/AGENTS.

## Verification and limits

CI results should be checked for this exact commit; the tool is metadata-only, not a real connected Google Drive directory test. No user files were copied to GitHub. This helper does not decide authoritative revisions or change the user's folders.

## Files

scripts/group_course_sources.py; tests/test_professor_contracts.py; skills/econ-phd-professor/templates/course-state.example.json; skills/econ-phd-professor/references/course-state-and-sources.md; README.md; AGENTS.md; CHANGELOG.md; logs/README.md; this record.
