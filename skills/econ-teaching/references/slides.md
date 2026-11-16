# Slides for Presenting a Paper or Lecture

Use this reference only when the user asks for slides, for example to present someone else's paper in a reading group, seminar or class. Ordinary questions about a paper are answered in chat.

## The deck is for the audience; the handover is for the user

Slides are what the presenter shows to an audience, not a study document. The teaching habits that serve the student in chat move off the slides into the handover, but they still happen.

| On the slides (for the audience) | In the handover (for the user, in chat or a short `.md` beside the deck) |
| --- | --- |
| The argument: question, mechanism, results, conclusion | Which version of the paper was read, and whether its equations were read as typeset or rebuilt from text ([Slide Fidelity](slide-fidelity.md#papers-and-screenshots)) |
| The paper's notation, unchanged | The paper page or section behind each slide |
| One full citation on the title slide; a page for a direct quotation. No source line on slides that reproduce the paper's own figures or tables (see [Figures](#each-slide)) | Every number computed rather than copied, with the check |
| Your own derivations, in **Appendix** slides | Reading advice and the reusable lesson, if useful |
| Your judgment, only if the user asks, as a **Discussion** slide | Anything left unverified |

Never put these on a slide: notes about how the paper was read or extracted, a source line under a figure or table taken from the paper being presented, or on a text-only slide (section numbers, page numbers and table numbers go in the handover), per-bullet labels such as "Paper states", "Derived (my check)" or "Caveat (paper)", page tags on every bullet, intuition checks written for the student, reading-order advice, "reusable lesson" lines, long disclaimers, or first person ("my judgment").

The paper's Propositions and Assumptions, named by their number, and the intuition or analogy that makes a step understandable are part of the argument and belong on the slides.

Labels are not lost, they are placed: an Appendix slide title already says the content is supplementary, a Discussion slide (on request) already says it is judgment, and a source line on a figure says it is recomputed or from another source.

## Settle the source before building

A deck depends on the whole paper, so apply the [source-given-as-a-link rule](slide-fidelity.md#papers-and-screenshots) before building: state the version and date in the handover, and ask the user to attach the PDF if only fetched text was read. If they do not, build only on what was verified and say in the handover that figures and equations were not seen.

## Revising an existing deck

A deck for a different length or audience is a new deck: plan it again from [Plan the story first](#plan-the-story-first) and reuse slides where they fit. Do not grow or cut an existing deck slide by slide to reach a new length.

When the user asks to revise or "recheck" a deck of the same length:

1. Keep a copy of the old `.tex` before editing, and keep its filename for the new one.
2. Re-verify against the current source first (version and date, as above). A deck built from an older version needs its numbers, equation numbers and page references reissued, not patched one by one.
3. A missed item that carries the argument goes into the main sequence at the point where the story needs it; anything else goes to **Appendix**.
4. In the handover, list what changed and why (for example a table of old versus new numbers), so the user can see what to re-check.

## Plan the story first

A deck is a talk, not a summary of the paper. A summary lists what the paper contains; a talk takes the listener from the question to the answer, each slide following from the one before. How to tell the story is a matter of judgment, not a fixed pattern: use the paper's own framing and wording, or improve on them.

1. **Purpose and audience.** Default: a reading-group talk to PhD students. There is no default length or slide count: use as many main slides as telling the story clearly needs, plus Appendix. If the user did not say, use the default and state it in the handover; do not stop to ask. A length or slide count the user states is followed.
2. **One takeaway sentence**, written before any slide.
3. **Sketch the story before writing slides.** List the main slides, one line each: what the slide establishes and why the listener needs it at that point. One idea per slide. If a slide does not follow from the one before, change the order or add a slide; a connecting sentence does not repair it. At every major section transition, identify what the previous section established, what economic question remains, and why the next section is needed; when the connection is not obvious, add a substantive bridge slide or a spoken transition, using the paper's own transition when it has one.
4. **Order: follow the source.** The body follows the paper's own section order (or the lecture's). The deck ends with a Conclusion (or Takeaways) slide and then the Appendix. There is no Discussion slide unless the user asks for one. Do not reorder sections; if the purpose needs another order (for example a class that teaches a special case before the paper's general model), say what was moved and why in the handover.
5. **Give the core the space.** Build the central mechanism step by step in the main slides, including the Propositions that carry the argument and the reason each holds; do not compress it onto one slide or move it to the Appendix. Compress secondary sections to one slide each or move them to Appendix. Every section still appears somewhere; a section left out entirely is named in the handover with the reason.
6. **Titles.** Consecutive slides on one topic share one title ("The Task Model", "Automation Accounting: Results"), so the audience sees a few block titles rather than a new title on every slide; one line, in one consistent style. Each slide's specific point is said by the presenter, and appears in the speaker notes when they are requested. A slide that states a Proposition, Definition or Assumption names it in a bold lead-in line in the body ("**Proposition 3.** When automation is smooth, switching itself adds zero to TFP growth:"). Appendix slides share the title "Appendix" and carry a subtitle (`\framesubtitle{...}`) saying what each one holds, so a presenter who jumps there from a link sees at once where they are.
7. **Outline.** One outline slide near the start is fine; title it "Outline", not "Roadmap". No section-divider slides and no outline repeated at each section (no `\AtBeginSection`).

## Each slide

- **Text:** bullets, each a complete thought, or a short paragraph of two or three sentences where prose carries the point better (an intuition, an analogy, a figure's message); no long paragraphs. There is no fixed bullet count: use as many as the point needs, and sub-bullets (a nested `itemize`) to group details under the point they support. Split the slide when it carries two ideas or no longer fits at a readable size.
- **Math:** at most two displayed equations. Define every symbol on the slide where it first appears, in a plain sentence or by naming the term on the equation (`\underbrace`), not in a list of definitions joined by semicolons. Use `\alert{}` for the term being discussed. Secondary derivations and long algebra go to Appendix; the steps of the core argument stay in the main slides.
- **Figures:** use an original figure only if it was actually inspected (open the PDF page as an image; crop the figure from the page rather than redrawing it), and leave it without a source line when the talk is about that one paper: the title slide already names it. Add a one-line source only when the figure is recomputed from the paper's formula ("Computed from Jones (2026), p. 10"), comes from another paper or dataset, or is mixed with figures from other sources; one line for a pair of figures is enough. Every figure carries a one-sentence message. Cropped figures go in a folder beside the deck and are cited by relative path in `\includegraphics` (no `\graphicspath`); load `graphicx`.
- **Tables:** show only the rows and columns the argument needs (usually the main coefficient, its standard error and N), with the paper's variable names and the numbers copied exactly; `\alert{}` the main coefficient and state in the first line what it means in units, in the paper's own interpretation or computed from the table and traced in the handover. Prefer the paper's figure for the same result if it has one. No source line for the paper's own table; if only some rows or columns are kept, the full table goes to Appendix only when it is likely to be asked about. A table built from other sources gets a one-line source.
- **Numbers:** only numbers that appear in the paper or are computed from it; each must be traceable in the handover.
- **Appendix links.** Every Appendix slide is one click from the main slide it supports and one click back, so the presenter can answer a question and return. Label both frames (`\begin{frame}[label=m-gain]{...}`), end the main slide with `\vfill\hfill\hyperlink{a-gain}{\beamergotobutton{Appendix: steps}}`, and end the Appendix slide with `\vfill\hfill\hyperlink{m-gain}{\beamerreturnbutton{Back}}`. Several Appendix slides may return to the same main slide. An Appendix slide that no main slide points to is linked or cut.

## Literature and assessment

- A related-literature slide may list only papers the paper itself cites (copied from its reference list) or papers verified with `econ-research`. Otherwise leave the slide out; never list papers, years or journals from memory.
- A Discussion slide, only on request, judges the paper on its own terms (which assumption drives the result, which numbers are chosen rather than estimated) and are best phrased as questions for the audience.

## Format and checks

- **Complete story, checked once the deck is drafted.** Read only the slides, in order, as someone who has not read the paper:
  1. **Flow.** The block titles follow the story's parts in order, the slides under one title build that part step by step, and each slide follows from the one before.
  2. **Skeleton.** Every Proposition and Assumption the results rest on is named on a main slide. The handover shows where each of the paper's sections, main tables and figures went: main slide, Appendix, or left out with the reason.
  3. **Framework before results.** Before the first result the deck has stated the setup, what agents or the estimator do, the objects the results use, and which are observed and which inferred.
  4. **Nothing undefined.** Every symbol, acronym, data source and term is explained on its slide or an earlier one, and no step is asserted without its reason.

  A small gap is fixed on its slide. If the story itself does not hold, go back to the sketch and replan that part; do not add text slide by slide.

- Default: Beamer, 16:9, from the [slides template](../templates/simple-slides.tex), delivered as `.tex` and compiled `.pdf` under [TeX/PDF Outputs](latex-outputs.md). For Chinese, use `ctexbeamer` with XeLaTeX and keep technical terms in English. A requested `.pptx` follows the same content rules.
- **Content file.** Deliver a Markdown file beside the deck (the deck's name with `_content.md`) so the user can revise the wording: one `## Slide N: Title` section per slide, in order, with N matching the page of the compiled PDF and the text matching the `.tex` exactly. Math stays in LaTeX (`$...$` inline, `$$` blocks) with the deck's own macros written out in standard LaTeX so a Markdown editor can render them, bold marks `\textbf` or `\alert`, sub-bullets are indented list items, tables are Markdown tables, figures are relative image links, and each Appendix button is its own line, `*Button: Appendix: steps → Slide 61*`. When the user returns it edited, apply their text to the matching slides in the `.tex`, recompile and regenerate the file, so the three stay in step. The bundle checker fails when the sections and the frames differ in number or in title; it does not compare the body text.
- No `\pause` or overlays by default, so the PDF has one page per slide; use them only on request.
- Speaker notes or a handout version only on request.
- Before delivering, run the [bundle checker](../scripts/check_tex_bundle.py) with `--compile` on the `.tex`; it fails on a missing figure or on `\graphicspath`. List the output folder and confirm every file the handover names exists. Do not name a PDF that was not produced ([TeX/PDF Outputs](latex-outputs.md)).
- Before delivering: the deck compiles with no overfull boxes; look at every rendered page for overflow and small type; if pages cannot be rendered (no PDF renderer in the environment), say in the handover which pages were not viewed; every Appendix button goes to its intended page and back (read the PDF's link targets when a PDF library is available, otherwise click through them); every number and figure is traceable in the handover; none of the never-on-a-slide items above appears. Search the `.tex` for "my ", "Paper states" and "Derived" and read the compiled slides for first person; a length or timing the user stated is met, and the handover says so.
