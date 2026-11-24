# 2026-11-24 — Presentation workflow review

- **Component:** econ-present
- **Change type:** Workflow clarification
- **Status:** Local revision for review

## Changes

The README still required the source's order. The presentation instructions repeated parts of the handover and treated text-only access as a reason to ask for a PDF even when the requested slides needed only text. The content-file instructions numbered by rendered page while the checker expected one section per frame.

- The README and skill agree on when to reorder the source. The skill distinguishes evidence for the requested content from the format in which the source was retrieved.
- Literature comparisons identify the support for the comparison. The handover maps claims and checked additions to the source. Tables retain context needed to interpret the results.
- The revision and content-file tasks agree on updating a companion file. Its numbering follows the editable frames and includes a page range when overlays change the mapping.
- The template models inline citations on Related Literature and uses standard displayed equations. The two generated presentation editions follow the canonical instructions.

## Verification

| Check | Result | Evidence |
| --- | --- | --- |
| Repository checks | Pass | Build, structural validation, unit tests and whitespace passed. |
| Template and overlay fixture | Pass | The seven-slide template compiled without overflow. Inspected the literature and equation slides. A two-frame fixture produced three PDF pages, and the bundle checker correctly skipped the overlay count. |
| GitHub Actions | Not run | Local review. |

### Source-based walkthrough

Use the same request in each pass: “Draft two slides in chat for a 20-minute seminar. Cover related literature and the U.S. private-business result using only the supplied text extracts. Say what you checked.” The source is Jones and Tonetti, November 2026, version 1.0, printed pp. 4–5 and 30–31, the summary on p. 52 and selected reference entries on pp. 53 and 55. [Source paper](https://web.stanford.edu/~chadj/JonesTonetti_Automation.pdf).

| Guidance | Literature slide draft | Result slide and handover |
| --- | --- | --- |
| No skill | Grouped Aghion, Jones and Jones (2019) and B. Jones and X. Liu (2024) under task-based growth, then stated the contribution of linking task models to measurement. | Stated the 4.9 percentage-point annual gap. Named the paper, but did not distinguish its account of related work from independently read evidence. |
| Prior instructions | Used a dedicated slide grouping bottlenecks and task-specific technology, with the same cited papers and the authors' contribution. | Stated the 4.9 percentage-point gap and mapped it to Table 6. The text-only instruction also called for asking for a PDF despite the requested scope. |
| Revised instructions | Used the same two mechanisms. Attributed the comparison to Jones and Tonetti's account and distinguished bibliographic checking from reading the cited studies. | Identified the figure as a growth-accounting estimate for U.S. private business, retained its units and period, and traced the slide to Table 6 and the conclusion. The text extracts sufficed for this request. |

These are manually drafted walkthroughs by the same reviewer, using the checked-in and revised instructions and a baseline without repository guidance. They exercise the text-only path and its evidence decisions. They do not establish independent agent performance on full decks.
