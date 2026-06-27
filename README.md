# Veda Advisors

Production website for **Rajat Rajkamal Agarwal** (Rajat Sir) — Startup Fundraising Advisor.
Live at **https://veda-advisors.vercel.app**.

The site markets Rajat Sir's BSCVI 3.0 advisory system, routes qualified founders
to a free Stage 0 assessment, and rejects (gracefully) everyone who isn't a fit.

---

## Tech Stack

| Layer | Choice |
|-------|--------|
| Framework | Next.js 16 (App Router, React 19) |
| Language | TypeScript 5 |
| Styling | Tailwind CSS 4 + inline styles on landing pages |
| UI primitives | shadcn/ui (Radix UI) |
| ORM | Prisma 6 (SQLite locally, swappable to Postgres in prod) |
| Form backend | Supabase (Stage 0 submissions) — Prisma mirror optional |
| Auth | next-auth installed, not yet wired up |
| Hosting | Vercel (`bom1` region — Mumbai) |
| Package manager | bun (lockfile committed) — npm also works |

---

## Project Layout

```
veda-advisors/
├── src/
│   ├── app/
│   │   ├── page.tsx              # Home (iframe-loads VedaAdvisors_Demo/index.html)
│   │   ├── layout.tsx            # Root layout, SEO metadata
│   │   ├── loading.tsx           # Brand loading state
│   │   ├── not-found.tsx         # Brand 404 page
│   │   ├── sitemap.ts            # Dynamic sitemap
│   │   ├── india/page.tsx        # /india landing page
│   │   ├── founders/page.tsx     # /founders landing page
│   │   ├── students/page.tsx     # /students landing page
│   │   ├── stage0/page.tsx       # /stage0 — 7-question assessment form
│   │   └── api/
│   │       ├── route.ts          # GET /api — health check
│   │       └── veda/route.ts     # GET /api/veda — serves demo HTML
│   ├── lib/
│   │   ├── db.ts                 # Prisma singleton
│   │   └── utils.ts              # cn() helper
│   ├── components/ui/            # shadcn/ui components
│   └── hooks/                    # use-toast, use-mobile
├── prisma/schema.prisma          # DB schema
├── public/
│   ├── images/                   # All client logos + Rajat photos
│   ├── demo.html                 # Copy of merged VedaAdvisors_Demo/index.html
│   ├── veda-demo.html            # Same, kept for legacy links
│   ├── logo.svg
│   └── robots.txt
├── VedaAdvisors_Demo/            # Source for the home-page iframe (HTML/CSS/JS demo)
│   ├── index.html                # Final merged file (~120 KB)
│   ├── merge_all.py              # Script that merges 12 fragments → index.html
│   ├── modules/                  # 12 Python modules that generate HTML fragments
│   ├── fragments/                # 12 generated HTML fragments
│   └── images/                   # Same images as public/images
├── .github/workflows/            # ci.yml, codeql.yml
├── package.json
├── next.config.ts
├── tailwind.config.ts
├── vercel.json                   # Vercel build config (npm install, bom1 region)
├── VEDABOSS.md                   # Master task backlog (boss/worker workflow)
└── worklog.md                    # Append-only multi-agent work log
```

---

## Getting Started (Local)

### Prerequisites
- Node.js 20+ (or Bun 1.3+)
- Python 3.10+ (only if you want to regenerate `VedaAdvisors_Demo/index.html`)

### Install & Run

```bash
# 1. Clone
git clone https://github.com/FChecklist/veda-advisors.git
cd veda-advisors

# 2. Install dependencies (either works)
bun install                 # faster, uses bun.lock
# or
npm install --include=dev   # matches vercel.json's installCommand

# 3. Configure env
cp .env.example .env
# Edit .env — at minimum set DATABASE_URL (file:./db/custom.db works locally)

# 4. Set up the database
bun run db:generate         # generates the Prisma client
bun run db:push             # creates the SQLite file + tables

# 5. Run the dev server
bun run dev                 # http://localhost:3000
```

Open **http://localhost:3000** — the home page iframes the merged demo HTML.

---

## Available Scripts

| Script | What it does |
|--------|-------------|
| `dev` | Start Next.js dev server on port 3000, tee output to `dev.log` |
| `build` | Production build |
| `start` | Run the production build (after `build`) |
| `lint` | ESLint |
| `typecheck` | `tsc --noEmit` (no emit, type-check only) |
| `test` | Placeholder — exits 0 (no tests yet) |
| `test:e2e` | Placeholder — exits 0 (no Playwright tests yet) |
| `db:generate` | `prisma generate` — regenerate the Prisma client after schema changes |
| `db:push` | `prisma db push` — push schema to the database (no migration history) |
| `db:migrate` | `prisma migrate dev` — create + apply a migration |
| `db:reset` | `prisma migrate reset` — drop & recreate the database |

---

## Deploying to Vercel

The project is already configured for Vercel:
- `vercel.json` sets `installCommand: npm install --include=dev` and `regions: ["bom1"]` (Mumbai).
- The production deployment is at **https://veda-advisors.vercel.app**.
- Builds are triggered automatically on every push to `main`.

### Required Vercel environment variables
Set these in **Project Settings → Environment Variables** (Production + Preview):

- `DATABASE_URL` — a real Postgres URL (e.g. Vercel Postgres or Supabase Postgres)
- (Optional) `STARTED_AT` — ISO timestamp, surfaced in `/api` health check

CI also expects `NEXTAUTH_SECRET` and `NEXTAUTH_URL` for the build step, but
they're not yet used by the app — see `.env.example` for details.

---

## The VedaAdvisors_Demo Subproject

The home page iframes a self-contained HTML site under `VedaAdvisors_Demo/`.
That site is generated by 12 Python modules → 12 HTML fragments → 1 merged
`index.html`. To regenerate after editing a module:

```bash
cd VedaAdvisors_Demo
python3 merge_all.py        # writes a new index.html
# Then copy to public/ for the iframe to pick up:
cp index.html ../public/demo.html
```

The design system (colours, fonts, spacing) is documented in `worklog.md`.

---

## CI / CD

- **`.github/workflows/ci.yml`** — lint, typecheck, unit-tests, build, deploy-preview (on PRs)
- **`.github/workflows/codeql.yml`** — GitHub CodeQL security scan, weekly cron

Both workflows run on `push` and `pull_request` to `main` and `develop`.

---

## Project Workflow: VEDABOSS / Worker

This project uses a single-agent role-play workflow for incremental work:

- **`VEDABOSS.md`** is the master backlog — every task has a status (`pending`,
  `in_progress`, `done`, `blocked`, `not_needed`) and a commit hash.
- **`worklog.md`** is the append-only multi-agent log.
- Worker picks one task at a time, commits, updates both files, reports back.

See `VEDABOSS.md` for the current state.

---

## License

Proprietary — © 2026 Veda Advisors / Rajat Rajkamal Agarwal. All rights reserved.
