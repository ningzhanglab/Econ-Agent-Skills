# 2026-11-16 — Econ Teaching: prompt tidy after a full review

- **Date:** 2026-11-16
- **Component:** `econ-teaching` (and one sentence in `econ-research`)
- **Change type:** Changed / Fixed
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

The user asked for a review of every prompt in the repository for fit and efficiency, then asked for all findings to be fixed. The review read the three `SKILL.md` files and all reference files. `econ-writing` and `econ-research` needed no structural change. `econ-teaching` was correct but repeated rules across files, used bold on about 370 spans, carried wording that answered earlier versions of the skill, and had three small inconsistencies.

## Changes made

- **Inconsistencies fixed.**
  - `visuals-and-homework.md` told the agent to create a Figure Index for substantive lectures and to make a lecture-to-homework map, without condition. Both now apply only when a reusable record helps, which matches `course-navigation.md` and `teaching-design.md`.
  - `slides.md`: grammar error in the Discussion-slide sentence.
- **Repeated rules replaced by pointers** where another file already holds the full rule:
  - `teaching-design.md`: the Homework and exam rows of the mode table are one row pointing to the Homework standard; the source/derived/illustration section points to Slide Fidelity and Visuals and Homework and keeps only the two points specific to planning.
  - `course-navigation.md`: the cross-lecture section and the storage section point to Teaching Design and Cloud Drive workflow.
  - `latex-outputs.md`: the save-and-return steps point to Cloud Drive workflow.
  - The four domain lenses: the paragraph introducing the common traps is one sentence.
- **Wording that answered earlier versions removed** from `SKILL.md` ("not several competing personalities", "not an automatic cloud-sync service, a theorem prover") and `time-series.md` (the list of templates not to enforce, the Project-context paragraph). Course-specific residue replaced: "SAS diagnostics" in the routing table, the `ECONS509` example filename.
- **`SKILL.md`:** the list of modes (a) to (h) that preceded the same modes as bullets is gone; "Scope and boundaries" is five labeled bullets instead of one paragraph.
- **Emphasis:** 149 inline bold spans removed from `SKILL.md` and the references. Bold that opens a list item, table row or paragraph is kept. Three all-caps words lowered. No wording changed in this pass.
- **`slides.md`:** the "Never put these on a slide" sentence is a five-item list with the same content.
- **`econ-research`:** `research-questions.md` no longer explains that it agrees with `SKILL.md`; the rule itself is unchanged.
- `link/econ-teaching.md` rebuilt.

## Files affected

- `skills/econ-teaching/SKILL.md`
- `skills/econ-teaching/references/`: `teaching-design.md`, `visuals-and-homework.md`, `course-navigation.md`, `latex-outputs.md`, `slides.md`, `time-series.md`, `econometrics.md`, `macroeconomics.md`, `microeconomics.md`, `learning-log.md`; bold only in `cloud-drive-workflow.md`, `course-state-and-sources.md`, `expert-teaching.md`, `large-file-strategy.md`, `mathematical-reasoning.md`, `slide-fidelity.md`
- `skills/econ-research/references/research-questions.md`
- `link/econ-teaching.md` (rebuilt)
- `CHANGELOG.md`, this log

## Behavior and compatibility

Intended behavior is unchanged except for the two conditions above: a Figure Index and a lecture-to-homework map are no longer asked for on every substantive lecture or Homework question. No course-state, Homework-map or output-bundle format changed. Heading `Solving Homework and preparing for exams` lost its subtitle, so its anchor changed; the one link to it is new in this change.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| File / syntax inspection | Pass | Read the diff of `SKILL.md`; a script checked every `file.md#anchor` link under `skills/` against the target's headings: 0 bad |
| Automated structural validation | Pass | `python3 tests/validate_skills.py`: 3 skills OK. `python3 -m unittest discover -s tests`: 61 tests OK, run after `python3 tools/build_link_editions.py` |
| Real slide / domain evaluation | Not run | Editorial change; no lecture or deck was taught or built |
| GitHub Actions or other CI | Not run | Runs on push |

## Known limitations and risks

- The saving in length is small: `SKILL.md` plus references went from 19,300 to 19,003 words. Most repetition between references was left in place, because each reference is loaded on its own and must still make sense alone. A typical Homework question still loads about 8,400 words.
- The effect of less bold on model behavior was not measured.
- The `econ-teaching` description is 961 characters, close to the 1,024-character limit; not changed.

## Follow-up

None planned. A deeper cut of `teaching-design.md` would change what a single reference says on its own and should be tested on a real lecture first.

## Correction (same day)

"Files affected" omitted `link/econ-research.md`, which the link-edition build also rewrote after the `research-questions.md` edit. The change was committed as `6a577c5`.
