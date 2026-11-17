# 2026-11-16 — v2 rebuild: four skills, task pages, shared text

- **Date:** 2026-11-16
- **Component:** all skills, tools, tests and repository documents
- **Change type:** Changed (architecture), Added (`econ-present`, `shared/`, tools, tests)
- **Status:** Implemented on branch `rebuild-v2`; structural tests only
- **Related commit / PR:** See Git history for this change

## Motivation

After a review of every prompt, the user asked for a redesign that is efficient, flexible and actually followed by agents, allowed a rebuild from scratch, asked that the current preferences be kept, and approved the design described in `DESIGN_V2.md`. The design answers failures recorded in earlier logs: a rule missed because it sat mid-paragraph in one of five files; teaching habits printed on slides; a no-skill deck judged better than the skill's deck; duplicated rules updated in some files and not others; 20 of 80 logs changing slide preferences inside a teaching reference.

## Changes made

- **Four skills, divided by what the agent may add.** `econ-teaching` is now `econ-learn`; `econ-writing` is now `econ-write`; slides moved out of the teaching skill into the new `econ-present`; `econ-research` keeps its name.
- **Files organized by task.** `econ-learn/references/` (16 topic files) became `tasks/` (term-or-screenshot, paper, explain, derive, homework-exam, whole-lecture, cross-lecture, course, learning-log, deliver-file) and `guides/` (four field guides, figures, reading-sources, sources-and-versions, large-files). A request needs `SKILL.md` and one task page; a quick step needs only `SKILL.md`. `econ-research/references/` became `tasks/`; `econ-write/references/` became `guides/`.
- **`econ-present/SKILL.md` is the whole deck method** in one file. The slide rules were carried over from `slides.md` almost word for word; the source-settling rule that used to be a link into the teaching skill is written out, and the adjustable choices (audience, length, format, overlays, extras on request) moved to its Defaults section.
- **Guarantees and Defaults.** Every `SKILL.md` has Mission, Guarantees, Defaults. Five guarantees and four global defaults are written once in `shared/` and copied into each skill between `<!-- shared:... -->` markers. Each skill then states what the guarantees mean for its material. Two global defaults are new: replies follow the user's language in every skill (it was stated only in the teaching skill), and when the user states a lasting preference the skill says which default it replaces.
- **Shared file delivery.** `latex-outputs.md` and `cloud-drive-workflow.md` were merged into `shared/deliver-file.md`, copied into `econ-learn` and `econ-present` together with `check_tex_bundle.py`.
- **Handoffs.** Each skill has an "Other skills" section naming where neighboring work goes and the order for jobs that cross skills (for example a referee report).
- **Tools.** `tools/sync_shared.py` (copy shared text, `--check`), `tools/build_all.py` (sync, then link editions), `tools/list_defaults.py` (print every Defaults section). `build_link_editions.py` writes redirect pages at the old `link/econ-teaching.md` and `link/econ-writing.md` addresses and names the four skills in the index.
- **Tests.** `tests/test_shared_and_defaults.py`: copies match `shared/`; every skill has the same shape and no `references/` folder; 42 phrases for preferences the user asked for are still stated; the slides template keeps the requested look. Existing tests repointed to the new paths.
- **Documents.** `DESIGN_V2.md` added; `DESIGN_V1.md` marked historical; `AGENTS.md` rewritten for the new layout, with lighter recording rules (a preference change is one changelog line; behavior changes still get a dated log); `README.md` updated (catalog, links, prompts, layout, roadmap); `STORAGE_POLICY.md` names updated. Link targets in `CHANGELOG.md` and `DESIGN_V1.md` were repointed to where each rule lives now; their text was not changed.

## Files affected

- `skills/econ-learn/` (renamed from `econ-teaching`; new `SKILL.md`, `tasks/`, `guides/`; `references/` removed)
- `skills/econ-present/` (new)
- `skills/econ-write/` (renamed from `econ-writing`; `references/` renamed `guides/`)
- `skills/econ-research/` (`references/` renamed `tasks/`)
- `shared/` (new), `tools/`, `tests/`, `link/`
- `README.md`, `AGENTS.md`, `DESIGN_V2.md`, `DESIGN_V1.md`, `STORAGE_POLICY.md`, `CHANGELOG.md`, this log

## Behavior and compatibility

- **Breaking:** installed `econ-teaching` and `econ-writing` folders must be replaced by the new names; prompts naming `$econ-teaching` or `$econ-writing` need the new names; release zips will be named `econ-learn.zip`, `econ-present.zip`, `econ-write.zip`, `econ-research.zip`. Old paste-a-link pages remain as redirects.
- A slides request now triggers `econ-present`, not the teaching skill.
- Words read per request, counted with `wc -w` (before is v1 at commit `38b20c6`, following its routing table):

