# VEDABOSS — Master Task Backlog

> Single source of truth for the VEDABOSS / WORKER workflow.
> WORKER reads this file at the start of every cycle, picks the next `pending` task,
> executes it, commits with a clear message, then marks it `done` here and appends
> a section to `worklog.md`. VEDABOSS then assigns the next task.

## Project Context
- **Repo**: `FChecklist/veda-advisors` (Next.js 16 + Prisma + Supabase)
- **Live site**: https://veda-advisors.vercel.app
- **Client**: Rajat Sir (Rajat Rajkamal Agarwal) — Startup Fundraising Advisor
- **Worker must**: keep each task atomic (one commit per task), keep Supabase Stage 0
  form working (live users), keep `npm run build` passing, never break the main branch.

## Status Legend
- `pending` — not started
- `in_progress` — worker is currently executing
- `done` — committed locally AND pushed to GitHub
- `blocked` — worker cannot proceed; needs VEDABOSS decision

## Backlog

| ID | Task | Status | Commit |
|----|------|--------|--------|
| T1 | ~~Fix CI workflow YAML typo~~ — closed as `not_needed` (YAML was always valid; `[m` was eaten by terminal as ANSI escape) | not_needed | — |
| T2 | Add `typecheck` script to package.json (`tsc --noEmit`) | done | c9d619a |
| T3 | Add `test` and `test:e2e` placeholder scripts to package.json | done | 98c513a |
| T4 | Remove always-warning storybook + e2e jobs from CI workflow | done | 73c921e |
| T5 | Replace `/api/route.ts` Hello World with structured health-check JSON | done | 42f82ec |
| T6 | Create `src/app/not-found.tsx` (Veda-branded 404 page) | done | 94db565 |
| T7 | Create `src/app/loading.tsx` (Veda-branded loading state) | done | 17027c5 |
| T8 | Create `.env.example` documenting required env vars | done | 843982b |
| T9 | Create `README.md` with setup/run/deploy instructions | done | a58e9be |
| T10 | Add JSON-LD structured data (Person schema for Rajat Sir) to `layout.tsx` | done | 9dbcdd0 |
| T11 | Add `public/manifest.json` for PWA basics | done | 323891c |
| T12 | Add `Stage0Submission` model to Prisma schema (Supabase path stays primary) | done | 7250b10 |
| T13 | Create `src/lib/stage0.ts` server-side helper (Prisma-based, optional) | done | 225d30b |
| T14 | Add POST handler at `src/app/api/stage0/route.ts` (server-side fallback) | done | e0dba64 |
| T15 | Run `prisma generate` + `prisma db push` locally to verify schema | done | (no artifact) |
| T16 | Push all commits to GitHub `main` branch | pending | — |
| T17 | Update VEDABOSS.md with final summary, mark project complete | pending | — |

## Rules for WORKER
1. ONE task at a time. No multitasking.
2. After finishing a task:
   - `git add` the changed files
   - `git commit -m "<commit msg>"`
   - Update this file: mark task `done`, fill the Commit column with the short hash
   - Append a `---`-delimited section to `worklog.md` (see worklog format)
   - Report back to VEDABOSS
3. If a task would break prod, mark `blocked` with a one-line reason and stop.
4. VEDABOSS decides what the next task is — worker does not skip ahead.
5. Final task: push everything to GitHub with `git push origin main`.

## Progress Log (most recent on top)
(none yet)
