# 2026-11-24 — Presentation questionnaire revision

- **Component:** econ-present
- **Change type:** Defaults, presentation workflow and verification
- **Status:** Local revision for review

## Changes

- Q01–Q05 allow justified design exceptions, default to a PhD seminar audience, allow a finding-first opening and a clearer order, and focus the main talk on the central argument. Explain consequential edits and omissions in the handover.
- Q07, Q08 and Q10 allow more than two equations when they form a readable step, keep the main derivation steps in the talk and put the full derivation or necessary supporting details in the Appendix. Define new notation at first use and highlight selectively.
- Q11 and Q13 center figures with left-aligned explanations by default and put the current frame and total at the bottom right. Use a side-by-side layout when it helps.
- Q15–Q16 prefer original figures and permit verified, labeled redraws where originals are hard to read. Use the handover to map original figures and tables to the source.
- Q21–Q22 allow equivalent checks when a script is unavailable and require the handover to report significant design decisions and limits. Review accuracy, readability, story, pacing, compilation and links.

Q06, Q09, Q12, Q14 and Q17–Q20 retain the existing defaults for length, titles, Beamer style, vertical placement, discussion, Appendix links, outline and file delivery.

The changes are in the presentation instructions and template, the content-file check, the generated presentation routes, the pinned preference tests, the README and the changelog. Existing decks keep their own formatting and source files.

## Verification

| Check | Result | Evidence |
| --- | --- | --- |
| Repository checks | Pass | Generated files, structural validation, all 99 unit tests and whitespace checks passed. |
| Compiled example | Pass | Built and visually inspected seven Beamer slides. Checked the right-aligned counters, figure explanation, PDF link actions in both directions and absence of overfull boxes. |
| Real-paper comparison and CI | Not run | The example checks layout and compilation. It does not measure presentation quality against an earlier edition. |
