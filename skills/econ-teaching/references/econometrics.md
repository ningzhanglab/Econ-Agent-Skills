# Econometrics Professor Lens

Use this for probability/statistics, econometric theory, causal inference, time series, structural estimation and empirical research slides.

## Questions an econometrics expert asks

- What is the target: population parameter, estimand, estimator, hypothesis, forecast or causal effect?
- What is the data-generating process and sampling/time-series structure?
- What assumptions identify the target? Which only justify estimation or inference?
- What do consistency, unbiasedness, asymptotic normality, efficiency and finite-sample properties say *separately*?
- How do dependence, heteroskedasticity, endogeneity, misspecification or limited overlap affect conclusions?

## High-value explanations

- OLS: distinguish algebraic projection, statistical conditional expectation and causal interpretation.
- IV: explain why instrument relevance and exclusion are different and what quantity is identified.
- Potential outcomes/DID/RDD: explicitly track treatment definition, counterfactual assumptions and the scope of identified effects.
- Maximum likelihood/GMM: connect sample criterion, population moment or likelihood, regularity conditions and uncertainty.
- Time series: explain lag polynomials, stationarity, invertibility, innovations and forecast error using the **lecture's symbols and sign conventions**, not a different textbook's ARMA convention. For specialized interpretation of AR/MA/ARMA dynamics, ACF/PACF, tests or forecasts, use the optional [Time Series reasoning lens](time-series.md) within this same Skill; it does not prescribe a course teaching format.

## Common traps to anticipate

These are general economics, not claims about the lecture. Use them as described in [Teaching Design](teaching-design.md#anticipate-common-traps): restate the point in the Slide's notation and under its assumptions, follow the Slide's sign and timing conventions, and raise only the trap that bears on the current question.

- **A strong instrument taken to be a valid one.** Relevance and exclusion (exogeneity) are separate conditions; first-stage strength cannot test exclusion.
- **IV taken to identify the average treatment effect.** With heterogeneous effects, a binary treatment and a binary instrument, under independence, exclusion and monotonicity it identifies a local average treatment effect for compliers.
- **Heteroskedasticity said to bias OLS.** Under exogeneity OLS remains unbiased and consistent. Heteroskedasticity invalidates conventional standard errors and Gauss–Markov efficiency.
- **Unbiasedness and consistency treated as the same property.** An estimator can be biased yet consistent, such as the variance estimator that divides by the sample size, or unbiased yet inconsistent, such as using only the first observation to estimate a mean.
- **A high R² read as causal evidence or correct specification.** R² measures in-sample fit and says nothing about identification.
- **More controls assumed to be safer.** Conditioning on a post-treatment variable or a collider can create bias that was not there.
- **p-values and non-rejection misread.** A p-value is the probability, under the null, of a statistic at least as extreme as observed; it is not the probability the null is true. Failing to reject is not accepting the null; it can reflect low power.
- **Flat pre-trends taken to prove parallel trends.** The assumption concerns untreated potential outcomes after treatment, which are never observed; pre-trends are supporting evidence only. With staggered adoption and heterogeneous effects, two-way fixed-effects estimates can put negative weight on some group-period effects.

When reading graphs, distinguish fitted relations, residual diagnostics, confidence intervals and causal diagrams. If an equation is about correlation, do not relabel it a causal effect.

A compelling real-world example should clarify the statistical object **without** turning unverified data into facts.
