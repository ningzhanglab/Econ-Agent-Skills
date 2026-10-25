# 2026-10-24 — Professor Course State, Homework Map and Reproducibility Hardening

- **Date:** 2026-10-24 (America/Los_Angeles)
- **Component:** `econ-phd-professor` and repository CI
- **Change type:** Added / Changed / Tests / Fix
- **Status:** Implementation committed; CI results must be read by exact final commit; Drive paired-file upload remains untested
- **Related commit:** See the Git history for this log and the accompanying files.

## Motivation

The prior architecture audit identified practical risks in the Professor workflow: no reliable cross-session recovery, ambiguity among slide TeX and handout/presenter PDFs, a Course Map without an explicit Homework alignment section, fragile TeX figure dependencies, limited automated validation, and prompt-like instructions embedded in untrusted course files.

## Changes implemented

- Added `references/course-state-and-sources.md`: evidence-based variant/revision selection, role distinctions among LaTeX source/handout/presenter, instructor designations, slide/page locators, cross-session source-ID/version validation, selective invalidation, and untrusted source-instruction boundaries.
- Added a small valid `templates/course-state.example.json` schema example. State checkpoints are private cloud artifacts only when authorized for persistent onboarding; machine-readable metadata **supplements** the default human-readable TeX/PDF files, not replaces them.
- Added `templates/homework-map.md` and a Lecture ↔ Homework table and source-role section in `templates/course-map.md`; updated `templates/lecture-index.md`, `references/course-navigation.md`, and `references/large-file-strategy.md`.
- Added `templates/simple-notes-cn.tex` as a minimal XeLaTeX/ctexart alternative for Chinese notes.
- Added `scripts/check_tex_bundle.py` to check literal relative \input/\include/\includegraphics dependencies, a matching PDF, and optionally recompile from a small scratch copy. It deliberately **does not copy every file in the user's Agent Outputs folder**.
- Expanded `references/latex-outputs.md`, `references/visuals-and-homework.md`, `references/cloud-drive-workflow.md`, `SKILL.md`, `README.md`, and `AGENTS.md`.
- Added standard-library `tests/test_professor_contracts.py` (source-state schema, homework map, untrusted-source rule, relative dependencies, simple Latin/Chinese templates and English minimal LaTeX compilation). Updated GitHub Actions to install minimal TeX and run these tests in addition to structural validation.
- Added manual evaluation scenarios 27–34 for source-version selection, resume/revision, prompt injection, Homework mapping, TeX asset dependency and Chinese compilation.

## Verification and actual failures

| Check | Result | Evidence and limits |
| --- | --- | --- |
| Earlier GitHub Actions structure validation | Pass | The new workflow's structural validation step succeeded on a failed earlier run. |
| Automatic English LaTeX compile/scratch recompile | Pass within a CI run | GitHub Actions ran the `test_default_english_template_compiles_cleanly` case successfully. |
| First new CI suite run | **Fail (discovered and corrected)** | A contract assertion expected the exact word "reopen" in source-selection guidance, while the document said "open". Updated guidance to state "reopen"; also fixed invalid-escape and unclosed-file warnings in the checker. |
| Final GitHub Actions run | Pending final-commit verification | Do not claim overall green until a completed run for the final HEAD is verified. |
| CJK example / external figure cases | Not part of CI | Full XeLaTeX/CJK fonts and nontrivial slide figure layouts require compatible environments and separate real-world checks. |
| Paired `.tex`+`.pdf` cloud upload and re-download | **Not run** | No paired-files test was performed against a user course folder; the upload connector requires a valid file-reference handoff. |
| Real cross-session Professor host Skill activation | **Not run** | Source-selection and state rules are implemented but have not been independently exercised by an installed host Agent. |
| Existing lecture and Homework content | Not uploaded | No user course content copied into this public GitHub repository. |

## Files touched

New: `references/course-state-and-sources.md`, `templates/course-state.example.json`, `templates/homework-map.md`, `templates/simple-notes-cn.tex`, `scripts/check_tex_bundle.py`, `tests/test_professor_contracts.py`.

Modified: `SKILL.md`, `references/course-navigation.md`, `references/large-file-strategy.md`, `references/latex-outputs.md`, `references/cloud-drive-workflow.md`, `references/visuals-and-homework.md`, `templates/course-map.md`, `templates/lecture-index.md`, `tests/professor-evaluation.md`, `.github/workflows/validate-skills.yml`, `README.md`, `AGENTS.md`, `CHANGELOG.md`, and `logs/README.md`.

## Known limits and next steps

- The course-state example is a documented checkpoint shape, **not** a connected persistent database or automatic cross-session indexer.
- The bundle checker recognizes only simple static TeX dependencies and uses a PDF signature check; it does not prove visual/math quality, interpret arbitrary TeX macros, or upload files to the cloud.
- On an actual course, run a lesson with multiple handout/TeX revisions plus Homework, request paired notes with a real figure, upload both files/assets to the correct `Agent Outputs/`, read metadata back, re-download and compile in a clean directory.
- After the last source edits, check GitHub Actions by final commit SHA, and address any newly observed failures rather than claiming success from a previous run.
