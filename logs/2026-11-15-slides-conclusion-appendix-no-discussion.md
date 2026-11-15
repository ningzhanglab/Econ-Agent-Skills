# 2026-11-15 — Slides: Conclusion, Appendix, no Discussion by default

- **Date:** 2026-11-15
- **Component:** `econ-teaching` (slides reference and template)
- **Change type:** Changed
- **Status:** Implemented
- **Related commit / PR:** See Git history for this change

## Motivation

After the first real deck (a paper presentation), the user said they usually end with a Conclusion or Takeaways slide, call the extra slides "Appendix" rather than "Backup", and do not add a Discussion slide by default. The same exchange also showed that source lines had been put on text-only slides; the existing rule (one source line under each figure or table) already covered that, so only the deck was corrected. The user then asked again why so many source notes were needed, so the rule was made explicit (see the addition below).

## Changes made

- `slides.md`: "Backup" becomes "Appendix" throughout; the deck ends with a Conclusion (or Takeaways) slide then the Appendix; a Discussion slide is made only on request.
- `slides.md`: source lines only under figures and tables (and quotations); a text-only slide carries none, and section or equation references go in the handover.
- `simple-slides.tex`: the Takeaways frame is titled "Conclusion", the Discussion frame is removed, and the appendix frame is titled "Appendix: derivation".
- `tests/test_professor_contracts.py`: the slides contract test now looks for "Appendix".
- `link/econ-teaching.md`: regenerated with `tools/build_link_editions.py`.

## Files affected

`skills/econ-teaching/references/slides.md`, `skills/econ-teaching/templates/simple-slides.tex`, `tests/test_professor_contracts.py`, `link/econ-teaching.md`, `CHANGELOG.md`.

## Behavior and compatibility

New decks have no Discussion slide unless asked, and use "Appendix". Existing decks are unaffected. Users who want a Discussion slide can ask for it.

## Verification and evidence

| Check | Result | Evidence or reason |
| --- | --- | --- |
| File / syntax inspection | Pass | Searched `slides.md` and the template for "Backup" and "Discussion"; only the on-request wording remains. |
| Automated structural validation | Pass | `python tests/validate_skills.py`: 3 skills passed; `python -m unittest discover -s tests`: 60 tests OK. |
| Real slide / domain evaluation | Partial | The edited 22-page deck for the paper that prompted this change compiled with no overfull boxes; no new deck was built from the template. |
| GitHub Actions or other CI | Not run | Not pushed. |

## Known limitations and risks

The "on request" wording relies on the agent not adding a Discussion slide; no test checks deck contents.

## Follow-up

None planned.
