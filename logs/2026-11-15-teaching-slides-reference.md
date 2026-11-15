# 2026-11-15 — Slides reference: a clean deck for the audience, notes for the user

- **Date:** 2026-11-15
- **Component:** `econ-teaching`
- **Change type:** Added
- **Status:** Implemented; template compile not run locally (Beamer missing)
- **Related commit / PR:** See Git history for this change

## Motivation

The user presents other people's papers and asked whether output formats such as homework, slides, reports or papers need their own requirements. A review of the skills found that homework (teaching), reports (writing's referee-report conventions; teaching's default `.tex` + `.pdf`) and papers (the user's own text, `econ-writing`) already have a home; slides had none. `latex-outputs.md` covers only file formats.

The user then shared a Beamer deck on Jones, "AI and Our Economic Future", produced with the current skill. The agent read it page by page (14 slides, rendered locally with PDFKit). Teaching habits meant for chat had been printed on the slides:
- a process note on the title slide ("read from the uploaded PDF", "Equations were read as extracted text");
- "Paper states [p. n]" on most slides and per-bullet page tags;
- "Derived (my check)" and "Intuition check (sign and limit)" boxes;
- reading-order advice and a "reusable lesson" line;
- a multi-line disclaimer under a recomputed figure;
- first person ("my judgment, not the paper's").

The last slide also listed related papers with years and journals; from the deck alone it cannot be told whether these were copied from the paper's reference list or written from memory. The user said these parts were unnecessary and got in the way of presenting.

## Decisions

- **Separate the deck from the handover.** Fidelity rules stay; their output moves. The deck carries the argument, one title-slide citation, one-line figure source lines and quotation pages. Provenance per slide, the version read, computed-number checks, reading advice and anything unverified go to the handover (chat or a short `.md`).
- **Placement replaces labels.** Own derivations go in Backup slides and judgment goes in a Discussion slide, so per-bullet labels are unnecessary.
- **Literature slide only from verified sources:** papers the paper itself cites, or papers verified with `econ-research`.
- **Story first:** a default purpose, length and audience (20-minute reading group, 12–15 slides) stated in the handover instead of asked; one takeaway sentence; assertion titles; most time spent on the core mechanism.
- **No new skill.** One on-demand reference, one template and one routing row, so ordinary chat answers are unaffected. An earlier plan in the session put a source line on every slide and "Derivation (not in paper)" labels in the deck; the user's deck showed that this kind of labeling is what clutters a presentation, so the plan was revised before implementation.

## Changes made

- `skills/econ-teaching/references/slides.md` (new): the deck/handover split, the never-on-a-slide list, story planning, per-slide limits (3–4 bullets, at most two displayed equations, symbols defined on the slide, derivations in Backup), figure and number sourcing, the literature rule, format (Beamer 16:9; `ctexbeamer` with XeLaTeX for Chinese; `.pptx` on request) and pre-delivery checks.
- `skills/econ-teaching/templates/simple-slides.tex` (new): a minimal Beamer deck with assertion-title placeholders, Takeaways, Discussion and a Backup appendix.
- `skills/econ-teaching/SKILL.md`: routing row for requested slides.
- `tests/test_professor_contracts.py`: one contract test for the reference, routing and template class; one compile test that skips when Beamer is not installed.
- `README.md`: one sentence on slides in the file-output paragraph; the tree lists the new reference and template.
- `link/econ-teaching.md` rebuilt (edition code `a47bf9`).

## Files affected

The files above, plus `CHANGELOG.md` and this log.

## Behavior and compatibility

Only requests for slides load the new reference. Notes, homework and chat answers are unchanged. The no-papers-from-memory and fidelity guarantees are unchanged; on slides they are met through the handover and placement rules.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| Review of the user's generated deck | Pass | All 14 pages rendered with PDFKit and read; problems listed above |
| Structural validation | Pass | `python3 tests/validate_skills.py` |
| Unit tests | Pass | `python3 -m unittest discover -s tests -p 'test_*.py'`: 60 tests OK, 1 skipped |
| Template compile | Not run | Local TinyTeX has no `beamer.cls`; the compile test skips. Not installed without the user's approval |
| Real deck with the new rules | Not run | Jones deck not regenerated yet |
| GitHub Actions | Not run | `gh` not installed locally |

## Known limitations and risks

- The template has not been compiled anywhere yet.
- Whether CI has Beamer is unknown; if not, the compile test skips there too.
- The handover may itself grow long; the rule keeps it out of the deck but does not limit it.

## Follow-up

Install Beamer (`tlmgr install beamer`) or compile in an environment that has it, then regenerate the Jones deck with the new rules and compare it with the deck reviewed here.
