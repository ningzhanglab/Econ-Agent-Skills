# Time Series — Specialist Reasoning Lens

This is an **optional domain reference inside the existing `econ-phd-professor` Skill**, not a separate course Skill or a fixed STAT 516 teaching script. Use it only when a Time Series question benefits from domain-specific reasoning. It applies to statistics and econometrics; do not force economic or causal interpretations onto a statistical result.

## Start from the real learning task

Identify what the user is trying to understand: an intuition, one notation sign, a derivation, interpretation of a plot, comparison of models, analysis of software output, an assignment, exam preparation, or a larger lesson. Match the **depth, prerequisites, representation and level of explanation** to the current request and the material actually available.

- For a narrow technical question, answer directly and justify the decisive step.
- For a conceptual or multi-step question, motivate the statistical object, define what matters, derive the relevant relationships and interpret the result with a useful example or visual **when it improves understanding**.
- For a requested course lesson, keep the instructor's verified sequence while bridging important prerequisites if needed.
- Do **not** enforce an Intuition → Example → Definition → Derivation → Graph template, assume every student starts from zero, require SAS, or produce a long textbook chapter by default.
- Do not equate mathematical rigor with excessive length. Mathematical correctness, conceptual clarity and source fidelity matter more than any prescribed format.

## Domain-specific reasoning checks

Apply **only the checks relevant to the actual problem**, and retain the source's symbols and conventions.

- **Process versus data:** distinguish a stochastic process, an individual realization, sample estimates and population quantities. Specify what assumptions justify a formula for moments, dependence or uncertainty.
- **Lag notation and model conventions:** distinguish innovations from observed values, intercepts from unconditional means, and the lag polynomial of an AR component from that of an MA component. Track signs, indices and normalization instead of swapping in another textbook's convention.
- **Stationarity and dynamics:** clarify strict versus weak stationarity and the needed moments; analyze linear recursions, characteristic roots, unit roots and transformations under explicit assumptions. A visual impression alone does not prove stationarity.
- **Stationarity versus invertibility:** identify the *correct polynomial for each property*, explain the relevant root condition using the course's notation, and distinguish a model representation property from estimated-sample diagnostics.
- **ACF, PACF and identification:** distinguish theoretical from sample ACF/PACF. Explain model patterns with appropriate assumptions, and do not treat estimated cutoff/tail-off patterns as deterministic model-selection rules.
- **Estimation, tests and forecasts:** separate identifying/model assumptions, parameter estimation, uncertainty, diagnostic adequacy and predictive performance. For unit-root or other specialized tests, identify the null, regression specification, deterministic terms and appropriate reference distribution rather than using generic shortcuts.
- **Software output:** if SAS, R, Python or other output is supplied, inspect the actual command, model, table, axes and diagnostics before interpreting coefficients, tests or forecasts; do not fabricate computed results.

A good explanation should illuminate *why* the property is relevant (e.g. what invertibility buys, why differencing is considered, what PACF measures) without automatically covering every nearby concept.

## Common traps to anticipate

These are general economics, not claims about the lecture. Use them as described in [Teaching Design](teaching-design.md#anticipate-common-traps): restate the point in the Slide's notation and under its assumptions, follow the Slide's sign and timing conventions, and raise only the trap that bears on the current question.

- **The intercept read as the mean.** In a stationary autoregression with an intercept, the unconditional mean is the intercept divided by one minus the sum of the autoregressive coefficients, under the usual sign convention; check the Slide's convention.
- **Stationarity and invertibility attached to the wrong polynomial.** Stationarity (causality) depends on the roots of the AR polynomial and invertibility on the roots of the MA polynomial. Whether the condition reads "outside" or "inside" the unit circle depends on whether roots of the lag polynomial or of the characteristic equation are used; follow the Slides.
- **Sample ACF and PACF cut-offs treated as rules.** Theoretically the PACF of an AR(p) cuts off after lag p, the ACF of an MA(q) after lag q, and both tail off for a mixed ARMA. Sample versions carry sampling error, so they guide identification alongside diagnostics rather than decide it.
- **Failure to reject a unit root read as proof of one.** The augmented Dickey–Fuller null is a unit root and the test has low power against near-unit-root alternatives; KPSS reverses the null. The deterministic terms in the test regression change the reference distribution.
- **Differencing assumed harmless.** Differencing a trend-stationary series introduces a non-invertible MA unit root (over-differencing).
- **Regressions between integrated series taken at face value.** Independent random walks often produce high R² and significant t-statistics (spurious regression) unless the series are cointegrated.
- **Forecast uncertainty misjudged.** For a stationary process, forecasts revert to the mean and the forecast-error variance rises toward the unconditional variance; for a unit-root process it grows without bound. Plug-in intervals also ignore parameter-estimation uncertainty.

## Sources, examples and assignments

Follow [Slide Fidelity](slide-fidelity.md), [Mathematical Reasoning](mathematical-reasoning.md), and [Visuals and Homework](visuals-and-homework.md). Determine source roles from the **actual course**: verified syllabus/order, authoritative instructor materials, specific assignments and any supplemental notes. Do not infer chronology solely from filenames.

Keep the professor's stated result distinct from your derivation, any apparent correction, and a newly constructed example. Original figures require inspection; example figures and computed results need explicit provenance. Respect verified assignment constraints and the user's requested detail. No fixed homework answer length or study-guide structure is imposed by this reference.

**Course-specific Project context is separate from this Skill:** course URLs, previous generated handbooks, a preferred PDF's writing style, individual assignment policies and output-folder names should not become default behavior across courses. Treat prior generated materials as possible learning aids, not as verified authority over original lectures. File creation and private cloud saving remain request-driven under the existing general workflow.
