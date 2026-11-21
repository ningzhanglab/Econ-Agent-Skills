# Link Route Evaluation (manual)

Checks the paste-a-link method in a real chat Project: does each request fetch the one route page it should, and is the answer as good as with installed skills? Run it after a change to `tools/build_link_editions.py` or the README router block.

## Setup

1. Paste the current router block from the README ("All four skills in a Project") into the Project instructions, replacing any older Econ Agent Skills text.
2. Start a **new chat** for each case, so no page is reused from an earlier request.
3. Use your own course files only where a case asks for them. Never copy private course material into this repository; record only what the table asks.

## Cases

| # | Request (paste as written, or attach the file named) | Expected page | Also acceptable |
| --- | --- | --- | --- |
| 1 | 什么是 elasticity？ | `route/term.md` | — |
| 2 | 为什么 Euler equation 里是 $\beta R$ 而不是 $R$？请推导一下。 | `route/explain.md` | — |
| 3 | A homework problem from one of your courses, attached, with "请帮我做这道题，输出 .tex 和 .pdf" | `route/homework.md` | — |
| 4 | A published paper's PDF, attached, with "这篇论文讲了什么？" | `route/paper.md` | — |
| 5 | The same paper, with "给读书会做一个 slides" | `route/slides.md` | — |

## Record for each case

| # | Edition line shown? Code matches the page? | Pages the agent says it fetched | Extra fetches beyond the expected page | Answer quality (1–5) and the main problem, if any |
| --- | --- | --- | --- | --- |
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

To see the current code of a page, open it in a browser: the code is on the third line.

## Reading the result

- **Route works:** each case fetched its expected page and nothing else (case 3 may fetch nothing else either: file delivery is on the homework page).
- **Router misread:** a wrong page was fetched. Reword that row's request text in `ROUTES`, not the skill.
- **Fetch failed or stale:** the page could not be opened, or the code differs from the page. Note the client and time; repeat once later before changing anything.
- **Quality problem:** compare with the same request using the installed skill, if available, before changing a rule. The repository's change policy applies.

Record a completed run as a dated log in `logs/`.
