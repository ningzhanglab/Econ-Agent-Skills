# Macroeconomics Professor Lens

Read this when slides address dynamic macroeconomic models or aggregate outcomes. Retain slide-specific notation and conventions.

## Questions a macro expert asks

- Is the object a household, firm, social planner, representative agent, heterogeneous agent, government or entire equilibrium?
- What are the endogenous states, controls, shocks and equilibrium prices?
- Which forces operate across time: substitution, wealth effects, uncertainty, capital accumulation, expectations, borrowing constraints, adjustment costs?
- What maps individual decisions into aggregate quantities? Is aggregation valid?
- Is the result transitional dynamics, steady state, balanced growth path, impulse response, welfare comparison or distributional outcome?
- Which closures, market clearing conditions and expectation assumptions are essential?

## High-value explanations

- Dynamic programming: show the *economic recursive structure*, not just Bellman algebra; relate current control and continuation value.
- Euler/envelope conditions: explain intertemporal trade-offs with relevant uncertainty, shadow value and constraints.
- Growth theory: distinguish level effects, long-run growth effects and transition dynamics.
- RBC/New Keynesian: compare underlying shocks, frictions, propagation, policy, and empirical interpretation when the particular lecture warrants it.
- Heterogeneous-agent models: distinguish individual policy functions, cross-sectional distribution dynamics and aggregate welfare; note why representative-agent intuition can fail.

## Common traps to anticipate

These are general economics, not claims about the lecture. Use them as described in [Teaching Design](teaching-design.md#anticipate-common-traps): restate the point in the Slide's notation and under its assumptions, follow the Slide's sign and timing conventions, and raise only the trap that bears on the current question.

- **Euler equality at a binding borrowing limit.** When a lower bound on assets binds, the household would like to borrow more than it can, so the Euler condition holds as an inequality with a nonnegative multiplier and complementary slackness, not as an equality. Derive the direction of the inequality from the Slide's constraint convention.
- **Envelope condition used where it may fail.** The envelope (Benveniste–Scheinkman) result needs the value function to be differentiable at that point, which interior choices help deliver. At a corner or kink, check differentiability before using the derivative of the value function.
- **Euler equation plus resource constraint taken to pin down the path.** These difference equations also admit explosive paths; the transversality condition, or another terminal condition, selects the optimal one.
- **Level effects read as growth effects.** In the Solow model a higher saving rate raises the steady-state level of output per worker, and the growth rate only during the transition; long-run growth comes from technology. Endogenous-growth models differ, so check which model the Slide uses.
- **Partial-equilibrium response read as general equilibrium.** A household's saving response to the interest rate, holding the rate fixed, is not the equilibrium effect once the rate adjusts to clear the asset market.
- **Jensen's inequality ignored.** Expected marginal utility of uncertain consumption differs from marginal utility of expected consumption unless marginal utility is linear. With convex marginal utility (prudence), income risk raises saving: precautionary saving. Certainty equivalence is a linear-quadratic result, not a general one.
- **Representative-agent aggregation taken for granted.** Aggregates behave like one household only under conditions such as Gorman-form preferences or suitable complete markets. With incomplete markets and borrowing limits, the wealth distribution matters for aggregates.
- **Timing of states and shocks misread.** Whether capital in a period is chosen one period earlier, and when a shock is realized, decides which variables can jump on impact. Read the Slide's dating before interpreting an impulse response.
- **Ricardian equivalence stated without its conditions.** It needs lump-sum taxes, no binding borrowing constraints and a horizon, or altruistic links, that covers the future tax burden.

### Numerical methods

- **A small change between value-function iterations read as a small error.** For a contraction with modulus β in the sup norm, the distance to the fixed point is bounded by β/(1−β) times the last change; with β near one that factor is large.
- **Convergence on the grid read as an accurate policy.** Evaluate Euler-equation errors at points off the grid, and report them in the units the course uses.
- **A solved household problem read as an equilibrium.** In a stationary heterogeneous-agent model, the household solution at a guessed price must also clear the asset market. Inner-loop and outer-loop errors are different objects.

Connect to microeconomic foundations or econometric identification when illuminating, but never inject a different model's symbols without an explicit map.
