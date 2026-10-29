# 2026-10-29 — Common-trap lists and scripts inside the skill folder

- **Date:** 2026-10-29
- **Component:** `econ-phd-professor`, tests, repository documentation
- **Change type:** Added / Changed / Fixed
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change (same pull request as the v1.1 teaching revision)

## Motivation

After the [v1.1 teaching revision](2026-10-29-professor-v1-1-teaching-revision.md), the user chose two of its follow-up proposals:

1. **Misconception banks:** short per-field lists of well-known PhD-level traps that the Professor can use to anticipate errors.
2. **Portable helpers:** move `scripts/` into the skill folder, so a standalone install of `skills/econ-phd-professor/` keeps its helper scripts. `AGENTS.md` already requires each Skill to be independently usable.

A review pass before merging found four further defects, fixed here.

## Changes made

- **Common traps.** Added a *Common traps to anticipate* section to each domain lens: macroeconomics (nine entries plus three numerical-methods entries), microeconomics (eight), econometrics (eight) and time series (seven). Each entry names the trap, why it fails and the correct condition, in words rather than symbols, so it never overrides a Slide's notation.
- **Usage rules.** New *Anticipate common traps* section in Teaching Design: use the lists to choose the bottleneck tentatively, to check a Homework or exam answer, and to name likely mistakes in exam preparation; raise a trap only when relevant; restate it in the Slide's notation and conventions; never let it override what the Slide says. SKILL.md principle 2 and the exam-preparation guidance in Visuals and Homework point to the lists.
- **Scripts moved** with `git mv` from `scripts/` to `skills/econ-phd-professor/scripts/`. Updated links in four references and the Figure Index template (`../../../scripts/` → `../scripts/`), usage lines in the three scripts, paths in `tests/test_professor_contracts.py`, and the README links and repo tree. SKILL.md now lists the helpers under *Supporting duties*. Historical dated logs keep the old path as written.
- **Review fixes:**
  - `cloud-drive-workflow.md` linked to `STORAGE_POLICY.md` outside the skill folder; it now states that it carries the full contract itself and names the repository policy in plain text.
  - Teaching Design's *answer first* rule now says that for a "why is this true?" or proof request, the direct answer is the key reason in one sentence, not a restatement of the claim.
  - The econometrics LATE entry now states its full conditions: binary treatment, binary instrument, independence, exclusion and monotonicity.
  - `DESIGN_V1.md` responsibility map mentions the trap lists.
- **Evaluation:** case 49 tests that a trap is raised tentatively and only when relevant.

## Files affected

`skills/econ-phd-professor/references/{macroeconomics,microeconomics,econometrics,time-series,teaching-design,visuals-and-homework,cloud-drive-workflow,course-navigation,course-state-and-sources,latex-outputs}.md`; `skills/econ-phd-professor/templates/figure-index.md`; `skills/econ-phd-professor/SKILL.md`; `skills/econ-phd-professor/scripts/*.py` (moved); `tests/test_professor_contracts.py`; `tests/professor-evaluation.md`; `README.md`; `DESIGN_V1.md`; `CHANGELOG.md`; `logs/README.md`; this log.

## Behavior and compatibility

- **Path change:** anyone running the helpers from the old location must use `skills/econ-phd-professor/scripts/…`. No script logic changed.
- The traps are general economics. They do not change notation rules, source priority, the Homework method rule or file behavior.

## Verification and evidence

| Check | Result | Evidence or reason |
| --- | --- | --- |
| File / syntax inspection | Pass | Read the full diff against `main`; checked every trap entry for correctness under standard assumptions. |
| Standalone-install link check | Pass | Copied only `skills/econ-phd-professor/` to a scratch folder and resolved every Markdown link: none missing, none leaving the folder. |
| Automated structural validation | Pass | `python tests/validate_skills.py`: 1 skill passed. `python -m unittest discover -s tests -p 'test_*.py'`: 19 tests OK, including LaTeX compile tests. |
| Scripts from new path | Pass | `python skills/econ-phd-professor/scripts/check_tex_bundle.py --help` runs. |
| Real slide / domain evaluation | Not run | Cases 45–49 await a real-course run. |
| GitHub Actions | See pull request | Checked before merge. |

## Known limitations and risks

- The trap lists are curated, not exhaustive, and some entries depend on conventions (constraint signs, root conventions) that the Slides decide.
- A Professor that over-applies the lists could append irrelevant warnings; case 49 is the check for that.

## Follow-up

- Run cases 45–49 on one macro and one econometrics lecture and record scores.
- Remaining proposals not implemented: an optional private learner profile; spaced review from saved Learning Logs.

## Post-merge update (2026-10-29)

_Added after merging; the sections above are unchanged._

- **Pull request:** [ningzhanglab/Econ-Agent-Skills#1](https://github.com/ningzhanglab/Econ-Agent-Skills/pull/1), merged into `main` as merge commit `526b477`.
- **This change's commit:** `27a0073`.
- **GitHub Actions:** Pass. Both `structural-validation` runs on `27a0073` (push and pull-request triggers) and the run on `main` after the merge succeeded. This replaces the *See pull request* entry in the verification table.
- **README** updated after the merge to describe the trap lists, the four domain lenses and the self-contained skill folder, and to name cases 45–49 as the next evaluation step.
