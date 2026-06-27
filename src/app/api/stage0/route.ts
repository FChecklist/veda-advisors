import { NextRequest, NextResponse } from 'next/server'
import { saveStage0Submission, type Stage0SubmissionInput } from '@/lib/stage0'

/**
 * POST /api/stage0
 *
 * Server-side fallback for the Stage 0 assessment form. The live form at
 * /stage0 continues to write to Supabase as the primary path; this endpoint
 * exists so that:
 *   1. Future versions of the form can opt to POST here instead of Supabase
 *   2. The Supabase → Prisma backfill script has a target shape
 *   3. Manual submissions (e.g. from an admin tool) can be ingested
 *
 * NOT yet wired into src/app/stage0/page.tsx — that change is a separate
 * decision because it requires deploying a real DATABASE_URL to Vercel.
 *
 * Validation:
 *   - name: required, non-empty after trim
 *   - email: required, must contain "@"
 *   - whatsapp: optional
 *   - all other fields: optional, passed through
 *
 * Errors:
 *   - 400: missing/invalid name or email
 *   - 500: Prisma write failed (DB unreachable, schema drift, etc.)
 */
export async function POST(req: NextRequest) {
  let body: Partial<Stage0SubmissionInput>
  try {
    body = await req.json()
  } catch {
    return NextResponse.json(
      { error: 'Invalid JSON body' },
      { status: 400 },
    )
  }

  const name = (body.name ?? '').toString().trim()
  const email = (body.email ?? '').toString().trim().toLowerCase()

  if (!name) {
    return NextResponse.json(
      { error: 'name is required' },
      { status: 400 },
    )
  }
  if (!email || !email.includes('@')) {
    return NextResponse.json(
      { error: 'valid email is required' },
      { status: 400 },
    )
  }

  try {
    const saved = await saveStage0Submission({
      name,
      email,
      whatsapp: body.whatsapp ?? null,
      startupStage: body.startupStage ?? null,
      revenueStatus: body.revenueStatus ?? null,
      fundingAsked: body.fundingAsked ?? null,
      investorConversations: body.investorConversations ?? null,
      biggestChallenge: body.biggestChallenge ?? null,
      howHeard: body.howHeard ?? null,
    })

    return NextResponse.json(
      { ok: true, id: saved.id, status: saved.status },
      { status: 201, headers: { 'Cache-Control': 'no-store' } },
    )
  } catch (err) {
    console.error('[POST /api/stage0] save failed:', err)
    return NextResponse.json(
      { error: 'Could not save submission' },
      { status: 500 },
    )
  }
}

/**
 * GET /api/stage0
 * Returns a tiny stub so the route is discoverable. Listing submissions is
 * intentionally not exposed — that belongs behind auth in a future task.
 */
export async function GET() {
  return NextResponse.json(
    { endpoint: '/api/stage0', method: 'POST', description: 'Submit a Stage 0 form entry' },
    { headers: { 'Cache-Control': 'no-store' } },
  )
}
