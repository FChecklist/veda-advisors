# Veda Advisors — AI Governance Baseline

> Version 1.0.0 | Added 2026-07-11 | Owner: raajat.agarwal@gmail.com

## What this document is

This is the single governance document for AI-assisted work on this repo. It
replaces the need to write three separate constitutional documents (as was
done in the sibling repo `FChecklist/compliance-tracker`) because Veda
Advisors is a materially smaller, single-tenant marketing/lead-generation
site with no AI-facing product feature — there is no business-purpose/privacy
surface, no multi-tenant platform-architecture surface, and no task-governance
engine to write a constitution *about* beyond the lightweight `ai-os/` scaffold
already in this repo. If this product later grows AI features or multi-agent
orchestration comparable to compliance-tracker's VERIDIAN AI OS, split this
into more documents at that point — don't pre-build structure for capabilities
that don't exist yet.

For the fuller three-document framework this is deliberately *not* copying,
see `compliance-tracker`'s `VERIDIAN_AI_CONSTITUTION.md`,
`MASTER_AI_OS_ARCHITECTURE.md`, and `VERIDIAN_TASK_GOVERNANCE_CONSTITUTION.md`.
That framework exists because that product is a multi-tenant AI platform with
LLM calls in production, a 51-role AI Dev Team roster, and a Policy
Enforcement Engine. None of that applies here today.

## What this product actually is

Verified by reading the code on 2026-07-11, not assumed from prior notes:

