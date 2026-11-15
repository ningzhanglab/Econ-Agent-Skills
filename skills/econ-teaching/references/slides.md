# Slides for Presenting a Paper or Lecture

Use this reference only when the user asks for slides, for example to present someone else's paper in a reading group, seminar or class. Ordinary questions about a paper are answered in chat.

## The deck is for the audience; the handover is for the user

Slides are what the presenter shows to an audience, not a study document. The teaching habits that serve the student in chat move off the slides into the handover, but they still happen.

| On the slides (for the audience) | In the handover (for the user, in chat or a short `.md` beside the deck) |
| --- | --- |
| The argument: question, mechanism, results, discussion | Which version of the paper was read, and whether its equations were read as typeset or rebuilt from text ([Slide Fidelity](slide-fidelity.md#papers-and-screenshots)) |
| The paper's notation, unchanged | The paper page or section behind each slide |
| One full citation on the title slide | Every number computed rather than copied, with the check |
| One short source line under each figure or table, and a page for a direct quotation | Reading advice and the reusable lesson, if useful |
| Your own derivations, in **Backup** slides | Anything left unverified |
| Your judgment, as a **Discussion** slide | |

Never put these on a slide: notes about how the paper was read or extracted, per-bullet labels such as "Paper states", "Derived (my check)" or "Caveat (paper)", page tags on every bullet, intuition checks written for the student, reading-order advice, "reusable lesson" lines, long disclaimers, or first person ("my judgment").

Labels are not lost, they are placed: a Backup slide title already says the content is supplementary, a Discussion slide already says it is judgment, and a figure source line says whether the figure is the paper's or recomputed.

## Settle the source before building

A deck depends on the whole paper, so apply the [source-given-as-a-link rule](slide-fidelity.md#papers-and-screenshots) before building: state the version and date in the handover, and ask the user to attach the PDF if only fetched text was read. If they do not, build only on what was verified and say in the handover that figures and equations were not seen.

## Revising an existing deck

When the user asks to revise or "recheck" a deck:

1. Keep a copy of the old `.tex` before editing, and keep its filename for the new one.
2. Re-verify against the current source first (version and date, as above). A deck built from an older version needs its numbers, equation numbers and page references reissued, not patched one by one.
3. Add what was missed to **Backup** first. Move it into the main sequence only if it carries the argument, and recheck that the slide count still fits the time.
4. In the handover, list what changed and why (for example a table of old versus new numbers), so the user can see what to re-check.

## Plan the story first

1. **Purpose, time and audience.** Default: a 20-minute reading-group talk to PhD students, about 12–15 main slides (1.5–2 minutes each) plus Backup. If the user did not say, use the default and state it in the handover; do not stop to ask.
2. **One takeaway sentence**, written before any slide.
3. **Assertion titles.** Each title states the slide's point ("Automating half of GDP raises output only 19%"), not a topic ("Results"). Read in order, the titles tell the argument.
4. **Default order for someone else's paper:** question and motivation; what the paper does, in the authors' terms; preview of the main result; setup; the core mechanism (one equation, its intuition, one figure); main results with magnitudes; extensions, briefly; Takeaways; Discussion questions; Backup. Adjust to the purpose.
5. **Spend the time on the core.** Give the central mechanism several slides; compress secondary sections (applications, side arguments) to one slide each or move them to Backup. Covering every section of the paper is not the goal.

## Each slide

- **Text:** at most 3–4 bullets, each about one line. No paragraphs. If a slide needs a paragraph, split it.
- **Math:** at most two displayed equations. Define every symbol on the slide where it first appears. Use `\alert{}` for the term being discussed. Multi-step derivations go to Backup.
- **Figures:** use an original figure only if it was actually inspected (open the PDF page as an image; crop the figure from the page rather than redrawing it), and credit it ("Source: Jones (2026), Figure 2"). A figure recomputed from the paper's formula says so in its source line ("Computed from Jones (2026), p. 10"), in one line, not a disclaimer. Every figure carries a one-sentence message. Cropped figures go in a folder beside the deck and are cited by relative path in `\includegraphics` (no `\graphicspath`); load `graphicx` and credit them as reproduced.
- **Numbers:** only numbers that appear in the paper or are computed from it; each must be traceable in the handover.

## Literature and assessment

- A related-literature slide may list only papers the paper itself cites (copied from its reference list) or papers verified with `econ-research`. Otherwise leave the slide out; never list papers, years or journals from memory.
- Discussion slides judge the paper on its own terms (which assumption drives the result, which numbers are chosen rather than estimated) and are best phrased as questions for the audience.

## Format and checks

- Default: Beamer, 16:9, from the [slides template](../templates/simple-slides.tex), delivered as `.tex` and compiled `.pdf` under [TeX/PDF Outputs](latex-outputs.md). For Chinese, use `ctexbeamer` with XeLaTeX and keep technical terms in English. A requested `.pptx` follows the same content rules.
- Speaker notes or a handout version only on request.
- Before delivering, run the [bundle checker](../scripts/check_tex_bundle.py) with `--compile` on the `.tex`; it fails on a missing figure or on `\graphicspath`. List the output folder and confirm every file the handover names exists. Do not name a PDF that was not produced ([TeX/PDF Outputs](latex-outputs.md)).
- Before delivering: the deck compiles with no overfull boxes; look at every rendered page for overflow and small type; if pages cannot be rendered (no PDF renderer in the environment), say in the handover which pages were not viewed; the slide count fits the time; every number and figure is traceable in the handover; none of the never-on-a-slide items above appears. Search the `.tex` for "my ", "Paper states" and "Derived" and read the compiled slides for first person; a stated length or timing from the user overrides the default slide count, and the handover says so.
