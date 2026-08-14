# AGENTS.md — Authorized AI Agents

> All agents listed here have been explicitly authorized by the repository owner.
> Owner: raajat.agarwal@gmail.com | ID: 9f3b0147-85ba-4461-9e27-aa782b313285

## Authorized Agents

### Z.ai GLM (Primary Full-Stack Agent)
- **Authority**: FULL_ACCESS — all repositories, all files, all operations
- **Owner**: raajat.agarwal@gmail.com (user_id: 9f3b0147-85ba-4461-9e27-aa782b313285)
- **Trigger**: `repository_dispatch` event type `zai-task`
- **Can**: read/write all code, create/push/merge branches, delete branches, deploy, run migrations, seed DB
- **API key**: stored as `ZAI_API_KEY` in GitHub Secrets

### Claude Code (Secondary Agent)
- **Authority**: FULL_ACCESS — all repositories, all files, all operations
- **Owner**: raajat.agarwal@gmail.com
- **Trigger**: `repository_dispatch` event type `claude-task`
- **Can**: read/write all code, create/push/merge branches, architecture decisions, code review
- **API key**: stored as `ANTHROPIC_API_KEY` in GitHub Secrets

## Operating Rules
1. Zero human coding — all changes made by AI agents only
2. All changes logged through SENTINEL (ai-os/sentinel/)
3. BOSS agent (ai-os/boss/BOARD.yaml) tracks all tasks
4. Both agents have identical repo-level permissions via PAT_FCHECKLIST
5. GitHub is the single source of truth — all work committed here

## Search-Reuse Discipline

**Added 2026-08-14 (Owner-approved, addendum to P1 UMR-20260806-171945-5767; citation:
`OWNER_DECISIONS_NEEDED_2026-07-23.yaml` entry `id=crontab-drift-approved-2026-08-14`,
`status=approved`).** Real indexes already exist and are already used by the deterministic
dedup reviewer for dispatch-level decisions:

- `system_index` (`/opt/veridian/ai-os/memory/superboss-register.sqlite#system_index`)
- `capability_registry` (`/opt/veridian/ai-os/memory/superboss-register.sqlite#capability_registry`)
- `wiring_registry` (`/opt/veridian/ai-os/memory/superboss-register.sqlite#wiring_registry`)
- `CLAUDE_MEMORY_INDEX.md` (`/opt/veridian/ai-os/memory/CLAUDE_MEMORY_INDEX.md`)
- `dead_ends.json` (`/opt/veridian/ai-os/memory/dead_ends.json`)
- `open_questions.json` (`/opt/veridian/ai-os/memory/open_questions.json`)

A cross-repo audit on 2026-08-14 found zero instances of any "check the index first"
instruction in any real `AGENTS.md` under `/opt/veridian/repos` or `/opt/veridian/workspace`
— different worker tasks were repeatedly re-discovering the same real facts via fresh
`grep`/`find`, wasting real tokens. This section closes that gap. It does not assume zoekt
or any other code-search service is running — no zoekt systemd unit exists as of this
writing; verify what's actually available before relying on it, don't assume.

Every worker (human or AI agent) doing exploratory or fact-finding search must:

1. **Check the real indexes above first.** Before running a broad exploratory
   `grep`/`find`/repo-wide search, check whether the fact you need is already answered by
   one of the six indexes above. Cite what you checked (which index, what query) in your
   PR description or progress log — even if the check came up empty.
2. **Search fresh only for what those don't already answer.** Once you've checked and
   confirmed the fact isn't already recorded, do the fresh grep/find/broad search you
   actually need. Checking the index first is not a reason to skip real verification of
   current state — it's a reason not to duplicate a search someone already did.
3. **Write back genuinely new, reusable facts.** If your fresh search turns up a real fact
   worth another worker not having to rediscover, write it back to the appropriate index
   (`capability_registry`/`wiring_registry` via `superboss-register.py`, `CLAUDE_MEMORY_INDEX.md`,
   `dead_ends.json`, `open_questions.json`) so the next worker finds it in step 1 instead of
   re-deriving it from scratch.
4. **This does not relax any other requirement.** Search-reuse discipline is additive, not a
   substitute for any existing audit, test, or completion requirement in this file — a cited
   index lookup is never a stand-in for real verification of actual current state before you
   rely on it, and never a reason to skip an audit or test this file otherwise requires.

## Contact
Repository owner: raajat.agarwal@gmail.com | Z.ai user_id: 9f3b0147-85ba-4461-9e27-aa782b313285