- **Product**: Veda Advisors — an education/advisory marketing and
  lead-generation website (Rajat Agarwal's advisory business). Sections:
  Home, Founders program, Students program, India program, "Stage 0" lead
  capture funnel.
- **Stack**: Next.js 16 (App Router) + TypeScript + Tailwind, `bun` as package
  manager, deployed on Vercel. Route surface is small:
  `src/app/{page,layout,sitemap}.tsx` plus `founders/`, `students/`, `india/`,
  `stage0/` subpages, and two API routes (`src/app/api/route.ts` — a hello-world
  stub; `src/app/api/veda/route.ts` — serves a static generated demo HTML file
  from `VedaAdvisors_Demo/index.html`).
- **Data**: Supabase Postgres is the real backing store for the Stage 0 lead
  form (per commit `b900f79`, "Stage0 form->Supabase"). `prisma/schema.prisma`
  exists in the repo but targets `sqlite` with generic `User`/`Post` models
  unrelated to the actual product — it appears to be unused template
  boilerplate, not the live data layer. Worth the owner's confirmation; not
  fixed here since it's outside this task's scope.
- **`.env` is currently tracked in git** (`git ls-files` shows `.env` present
  despite being gitignored now). Two PRs are already open addressing this
  (`fix/untrack-env` #14, `security/untrack-env-file` #13) — a real,
  already-flagged issue, not something this document needed to (re)discover
  or fix.

## AI-facing surface: there isn't one

Searched `src/` for any LLM/AI SDK usage (`z-ai-web-dev-sdk` is a
`package.json` dependency, `openai`, `anthropic`, `generateText`,
`chat.completions`, etc.) — **zero matches**. No route, component, or lib file
in this product calls an LLM API. The only AI-adjacent things in this
repository are the meta-tooling that *builds* the site
(`ai-os/`, `SENTINEL.md`, `AGENTS.md`, the `zai-task`/`claude-task`
`repository_dispatch` triggers in `.github/workflows/ai-dispatch.yml`) — i.e.
AI agents write code here, but the shipped product does not call AI at
runtime.

**Business-purpose / privacy rule for AI usage in this repo: [NOT APPLICABLE].**
There is no AI feature to write a usage policy for. If one is added later
(e.g. an AI advisor-matching feature, a chatbot, AI-generated content), this
section must be filled in before that feature ships — at minimum: what data
it can see, what it's allowed to say, and how errors/hallucinations are
handled. Do not add an AI feature to this product without updating this
section first.

## Task / lifecycle discipline

This repo already has an `ai-os/` scaffold (`ai-os/OS.yaml`,
`ai-os/LIFECYCLE.yaml`, `ai-os/boss/{BOSS,BOARD,ROSTER,COMPLETED}.yaml`,
`ai-os/sentinel/{SENTINEL,VIOLATIONS,HEALTH}.yaml`, `ai-os/registry/ARTIFACTS.yaml`,
`ai-os/specs/modules/*.yaml`) installed 2026-06-26–06-28. It defines an
11-stage lifecycle (UNDERSTAND → RESEARCH → DESIGN → VALIDATE → IMPLEMENT →
TEST → REVIEW → DEPLOY → MONITOR → LEARN → IMPROVE) and a project BOSS
(`VEDAADVISORBOSS`). This was reviewed for this pass and left as-is — it's
still roughly accurate as a description of the intended process for a site
this size, and rewriting it wholesale was not warranted. Two things about it
are worth knowing rather than fixing right now:

- `ai-os/boss/ROSTER.yaml` → `registered_agents: []`. The lifecycle mandates
  agents register there before working; nobody ever has. The lifecycle is
  aspirational, not currently followed.
- `ai-os/boss/BOARD.yaml` has at least one stale entry (`T-NEXT-001`, "merge
  PR #7 into main", marked `open`) for a PR that already merged on 2026-06-28
  per git history (`7c35bb8`). The board is not being kept current.

Neither of these blocks anything — they're just evidence that the heavier
process described in `LIFECYCLE.yaml` isn't actually being run per-task. For
a site this size, the practical minimum going forward is:

1. Work on a branch, open a PR against `main` (branch protection requires
   this — see `AGENTS.md` Operating Rule 1).
2. Get it reviewed — currently the only real enforcement is 1 GitHub-side
   approving review; there is no dedicated human reviewer or second-agent
   auditor process established for this repo (unlike compliance-tracker's
   doer/auditor rule, which exists because two full-access agents there
   collided on `main` once — nothing analogous has happened here, so that
   heavier rule isn't ported).
3. Once CI is actually wired to fail on real errors and required as a status
   check (see `AGENTS.md` Operating Rule 2 — not true today), treat CI green
   as part of the merge bar too.

If task volume or agent count on this repo grows to where BOARD.yaml/ROSTER.yaml
staleness becomes a real problem (duplicate work, agents colliding), look at
`compliance-tracker`'s `VERIDIAN_TASK_GOVERNANCE_CONSTITUTION.md` for the
fuller pattern (task-tightening validation, guardrail-presence CI check,
doer+auditor logging in `COMPLETED.yaml`) before inventing something new here.

## Guardrail honesty ledger

Status tags used throughout this repo's governance docs going forward:
`[ENFORCED]` (a real, verifiable mechanism blocks the bad outcome — cite what
it is), `[PARTIALLY ENFORCED]` (something real exists but doesn't cover the
full claim), `[NOT ENFORCED]` (written down as a rule, nothing mechanically
checks it), `[NOT APPLICABLE]` (there is nothing here for the rule to apply
to yet). As of 2026-07-11:

| Claim | Status | Evidence |
|---|---|---|
| PR required to merge to `main` | **ENFORCED** | GitHub branch protection API: `required_pull_request_reviews.required_approving_review_count: 1`, `enforce_admins: true` |
| No force-push / no branch deletion on `main` | **ENFORCED** | Same API response: `allow_force_pushes: false`, `allow_deletions: false` |
| CI must pass before merge | **NOT ENFORCED** | `required_status_checks.contexts` is empty; also most `ci.yml` steps swallow failures via `\|\| echo "::warning"` |
| Secrets never committed to source | **PARTIALLY ENFORCED** | `sentinel.yml` runs gitleaks + a grep-based pattern check on every PR, `continue-on-error: true` on the gitleaks step; and `.env` is *already* tracked in git history from before this was added (open PRs #13/#14 address it) |
| Agents register before working | **NOT ENFORCED** | `ai-os/boss/ROSTER.yaml` has always been empty |
| AI usage has a documented business-purpose/privacy policy | **NOT APPLICABLE** | No AI-facing feature exists in the product |
| Guardrails can't be weakened without owner sign-off | **NOT ENFORCED (newly documented, not mechanically checked)** | New rule added in `AGENTS.md` Operating Rule 6 this pass; nothing in CI verifies it (compliance-tracker's analogous rule has a CI script, `check-guardrail-presence.mjs` — porting that machinery here isn't warranted yet for a repo this size, but the rule is written down as a norm) |

Keep this table current. When a claim's status changes (e.g. required status
checks get configured), update the evidence column with how you verified it —
don't just flip the tag.
