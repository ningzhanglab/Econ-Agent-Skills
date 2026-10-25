# Instructions for Agents Working in Econ-Agent-Skills

These are repository-maintenance instructions, not the runtime instructions of any particular Skill. Follow them when editing this repository in an environment that reads AGENTS.md.

## Work scope

- Keep each Skill independently usable. The portable entry point is `skills/<skill-name>/SKILL.md`.
- Read the target Skill and its relevant reference files before changing behavior.
- Preserve the core `econ-phd-professor` guarantee: explanations based on a lecture must use the lecture's exact notation and distinguish slide facts from supplementary economics knowledge.
- Preserve the cloud storage convention: source course files belong in the user's authorized cloud drive; any requested generated files must be placed in the verified course workspace's exact `outputs/` folder and verified after writing. Never put private course outputs into this public repository.
- Do not present `econ-research-agent` as implemented until it has actually been created and tested.
- Make focused changes. Do not rewrite unrelated skills or overwrite past logs.

## Required change logging

**For every meaningful repository change**, complete all of these within the same PR/commit series:

1. Update the newest section of [CHANGELOG.md](CHANGELOG.md) with a concise, user-readable description and a link to a detailed log entry.
2. Create a new dated record at `logs/YYYY-MM-DD-short-descriptive-slug.md` based on [logs/TEMPLATE.md](logs/TEMPLATE.md). Never overwrite an older event, even if there are multiple changes on the same day. Use a unique slug for each event.
3. Record **what changed, why it changed, files touched, compatibility/behavioral effect, verification performed, known limitations and next steps**. State whether tests were passed, failed, not run or not applicable, and why.
4. Keep [README.md](README.md) and the skills catalog accurate when capabilities, installation, user workflow or availability change.
5. In the final report to the user, give the commit or PR link and the log link. Commit hashes may be placed in the log **after** the related commit is known, or Git history can serve as the authoritative commit pointer. Do not invent a future commit hash to place in the same commit as its log.

Pure formatting fixes may be grouped into a single short log, but changes to teaching principles, equations, source handling, reference routing, tests, scripts, permissions or installation behavior **must** be recorded explicitly.

### Log quality rules

- Logs are **append-only by event**. Correct factual errors with a clearly marked correction, rather than rewriting the historical narrative.
- A commit tells *what* the exact diff is; a log explains the *intent, decisions, trade-offs and validation evidence*.
- Do not claim an agent read a slide, executed a test, verified a theorem or checked GitHub Actions unless it actually did.
- If a test could not run, write `Not run` and the reason; never present source inspection as an execution test.
- Note user requirements that materially constrain behavior, especially **keep the exact notation from slides**.
- Never store confidential course material, private access tokens or personal information in public logs.

## Suggested workflow

1. Inspect the current `README.md`, `CHANGELOG.md`, existing logs, and target Skill.
2. Identify the scope and acceptance criteria before editing.
3. Implement the smallest coherent change.
4. Run structural checks (`python tests/validate_skills.py`) and relevant examples/tests when tools are available. Record actual outcomes.
5. Add one dated log and update `CHANGELOG.md` in the same change set.
6. Review all touched files and the log, commit changes, and report the links.

For detailed conventions, see [logs/README.md](logs/README.md).
