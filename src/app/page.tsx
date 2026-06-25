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
      {/* Loading state */}
      {loading && (
        <div style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          height: '100vh',
          background: '#0D2B1F',
          color: '#C9A84C',
          fontFamily: 'Inter, Arial, sans-serif',
        }}>
          Loading...
        </div>
      )}

      {/* Iframe displaying the full HTML */}
      <iframe
        ref={iframeRef}
        src="/demo.html"
        style={{
          width: '100%',
          height: '100vh',
          border: 'none',
          display: loading ? 'none' : 'block',
        }}
        onLoad={() => setLoading(false)}
        title="Veda Advisors"
      />
    </div>
  )
}