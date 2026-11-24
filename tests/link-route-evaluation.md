# Link Route Evaluation (manual)

Check route choice, reuse of inspected evidence and the requested output in a real chat Project. Run this after changes to the linked workflow or its setup prompt.

## Setup

1. Paste the one-link prompt from the README ("Start here") into the Project instructions, replacing any older Econ Agent Skills text. To test the longer router block instead, paste that and note which one was used.
2. Start each case in its own chat. Keep the three turns of case 6 or 7 in that case's chat.
3. Use your own course files only where a case asks for them. Never copy private course material into this repository; record only what the table asks.

## Cases

| # | Request (paste as written, or attach the file named) | Expected page | Also acceptable |
| --- | --- | --- | --- |
| 1 | 什么是 elasticity？ | `route/term.md` | — |
| 2 | 为什么 Euler equation 里是 $\beta R$ 而不是 $R$？请推导一下。 | `route/explain.md` | — |
| 3 | A homework problem from one of your courses, attached, with "请帮我做这道题，输出 .tex 和 .pdf" | `route/homework.md` | Open the relevant source and one matching English or Chinese TeX template when needed. Verify the `.tex`, fresh PDF and any required dependencies. |
| 4 | A published paper's PDF, attached, with "这篇论文讲了什么？" | `route/paper.md` | — |
| 5 | The same paper, with "给读书会做一个 slides" | `route/slides.md` | — |
| 6 | **One chat, three messages in a row:** "什么是 moral hazard？", then a homework problem attached with "请帮我做这道题", then "把上面的解答改得更简洁" | `route/term.md`, then `route/homework.md`, then `route/writing.md` | The third may reuse `homework.md` if it treats the request as part of the solution |
| 7 | **One chat, three messages in a row:** using the [July 2023 Bai working paper](https://www.povertyactionlab.org/sites/default/files/research-paper/WP2645_Melons-as-Lemons_Bai_July2023_0.pdf), explain the signaling-cost lower bound in Proposition 1, then explain only its denominator, then show the same bound as one Beamer frame in chat | `route/paper.md`, same page and source, then `route/slides.md` | Reopen the exact source if the original passage is unavailable or the version changes |

## Record for each case

| # | Route and edition per turn | Necessary reads and why | Avoidable or repeated reads | Answer quality (1–5) | Requested files verified |
| --- | --- | --- | --- | --- | --- |
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |
| 7 | | | | | |

Each reply that follows a page starts with `Skill: <page> · <code>`. Check the code against line 3 of the route page. Record tool activity when visible and distinguish it from the agent's account of what it opened. Mark unavailable traces as unobserved.

## Reading the result

- **Route works.** The turn uses its expected page or an allowed alternative. Necessary source reads and requested templates are consistent with a pass. Check response accuracy and file completion separately.
- **Avoidable read.** An unrelated guide, a second language template or another open of still-available evidence without a version change or new question requiring it. Count these separately from an incorrect route.
- **Router misread:** a wrong page was fetched. Reword that row's request text in `ROUTES`, not the skill.
- **Fetch failed or stale:** the page could not be opened, or the code differs from the page. Note the client and time; repeat once later before changing anything.
- **Quality problem:** compare with the same request using the installed skill, if available, before changing a rule. The repository's change policy applies.

For case 7, record which source pages were inspected at each step, any repeated source reads, and whether the two explanations and the frame preserve the source's notation and assumptions. Compare the current and previous routes with the same task without a skill.

Record a completed run as a dated log in `logs/`.
