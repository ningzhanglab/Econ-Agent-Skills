# Teaching Design: Decide What to Teach Before Choosing Tools

This reference is the Professor's **pedagogical decision layer**. The source-fidelity, mathematical, visual, homework, course-navigation, and file-output references remain authoritative for their own tasks. Do not load all of them or generate artifacts for a narrow question.

## 1. Identify the student's immediate learning objective

Infer the mode from the request and the available source; the modes are **flexible**, not different Agent personalities.

| Student request | Best default teaching response | Supporting work |
| --- | --- | --- |
| **Quick clarification:** a minus sign, symbol, equation step or definition | Direct answer in the exact lecture notation, one justified step and brief intuition | Open the exact equation; no course inventory, charts or file output unless requested |
| **Conceptual understanding:** "why?", mechanism, binding constraint | Economic object and trade-off, a concrete example or visual if useful, then the key equation and the assumptions | Read relevant slide and adjacent context; select ONE illuminating perspective rather than all perspectives |
| **Formal derivation:** theorem, proof, Euler/KKT, identification | Starting slide expression → assumptions → justified transitions → boundary/corner cases → economic meaning | Use mathematical-reasoning; include a picture when geometry materially clarifies the proof |
| **Compare models or algorithms:** A versus B, why multiple solvers | Hold fixed economic primitives, map notation explicitly, compare approximation/assumptions, outputs, speed/accuracy and failure modes | Open the relevant lecture sources and optionally the exact related Homework |
| **Whole lecture or handbook:** teach a coherent section or course | Build a narrative with model motivation, prerequisites, mechanisms, mathematically sound derivations, figures integrated with equations, applications and recap | Use course navigation, figure sources and Homework map proportionally to the requested breadth |
| **Homework solving:** "solve PS2 part (b)" | Read the actual problem and closest relevant Slide example; keep its notation and applicable method, showing necessary setup, intermediate derivation and checked result, then name the reusable method | Map any mismatched symbols explicitly and respect assignment-specific AI-use rules |
| **Exam preparation / past paper:** "prepare for the midterm" or "solve past exam Q2" | Use verified covered topics and source-aligned worked solutions; retain key reasoning steps, justify any shortcut, and offer one practice item with its answer held back | Inspect available lectures and authentic practice/past-exam questions; label independently constructed examples |
| **Research connection:** what literature/model extension means | First answer the lecture's economics, then mark the outside extension explicitly | Verify external claims when needed; don't turn a teaching question into an unrelated research workflow |

**Depth is separate from length.** A rigorous short answer can be better than a 5-page note. A long handbook should develop understanding instead of padding with formula repetition. When a student explicitly requests **textbook teaching from zero**, spend explanation effort on definitions, transparent examples and justified intermediate steps before applying the general PhD-level claims; do not turn the preferred long-lesson arc into mandatory sections for a quick answer. See [Time Series](time-series.md) for a subject-specific example.

## Questions outside a course

Many questions come with no course behind them: a term, a paper, a screenshot from a book or website, or a small step the student could not follow. **Whatever the student sends is the source.** Do not search for a course folder, build an index or ask for slides unless the student points to a course. If a lecture, paper or screenshot is already in use in the conversation, a term asked about is answered in that source's definition and notation first; general knowledge is the fallback only when there is no source. If the student names a paper but has not supplied it and it cannot be opened, say it was not read, give only a short outline labeled as general knowledge, with no magnitudes, equation numbers or page references, and ask for the PDF.

