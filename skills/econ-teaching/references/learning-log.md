# Learning Logs — Optional Private Study Session Summaries

**Purpose:** support continuity across teaching conversations **without** logging every question, writing full chat transcripts or confusing student learning notes with the Skill repository's development logs.

## Consent and activation

- **Default is ON-DEMAND, not continuous.** The student can say "记录今天的学习", "save a learning log", "summarize this session in my course log", or explicitly request the equivalent. Creating a reusable log template is **not** permission to automatically archive future conversations.
- If they explicitly opt in to an ongoing end-of-session recap convention, follow that preference **only in sessions where a suitable trigger or user-requested save is actually available**. A plain Skill markdown file does not install an event listener, monitor future chats, save after closing a session or schedule background work.
- Do **not** treat routine math questions as implicit consent to persist private notes. A normal in-chat summary is not a cloud write unless specifically requested or covered by a clearly established logging preference.
- Avoid copying sensitive personal details, chat transcripts, uploaded answer keys, passwords or confidential data into logs. Record course-specific learning concepts and links only as needed.

## Where this log lives

- **Public repository:** [learning-log.md template](../templates/learning-log.md) and this behavior reference only; GitHub `logs/` remains the **development changelog**, not a student's learning diary.
- **Private active course folder:** `<verified course>/Agent Outputs/Learning Logs/` (exact spelling). For example, an authorized course folder may contain `Learning Logs/2026-10-24.md`. No logs are copied to another course or a public repo.
- These are specifically requested **Markdown log files**, so they use `.md` rather than the generic on-request teaching-document default `.tex + .pdf`. A user-requested PDF/TeX version is an additional explicit export choice.
- Identify course identity by verified folder/source metadata, not the latest mentioned school or a name guess. If not known and no accurate destination is possible, ask one focused question or provide the in-chat summary without falsely claiming a save.

## What to record

Only summarize **information present in the current accessible session, verified original lecture/Homework sources, or the student's explicit report**. Include useful source locators when known.

1. **Date, course, session/topic and logging trigger**, with timezone if grounded.
2. **Studied:** specific lecture/model/method actually discussed. Do not turn possible future topics into topics already studied.
3. **Key questions:** what the student asked, paraphrased concisely rather than a verbatim transcript.
4. **Clarifications:** important reasoning or derivations that were actually established. Keep exact lecture notation, assumptions and source-vs-extension distinctions.
5. **Lecture/Homework connections:** only when actual sources or user statements support them. Mark provisional or unverified links.
6. **Open questions / next session:** unresolved steps or productive next topics. Suggestions are recommendations, not memories of completed learning.
7. **Understanding status:** `discussed`, `student-confirmed`, or `not verified` when it matters. **Never infer mastery merely because an explanation was delivered.**

Do not invent study duration, quiz results, grades, exact slide numbers, student progress or understanding state.

## Update an existing date without losing prior entries

- List the **exact course Learning Logs folder** first and check whether the chosen date filename exists.
- When it exists, **read its current contents**, preserve earlier entries unchanged, and append a separately identified session section. Prefer a native provider content update that keeps the same file ID and existing content, if the connector supports this with authorized file bytes.
- If safe append-in-place is unavailable or a concurrent revision cannot be reconciled, **do not overwrite**. Write a unique dated session filename (for example, `2026-10-24-session-02.md`) and say that it is a separate file rather than a merge.
- If a date cannot be established reliably, use a clearly labeled undated session identifier or ask for the requested date. Do not fake an exact clock time.
- Check the resulting cloud file ID, name and parent folder via metadata/listing. Only then tell the student the log was saved. On failure, give the draft in chat and report the failure.

## Use in a later teaching session

On an explicit request to resume learning, read the **relevant accessible log** to find prior questions, source locators and open issues. A Learning Log is a **study checkpoint**, not an authoritative copy of Slides, an eternal memory, or proof that the student mastered a concept. Reopen original Slides and problem statements before making detailed mathematical claims, and correct stale/conflicting log content transparently.

**Effort:** one short, useful recap is enough. Do not rerun Handbook generation, create a second syllabus index, or run a test suite just because a log entry was requested.
