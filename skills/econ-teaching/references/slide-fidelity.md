# Slide Fidelity and Notation

This file defines hard source-grounding requirements for any lecture-based answer.

## Source hierarchy

1. Use the **provided lecture slide** to determine the locally defined model, not a familiar external version.
2. Use adjacent pages or equations to resolve missing definitions where available.
3. Supplement with standard economics and external research only after correctly separating the lecture's claims from supplementary discussion.

When answering, distinguish:

- **Slide states:** directly visible definitions, equations, claims, assumptions, figure labels and data.
- **Derived from slide:** algebraic or economic consequences that follow after stated assumptions (show the relevant justification).
- **Additional perspective:** textbook variation, empirical finding, analogy or a proposed extension.

Do not attribute the latter two to the lecturer without evidence.

## Lock notation

Make a local internal ledger when needed:

| Item | Verify |
| --- | --- |
| Choice/state variables | letter, capitals, accents, primes and economics meaning |
| Parameters | names and domain restrictions |
| Timing | t versus t+1, primes, leads/lags and dating of shocks |
| Operators | expected value E versus E_t, conditional expectations, integrals, gradient, derivatives |
| Indices | agent i, group j, goods, time and sample observations |
| Equalities | equality, strict inequality, weak inequality, approximation, proportionality |
| Equilibrium concept | planner, competitive, partial/general, static/dynamic, information sets |

Preserve symbols, including variants that look interchangeable: c versus C, \beta versus \delta, \pi versus p, q_t versus Q_t, k' versus k_{t+1}, x^* versus x, \mathbb{E}_t versus \mathbb{E}. They may carry different meanings. Do not silently normalize indices, rename discount factors or collapse indexed quantities.

If another model uses a different symbol, explicitly say something like: "The external source writes a_t; on these slides, the corresponding object is k_t." Then use the slides' k_t throughout your own ongoing exposition.

If the slides themselves appear inconsistent, **quote or reproduce the displayed expression as-is**, state the suspected issue separately, and explain the implications under both readings where helpful. Do not silently fix a typo.

For an introduced *new* object that the slides do not name, choose a clearly fresh symbol, explicitly label it as an auxiliary definition, and never reuse an existing symbol with a different meaning.

## Work with images, not just extracted text

Slides can put essential assumptions into plots, handwritten arrows, legends, panels or layout. Inspect those elements when the host allows. For graphs identify:

- Axis variables, units, scale and whether quantities are levels, logs, rates or deviations.
- Equilibrium intersection, feasible set, dynamics, curve shifts versus movements along a curve.
- Whether a visible line is a theoretical relationship, estimated fit, histogram, projection or annotation.
- What is **observed** versus what is inferred from the model.

For tables, preserve labels, sample definitions, units, signs, significance conventions and reported uncertainty. Never invent unreadable tick marks or values.

If a PDF extraction loses mathematical layout or a figure's content, use page images or screenshots if tools permit. If reliable inspection is unavailable, state the limitation and avoid falsely precise readings.

## Source references

Cite the lecture page/slide number where it is actually available. Do not guess numbering from file order. **When the content was read from TeX, take every cited page number from the rendered PDF, not from counting frames in the source:** the title page, `\maketitle`, overlays and appendix frames all shift the count. Before finishing, check each cited number against the PDF page it names; if no rendered PDF is available, cite the frame title instead of a number. If an external model or paper is discussed, make clear it is external, and do not fabricate an exact citation or finding.

When the user asks about "slide 12" without supplying the slide, explain the general principle only if useful, and say that an exact notation-preserving explanation requires the page.