| Request | Before | After |
| --- | --- | --- |
| A term with no course | about 4,750 (`SKILL.md` + `teaching-design.md`) | about 2,300 (`SKILL.md` + term page) |
| A Homework problem in macro | about 8,400 (`SKILL.md` + five references) | about 3,500 (`SKILL.md` + homework page + macro guide) |
| A deck | about 7,300 (`SKILL.md` + slides + fidelity + two output references) | about 4,100 (`econ-present/SKILL.md` + deliver-file) |

- `econ-learn/SKILL.md` is 1,935 words, about the same as v1 (1,850): it gained the shared blocks and lost the scope paragraph and half the routing prose.
- Teaching text was regrouped, not rewritten from nothing. A script compared every sentence of the v1 teaching skill with the new files; sentences without a counterpart were reviewed and eight rules were restored. Sentences judged redundant or historical were dropped on purpose (for example the expert-teaching question list, most of which the "why the model is specified this way" lenses already cover).

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| File / syntax inspection | Pass | Link and anchor check over `skills/`: 0 bad. Sentence-level comparison with v1 reviewed by hand |
| Automated structural validation | Pass | `python3 tests/validate_skills.py`: 4 skills OK. `python3 -m unittest discover -s tests`: 66 tests OK, including the TeX compile tests. `python3 tools/build_all.py --check`: in sync. `python3 tools/build_skill_zips.py`: four zips built (37, 5, 6 and 5 files) |
| Real slide / domain evaluation | Not run | No lecture, Homework, paper, draft, topic or deck was run with v2. The planned comparison of v2, v1 and no skill on a fixed set of cases has not been made |
| GitHub Actions or other CI | Not run | Branch not pushed |

## Known limitations and risks

- **Untested behavior.** Whether agents follow v2 better than v1 is not known. The design follows observed failures, but only runs on real material can show it. `tests/professor-evaluation.md` still describes cases in v1 terms.
- **Triggering.** A slides request must now select `econ-present`; this was not tried in any client.
- **Regrouping risk.** Moving 19,000 words by section can change emphasis or drop a nuance that no test pins. The v1 files remain at commit `38b20c6` for comparison.
- **Paste-a-link addresses** in `link/` point to `main`; they resolve only after this branch is merged.
- `tasks/course.md`, `tasks/learning-log.md`, `guides/sources-and-versions.md` and `guides/large-files.md` were moved with link repairs only and do not yet have a Defaults section.
- The `econ-learn` description is 966 characters, close to the 1,024 limit.

## Follow-up

1. Run a fixed set of cases (a term, a derivation, a Homework problem, a paper, a deck) with v2, with v1 and with no skill, and compare, before merging to `main` or publishing a release.
2. A fifth skill for work on the user's own research object (model, proof, data, code) is foreseen in `DESIGN_V2.md` and not built.

## Addition (same day): first comparison run

A small comparison was run after the commit above. It is weak evidence: one run per cell, synthetic material, one grader.

- **Setup.** Three student messages in Chinese, each answered by a fresh subagent in three arms: the v2 `econ-learn` folder, the v1 `econ-teaching` folder (commit `38b20c6`), and no skill. Cases: (A) a bare term, "什么是 elasticity？"; (B) a "why" question on a two-slide lecture excerpt written for the test, with non-standard notation ($\delta$ discount factor, $q$ bond price, multiplier $\mu_t$ on a borrowing limit); (C) a Homework part on that excerpt whose problem set writes $\beta$ and $R$. The nine answers were shuffled under labels X, Y, Z and scored by a separate subagent that did not know the arms, on seven dimensions (0 to 2 each, maximum 14).
- **Scores.**

| Case | v2 | v1 | No skill |
| --- | --- | --- | --- |
| A, term | 14 | 13 | 11 |
| B, why $\mu_t$ | 14 | 13 | 13 |
| C, Homework | 13 | 14 | 13 |
| Total | 41 | 40 | 37 |

- **What the grader cited.** No critical fail in any arm: all nine answers were mathematically correct and kept the lecture's notation, including the no-skill arm. v2 lost its point in C for length (a path table restating earlier sections, and a closing offer). v1 lost points in A and B for length and repetition. No skill lost points for not marking conventions and its own inferences (in C it stated $q = 1/R$ as a fact; in B one table cell had a strict inequality that fails when $\mu_t = 0$). Three of these claims were checked against the answer files and hold.
- **Files read.** v2 read `SKILL.md`, the one task page, and two guides in every case (for the term: `microeconomics.md` and `figures.md`). v1 read `SKILL.md` and one reference for the term, and four references for B and C.
- **Reading of the result.** The differences are one point per case and well within what a second run could reverse. The run does not show v2 to be worse than v1, and does not show it to be clearly better. It does show that the design goal "`SKILL.md` plus one task page" is not met as written: agents open the guides too.
- **Not covered:** `econ-present` (needs a real paper), `econ-write`, `econ-research`, a real lecture or Homework, triggering in a real client, and the paste-a-link method.
