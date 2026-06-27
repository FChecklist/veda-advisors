const gold = '#C9A84C'
const darkGreen = '#0D2B1F'

/**
 * App-level loading UI shown by Next.js 16 while server components
 * in the root segment are streaming. Mirrors the home page's loading
 * state so transitions feel native instead of a white flash.
 */
export default function Loading() {
  return (
    <div
      style={{
        width: '100vw',
        height: '100vh',
        background: darkGreen,
        color: gold,
        fontFamily: 'Inter, Arial, sans-serif',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        gap: '20px',
      }}
    >
      <div
        aria-label="Loading"
        style={{
          width: '36px',
          height: '36px',
          borderRadius: '50%',
          border: `3px solid ${gold}33`,
          borderTopColor: gold,
          animation: 'veda-spin 0.9s linear infinite',
        }}
      />
      <span style={{ fontSize: '13px', letterSpacing: '2px', textTransform: 'uppercase', fontWeight: 700 }}>
        Loading Veda Advisors…
      </span>
      <style>{`@keyframes veda-spin { to { transform: rotate(360deg); } }`}</style>
    </div>
  )
}
