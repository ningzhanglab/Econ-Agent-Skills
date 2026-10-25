# Mathematical Reasoning for Economics PhD Slides

## Derive without notation drift

1. Copy or restate the exact starting equation using the slide's symbols.
2. Identify the choice, state and parameter objects, plus feasibility/regularity conditions.
3. Write algebraic transformations in a justified sequence; explain the economic interpretation of the crucial steps.
4. Check conditioning, law of motion, timing, dimensions and signs.
5. Interpret the final result and identify whether it requires interiority, concavity, transversality, differentiability, stationarity or another restriction.

Never silently swap a prime for t+1, a sequence constraint for a scalar constraint, \mathbb E_t for \mathbb E, or an equality for an inequality.

## Optimization and equilibrium checklist

- Distinguish objective from constraints and equilibrium conditions.
- For Lagrangians, check multiplier conventions and the sign of constraints.
- For derivatives, state what is held fixed; distinguish total from partial and envelope derivatives.
- For dynamic models, maintain continuation values, discount factors, integration and information sets from the slides.
- For FOCs, verify necessary/sufficient conditions; discuss corners and complementary slackness where relevant.
- For stochastic models, preserve order of expectation and nonlinear functions; do not imply E[f(X)] = f(E[X]) without justification.
- For general equilibrium, close markets and consistency conditions where needed; do not infer aggregate comparative statics from a partial-equilibrium sign alone.

## Choose proofs, counterexamples and numerical checks carefully

- Restate the **exact** proposition, quantifiers, conditioning and assumptions before deriving or challenging it. Separate source assumptions from supplemental ones.
- Show the pivotal mathematical step and distinguish necessary from sufficient conditions. A first-order equality need not prove an unconstrained optimum.
- For a **counterexample**, change a specific assumption, confirm the construction is feasible (and consistent with equilibrium if that matters), and verify it refutes the **same** claim.
- At a boundary, rederive KKT/complementarity and multiplier signs using the source's constraint convention; do not automatically apply an interior Euler equality.
- For comparative statics, state what is held fixed and whether prices/aggregates adjust.
- For computations, separate stopping criteria, theoretical bounds, Bellman residuals, policy/Euler errors and market clearing. These are not interchangeable proof of correctness.

Explain the economic meaning of the **step on which the conclusion turns**, rather than offering a long generic calculation.

## What if a slide skips steps?

Work out the missing steps **in the slide's notation**, explicitly describing them as supplementary derivation. If crucial assumptions are missing, state which ones make the derivation valid. For a potential error, preserve the source version first and offer a clearly labeled correction rather than silently rewriting the course material.

## Validate intuition mathematically

An analogy is not a proof. After a verbal explanation, use sign checks, special cases or a numerical thought experiment to make the economic interpretation consistent with the displayed condition. Do not invent coefficients to claim they came from the lecturer.
