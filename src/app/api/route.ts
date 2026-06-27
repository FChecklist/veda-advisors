import { NextResponse } from 'next/server'

/**
 * GET /api
 * Lightweight health-check endpoint used by uptime monitors and deploy verification.
 * Returns 200 with a small JSON payload. No DB or external calls — must always be fast.
 */
export async function GET() {
  const startedAt = process.env.STARTED_AT ?? null
  const vercelEnv = process.env.VERCEL_ENV ?? 'local'
  const region = process.env.VERCEL_REGION ?? null

  return NextResponse.json(
    {
      status: 'ok',
      service: 'veda-advisors',
      version: '0.2.0',
      time: new Date().toISOString(),
      env: vercelEnv,
      region,
      startedAt,
    },
    {
      headers: { 'Cache-Control': 'no-store' },
    },
  )
}
