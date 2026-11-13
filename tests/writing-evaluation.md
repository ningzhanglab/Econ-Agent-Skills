# Econ Writing: Manual Evaluation Cases

**Purpose:** check that `econ-writing` improves prose without changing what the writer said. Structural tests only confirm that the files and links exist.

## Critical fails

Any of these fails a case regardless of how much the prose improved:

- A technical or defined term replaced by a synonym or a nearby term.
- A symbol, number, citation key, label or table/figure reference changed.
- A condition, caveat or scope statement dropped, or a claim made stronger or weaker than the original.
- An invented reference, result, robustness check or motivation.

## Cases

### 1. Terminology under pressure

**Fixture:** a results paragraph that repeats "local average treatment effect" four times and also uses "estimate" and "estimator" correctly.

**Prompt:** "Make this paragraph read better."

**Pass:** the term appears in the same form every time it did before; no "impact" or "effect size" substitutions; estimate and estimator are not swapped.

### 2. LaTeX file edit

**Fixture:** a `.tex` section with inline and display math, `\citet` keys, `\eqref`, a footnote and a table.

**Prompt:** "Tighten the prose in section 3 of this file."

**Pass:** only running prose and footnote text change; math, keys, labels, macros and table numbers are identical; braces balance; the file compiles if a compiler is available, or the response says compilation was not run.

### 3. Hedges that carry conditions

**Fixture:** "Under the exclusion restriction, and conditional on county fixed effects, the estimates could suggest that access to credit may raise small-business entry."

**Prompt:** "Remove the hedging."

**Pass:** the empty hedges go; "under the exclusion restriction" and "conditional on county fixed effects" stay.

### 4. Causal language

**Fixture:** a descriptive cross-sectional regression written up as "X causes Y".

**Prompt:** "Edit this results section."

**Pass:** the causal wording is flagged with a reason; it is not silently rewritten in either direction.

### 5. No invented literature

**Fixture:** an introduction paragraph claiming "a large literature has studied this question" with no citations.

**Prompt:** "Polish the introduction."

**Pass:** no citations or paper names are added; the response flags that the claim needs references from the writer.

### 6. Review mode

**Prompt:** "Review my introduction, don't rewrite it."

**Pass:** returns a ranked list of issues with locations and suggested fixes, starting with structure (is the contribution clear, are results stated with magnitudes), and does not return a rewritten introduction.

### 7. Homework write-up

**Fixture:** a homework solution with a missing justification step, and a course policy that allows editing help with presentation only.

**Prompt:** "Clean up my write-up."

**Pass:** improves the wording, keeps the course notation and method, points out the missing justification without supplying it, and mentions the course policy once.

## Run log template

| Date | Case | Fixture source | Critical fail? | Notes |
| --- | --- | --- | --- | --- |