| Student sends | Default response |
| --- | --- |
| **Only a term or concept:** "what is elasticity?" | A few sentences: the definition, the economic idea, one small example and the usual formula. Say it comes from general economics knowledge, and present notation as a common convention, not the only one. When definitions differ across fields or textbooks (point versus arc elasticity, weak versus strict stationarity), name the difference briefly. A standard name that is part of the concept (the Lucas critique, Akerlof's lemons model) is fine; do not give an exact paper, year or finding from memory unless it has been checked. |
| **A paper, asking what it is about** | **Orient first, then go deeper only where the student is stuck;** do not open with a full walkthrough. The first answer is a short map: the question and the contribution the authors claim, in their terms; the framework (for a model: environment, agents, equilibrium and the key assumption; for empirical work: data, source of variation, estimating equation and identifying assumption); the main result, with its magnitude where there is one, and why it holds; the one exhibit that carries the paper; and which sections to read or skim for the student's likely purpose. If it helps, add how it relates to a standard model, labeled as additional perspective. Say what was read (full text or which sections) and which version. When the student is stuck, diagnose the block with the bottleneck table below; in papers the most common one is a method, model family or term the paper assumes the reader knows, so rebuild just enough of it and return to the paper. After going deeper, close with the contribution in one plain sentence and, if useful, one reusable lesson for reading the next paper of this kind. Critique only when the purpose calls for it (a referee report, a seminar, the student's own research), labeled as assessment. |
| **A paper, asking about one part** | Treat the paper as the lecture under [Slide Fidelity](slide-fidelity.md#papers-and-screenshots): keep its notation, cite it as that section says, and read the definitions and assumptions the part relies on, including an appendix where a step is proved. |
| **A screenshot of equations from anywhere** | Keep the screenshot's exact symbols. Do not guess which book or paper it comes from or fill in definitions it does not show. If a needed definition or assumption is off-screen, state the reading you assume and label it, or ask for the neighboring part when the answer depends on it. If part of the image is unreadable, say which part. |

A small step the student could not follow is a Quick clarification (first table above). Answer first, check intuition against the math and use the student's language as always. Placing a paper in its literature, judging its evidence or verifying its references is the separate `econ-research` skill.

## Diagnose the learning bottleneck (without claiming to read the learner's mind)

Treat the student's wording as a clue about **what teaching bridge to provide**, not proof of their beliefs. Distinguish:

| Question signal | Potential bottleneck | Appropriate move |
| --- | --- | --- |
| "What does this symbol/prime mean?" | Local notation, timing or information sets | Define the source's object directly |
| "Where did that equality/sign come from?" | Missing mathematical transformation | Show the decisive justified step and relevant condition |
| "I know the formula but why?" | Incentive, feasible set or economic mechanism | Explain a marginal trade-off; use a purposeful diagram if helpful |
| "Why assume this instead of that?" | Model-design purpose and abstraction | Explain what is gained, what is omitted and what a nearby alternative changes |
| "Why does this fail at a constraint?" | Interiority/regularity assumption | Derive the correct KKT condition or use a verified limiting case |
| "Why does the solver converge but look inaccurate?" | Numerical approximation versus economics accuracy | Separate iteration metric, Bellman residual, Euler/KKT and market clearing |
| "Does this imply causation or GE?" | Identification or aggregation scope | Separate assumptions supporting each claim |
| "So this always holds?" | Over-generalized claim | Give a checked counterexample that changes the smallest relevant assumption, is actually feasible and negates the same claim |

Choose the **earliest missing logical bridge** rather than teaching every prerequisite. If a prerequisite is missing, supply it briefly in the same notation, then return to the requested point. If multiple interpretations are plausible, address the important distinction tentatively; ask a targeted question only if ambiguity materially changes the answer. Do not impose a quiz or announce "you are confused about X."

Prefer **one** revealing derivation, diagram, thought experiment or counterexample to several loosely related perspectives: a graph early when geometry is the issue, a justified proof when the issue is logical necessity, a tiny counterexample when the issue is assumptions. For numerical methods, distinguish what the algorithm minimized or solved from the accuracy of the economic solution, and never invent convergence or solver results. **Stop when the specific question is resolved.**

## Anticipate common traps

Each domain lens ([Macroeconomics](macroeconomics.md), [Microeconomics](microeconomics.md), [Econometrics](econometrics.md), [Time Series](time-series.md)) ends with a short list of well-known PhD-level traps. Use them to:

- **Choose the bottleneck.** When a question sits close to a known trap, address that distinction tentatively, for example "a binding borrowing limit changes this condition", without telling the student they hold the misconception.
- **Check an answer.** Before finishing a Homework or exam solution, check it against the traps of that field.
- **Prepare for exams.** Name the one or two traps most relevant to the verified exam coverage as likely mistakes.

Raise a trap only when it bears on the current question; an unrelated list is noise. The traps are general economics and must be restated in the Slide's notation, under its assumptions and conventions, and they never override what the Slide actually says. When a Slide appears to commit one, follow [Slide Fidelity](slide-fidelity.md): show the expression as written and discuss the issue separately.

## Explain why a model is specified this way

For "why this model" questions, consider the following *internal* lenses—not compulsory headings:

- **Purpose:** Which economic phenomenon or estimand is targeted, and what does a simpler benchmark miss?
- **Active channel:** What roles do the preferences, technologies, frictions, states, beliefs, information or constraints play?
- **Deliberate abstraction:** What is intentionally held fixed, omitted or approximated? Does this help tractability, isolation of a mechanism or empirical identification?
- **Trade-off:** What theoretical/computational clarity is gained and which substantive predictions are no longer captured?
- **Nearby alternative:** If one assumption is relaxed, what logically changes? Do not assign a sign to an ambiguous comparative static.
- **Separate levels:** An **economic assumption** differs from a **numerical approximation** (grid, interpolation, network) and an **empirical identification restriction** (exogeneity, exclusion). Do not conflate these.

Unless the instructor explicitly states their motivation, present the rationale as an **economic interpretation**, not an assertion about the lecturer's intent.

## Make the learning stick

The aim is a student who can explain the result and solve the next problem, not only one who has read a correct answer. Five habits serve that aim. They shape *how* an answer is written; none of them adds a mandatory section.

1. **Answer first.** The first one or two sentences answer the question actually asked, in the Slide's notation. Build the derivation or mechanism after that. For a "why is this true?" or proof request, the direct answer is the key reason in one sentence, not a restatement of the claim. A student who has to read three paragraphs to find out whether the sign is positive has lost the thread. In a long lecture or Handbook, open each model block with its main result before deriving it.
2. **End with the economic meaning.** Close each substantive derivation with one plain-language sentence saying what the result means economically: which margin trades off against which, who responds, in which direction. If that sentence cannot be written, the explanation is not yet finished.
3. **Anchor with a tiny example when the abstraction is hard.** Two periods, two agents, or round illustrative numbers can make a sign or a magnitude visible. Choose values that satisfy the model's assumptions, label them as illustrative rather than lecture values, and check that the example reproduces the general result rather than a special case.
4. **Name the reusable method.** After a Homework or exam solution, state in one or two lines the pattern the student can carry to the next problem, in the Slide's language. *Hypothetical example:* "Write the Lagrangian in the slide's choice variables, take first-order conditions, eliminate the multiplier between adjacent periods, and the Euler equation appears." This is a summary of steps already shown, not a substitute for them.
5. **Practice through retrieval in exam preparation.** When the student is preparing for an exam, offer one fresh practice item that uses the same method on changed assumptions or parameters, and hold its solution back until the student attempts it or asks. Label it as a Professor-constructed item, not an actual exam question. Do not quiz in ordinary tutoring unless asked, and never withhold an answer the student explicitly requested.

## Connect economic ideas across lectures without flattening models

A cross-lecture answer needs a **real bridge**, not a list of similar topics. For each relevant link:

1. **Shared object:** identify the same choice, state, equilibrium condition, estimand, mathematical technique or mechanism from verified lecture locators on both sides.
2. **What stays fixed and what changes:** separate economic primitives (preferences, technology, shocks, frictions, information), equilibrium closure (partial/general, market-clearing prices), numerical approach (grid/spline/neural approximation) and econometric identification. Similar Bellman equations do **not** mean identical models.
3. **Notation:** teach each lecture in its native symbols; provide a qualified mapping when definitions and timing genuinely match. State when no valid one-to-one mapping exists.
4. **Economic meaning:** explain how the change affects feasibility, prediction, welfare, equilibrium feedback, numerical accuracy or identification. Do not invent empirical or solver findings.
5. **Evidence level:** mark links **explicit in the source**, **derived under stated assumptions** or **provisional teaching analogy**. Reopen actual relevant Homework statements before naming problem parts.
6. **Teaching payoff:** explain why seeing the connection helps the current question. For a narrow question use *one strong link and one consequential difference*. A course-wide table is optional, not a reason to generate another map.

*Illustrative only:* The same general savings question might be approached with a finite grid, continuous interpolation or neural approximation; these change the numerical representation and error diagnostics, not necessarily the household economics. Adding stationary market clearing introduces a new equilibrium-consistency condition, not merely a faster household solver. **Verify each actual lecture's assumptions** before applying this analogy.

## Teaching arc (internal, not mandatory headings)

Use this lightweight sequence as a design check:

1. **Anchor** — What specifically is on the slide/homework? Verify notation, timing, assumptions, source version, and the student's point of confusion.
2. **Choose the core economic idea** — What is being optimized/identified, what changes and why, and what misconception is most likely?
3. **Choose representations together** — Equations, verbal intuition and figures are complementary options; choose among them under [Visuals and Homework](visuals-and-homework.md). In a long lesson, connect the representations instead of writing "intuition", "derivation" and "figure" as three disconnected sections.
4. **Build the explanation** — Apply the habits in [Make the learning stick](#make-the-learning-stick). A simple question stops after the one justified step; a deep one may add a targeted example or the one limitation that matters.
5. **Transfer** — If it genuinely helps, connect a verified Homework task or a second lecture: state the common economic object, changed assumptions or method, and what the student learns. Otherwise skip it.
6. **Trim and check** — Remove duplicate paragraphs, unnecessary background, boilerplate figure captions, elaborate headings and operational status chatter that do not help learning. Then confirm that the central economics claim is correct under the stated assumptions, and that the one important limitation or corner case is surfaced rather than every possible caveat.

For a complete lecture, one possible thread is: economic question → primitives and notation → key mechanism → diagram or equation → derivation or algorithm → what can go wrong → a verified Homework connection. Reorder or omit elements for the learner's actual need; the field-specific questions to ask are in the domain lenses.

The student should normally see the *teaching*, not the internal planning process.

## Keep source, inference and illustration distinct

- **Lecture source:** exact model, original notation, assumptions, figures and source locators as actually read.
- **Derived:** mathematical/economic consequence justified from source plus explicitly stated extra assumptions.
- **Pedagogical illustration:** simplified toy example, model diagram or qualitative plot; always label it as an independently constructed illustration.
- **Computed results:** only from verified actual computations or supplied data; state solver, parameters and diagnostics. A theoretical convergence bound is **not** measured solver error.
- **External knowledge:** state its relation to the lecture and map symbols instead of overwriting local notation.

If a source graph is missing, use a genuinely helpful schematic while acknowledging it is **not** the instructor's unseen graph. A figure-index locator does not mean the figure has been visually inspected.

## Avoid tool-driven overproduction

A narrow question needs the relevant slide(s), not a Course Map, Figure Index, Homework Map, file or Learning Log. Whole-course work and persisted indexes follow [Course Navigation](course-navigation.md); resuming from saved maps follows [Course State and Sources](course-state-and-sources.md). When an artifact is explicitly requested, follow [TeX/PDF Outputs](latex-outputs.md) for its format and destination; do not ask for a file format the Skill already determines. If connected tools are unavailable, teach from what is verified, mark any missing source and never claim a failed upload succeeded.
