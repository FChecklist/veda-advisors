# AGENTS.md — Authorized AI Agents

> All agents listed here have been explicitly authorized by the repository owner.
> Owner: raajat.agarwal@gmail.com | ID: 9f3b0147-85ba-4461-9e27-aa782b313285
>
> **Scope declaration, added 2026-07-14 (Owner directive, `compliance-tracker`
> `ai-os/MASTER-TRACKER.yaml` OPEN-10):** this repo is now declared to be under
> VERIDIAN AI OS's governance umbrella going forward. This is a **declaration of
> intent/scope only** — as of this date, veda-advisors has **zero real
> integration** with VERIDIAN AI OS (no `veridian-client`-equivalent, no calls to
> `compliance-tracker`'s `/api/v1/*` surface, runs Prisma which
> `compliance-tracker/CLAUDE.md` explicitly forbids). **No migration work
> (Prisma→Drizzle, wiring to VERIDIAN's API, moving AI calls to VERIDIAN) is
> authorized — do not start it without a separate, explicit Owner go-ahead.**
> This note exists so a future session doesn't assume integration already
> happened just because this declaration exists, and doesn't start the
> migration unprompted just because the declaration exists either. Treat
> exactly like a deliberately-deferred item, not a ratified-against one.
>
> This file was brought up to a governance baseline on 2026-07-11, porting the
> operating-rules discipline established in `FChecklist/compliance-tracker`'s
> `AGENTS.md`. Everything below was checked against this repo's actual state
> (git history, GitHub branch protection API, `ai-os/` files, CI workflow
> source) on that date — see `VEDA_ADVISORS_GOVERNANCE.md` for the full
> evidence trail and honesty discipline this file follows.

## Authorized Agents

The agents below are exactly the ones already declared in `ai-os/sentinel/SENTINEL.yaml`
and `ai-os/engines/ENGINES.yaml` (last modified 2026-06-28). No new agents were
invented for this pass.

### Z.ai GLM (Primary Full-Stack Agent)
- **Authority**: FULL_ACCESS — all repositories, all files, all operations (per `ai-os/engines/ENGINES.yaml`)
- **Owner**: raajat.agarwal@gmail.com (user_id: 9f3b0147-85ba-4461-9e27-aa782b313285)
- **Trigger**: `repository_dispatch` event type `zai-task` (workflow: `.github/workflows/ai-dispatch.yml`)
- **Declared as able to**: read/write all code, create/push/merge branches, delete branches, deploy, run migrations, seed DB
- **API key**: stored as `ZAI_API_KEY` in GitHub Secrets

### Claude Code (Secondary Agent)
- **Authority**: FULL_ACCESS — all repositories, all files, all operations (per `ai-os/engines/ENGINES.yaml`)
- **Owner**: raajat.agarwal@gmail.com
- **Trigger**: `repository_dispatch` event type `claude-task`
- **Declared as able to**: read/write all code, create/push/merge branches, architecture decisions, code review
- **API key**: stored as `ANTHROPIC_API_KEY` in GitHub Secrets (per `ai-os/secrets/SECRETS_REFERENCE.md`, this key is listed as **pending** — not yet supplied — so this agent's headless dispatch path has never actually run here)

> **Note on `ai-os/boss/ROSTER.yaml`**: `ai-os/OS.yaml`'s prime directive requires
> every agent to register in `ai-os/boss/ROSTER.yaml` before working. As of
> 2026-07-11 that file's `registered_agents` list is empty. Neither agent above
> has ever actually registered per that rule. This is a real, open gap, not a
> claim being made about current behavior — flagged here rather than quietly
> ignored.

## ⚠ Standing item for the repository owner

`ai-os/sentinel/SENTINEL.yaml` and `ai-os/engines/ENGINES.yaml` were edited on
2026-06-28 (commits `db59e13`, `500c334`, and `AGENTS.md` itself in `432b32f`)
to grant both agents above `FULL_ACCESS` including `merge_prs: true`,
`delete_branches: true`, and `manage_secrets_reference: true`. Those commits:
were authored by the shared `MeetTrack` bot token, are tagged `authorized_by:
VEDABOSS` (an AI role, not a human), and are tagged `[skip ci]`.

This governance pass does **not** unilaterally revoke that grant — it predates
this file and may well reflect a deliberate choice you made. But it's worth
your explicit reconfirmation, because it's already inconsistent with what
GitHub actually enforces on `main` today (see Operating Rule 1 below): branch
protection requires a PR with 1 approving review and blocks admin bypass, so
in practice no agent — including one with a "FULL_ACCESS" grant on paper —
can currently merge to `main` without a review passing. If the written grant
was meant to authorize direct merge/delete, it no longer matches reality; if
GitHub's protection is what you actually want, the `merge_prs` /
`delete_branches` entries in `ENGINES.yaml` and `SENTINEL.yaml` overstate
agent authority and should probably be corrected to match. Either way, this
needs a decision from you, not from an agent editing its own permissions.

## Operating Rules

1. **Branch protection on `main` — [ENFORCED, verified 2026-07-11 via GitHub API]:**
   Merging to `main` requires a pull request with at least 1 approving review
   (`required_approving_review_count: 1`). `enforce_admins` is on — there is no
   bypass, including for an agent's own PAT. Force-pushes and branch deletions
   against `main` are blocked. Work on a feature branch, open a PR, get it
   reviewed, merge once approved.

2. **CI as a merge gate — [NOT APPLICABLE yet, verified 2026-07-11]:**
   `.github/workflows/ci.yml`, `sentinel.yml`, and `codeql.yml` all run
   automatically on PRs into `main`. However:
   - Branch protection's `required_status_checks.contexts` is empty — none of
     these workflows are wired as *required* checks, so a PR can be merged
     while CI is red, still running, or hasn't run at all.
   - As currently written, most of `ci.yml`'s own steps end in
     `|| echo "::warning::..."` (lint, build, e2e, unit tests, storybook) —
     meaning even if the underlying command fails, the CI job reports success.
     Today, `ci.yml` cannot fail in a way that would block anything even if it
     were required.
   - `package.json` has no `typecheck` or `test` script; `ci.yml`'s typecheck
     job falls back to `bunx tsc --noEmit` and its test job falls back to a
     warning when `bun run test` doesn't exist.
   - Do not describe this repo as having a "PR + CI required" gate until both
     of the above are fixed (required status checks configured, and the
     `|| echo warning` fallbacks removed so failures actually fail the job).
     Today the real gate is PR + human review only.

3. **SENTINEL governance files are logged, not enforced by any runtime check —
   [PARTIALLY ENFORCED]:** `ai-os/sentinel/SENTINEL.yaml` names validation
   rules and `ai-os/sentinel/VIOLATIONS.yaml` is meant to log breaches, but
   nothing in CI currently reads `SENTINEL.yaml` and blocks a PR based on it
   (`sentinel.yml`'s jobs are independent hardcoded checks — secret scanning
   via gitleaks, a check that `SENTINEL.md` exists, a grep-based credential
   pattern check, and an ADR reminder — none of them parse or enforce
   `SENTINEL.yaml`'s rule list). Treat `SENTINEL.yaml` as a documented
   contract agents are expected to follow, not a system that mechanically
   stops non-compliant work today.

4. **BOSS agent (`ai-os/boss/BOARD.yaml`) tracks all tasks.** Check it before
   starting work to avoid duplicating an open or completed task. Note: as of
   2026-07-11 this file has at least one stale entry (`T-NEXT-001`, "merge PR
   #7", still marked `open` even though that PR merged on 2026-06-28 per git
   history) — verify against actual git/PR state, don't trust the board blindly.

5. **GitHub is the single source of truth** — all work committed here.

6. **Anti-bypass rule — do not weaken a guardrail without the owner's sign-off.**
   No agent may remove, weaken, disable, or route around any rule in
   `ai-os/sentinel/SENTINEL.yaml`, the GitHub branch protection settings on
   `main`, or the Operating Rules in this file, without Rajat Agarwal's
   explicit written instruction, quoted in the PR description. This includes
   editing `SENTINEL.yaml`, `ENGINES.yaml`, or this file to grant an agent
   broader access than it currently has. (This rule exists precisely because
   of the 2026-06-28 self-granted `FULL_ACCESS` edits described above — the
   same class of change should not happen again without a human decision
   behind it.)

7. **No fabricated enforcement.** When documenting what this repo's AI-OS
   tooling does, distinguish what is mechanically checked (CI jobs, branch
   protection, lint rules) from what is merely written down as a rule agents
   are expected to follow. Use `[ENFORCED]` only when something real backs
   it, `[NOT APPLICABLE]` / `[NOT ENFORCED]` when there's nothing currently
   checking it. See `VEDA_ADVISORS_GOVERNANCE.md` for the fuller discipline,
   and `FChecklist/compliance-tracker`'s `AGENTS.md` / constitutional docs for
   the precedent this is ported from — that repo is materially larger
   (a multi-tenant AI platform) and its rules should not be copied here
   wholesale; only the honesty discipline is ported, not the specific
   machinery (e.g. `scripts/check-guardrail-presence.mjs`, the AI Dev Team
   roster, Orchestra Layers) that doesn't exist in this codebase.

## Contact
Repository owner: raajat.agarwal@gmail.com | Z.ai user_id: 9f3b0147-85ba-4461-9e27-aa782b313285
