# Content File

Use this only when the user asks for a content file, or returns one they edited. Everything in [SKILL.md](../SKILL.md) still applies.

A Markdown file beside the deck (the deck's name with `_content.md`) lets the user revise the wording:

- One `## Slide N: Title` section per slide, in order, with N matching the page of the compiled PDF and the text matching the `.tex` exactly.
- Math stays in LaTeX (`$...$` inline, `$$` blocks), with the deck's own macros written out in standard LaTeX so a Markdown editor can render them.
- Bold marks `\textbf` or `\alert`; sub-bullets are indented list items; tables are Markdown tables; figures are relative image links.
- Each Appendix button is its own line: `*Button: Appendix: steps → Slide 61*`.

When the user returns it edited, apply their text to the matching slides in the `.tex`, recompile and regenerate the file, so the three stay in step.

Use the [bundle checker](../scripts/check_tex_bundle.py) to compare section numbers and titles with countable TeX frames. If the checker is unavailable or skips the count because of overlays, section frames or nested inputs, compare the section numbers and titles with the compiled PDF pages. Check the body text against the `.tex`.
