# 2026-10-24 — Remove legacy STAT 516 template overfitting

## Motivation
The user clarified that the previously supplied STAT 516 Project Instructions were **an older design, not the design brief for current or future teaching**. The immediately preceding Time Series reference leaned too heavily on a specific seven-stage textbook style, beginner-first assumption, homework/study-guide distinction and SAS workflow.

## Change
- Reworked `skills/econ-phd-professor/references/time-series.md` as a **compact, optional domain-reasoning reference** inside the existing Professor Skill. Preserved source-notation rigor, process/population/sample distinctions, lag-polynomial root reasoning, AR/MA/ARMA/ARIMA understanding, diagnostics and forecast interpretation.
- Removed any prescribed lesson sequence, default beginner-assumption, specific software priority and required output structure. A user requesting beginner-level or textbook-style teaching still receives it via adaptive Professor rules.
- Updated Econometrics routing, LaTeX study-guide language and README to avoid describing the historical STAT 516 directions as a global design.
- Retained existing source-fidelity, user-selected cloud destination, opt-in Learning Logs and privacy policies.
- Did **not** modify any STAT 516 private materials, course Project Instructions, output files or previous historical changelog/log entries.

## Validation
- Reviewed the current Professor Skill and directly affected references and performed a narrow editorial consistency check.
- Verified reference-path and source-role consistency after writeback; existing GitHub Actions CI is the regression path. No duplicate Skill, new full-course PDF, Drive benchmark or speculative testing.

## Policy
A course's previous instructions are evidence of what worked or failed, **not a global teaching specification**. Add reusable rules only when they capture a genuine domain-method distinction or verified teaching failure. Preserve the student's current intent and lecturer's actual mathematics as primary.
