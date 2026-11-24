# 2026-11-24 — Workflow and helper fixes

- **Date:** 2026-11-24
- **Component:** All four skills, Project routes and verification helpers
- **Change type:** Fixed / Changed / Testing
- **Status:** Implemented locally
- **Related commit / PR:** Local checkout refused the Git index lock. See Git history if the changes are later committed.

## Motivation

The review reproduced a stale PDF passing scratch validation and a reference checker losing a DOI after a quoted LaTeX accent. It found a substring year comparison, avoidable Project page fetches and a missing label for partial paper reads. The user requested all four fixes and the four workflow improvements discussed afterward.

## Changes made

- The bundle checker compares the supplied PDF's rendered pages with a clean build under `--compile`. `--build-pdf` can deliver the successful scratch build directly and atomically replace the sibling PDF. Both modes retain the dependency checks. The default mode reports PDF presence and says when content is unchecked.
- The reference checker reads quoted and braced fields with nested braces and escapes. It distinguishes an unreadable entry from an entry without a DOI, and requires a complete year match for both canonical and late-print years.
- Local slide and prose edits use the requested scope, with wider review for global effects, a changed source or an explicit full review. A local slide edit still compiles the whole deck. The common reading guarantee carries inspected material and its coverage forward across tasks when the source and original evidence remain available.
- The lecture route resolves its Defaults link on the page. The course route includes file delivery. The homework route retains in-page field guidance, lists the task procedure first and fetches the selected starter only when needed. It is 47,827 bytes, down from 49,994.
- `econ-research` names selected sections or pages when a paper was read in part. The own-research pilot checks a proposed measure against observed public data before recommending any installed skill for that work.

## Files affected

Shared sources are `shared/guarantees.md`, `shared/deliver-file.md` and `shared/scripts/check_tex_bundle.py`. The skill sources changed in `skills/`, with rebuilt shared copies and `link/` pages from `tools/build_link_editions.py`. `README.md` and `DESIGN_V2.md` describe the workflow. The regression tests cover the two helpers and local route links. `tests/link-route-evaluation.md` and `tests/own-research-pilot.md` contain the real-material cases.

## Behavior and compatibility

The existing Project URLs still work. The PDF comparison requires Poppler if the PDFs differ byte for byte. For delivery, `--build-pdf` works without rendering and writes only after a successful compile. The reference checker still uses the standard library and sends only the DOI. It reports unsupported BibTeX field macros or concatenation as unchecked entries that need expansion.

## Verification and evidence

| Check | Result | Evidence |
| --- | --- | --- |
| Stale PDF and failed rebuild | Pass | Regression changed the source from 10 to 20. Comparison rejected page 1, a successful rebuild replaced the output, and a later compile failure preserved it. |
| BibTeX | Pass | The quoted umlaut entry kept its DOI, a malformed entry reported `ERROR`, the next valid entry was checked, and a year with a leading digit reported `WARN`. Crossref records were mocked. |
| Routing | Pass | Generated pages contain internal links to lecture Defaults and course delivery. Homework passed the regression size and template check. |
| Repository checks | Pass | `python3 tools/check_all.py` passed the rebuild, structural validation, all 96 unit tests and whitespace checks. |
| Real-material workflow comparison | Run | Three independent runs of [case 7](../tests/link-route-evaluation.md) used revised routes, previous routes at `78c9406`, and no skill. See the comparison below. |
| Own-research pilot | Pass | A programmatic tabulation of 445 public NSW rows found 252 disagreements between the proposed proxy and `treat`. See the [pilot](../tests/own-research-pilot.md). |
| GitHub Actions and live ChatGPT Project | Not run | Local validation and independent task runs use local generated pages. |

### Three-turn workflow comparison

The runs explained a bound in Proposition 1, answered a follow-up about its denominator and made one Beamer frame from the same [July 2023 working paper](https://www.povertyactionlab.org/sites/default/files/research-paper/WP2645_Melons-as-Lemons_Bai_July2023_0.pdf).

| Workflow | Source access | Output checks |
| --- | --- | --- |
| Revised routes | Inspected extracted text and the typeset proposition page. Reused inspected evidence for the follow-up and checked the frame against the retained view. No new source access in either later step. | Preserved the notation and put the source locator in the handover. One-page frame compiled with XeLaTeX and was visually checked. |
| Previous routes | Read the indexed text. Reopened the same indexed proposition page for both later steps. The typeset source page was unavailable in this run. | Marked the formula reconstructed from text. That reconstruction used a superscript zero where the source has a prime. One-page frame compiled with XeLaTeX and was visually checked. |
| No skill | Inspected extracted text and the typeset proposition page. Reused it for both later steps. | Preserved notation and placed the source locator on the frame. One-page frame compiled with XeLaTeX and was visually checked. |

The revised run showed the intended handoff and avoided two repeated opens in this case. The no-skill run also avoided them. The runs had different success getting a visual source view. They do not establish a time or quality advantage across requests. The revised route wording was regenerated during the trial, and the run used the edition available at each step.

## Known limitations and risks

Rendered-page comparison does not inspect PDF link destinations. Unsupported TeX dependencies still need a manual clean build. The own-research pilot is one public measurement case. A proof review or estimation-reproducibility case would test a different workflow.
