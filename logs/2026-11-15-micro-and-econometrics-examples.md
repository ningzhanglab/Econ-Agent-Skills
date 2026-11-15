# 2026-11-15 — Worked examples for microeconomics and econometrics

- **Date:** 2026-11-15
- **Component:** `econ-teaching`
- **Change type:** Added
- **Status:** Implemented; not yet tried in a real chat
- **Related commit / PR:** See Git history for this change

## Motivation

The design review in this session found that the skill gives many rules and one complete model answer, the Bellman (macro) example, and that agents followed an example more readily than a rule in the day's LaTeX episode. The user asked for examples in microeconomics and econometrics (item 6 of the list given in the session).

## Changes made

Two files in `skills/econ-teaching/examples/`, in the form of the Bellman example (hypothetical slide excerpt, a good response, why it is good, failure examples). Each shows a different teaching mode, so the three examples do not repeat one another:

- `slutsky-teaching-example.md` (micro, **quick question**): a student asks why the wealth term in the Slutsky equation has a minus sign. The response answers in one sentence, shows the one decisive step (differentiate $h_i(p,u) = x_i(p, e(p,u))$ and apply Shephard's lemma), states the meaning in words, checks the sign with labeled numbers, and stops.
- `omitted-variable-homework-example.md` (econometrics, **Homework by the Slide's method**): a hypothetical question on schooling, ability and wages. The response gives the answer first, maps the Homework's letters to the slide's once, shows each step including where $E[u_i \mid x_i, z_i] = 0$ is used, checks two limiting cases, states the economic meaning and names the reusable method.

Both write all math in LaTeX, including symbols in sentences, and say in their first lines that they are hypothetical.

- `skills/econ-teaching/SKILL.md`, last sentence of "Scope and boundaries": lists the three worked examples by field and mode, still "only as hypothetical style references".
- `README.md`: the two files added to the repository tree.
- `link/econ-teaching.md` regenerated.

## Files affected

`skills/econ-teaching/examples/slutsky-teaching-example.md`, `skills/econ-teaching/examples/omitted-variable-homework-example.md`, `skills/econ-teaching/SKILL.md`, `README.md`, `link/econ-teaching.md`, `CHANGELOG.md`.

## Behavior and compatibility

No rule added. An agent that opens the examples sees a short answer for a short question and a full step-by-step Homework solution, which the rules describe but no file showed before. About 1,100 words added to the skill folder, loaded only when an agent opens the examples.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| Economics and arithmetic | Pass (author's own check, no independent review) | Slutsky: with $x_1 = \tfrac12 w/p_1$, $w=100$, $p_1=2$: total effect $-12.5$, wealth term $-6.25$, substitution effect $-6.25$. Omitted variable: $\operatorname{Cov}(x,y)/\operatorname{Var}(x) = \beta_1 + \beta_2\delta_1$ given $\operatorname{Cov}(x,u)=0$; $0.08 + 0.05 \times 0.4 = 0.10$ |
| Structural validation and links | Pass | `python3 tests/validate_skills.py`; link tests in the 57-test run |
| Link edition | Pass | Rebuilt after the files were added to Git's index |
| LaTeX rendering | Not run | Not viewed in a renderer |
| Real chat | Not run | Whether agents imitate the examples is not shown |

## Known limitations and risks

- The examples are written by the agent that maintains the skill and were not reviewed by an economist other than the user.
- An agent may copy an example's structure too literally; `SKILL.md` calls them style references, and each says it is hypothetical.
- No time-series example and no paper-reading example.

## Follow-up

The user reads both examples for economics and tone. Include one micro and one econometrics prompt in any fixed test set.
