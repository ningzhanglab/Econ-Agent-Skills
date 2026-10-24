# Professor v0.1: Manual Evaluation Cases

**Purpose:** assess real teaching quality. Passing file-format checks is not evidence of subject expertise, accuracy, slide-reading quality or adaptive teaching.

## Scoring rubric

Score each dimension 0 = failure, 1 = partial, 2 = strong. Record the **exact source slide** used in the run.

| Dimension | 2-point target |
| --- | --- |
| Slide faithfulness | No invented slide claims, equations, numbering or visible features |
| Notation fidelity | No silent changes to letters, primes, conditioning, timing or signs |
| Expert insight | Explains model purpose and mechanism beyond repeating text |
| Rigor | Correct assumptions, derivation and special cases |
| Complementary perspectives | Useful alternative view or example when appropriate, not forced |
| Adaptivity | Matches the question's scope and the student's confusion |
| Cross-field relevance | Connects fields only when grounded and informative |
| Source transparency | Separates slide, derivation, hypothetical example and external source |

Critical fails: invented lecture content, unmarked notation substitutions, incorrect central claim, false citations, or pretending to inspect an unreadable graph. A critical fail means the case does not pass irrespective of numeric sum.

## Cases

### 1. Exact notation under a dynamic program

**Fixture:** any genuine lecture slide with an equation using a prime for a next-period choice and conditional expectations.

**Prompt:** "Explain this Bellman equation intuitively and derive the necessary optimality step. Keep the slide notation."

**Pass:** continues with the original prime and conditional operator; explains trade-offs; states needed assumptions; no invented definitions.

### 2. Narrow mathematics question

**Fixture:** slide with a minus sign after differentiation or a particular substitution.

**Prompt:** "Why does this negative sign appear?"

**Pass:** answers the exact algebra step briefly; does not produce an irrelevant mini-lecture.

### 3. Multiple economic interpretations

**Fixture:** slide with a consumption Euler equation.

**Prompt:** "I understand the formula but not the economics. Explain it from genuinely different angles."

**Pass:** offers different marginal trade-off, real-world and model-assumption perspectives; distinguishes constrained/interior cases; respects notations.

### 4. Visual analysis

**Fixture:** slide with graph, labeled axes, curves and one shift.

**Prompt:** "Explain everything this graph is telling us and what it cannot establish."

**Pass:** verifies actual visual content; identifies movement vs shift, axes and economic logic; does not fabricate numeric values.

### 5. Micro strategic mechanism

**Fixture:** lecture slide with information asymmetry or strategic game.

**Prompt:** "Why does the equilibrium change when information changes?"

**Pass:** states who observes what, why incentives/beliefs change, and a contrasting case.

### 6. Econometric identification

**Fixture:** IV or DID slide with explicit assumptions.

**Prompt:** "Why is this assumption needed? Give a counterexample."

**Pass:** separates identifying assumptions from estimator properties; counterexample changes a meaningful assumption; no causal overclaim.

### 7. Inconsistent lecture notation

**Fixture:** controlled test slide with a deliberate conflict between two equations.

**Prompt:** "Can you derive the result?"

**Pass:** flags the conflict, reproduces both versions, explains the possible interpretations, and does not quietly rewrite the slide.

### 8. Missing or unreadable slide

**Fixture:** reference to a slide number without uploading it, or an unreadable equation screenshot.

**Prompt:** "Explain equation (5) using my slide's notation."

**Pass:** does not hallucinate notation or claim the slide has been read; requests/reports the missing source while providing only clearly generic context if useful.

## Run log template

- Date / Agent & model / Skill commit SHA:
- Slide title or file, page reference:
- Case:
- Prompt:
- Score per dimension:
- Critical fail? Why:
- What should change in the skill:
- New regression case needed?:
