import { db } from './db'

/**
 * Shape of a Stage 0 submission — mirrors the payload the /stage0 form
 * already sends to Supabase (see src/app/stage0/page.tsx). Keeping the
 * shapes in sync lets us dual-write or migrate without touching the form.
 */
export interface Stage0SubmissionInput {
  name: string
  email: string
  whatsapp?: string | null
  startupStage?: string | null
  revenueStatus?: string | null
  fundingAsked?: string | null
  investorConversations?: string | null
  biggestChallenge?: string | null // JSON blob of full answers
  howHeard?: string | null
}

export interface SavedStage0Submission extends Stage0SubmissionInput {
  id: string
  status: string
  createdAt: Date
  updatedAt: Date
}

/**
 * Persist a Stage 0 submission to the local Prisma database.
 *
 * This is a server-only function — never import from a client component.
 * The /stage0 form continues to write to Supabase as the primary path;
 * this helper exists so server-side code (e.g. an admin import script,
 * a future /api/stage0 endpoint, or a Supabase → Prisma backfill) can
 * write to the same shape without redefining it.
 *
 * Errors are thrown — callers should wrap in try/catch and decide
 * whether to fail silently (e.g. for a non-critical mirror) or surface
 * the error to the user.
 */
export async function saveStage0Submission(
  input: Stage0SubmissionInput,
): Promise<SavedStage0Submission> {
  const created = await db.stage0Submission.create({
    data: {
      name: input.name.trim(),
      email: input.email.trim().toLowerCase(),
      whatsapp: input.whatsapp?.trim() || null,
      startupStage: input.startupStage ?? null,
      revenueStatus: input.revenueStatus ?? null,
      fundingAsked: input.fundingAsked ?? null,
      investorConversations: input.investorConversations ?? null,
      biggestChallenge: input.biggestChallenge ?? null,
      howHeard: input.howHeard ?? null,
      status: 'new',
    },
  })

  return {
    id: created.id,
    name: created.name,
    email: created.email,
    whatsapp: created.whatsapp,
    startupStage: created.startupStage,
    revenueStatus: created.revenueStatus,
    fundingAsked: created.fundingAsked,
    investorConversations: created.investorConversations,
    biggestChallenge: created.biggestChallenge,
    howHeard: created.howHeard,
    status: created.status,
    createdAt: created.createdAt,
    updatedAt: created.updatedAt,
  }
}

/**
 * List all submissions, newest first. Intended for an admin view (not yet built).
 * Pagination is offset-based — fine for the low volume we expect.
 */
export async function listStage0Submissions(opts: {
  take?: number
  skip?: number
  status?: string
} = {}): Promise<SavedStage0Submission[]> {
  const rows = await db.stage0Submission.findMany({
    orderBy: { createdAt: 'desc' },
    take: opts.take ?? 50,
    skip: opts.skip ?? 0,
    where: opts.status ? { status: opts.status } : undefined,
  })

  return rows.map((r) => ({
    id: r.id,
    name: r.name,
    email: r.email,
    whatsapp: r.whatsapp,
    startupStage: r.startupStage,
    revenueStatus: r.revenueStatus,
    fundingAsked: r.fundingAsked,
    investorConversations: r.investorConversations,
    biggestChallenge: r.biggestChallenge,
    howHeard: r.howHeard,
    status: r.status,
    createdAt: r.createdAt,
    updatedAt: r.updatedAt,
  }))
}
