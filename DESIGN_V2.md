# Econ Agent Skills — v2 Design

Adopted 2026-11-16 at the user's request, after a review of every prompt and of the 80 development logs. It replaces [DESIGN_V1.md](DESIGN_V1.md), which is kept as history. The v1 teaching rules are carried over; what changed is where they live.

## Why v1 was rebuilt

Each design choice below answers a failure recorded in the logs.

| Observed in the logs | Consequence for the design |
| --- | --- |
| An agent that read `SKILL.md` and four reference files still missed a rule placed in the middle of a long paragraph, and cited the line it had actually read | A rule sits where the decision is made. A request needs `SKILL.md` and one task page |
| Teaching habits meant for chat were printed on slides ("Paper states", "Derived (my check)", first person) | Slides are a separate skill; the Professor's habits are not loaded when building a deck |
| A deck built with no skill was judged better than the deck built with the skill | Fewer rules; a rule is kept only if it answers an observed failure |
| A rule repeated in several files was updated in some and missed in others; two merge passes did not stop the repetition from returning | Files are organized by task, and a rule is placed by its scope, so it has one place by construction |
| When an example contradicted a rule, the agent followed the example | Examples are linked from the task they illustrate and must agree with it |
| 20 of 80 logs changed slide preferences inside a general teaching reference | Preferences are separated from rules, in "Defaults" sections |

## Four skills, divided by what the agent may add

| Skill | The material belongs to | The reader is | The agent may add |
| --- | --- | --- | --- |
| `econ-learn` | a lecturer or a paper's authors | the user, learning | explanation, derivation and figures, each labeled by source |
| `econ-present` | a paper's authors, or the user | an audience | structure and delivery only |
| `econ-write` | the user | referees and readers | nothing; only clarity |
| `econ-research` | the literature | the user, deciding | verified references and labeled assessment |

A new task goes to the skill whose row it fits. A new skill is justified only by a new row. One is foreseen and not built: work on the user's own research object (solving their model, checking their proof, data and estimation code), where every result must come from an actual derivation or run.

Jobs that cross skills are named in each skill's "Other skills" section, with the order of the handoff (for example a referee report: assess with `econ-learn`, position with `econ-research`, structure with `econ-write`).

## The shape of a skill

```text
skills/<skill>/
  SKILL.md     Mission, Guarantees, Defaults, routing table, Other skills
  tasks/       one page per kind of request the user makes
  guides/      knowledge and how-to that apply only in some cases
  scripts/, templates/, examples/
```

Where a rule goes is decided by its scope:

- **Every request** in the skill: `SKILL.md`. It is the only file always read.
- **One kind of request:** that task page.
- **Only some cases** (a field of economics, a source that is a file, a figure): a guide.
- **Every skill:** `shared/`.

`econ-present` has one task, so its `SKILL.md` is the task page.

In the first comparison run, agents opened two guides beyond the task page in every case, including for a bare term. The routing table therefore states each guide's situation narrowly and says which requests need none.

A task page has the same parts: what the task is, its Defaults, the procedure, and the checks before answering. It links the example that shows a good answer when one exists.

## Guarantees, Defaults and rules

- **Guarantees** never change with the user or the task. Five are common to all skills and written once in [shared/guarantees.md](shared/guarantees.md); each skill then says what they mean for its own material.
- **Defaults** are preferences: adjustable choices such as the reply language, the deck's length, or whether a content file is made. Global ones are written once in [shared/defaults.md](shared/defaults.md); the rest sit in a "Defaults" section at the top of the `SKILL.md` or task page that uses them. The user's instruction in a conversation overrides a default, and the skill tells the user which default a lasting preference replaces. `python tools/list_defaults.py` prints all of them.
- **Rules** are the procedures in the task pages.

Defaults are not kept in a separate file, because a separate file is one more page that may not be read.

## Shared text

A skill must work when installed alone, so it cannot link outside its folder. Text several skills need is written once in `shared/` and copied in by `tools/sync_shared.py`: the two blocks above into every `SKILL.md`, and the file-delivery page and the TeX bundle checker into `econ-learn` and `econ-present`. A test fails when a copy differs. Edit the file in `shared/`, never the copy.

## Invariants carried over from v1

1. The source's assumptions, timing, expectations, notation and version are preserved; lecture text, derivation, outside perspective and independent illustration are told apart.
2. The teaching bottleneck is identified tentatively; length and medium follow the need, not a template.
3. Graphs are a first-class teaching medium; original figures need visual inspection, computed plots need real computation, and there is no figure quota.
4. Homework and exam solutions use the actual question and the closest inspected Slide method, with matching notation and sufficient steps, then name the reusable method.
5. Cross-lecture links need a verified common object and a statement of what differs; instructor order stays separate from conceptual prerequisites.
6. A small question never forces a course index; saved maps never replace the original evidence.
7. Requested files default to a matched `.tex` and compiled `.pdf` in the verified folder named exactly `Agent Outputs/`; private course content never enters this repository.
8. Answers lead with the direct answer and close with the economic meaning; the user's language is used with unchanged symbols.
9. Edits to the user's own text keep every term, symbol, number, citation key and condition; nothing is invented.
10. No reference is written from memory; what was read is stated; a paper's claims are kept apart from assessment.

## Change policy

- A new rule needs a specific observed failure, a new requirement from the user, or a demonstrated missing capability. Prefer changing a Default to adding a rule, and prefer the smallest fix.
- Size is a cost. Before adding to `SKILL.md`, ask whether the text applies to every request; if not, it belongs in a task page or a guide.
- A change to behavior is checked on real material when it is material: the same request run with the new version, the previous version and no skill. A skill that does not beat no skill on a task should lose rules, not gain them.

## Status at adoption

The rebuild moved and regrouped the v1 text; the slide rules were carried over almost word for word. It has passed the structural tests only. It has not been run on a real lecture, draft, topic or deck, and the comparison in the change policy has not been made.
