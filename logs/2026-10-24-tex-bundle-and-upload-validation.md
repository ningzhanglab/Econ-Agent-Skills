# 2026-10-24 — Fix TeX Bundle Dependencies and Cloud Delivery Honesty

- **Date:** 2026-10-24
- **Component:** TeX bundle checker, Professor cloud workflow and regression tests
- **Status:** Implemented; GitHub Actions result for this commit should be checked separately

## Issue found

The previous `compile_in_scratch()` copied a static dependency and then tried to read **every file** as UTF-8 text, including a PDF/PNG/JPG figure. Binary assets can contain invalid UTF-8; valid lecture notes with graphics could crash the validator. The previous `missing_dependencies()` also only scanned the root `.tex` file, missing images referenced in nested `\\input` sources.

A separate operational risk was assuming local artifact creation automatically implied a Google Drive upload. The connected Drive uploader requires a valid file reference; a successful local PDF does not prove a cloud file was created.

## Changes

- Implemented recursive static `\\input`/`\\include`/`\\includegraphics` resolution using the bundle root for paths and reading **only TeX** sources as text.
- Copy the exact dependency closure into a clean scratch directory rather than the entire (potentially enormous) `Agent Outputs/` folder. Reject traversal outside the bundle and unresolved dynamic references.
- Flag dynamic bibliography/graphicspath constructs for separate manual verification rather than silently treating them as portable.
- Added regressions for binary PDF figures with non-UTF8 bytes, nested missing/valid figure references, outside-bundle paths and actual compilation with an included PDF figure.
- Updated cloud workflow to verify actual host file-reference upload support, report partial uploads honestly and avoid silent deletion.

## Verification

- Python/CI test execution: **pending at time of log authoring**; inspect the final GitHub Actions run, not a prior passing run.
- A real Google Drive paired `.tex`/`.pdf` upload and round-trip download **was not performed** by this code change.
- This checker does not resolve arbitrary TeX macro expansion, bibliography databases, `\\graphicspath`, custom classes, or validate teaching/math correctness.

## Files changed

`scripts/check_tex_bundle.py`, `tests/test_professor_contracts.py`, `skills/econ-phd-professor/references/cloud-drive-workflow.md`, `skills/econ-phd-professor/references/latex-outputs.md`, `README.md`, `CHANGELOG.md`, `logs/README.md`, this log.
