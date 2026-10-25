# 2026-10-24 — Professor Visual-First Teaching and Figure Retrieval

- **Date:** 2026-10-24
- **Component:** econ-phd-professor
- **Change type:** teaching policy, figure provenance, tests and code simplification

## Motivation

The prior visual rule was excessively reactive: independent graphs were to be added only when prose and equations were insufficient. Three ECONS 509 Handbooks comprised 57 pages with no graphical figure commands in the reviewed TeX files. This observation alone does not demonstrate causality, but provides a concrete reason to test a more proactive approach.

## Changes

- **Teaching:** treat graphs, formal mathematics and economic explanations as complementary. Proactively consider graphs for constraints, equilibria, dynamic paths and numerical methods. No fixed minimum or maximum count; unnecessary decoration remains discouraged.
- **Original figures:** allow all useful visually inspected Slide figures. First locate original assets, then search matching rendered student handout PDF pages if assets are missing. Do not confuse a TeX image reference with actual visual inspection.
- **Provenance:** added the reusable Figure Index template with reviewed/unreviewed status and distinct original, independently constructed schematic, and computed plot categories. Added a read-only TeX figure reference inventory script; it deliberately cannot interpret pixels, infer unknown PDF pages, or access private cloud Drive.
- **Core clarity:** reduced the Professor's 12 operational rules to six source/teaching/outcome principles while preserving exact notation, Homework references, course files, and the verified Agent Outputs + TeX/PDF convention.
- **Teaching test quality:** added manual evaluation scenarios 38–44 and Python regressions for figure indexing, nested TeX sources and path restrictions. Documented figure handling and simple LaTeX compatibility in existing references/templates.

## Files

The main Skill; expert-teaching, visuals-and-homework, course-navigation and latex-outputs references; figure-index, course-map and lecture-index templates; scripts/inventory_tex_figures.py; tests/professor-evaluation.md, tests/test_professor_contracts.py; README, AGENTS, CHANGELOG and log index.

## Verification and limitations

| Check | Result | Evidence |
| --- | --- | --- |
| Existing rules and repo content inspected | Pass | Read existing GitHub Skill files, policy, templates and tests. |
| New source figure inventory | CI pending | New Python regression tests and tool added; inspect final commit's GitHub Actions. |
| Local reference links | CI pending | Existing repository link checker should validate new links. |
| Real Slides graphic extraction in Google Drive | Not run | No real course source image/PDF retrieval during this Skill modification. |
| Independent evaluation of illustrated Handbook | Not run | Future content comparison required; tests are contracts, not a blind pedagogical assessment. |
| TeX/PDF cloud delivery | Not applicable | No new course-specific file requested; only public reusable Skill instructions were updated. |

## Next validation

Use the existing ECONS 509 DSDP + PS1 lecture as a real source-backed example. Check both referenced figures and paired rendered handout PDF, then test an explanatory schematic that actually clarifies Bellman contraction, a borrowing constraint or algorithmic mechanism. Assess the improved lesson against the previous handbook on economic precision and clarity, rather than number of pictures.
