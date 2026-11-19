# 2026-11-18 — econ-present on Melons: changed skill against previous skill

- **Date:** 2026-11-18
- **Component:** `econ-present`
- **Change type:** Testing
- **Status:** Implemented (evaluation only; no skill text changed by this test)
- **Related commit / PR:** See Git history for this change

## Motivation

The same day's [figure cropper and shorter SKILL.md](2026-11-18-econ-present-crop-tool-and-shorter-skill.md) change was untested on real material. The user supplied the paper and asked whether the change made decks better. The user chose two arms (changed and previous skill) rather than three, so no-skill was not rerun.

## Setup

- **Source:** Jie Bai, "Melons as Lemons: Asymmetric Information, Consumer Learning and Seller Reputation," *Review of Economic Studies* 92 (2025), 3574–3610. This is the published version, 37 pages, with a Proposition, Tables 2–7 with standard errors, multi-panel figures and a structural model.
- **Request, identical in each arm:** "Make slides on this paper for my reading group: <pdf>". The user could not answer questions, and a file was to be delivered.
- **Arms:** two fresh subagents on the same model (Claude Opus 5.5), one run each. Arm A had a copy of the working tree's `skills/econ-present/` (changed). Arm B had `skills/econ-present/` from `HEAD` (`6e9c3e7`, previous).
- **Tools available to every agent:** TinyTeX with Beamer, and Poppler (installed for this test with the user's permission). No Python PDF libraries.
- **Grading:**
  - Decks and handovers were copied under random neutral labels (deck_P = changed, deck_Q = previous, mapped back afterwards). A search found no skill names in the copies.
  - A separate subagent read the whole paper, viewed the model, figure and table pages as images, and viewed every slide.
  - It checked every number and verified the handovers' algebra.
  - It scored nine dimensions, 0–2 each: the eight from the [2026-11-16 log](2026-11-16-econ-present-real-paper-comparison.md) with "self-contained delivery" replaced by Explanation and Tables, plus Handover.

## Results

| Dimension | Changed (P) | Previous (Q) |
| --- | --- | --- |
| Fidelity | 2 | 2 |
| Coverage and emphasis | 2 | 2 |
| Story and flow | 2 | 2 |
| Explanation | 2 | 2 |
| Slide craft | 1 | 1 |
| Figures | 2 | 1 |
| Tables | 1 | 1 |
| Separation | 2 | 2 |
| Handover | 2 | 2 |
| **Total (of 18)** | **16** | **15** |

| | Changed | Previous |
| --- | --- | --- |
| Pages (main + Appendix) | 39 (33 + 6) | 35 (28 + 7) |
| Paper figures used | 9 files: Fig 1(a), 1(b), 2(a)–(d), 2(e)–(f), 3, 4, 5(a), 5(b), 6 | 8 files: Fig 1(b), 2(c), two Fig 3 close-ups, 4, 5(a), 5(b), 6 |
| Compiles, overfull boxes; bundle checker | yes, 0; PASS | yes, 0; PASS |
| Tool calls, time | 84, 613 s | 63, 468 s |

**What the grader found.**

- **Both decks:**
  - Neither deck has a changed number, sign or symbol, and there were no critical failures.
  - Proposition 1 is on a main slide in both.
  - Both handovers found the same suspected errors in the paper. The grader confirmed each one: eq. (11) lacks a factor $(\overline\gamma-\underline\gamma)$; $r^*$ in eqs. (8) and (12) lacks a square; the sticker posterior is 0.080, not 0.09; and there are several typos. Both decks kept the printed forms on the slides.
- **Where they differ:**
  - The single point of difference is Figures. The previous deck's Fig 1(b) crop clips its "(b)" label (slide 5), and its Fig 2(c) carries a stray mark (slide 9). It also drops Fig 1(a), most of Fig 2 and the label-free panel of Fig 3.
  - The changed deck uses every main figure whole.
- **Weaknesses common to both:**
  - Main-slide tables lack N, and some lack units, although `SKILL.md` already asks for both.
  - Some type in the paper's own images is small.
- **The changed deck:** it is long for a reading group (33 main slides).
- **The previous deck:** it reads a little more like a talk (a Question/Answer frame on slide 2). It puts data collection and heterogeneity only in the Appendix.

The grader would present the changed deck "narrowly".

**Reading.**

- The one-point gap is within what a second run could reverse. It does not show that the shorter `SKILL.md` improved story or coverage: both arms scored 2 on those.
- The Figures difference matches what the change targets. The changed arm read `crop_figure.py`, and the grader found no crop flaw in its deck. The previous arm also cropped figures to separate PNG files, by its own means, and two of its crops were flawed.
- The missing N and units in both arms is a rule that exists and was not followed. Adding wording would not obviously fix it.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| File / syntax inspection | Pass | Both `.tex` files searched for TeX page trimming (none) and skill names (none); figure files listed with pixel sizes |
| Automated structural validation | Pass | Each maker reported 0 overfull boxes and bundle checker PASS with `--compile`; not rerun by the coordinator |
| Real slide / domain evaluation | Pass | Run as described above; one run per arm, one grader, blind labels |
| GitHub Actions or other CI | Not run | Not pushed at the time of writing |

## Known limitations and risks

- One paper, one run per arm, one grader on the same model as the makers. A one-point difference is noise-level.
- No-skill was not rerun, at the user's choice. The earlier ChatGPT runs on this paper are not comparable: they used a different model and a stated 60-minute length.
- Appendix buttons were checked against frame labels and the TeX log, not clicked in a viewer.
- Decks, handovers and grader notes are kept in the session's scratchpad only, not in this repository.

## Follow-up

- Tables without N or units recur across runs. If it recurs once more, consider a mechanical warning in the bundle checker rather than more wording.
- A second run per arm would show whether the Figures difference is stable.
