import Link from 'next/link'

const gold = '#C9A84C'
const darkGreen = '#0D2B1F'
const midGreen = '#1B3A2D'

export const metadata = {
  title: 'Startup Fundraising Advisor India | Veda Advisors — Rajat Sir',
  description: 'Rajat Sir has helped 400+ Indian startups raise funds. BSCVI 3.0 — a proven 5-stage system built for Indian founders. Stage 0 is free.',
}

export default function IndiaPage() {
  return (
    <div style={{ background: darkGreen, minHeight: '100vh', fontFamily: 'Inter, sans-serif', color: '#fff' }}>
      {/* Nav */}
      <nav style={{ borderBottom: `1px solid ${gold}22`, padding: '16px 24px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <Link href="/">
          <img src="/images/MAIN - Short Logo Veda logo Slate Teak BG.png" alt="Veda Advisors" style={{ height: '40px' }} />
        </Link>
        <Link href="/stage0" style={{ background: gold, color: darkGreen, padding: '10px 20px', borderRadius: '6px', fontWeight: 700, fontSize: '14px', textDecoration: 'none', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
          Start Free Assessment
        </Link>
      </nav>

      {/* Hero */}
      <section style={{ padding: '80px 24px 60px', maxWidth: '800px', margin: '0 auto' }}>
        <p style={{ color: gold, textTransform: 'uppercase', letterSpacing: '3px', fontSize: '12px', fontWeight: 700, marginBottom: '20px' }}>
          🇮🇳 India — Startup Fundraising
        </p>
        <h1 style={{ fontSize: 'clamp(32px, 5vw, 52px)', fontWeight: 900, lineHeight: 1.15, marginBottom: '24px' }}>
          INDIAN FOUNDERS.<br />
          <span style={{ color: gold }}>INDIAN INVESTORS.<br />REAL RESULTS.</span>
        </h1>
        <p style={{ color: '#bbb', fontSize: '18px', lineHeight: 1.8, marginBottom: '32px', maxWidth: '600px' }}>
          Rajat Sir has worked with 400+ founders across India — from IIT garages to registered companies with revenue.
          The BSCVI 3.0 system is built on 28 years of doing deals in India.
        </p>
        <div style={{ display: 'flex', gap: '16px', flexWrap: 'wrap' }}>
          <Link href="/stage0" style={{ background: gold, color: darkGreen, padding: '16px 32px', borderRadius: '8px', fontWeight: 800, fontSize: '16px', textDecoration: 'none', textTransform: 'uppercase', letterSpacing: '1px' }}>
            Start Stage 0 — Free →
          </Link>
          <a href="https://wa.me/919650397480" target="_blank" rel="noopener"
            style={{ background: '#25D366', color: '#fff', padding: '16px 24px', borderRadius: '8px', fontWeight: 700, fontSize: '16px', textDecoration: 'none' }}>
            📱 WhatsApp Rajat Sir
          </a>
        </div>
      </section>

      {/* India-specific proof */}
      <section style={{ background: midGreen, padding: '60px 24px' }}>
        <div style={{ maxWidth: '800px', margin: '0 auto' }}>
          <p style={{ color: gold, textTransform: 'uppercase', letterSpacing: '3px', fontSize: '12px', fontWeight: 700, marginBottom: '32px', textAlign: 'center' }}>
            Indian Startups. Real Raises.
          </p>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '24px', marginBottom: '48px' }}>
            {[
              { name: 'Chaitanya', startup: 'UElement', raised: '₹15 Crore', note: '~$1.8M' },
              { name: 'Abhinav', startup: 'ARC Electric', raised: '₹3 Crore', note: '~$360K' },
            ].map(s => (
              <div key={s.startup} style={{ background: darkGreen, border: `1px solid ${gold}33`, borderRadius: '12px', padding: '24px' }}>
                <p style={{ color: gold, fontSize: '22px', fontWeight: 900, marginBottom: '4px' }}>{s.raised}</p>
                <p style={{ color: '#888', fontSize: '12px', marginBottom: '12px' }}>{s.note}</p>
                <p style={{ color: '#fff', fontWeight: 600 }}>{s.startup}</p>
                <p style={{ color: '#777', fontSize: '13px' }}>Founder: {s.name}</p>
              </div>
            ))}
            <div style={{ background: darkGreen, border: `1px solid ${gold}33`, borderRadius: '12px', padding: '24px' }}>
              <p style={{ color: gold, fontSize: '22px', fontWeight: 900, marginBottom: '4px' }}>400+</p>
              <p style={{ color: '#888', fontSize: '12px', marginBottom: '12px' }}>startups funded</p>
              <p style={{ color: '#fff', fontWeight: 600 }}>Across India</p>
              <p style={{ color: '#777', fontSize: '13px' }}>28 years experience</p>
            </div>
          </div>
        </div>
      </section>

      {/* India-specific content */}
      <section style={{ padding: '60px 24px', maxWidth: '800px', margin: '0 auto' }}>
        <h2 style={{ fontSize: '28px', fontWeight: 800, marginBottom: '32px' }}>
          Why Indian Fundraising Is Different —<br />
          <span style={{ color: gold }}>And Why That Matters</span>
        </h2>
        {[
          { title: 'Indian Investors Need a Different Approach', body: 'A pitch that works for a Silicon Valley VC will not work for an Indian angel or family office. The relationship dynamics, the due diligence process, the negotiation style — all different. Rajat Sir has done it from both sides.' },
          { title: 'You Know the Right People — You Just Don\'t Know How to Approach Them', body: 'Most Indian founders are one or two connections away from the right investor. The problem is not access. It is approach. BSCVI 3.0 teaches you exactly how to approach YOUR specific investor.' },
          { title: 'The Godfather Offer in the Indian Context', body: 'In India, the deal is often made before the term sheet. The relationship, the storytelling, the structure of the offer — these are different here. Rajat Sir shows you how to structure a deal an Indian investor cannot refuse.' },
        ].map((item, i) => (
          <div key={i} style={{ borderLeft: `3px solid ${gold}`, paddingLeft: '24px', marginBottom: '32px' }}>
            <h3 style={{ color: gold, fontSize: '16px', fontWeight: 700, marginBottom: '8px' }}>{item.title}</h3>
            <p style={{ color: '#bbb', lineHeight: 1.8 }}>{item.body}</p>
          </div>
        ))}
      </section>

      {/* CTA */}
      <section style={{ background: midGreen, borderTop: `1px solid ${gold}22`, borderBottom: `1px solid ${gold}22`, padding: '60px 24px', textAlign: 'center' }}>
        <h2 style={{ fontSize: '28px', fontWeight: 800, marginBottom: '16px' }}>
          Stage 0 Is Free.<br /><span style={{ color: gold }}>Start Today.</span>
        </h2>
        <p style={{ color: '#888', marginBottom: '32px', fontSize: '16px' }}>
          7 questions. 10 minutes. Rajat Sir reviews every submission personally.
        </p>
        <Link href="/stage0" style={{ display: 'inline-block', background: gold, color: darkGreen, padding: '18px 48px', borderRadius: '8px', fontWeight: 800, fontSize: '17px', textDecoration: 'none', textTransform: 'uppercase', letterSpacing: '1px' }}>
          Begin Stage 0 — Free →
        </Link>
      </section>

      <footer style={{ padding: '24px', textAlign: 'center', color: '#555', fontSize: '13px' }}>
        © 2026 Veda Advisors | Rajat Rajkamal Agarwal | <a href="mailto:rajatkamalagarwal@gmail.com" style={{ color: '#666' }}>rajatkamalagarwal@gmail.com</a>
      </footer>
    </div>
  )
}
