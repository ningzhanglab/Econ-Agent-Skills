# 2026-10-29 — Professor v1.1 teaching revision

- **Date:** 2026-10-29
- **Component:** `econ-phd-professor`, repository documentation
- **Change type:** Changed / Added / Fixed / Documentation
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

The user asked to revise and improve the Professor Skill while **keeping the core argument about the teaching style and the way the Professor helps them learn**, and to show any better ideas. A review of the v1 baseline found the teaching argument strong but spread across many files; SKILL.md mixed teaching principles with file-handling duties; and three gaps between "a correct answer" and "a student who learned":

1. No rule that the answer to the question comes first. Long derivations could bury the direct answer.
2. No rule that a derivation ends with its economic meaning. Answers could stop at an uninterpreted equation.
3. Homework solutions showed every step but did not name the reusable method, so the student might not recognise it on the next problem. Exam preparation had no retrieval practice.

The README also promised bilingual teaching, but SKILL.md said nothing about language. Several references had rendering defects (escaped backticks shown literally, doubled backslashes), and the README tree and roadmap were stale.

## Changes made

- **SKILL.md** reorganised so the teaching argument leads: a Mission line stating the aim (the student understands the economics and can do the next problem), then **seven teaching principles**, then a separate "Supporting duties" section for source navigation and file output. All six v1 priorities are kept with their wording substantially intact. New principles: (3) answer first, close with economic meaning; (5) check intuition against the math; (6) extends the Homework/exam rule with naming the reusable method and an optional held-back practice item for exam preparation; (7) teach in the student's language with unchanged symbols and English technical terms beside translations.
- **teaching-design.md:** new section *Make the learning stick* with the five habits and the language rule; mode table, teaching arc and editorial check updated to match. A duplicated output-format sentence now links to TeX/PDF Outputs.
- **visuals-and-homework.md:** step 7, *Name the reusable method*, added to the Homework/exam procedure. **mathematical-reasoning.md:** guidance for tiny worked examples (valid values, labeled illustrative, no hidden corner case).
- **Formatting fixes:** literal `` \` `` and doubled `\\input`/`\\include`/`\\includegraphics` removed in course-navigation, course-state-and-sources, large-file-strategy, latex-outputs, visuals-and-homework and the homework-map template. Text content is otherwise unchanged in those files.
- **SKILL.md portability:** the routing table no longer links `../../STORAGE_POLICY.md`, which falls outside the skill folder when it is installed on its own; the self-contained Cloud Drive Workflow reference already carries the same contract.
- **README.md** rewritten more compactly: a "How the Professor teaches" section summarises the seven principles; repeated cloud/format paragraphs replaced by short bullets that link to the policy documents; repo tree now lists `time-series.md`, `learning-log.md` (reference and template) and `logs/`; roadmap no longer says v0.1; added Homework, exam and Chinese example prompts.
- **DESIGN_V1.md:** invariant 8 and a v1.1 note. **AGENTS.md:** preserve the v1.1 habits. **agents/openai.yaml:** default prompt asks for answer first and economic meaning last.
- **tests/professor-evaluation.md:** two rubric dimensions (answer-first clarity, learning transfer) and cases 45–48; title no longer says v0.1.
- **.gitignore** added for Python bytecode and LaTeX by-products created by local test runs.

## Files affected

`skills/econ-phd-professor/SKILL.md`; `skills/econ-phd-professor/references/{teaching-design,visuals-and-homework,mathematical-reasoning,course-navigation,course-state-and-sources,large-file-strategy,latex-outputs}.md`; `skills/econ-phd-professor/templates/homework-map.md`; `skills/econ-phd-professor/agents/openai.yaml`; `README.md`; `DESIGN_V1.md`; `AGENTS.md`; `CHANGELOG.md`; `tests/professor-evaluation.md`; `.gitignore`; this log.

## Behavior and compatibility

- Exact Slide notation, source-versus-supplement labeling, tentative diagnosis, model-design explanation, visual-first teaching, honest figure provenance, slide-matched Homework solutions with all necessary steps, the AI-use boundary, on-demand files with the TeX+PDF default in `Agent Outputs/`, and on-demand Learning Logs are all unchanged.
- New visible behavior: answers lead with the direct answer; substantive derivations end with one plain-language sentence of economic meaning; Homework and exam solutions end with a one- or two-line reusable method; exam preparation may offer one labeled practice item with its answer held back (never an answer the student asked for); replies follow the student's language with English terms on first use.
- No change to scripts, templates' fields, JSON schema, file destinations or tests' executable contracts.

## Verification and evidence

| Check | Result | Evidence or reason |
| --- | --- | --- |
| File / syntax inspection | Pass | Re-read every edited section; confirmed no remaining escaped backticks or doubled backslashes in skill Markdown. |
| Automated structural validation | Pass | `python tests/validate_skills.py`: 1 skill passed. `python -m unittest discover -s tests -p 'test_*.py'`: 19 tests OK, including LaTeX compile tests (latexmk and pdflatex present). |
| Real slide / domain evaluation | Not run | No course slides were used in this change; cases 45–48 are written for the next real-course run. |
| GitHub Actions or other CI | Not run at time of writing | Will run on the pull request. |

## Known limitations and risks

- The new habits are writing instructions; whether an installed Agent follows them consistently is unverified until cases 45–48 are run on real slides.
- "Answer first" could be over-applied to proof questions where the conclusion is the thing being proved; the guidance asks for the direct answer to the *question asked*, which for "why is this true?" is the key reason, not a restatement of the theorem.
- SKILL.md grew by about 170 words. Further growth should go into references, not SKILL.md.

## Follow-up

- Run cases 45–48 with a real lecture (one macro, one econometrics) and record scores.
- Proposals not implemented in this change, pending the user's decision: an optional private learner profile; spaced review that starts a session from open questions in a saved Learning Log; per-domain banks of common misconceptions; moving `scripts/` inside the skill folder so a standalone install keeps its helpers.

## Post-merge update (2026-10-29)

_Added after merging; the sections above are unchanged._

- **Pull request:** [ningzhanglab/Econ-Agent-Skills#1](https://github.com/ningzhanglab/Econ-Agent-Skills/pull/1), merged into `main` as merge commit `526b477`.
- **This change's commit:** `b84c346`.
- **GitHub Actions:** Pass. The `structural-validation` workflow succeeded on `b84c346`, on the PR head `27a0073` and on `main` after the merge (`526b477`).
- **Superseded follow-up:** two of the proposals listed under *Follow-up* (per-domain misconception banks and moving `scripts/` into the skill folder) were implemented in the same pull request; see [Common traps and portable scripts](2026-10-29-professor-common-traps-and-portable-scripts.md). The statement above that no scripts changed is true of this commit only.
- **Housekeeping:** the head branch `professor-teaching-revision` could not be deleted from this session (the proxy refused both the API call and `git push --delete`); it is fully merged and can be deleted from the pull request page.
