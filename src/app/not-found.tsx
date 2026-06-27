import Link from 'next/link'

const gold = '#C9A84C'
const darkGreen = '#0D2B1F'
const midGreen = '#1B3A2D'

export default function NotFound() {
  return (
    <div
      style={{
        background: darkGreen,
        minHeight: '100vh',
        fontFamily: 'Inter, Arial, sans-serif',
        color: '#fff',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '24px',
        textAlign: 'center',
      }}
    >
      <p
        style={{
          color: gold,
          textTransform: 'uppercase',
          letterSpacing: '3px',
          fontSize: '12px',
          fontWeight: 700,
          marginBottom: '16px',
        }}
      >
        Veda Advisors
      </p>
      <h1
        style={{
          fontSize: 'clamp(56px, 12vw, 120px)',
          fontWeight: 900,
          lineHeight: 1,
          marginBottom: '12px',
          color: gold,
        }}
      >
        404
      </h1>
      <h2
        style={{
          fontSize: 'clamp(20px, 4vw, 28px)',
          fontWeight: 800,
          marginBottom: '16px',
        }}
      >
        This page raised no funds.
      </h2>
      <p
        style={{
          color: '#bbb',
          fontSize: '16px',
          lineHeight: 1.7,
          maxWidth: '440px',
          marginBottom: '32px',
        }}
      >
        The page you were looking for doesn&apos;t exist — but your path to
        funding still does. Head back to the home page and start Stage 0.
      </p>
      <div style={{ display: 'flex', gap: '12px', flexWrap: 'wrap', justifyContent: 'center' }}>
        <Link
          href="/"
          style={{
            background: gold,
            color: darkGreen,
            padding: '14px 28px',
            borderRadius: '8px',
            fontWeight: 800,
            fontSize: '15px',
            textDecoration: 'none',
            textTransform: 'uppercase',
            letterSpacing: '1px',
          }}
        >
          ← Back to Home
        </Link>
        <Link
          href="/stage0"
          style={{
            background: midGreen,
            color: gold,
            border: `1px solid ${gold}66`,
            padding: '14px 28px',
            borderRadius: '8px',
            fontWeight: 700,
            fontSize: '15px',
            textDecoration: 'none',
            textTransform: 'uppercase',
            letterSpacing: '1px',
          }}
        >
          Start Stage 0 →
        </Link>
      </div>
    </div>
  )
}
