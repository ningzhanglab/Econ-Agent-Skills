# 2026-11-16 — econ-present on a real paper: v2, v1 and no skill

- **Date:** 2026-11-16
- **Component:** `econ-present` (v2), compared with the slide rules of `econ-teaching` (v1) and with no skill
- **Change type:** Testing
- **Status:** Implemented (evaluation only; no skill text changed)
- **Related commit / PR:** See Git history for this change

## Motivation

The v2 logs list `econ-present` as never run on a real paper. The user supplied one and asked for a test.

## Setup

- **Source:** Charles I. Jones, "AI and Our Economic Future," *Journal of Economic Perspectives* 40 (3), Summer 2026, pp. 3–22. Published version, 20-page PDF; an essay with two figures, a few displayed formulas, no tables and no Propositions.
- **Request, identical in each arm:** "Make slides on this paper for my reading group: <pdf>". The user could not answer questions. The PDF could be read as text and page images; `pdftoppm` was not installed; TinyTeX with Beamer was.
- **Arms:** three fresh subagents, one run each. (A) no skill, told to read nothing but the paper; (B) a copy of the current `skills/econ-present/`; (C) `skills/econ-teaching/` from commit `38b20c6` (v1).
- **Grading:** the outputs and each maker's handover were copied under neutral labels and scored by a separate subagent that read the whole paper and every slide as an image. Eight dimensions, 0 to 2 each (fidelity, coverage and emphasis, story and flow, slide craft, figures, separation of process notes and additions, handover, self-contained delivery). The labels were mapped back afterwards. Two skill names in the handovers were removed before grading.
- **Own checks:** each deck was recompiled from a clean copy of its folder and run through the bundle checker; quantities on the slides were extracted and compared with the paper.

## Results

| Dimension | v2 | v1 | No skill |
| --- | --- | --- | --- |
| Fidelity | 2 | 2 | 1 |
| Coverage and emphasis | 2 | 2 | 1 |
| Story and flow | 2 | 2 | 1 |
| Slide craft | 1 | 2 | 1 |
| Figures | 2 | 2 | 2 |
| Separation | 1 | 1 | 1 |
| Handover | 2 | 2 | 1 |
| Self-contained delivery | 2 | 2 | 0 |
| **Total (of 16)** | **14** | **15** | **8** |

| | v2 | v1 | No skill |
| --- | --- | --- | --- |
| Pages (main + Appendix) | 26 (23 + 3) | 24 (21 + 3) | 19 (18 + 1) |
| Compiles, overfull boxes | yes, 0 | yes, 0 | yes, 0 (in place) |
| Bundle checker | PASS | PASS | FAIL: Figure 1 is read from `../../paper/…` outside the deck's folder |
| Skill files opened | `SKILL.md`, template, deliver-file | `SKILL.md`, `slides.md`, `latex-outputs.md`, template, part of `slide-fidelity.md` | none |
| Tool calls, time | 56, 343 s | 36, 271 s | 13, 152 s |

**What the grader found.** No arm had a wrong number that changes a claim, an invented result or a misdescribed figure. Both skill decks cover every section in the paper's order, build the weak-link argument over seven or eight main slides, crop both figures from the paper, link three Appendix slides each way and keep process notes off the slides. The no-skill deck puts the CES setup, the harmonic mean and the infinite-output result on one slide, puts a grey page-source line on every slide, writes the rule of 70 as "35% × 2 = 2% × 35 = 70", ties Waymo's 170.7 million driverless miles to San Francisco (the paper gives a total), and cannot be rebuilt from its folder. The v1 deck repeats the Waymo error and calls brittle O-rings the cause "alone"; it marks a derived "98% of spending" only implicitly. The v2 deck has neither error, and only its handover mentions the author's disclosure note (he joins Anthropic from 30 June 2026).

**Reading of the v2 versus v1 gap.** The one point v2 lost on slide craft, and part of its separation score, come from following the house style the user set:

- v2 used one block title for consecutive slides, as `econ-present` asks, and took the paper's section headings verbatim ("Weak Links and the Future of Economic Growth" on eight slides). The grader preferred v1's "Weak Links: A Two-Task Example" style, which gives each slide its own title after a shared prefix. v1's `slides.md` contains the same shared-title rule; that agent did not follow it literally.
- v2 left "quoted on p. X" beside three direct quotations, which its rules allow ("a page for a direct quotation"); the grader counted them as page tags.

Under the user's house style the two skill versions are level; under a neutral grader v1 is one point ahead. Both are far ahead of no skill (14–15 against 8), the opposite of the earlier v1 result recorded in the design, where a no-skill deck was judged better.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| File / syntax inspection | Pass | Read each deck's `.tex` titles, page tags and quantities; compared with the paper |
| Automated structural validation | Pass | All three decks recompiled from clean copies (0 overfull boxes); bundle checker PASS for v2 and v1, FAIL for no skill |
| Real slide / domain evaluation | Pass | Run as described above; one run per arm, one grader |
| GitHub Actions or other CI | N/A | No repository change to test |

## Known limitations and risks

- One run per arm, one paper, one grader: a one-point difference is within what a second run could reverse.
- The paper is a short essay with no Propositions, tables or estimates, so the Proposition, table and Appendix-derivation rules were barely exercised.
- The grader scored against general criteria, not the user's house style; the two points noted above depend on that choice.
- Triggering was not tested: each skill arm was told which folder to read.
- The decks and handovers are kept in the session's scratchpad only, not in this repository.

## Follow-up

- Ask the user whether a shared block title should be a short topic name rather than the paper's full section heading, or whether "Block: point" titles are wanted. This is a preference; nothing was changed.
- Run the same comparison on an empirical paper with tables and on a theory paper with Propositions.

## Addition (same day): rebuild after the title change

The user then chose the v1 title style, and `econ-present` now asks for "Topic: point" titles with the same short topic on every slide of a section. The deck was rebuilt once by a fresh subagent with the updated skill, same request and paper. Result: 23 main and 4 Appendix slides; all 21 non-plain titles use one of four topics ("Two Scenarios", "Weak Links", "Labor Markets", "Catastrophic Risk"), each written identically within its section; Appendix slides keep "Appendix" with subtitles. Recompiled from a clean copy with 0 overfull boxes; bundle checker PASS; Waymo's mileage stated as a total, as in the paper. Not graded blind. The figure crops embed the whole source page beneath the clip (a side effect of cropping with TeX only), so copying text from those slides picks up the paper's text.
