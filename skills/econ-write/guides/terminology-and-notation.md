# Terminology and Notation

The writer's terms and symbols are fixed points. An edit that reads better but changes a term has changed the paper.

## Build the term list before editing

Read the whole document, or the whole section plus any definitions it relies on, and note:

- **Defined terms:** anything the writer introduces with "we call", "we define", "we refer to … as", a definition environment, or italics at first use.
- **Field terms:** standard vocabulary with a precise meaning in economics or econometrics. Examples: identification, estimand, estimator, estimate, treatment effect, ATE, LATE, instrument, first stage, exclusion restriction, fixed effects, clustering, stationarity, unit root, cointegration, steady state, balanced growth path, Euler equation, value function, policy function, stationary distribution, general equilibrium, partial equilibrium, incidence, pass-through, elasticity, marginal propensity to consume.
- **Proper names:** models (Aiyagari model, New Keynesian model), estimators (2SLS, GMM, difference-in-differences), tests (ADF, Hausman), datasets, surveys, programs and policies.
- **Acronyms**, with their expansion at first use.
- **Labels for the writer's own objects:** names of specifications, samples, treatment groups, scenarios or counterfactuals ("baseline sample", "Specification 2", "the no-borrowing economy").

## Rules

- Use each term in exactly the writer's form: spelling, capitalization, hyphenation and singular or plural as the writer uses them. Keep the writer's spelling convention (American or British).
- Never rotate synonyms for variety. Repeating "treatment effect" five times is correct; switching to "impact", "influence" or "consequence" is not.
- Never trade a term for a nearby one. These pairs are different objects: estimand and estimate; estimate and estimator; correlation and effect; association and causation; significant (statistical) and large (economic); shock and innovation; risk and uncertainty; equilibrium and steady state; a policy function and a policy.
- Keep the writer's choice of "we" or "I", and keep the tense conventions they use.
- Expand an acronym only where the writer first uses it, if the expansion is missing; do not expand it again later.
- When the writer uses two terms for one object or one term for two objects, flag it with both locations and let the writer choose. Do not unify silently.
- When a term appears to be used incorrectly, flag it with a short reason. Do not replace it in the text.

## Notation and numbers

- Leave every symbol, subscript, superscript, prime, hat, bar, tilde, time index and sign exactly as written, in display math and inline math.
- Leave every number unchanged: coefficients, standard errors, confidence intervals, p-values, sample sizes, percentages, dates, and table, figure, equation and section numbers.
- Do not reword "statistically significant at the 5 percent level" into a different threshold or drop the level.
- If prose and a table disagree, or a symbol is used inconsistently, flag it instead of editing either side.

## LaTeX files

Change only running prose. Keep these exactly as they are:

- Math in `$…$`, `\(…\)`, `\[…\]` and math environments (`equation`, `align`, `gather` and their starred forms).
- Commands and their arguments that are not prose: `\label`, `\ref`, `\eqref`, `\cref`, `\cite`, `\citet`, `\citep` and their keys, `\input`, `\include`, `\includegraphics`, file paths and options.
- User-defined macros and their names (`\E`, `\Var`, `\beta`), environments, preamble, comments (`% …`), tables' numeric content, `tikz` and `pgfplots` code, and code listings.
- Non-breaking spaces and spacing commands such as `~` and `\,` before references and units.

Prose inside `\section{}`, `\caption{}`, `\footnote{}` and `\emph{}` may be edited under the same terminology rules. Keep the braces balanced. After editing a file, compile it if the environment allows, and say so if it does not.

## Final check

Before returning the edit, compare it with the original:

1. Every entry in the term list appears in the same form wherever the writer used it.
2. Every symbol, number, label and citation key is unchanged.
3. No sentence that stated a condition, caveat or scope lost it.

Report anything you flagged but did not change.
