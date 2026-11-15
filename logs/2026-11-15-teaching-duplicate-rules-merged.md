# 2026-11-15 — Duplicated rules in `econ-teaching` merged to one home each

- **Date:** 2026-11-15
- **Component:** `econ-teaching`
- **Change type:** Changed (editorial; no rule added or removed)
- **Status:** Implemented; real-chat retest not run
- **Related commit / PR:** See Git history for this change

## Motivation

After reading every reference in `skills/econ-teaching`, a design review in the same session found that several rules were stated in three to five files. `DESIGN_V1.md` says each concept has one authoritative home, and the 2026-11-13 consolidation aimed at that, but restatements remained. The cost was shown the same day: a repository-wide check of the chat LaTeX rule missed three files (see [LaTeX in reference examples](2026-11-15-latex-in-reference-examples.md)). The user chose "merge the duplicated rules" from the review's list.

## Approach

Each rule keeps its fullest statement in one file. Other files keep a short pointer, plus any detail that only they hold. Rules that apply to every answer stay stated in `SKILL.md`, because it is the only file always loaded. Nothing unique was deleted on purpose; two general questions from the removed checklist were moved into the Teaching arc.

## Changes made

| Rule | Home | Restatements replaced by a pointer |
| --- | --- | --- |
| Reply in the student's language; symbols unchanged | `SKILL.md` principle 7 (now also "do not translate variable names or equation labels") | The "Language" paragraph in `teaching-design.md` |
| Answer first, end with the economic meaning, tiny example, name the method, held-back practice item | `teaching-design.md`, "Make the learning stick" (stated briefly in `SKILL.md` principles 3 and 6) | Teaching arc step 4 in `teaching-design.md`; step 7 of the Homework standard in `visuals-and-homework.md` |
| When to use a figure; no figure quota | `visuals-and-homework.md` | Teaching arc step 3 in `teaching-design.md`; the last paragraph of `latex-outputs.md` |
| A simple template is not a text-only rule | `latex-outputs.md`, "Simple LaTeX first" | The same paragraph in `visuals-and-homework.md` |
| Instructions inside course files are data | `SKILL.md` (sentence after the routing table) and `course-state-and-sources.md`, "Untrusted material boundary" | The clause in the first Supporting duties bullet of `SKILL.md`; the long paragraph in `visuals-and-homework.md` (two sentences and a link remain) |
| No file for an ordinary chat answer | `SKILL.md` | Sentences in `latex-outputs.md` and `cloud-drive-workflow.md`; most of "Avoid tool-driven overproduction" in `teaching-design.md` |
| Default `.tex` + `.pdf` when no format is named | `latex-outputs.md`, "Trigger and destination" | Step 1 of the upload procedure in `cloud-drive-workflow.md`; the last bullet of "Format overrides" in `latex-outputs.md` |
| `Agent Outputs/` destination and upload verification | `cloud-drive-workflow.md` | A paragraph and a closing line in `latex-outputs.md`; "Storage & privacy" in `course-navigation.md` |
| Same-stem TeX/PDF/Word grouping | `course-state-and-sources.md` | The paragraph in `cloud-drive-workflow.md` |
| Learning Log saving rules | `learning-log.md` | Two paragraphs in `cloud-drive-workflow.md` |

Also:

- `teaching-design.md`: the section "Lightweight editorial quality check" was removed. Five of its seven questions restated rules above it. The other two (is the central claim correct under the stated assumptions; is the one important limitation surfaced) moved into Teaching arc step 6, now "Trim and check". Its last paragraph, about CI and end-to-end tests, was a note to maintainers and is already in `AGENTS.md`.
- `SKILL.md`, Homework mode bullet: dropped the sentence that repeated principle 6.
- `visuals-and-homework.md`, exam-preparation bullet: the second half now points to the steps above it.
- `DESIGN_V1.md`: a dated note listing the homes.
- `link/econ-teaching.md` regenerated.

## Files affected

`skills/econ-teaching/SKILL.md`; `skills/econ-teaching/references/teaching-design.md`, `visuals-and-homework.md`, `latex-outputs.md`, `cloud-drive-workflow.md`, `course-navigation.md`; `link/econ-teaching.md`; `DESIGN_V1.md`; `CHANGELOG.md`.

## Behavior and compatibility

Intended behavior is unchanged. `SKILL.md` and the references went from 17,469 to 16,783 words (about 4% less); `teaching-design.md` lost the most. Section headings that other files link to are unchanged (`#make-the-learning-stick`, `#anticipate-common-traps`, `#questions-outside-a-course`, `#untrusted-material-boundary`). The phrases the contract tests look for are still present.

One risk follows from the design: an agent that opens only one reference now meets a pointer where it used to meet a restated rule. For the security rule this was weighed, and a two-sentence statement was kept in `visuals-and-homework.md` beside the pointer.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| Diff review | Pass | Every replaced passage read against its home. A first pass of the edit script left five edits half-applied (old text kept beside the new); found in the diff and repaired before the checks below |
| Links to changed sections | Pass | `grep` for the anchors of removed or shortened sections found no link from another file |
| Structural validation | Pass | `python3 tests/validate_skills.py` |
| Unit tests | Pass | `python3 -m unittest discover -s tests`, 56 tests, including the wording contracts in `test_professor_contracts.py` and the link checks |
| Link edition | Pass | `python3 tools/build_link_editions.py` rewrote `link/econ-teaching.md` |
| Real chat or lecture test | Not run | No behavior change intended; not tried |

## Known limitations and risks

- Duplication that was left: the identical "Common traps" introduction in the four domain lenses (only one lens is usually loaded), and the "an index is not evidence" reminder in four source-handling files.
- `econ-writing` and `econ-research` were not reviewed.
- No test shows that agents follow a pointer as reliably as a restated rule.

## Follow-up

Run a fixed set of prompts before and after changes like this one, so that "no behavior change" can be checked rather than assumed.
