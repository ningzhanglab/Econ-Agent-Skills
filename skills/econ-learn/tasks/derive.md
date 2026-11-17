# Derive: Derivations, Proofs, Skipped Steps and Counterexamples

## Defaults

- **Steps shown:** every step the conclusion turns on, with its reason. Routine algebra may be skipped when skipping it hides nothing.
- **Start from the source.** The first line is the source's own expression, in its symbols.
- **A picture** when geometry materially clarifies the proof.

## Derive without notation drift

1. Copy or restate the exact starting equation in the source's symbols.
2. Identify the choice, state and parameter objects, and the feasibility or regularity conditions.
3. Write the transformations in a justified sequence, and explain the economic meaning of the crucial steps.
4. Check conditioning, law of motion, timing, dimensions and signs.
5. Interpret the result and say whether it needs interiority, concavity, transversality, differentiability, stationarity or another restriction.

Never silently swap a prime for $t+1$, a sequence constraint for a scalar constraint, $\mathbb{E}_t$ for $\mathbb{E}$, or an equality for an inequality.

## Optimization and equilibrium checklist

- Distinguish the objective from constraints and from equilibrium conditions.
- For Lagrangians, check the multiplier convention and the sign of each constraint.
- For derivatives, state what is held fixed; distinguish total, partial and envelope derivatives.
- For dynamic models, keep continuation values, discount factors, integration and information sets as the source has them.
- For first-order conditions, check necessary versus sufficient; discuss corners and complementary slackness where relevant. At a boundary, rederive the KKT conditions and multiplier signs in the source's constraint convention; do not apply an interior Euler equality automatically.
- For stochastic models, keep the order of expectation and nonlinear functions; do not imply $E[f(X)] = f(E[X])$ without justification.
- For general equilibrium, close markets and consistency conditions; do not infer an aggregate comparative static from a partial-equilibrium sign alone.
- For computations, separate stopping criteria, theoretical bounds, Bellman residuals, policy or Euler errors and market clearing. They are not interchangeable evidence of correctness.

## Proofs and counterexamples

- Restate the exact proposition, quantifiers, conditioning and assumptions before deriving or challenging it. Separate source assumptions from supplemental ones.
- Show the pivotal step. A first-order equality need not prove an unconstrained optimum.
- A counterexample changes one specific assumption, is feasible (and consistent with equilibrium if that matters), and refutes the same claim. An anecdote is not a counterexample.
- For comparative statics, state what is held fixed and whether prices or aggregates adjust.

Explain the economic meaning of the step on which the conclusion turns, rather than offering a long generic calculation.

## When the source skips steps

Work out the missing steps in the source's notation and describe them as a supplementary derivation. If crucial assumptions are missing, state which ones make the derivation valid. For a possible error, show the source version first and offer a clearly labeled correction.

## Check the intuition

A tiny worked example is often the fastest check: two periods, two agents or round numbers that satisfy the model's assumptions. Label the values as illustrative, confirm they do not create a corner or special case the general claim excludes, and say what the example does not prove. After a verbal explanation, use a sign check or a special case to confirm it agrees with the displayed condition. Do not present invented coefficients as the lecturer's.

Close with the economic meaning in one plain sentence, and check the result against the traps of its field ([Macroeconomics](../guides/macroeconomics.md), [Microeconomics](../guides/microeconomics.md), [Econometrics](../guides/econometrics.md), [Time Series](../guides/time-series.md)).
