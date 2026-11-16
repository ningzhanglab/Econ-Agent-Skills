# 2026-11-15 — Slides: a talk, not a summary

- **Date:** 2026-11-15
- **Component:** `econ-teaching` (slides reference and template)
- **Change type:** Changed
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

The user compared two one-hour decks on the same paper: one built with this skill and one built with no skill. The user judged the no-skill deck clearly better: its structure was smooth and its story easy to follow, while the skill deck was complicated and hard to follow, and named some of the paper's propositions only in passing or not at all.

Reading both `.tex` files and rendered pages showed that the facts, numbers and equations were nearly the same. The difference was the ordering principle:

- The no-skill deck was a chain of questions. Each slide answered the question the previous slide left open, one idea per slide, with the paper's Propositions as slide titles, the terms of key equations named, each part opened by a plain question and closed by a plain lesson, and later parts recalling earlier results.
- The skill deck was a summary in the paper's order. It had been grown from a 20-minute deck through five patch passes (47 to 56 frames), so the core argument stayed compressed: the decomposition, the zero-switching result and the key equation shared one slide, and the reason for the zero-switching result sat in the Appendix. Proposition 5 was shown without its name. Definitions added by the cold-reader pass became semicolon lists, and the flow check added a formulaic lead-in to nearly every slide.

The rules that produced this were the short topic-label titles, "multi-step derivations go to Appendix", the bullet and equation caps applied to the core, references sent to the handover, a coverage check that was satisfied in the handover rather than on the slides, the required connecting line, and a planning section that asked only for time, a takeaway and source order.

## Changes made

A first draft of this change added a seven-step planning procedure (a named thread, a question chain, a fixed opening, a question and a lesson for each part). The user found it too complicated and too prescriptive, so it was cut back to the following.

- **Plan the story first.** Opens with the principle: a deck is a talk, not a summary; how to tell the story is a matter of judgment, using or improving the paper's own framing. One new step: sketch the story before writing slides, one line per slide, one idea per slide, each following from the one before. The core mechanism is built step by step in the main slides with the Propositions that carry it. Titles prefer the slide's point or question to a topic label, and name a Proposition when the slide states one. One outline slide near the start is allowed; no section-divider slides or repeated outline, at the user's request.
- **Each slide.** Symbols are defined in a plain sentence or on the equation, not in semicolon lists. Only secondary derivations and long algebra go to Appendix. A cut table's full version goes to Appendix only when likely to be asked about.
- **On-slide content.** Section, page and table numbers stay in the handover; Propositions and Assumptions by number, and the intuition or analogy that makes a step understandable, belong on the slides.
- **Revising.** A deck for a different length or audience is planned again, not grown or cut slide by slide. A missed item that carries the argument goes into the main sequence.
- **Checks.** Shortened to four lines (flow, skeleton, framework before results, nothing undefined). The connecting-line requirement is removed. A story that does not hold goes back to the sketch instead of being patched.
- Template: the Appendix placeholder now says secondary derivations go there and core steps stay in the main slides.

## Files affected

- `skills/econ-teaching/references/slides.md`: the changes above.
- `skills/econ-teaching/templates/simple-slides.tex`: Appendix placeholder text.
- `link/`: regenerated editions.
- `CHANGELOG.md`, this log.

## Behavior and compatibility

Decks should have more slides on the central argument and fewer in the Appendix, titles that state points, named Propositions, and no formulaic lead-in lines. The reference is about the same length as before (78 lines against 68). Rules the user set earlier are unchanged: no source line on the paper's own figures and tables, no Discussion slide by default, Conclusion then Appendix, the paper's notation and section order, traceable numbers, literature only from the paper's references, no overlays. The earlier flow rule (a connecting line on every slide) is withdrawn; the logs that introduced it remain as history.

## Verification and evidence

| Check | Result (Pass / Fail / Not run / N/A) | Evidence or reason |
| --- | --- | --- |
| File / syntax inspection | Pass | Read the edited sections; anchors `#each-slide` and `#plan-the-story-first` exist. |
| Automated structural validation | Pass | `python3 tests/validate_skills.py`: 3 skills passed. `python3 -m unittest discover -s tests`: 60 tests, OK, including the slides template compile. `tools/build_link_editions.py` rewrote `link/econ-teaching.md`. |
| Real slide / domain evaluation | Not run | No new deck was generated with the changed rules. The diagnosis rests on the two existing decks. |
| GitHub Actions or other CI | Not run | Not pushed. |

## Known limitations and risks

- The change follows from one paper and one pair of decks. The no-skill deck was produced later in the day and may have had access to the earlier deck's content, so the comparison is not fully controlled.
- The story sketch is a planning habit the text asks for; nothing enforces it.
- Unfolding the core raises the slide count for the core; the time budget in step 1 still has to hold.

## Follow-up

Regenerate the one-hour deck for the same paper with the changed rules and compare it with both existing decks.
