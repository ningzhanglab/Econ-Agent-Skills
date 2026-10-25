# 2026-10-24 — Same-basename multi-format lecture handling

- **Date:** 2026-10-24 (America/Los_Angeles)
- **Component:** `econ-phd-professor`, course sources and indexing
- **Change type:** Changed / Fixed / Testing instructions
- **Status:** Rule implemented; real mixed PDF/Word/TeX dataset test pending
- **Related commits:** See Git history for the relevant source edits.

## Motivation

The user clarified that lecture files will generally be supplied as PDF or Word, sometimes with matching TeX source. Files with the **same name/stem**, differing only in extension, can normally be treated as alternative representations of **the same logical file**. The Professor should choose the most readable representation itself, often TeX or readable Word, use PDF for graphs/layout as appropriate, and only ask whether files are equivalent if materially uncertain.

## What changed

- `references/course-state-and-sources.md`: added same-stem grouping within a verified course directory; explicit distinction between logical document identity and the actual content/version of each representation. Preferred readable source is adaptive. Material contradictions are checked, not silently collapsed.
- `SKILL.md`: made same-stem grouping a core source-selection behavior; retain exact slide notation and visual-source fidelity.
- `course-navigation.md` and `cloud-drive-workflow.md`: organize multi-format duplicates under one lecture in the course inventory and choose a workable source without unnecessary confirmation.
- `templates/lecture-index.md`: record grouped source IDs/formats and rationale for selecting a readable or rendered representation.
- `README.md`: replace the overly strict wording suggesting formats necessarily represent different lecture files.
- `tests/professor-evaluation.md`: updated case 27 and added cases 35–37: equivalent same-stem formats, genuinely conflicting content, and same stems belonging to different courses.
- `tests/test_professor_contracts.py`: added a lightweight contract assertion so future changes don't silently remove this behavior.

## Exact decision rule

1. Same basename (minus extension) **and** verified same course/lecture context → presumptively one logical source.
2. Choose a reliable readable `.tex`, `.doc`/`.docx`, or PDF based on actual accessibility/content; do not rank file formats unconditionally.
3. Check rendered PDF as needed for diagrams, annotations, pagination or potentially garbled math.
4. Treat presenter/handout variants, explicit instructor revisions, and meaningful contradictions as distinct views/versions even if names are similar.
5. Ask the user to clarify only when unresolved differences materially affect the explanation, rather than reflexively asking about every extension.

## Verification and evidence

| Check | Result | Evidence / caveat |
| --- | --- | --- |
| GitHub rule and template edits | Implemented | Connected repository edits returned commit SHAs. |
| New regression scenarios | Added, not run manually | Cases 35–37 document expectations; no independent multi-format teaching run. |
| Python contract test | Added; CI pending at log authoring | A static test checks that source rules, navigation and index template preserve same-stem guidance. |
| Real PDF/Word/TeX mixed lecture workflow | Not run | No complete mixed-format source dataset was processed in this change. |
| Google Drive artifact operations | N/A | No generated file requested; existing `Agent Outputs/` contents untouched. |
| GitHub Actions final HEAD | Pending verification | Will verify the workflow after logging changes. |

## Limitations and follow-up

Identical filename stems are evidence of likely equivalence, not a cryptographic/content match. Indexes must preserve which representation was actually inspected; teaching of figures still requires viewing the actual rendered source. Use a real course folder with Word, PDF and TeX variants to confirm correct grouping and avoidance of unnecessary clarification. The previous course state/LaTeX/Drive output rules remain in effect.
