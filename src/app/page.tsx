'use client'

import { useEffect, useRef, useState } from 'react'

export default function Home() {
  const iframeRef = useRef<HTMLIFrameElement>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // Load the Veda Advisors HTML via the API route
    setLoading(true)
  }, [])

  return (
    <div style={{ width: '100vw', height: '100vh', overflow: 'hidden', margin: 0, padding: 0 }}>
      {/* Info banner */}
      <div style={{
        background: '#C9A84C',
        color: '#0D2B1F',
        padding: '6px 16px',
        fontSize: '13px',
        fontWeight: 600,
        textAlign: 'center',
        letterSpacing: '0.5px',
      }}>
        VEDA ADVISORS DEMO PREVIEW — Generated from 12 Python Modules — Scroll down to see all sections
      </div>
      
      {/* Loading state */}
      {loading && (
        <div style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          height: 'calc(100vh - 32px)',
          color: '#C9A84C',
          fontFamily: 'Inter, Arial, sans-serif',
        }}>
          Loading Veda Advisors Demo...
        </div>
      )}
      
      {/* Iframe displaying the full HTML */}
      <iframe
        ref={iframeRef}
        src="/api/veda"
        style={{
          width: '100%',
          height: 'calc(100vh - 32px)',
          border: 'none',
          display: loading ? 'none' : 'block',
        }}
        onLoad={() => setLoading(false)}
        title="Veda Advisors Demo"
      />
    </div>
  )
}