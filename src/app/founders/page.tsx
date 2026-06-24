import Link from 'next/link'

const gold = '#C9A84C'
const darkGreen = '#0D2B1F'
const midGreen = '#1B3A2D'

export const metadata = {
  title: 'Startup Founders — Raise Funds with Rajat Sir | Veda Advisors',
  description: 'You\'ve been pitching. Nothing has moved. Let\'s fix that. Rajat Sir\'s BSCVI 3.0 system has helped 400+ founders raise funds. Stage 0 is free.',
}

export default function FoundersPage() {
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
          For Startup Founders
        </p>
        <h1 style={{ fontSize: 'clamp(32px, 5vw, 52px)', fontWeight: 900, lineHeight: 1.15, marginBottom: '24px' }}>
          YOU&apos;VE BEEN PITCHING.<br />
          <span style={{ color: gold }}>NOTHING HAS MOVED.<br />LET&apos;S FIX THAT.</span>
        </h1>
        <p style={{ color: '#bbb', fontSize: '18px', lineHeight: 1.8, marginBottom: '32px', maxWidth: '600px' }}>
          The problem is not your startup. The problem is the system — or the absence of one.
          Rajat Sir has helped 400+ founders raise funds using BSCVI 3.0.
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

      {/* The 4 real reasons */}
      <section style={{ background: midGreen, padding: '60px 24px' }}>
        <div style={{ maxWidth: '800px', margin: '0 auto' }}>
          <p style={{ color: gold, textTransform: 'uppercase', letterSpacing: '3px', fontSize: '12px', fontWeight: 700, marginBottom: '12px' }}>
            The Real Reason
          </p>
          <h2 style={{ fontSize: '28px', fontWeight: 800, marginBottom: '40px' }}>
            Why Startups Don&apos;t Raise Funds<br />
            <span style={{ color: gold }}>(And It&apos;s Not Your Pitch Deck)</span>
          </h2>
          {[
            { num: '01', title: 'Wrong Investors', body: 'Not every investor is your investor. Most founders approach investors who will never fund their type of business — no matter how good the pitch.' },
            { num: '02', title: 'Wrong Approach', body: 'You are missing the critical point: why does THIS specific investor need YOU? Not your startup. You.' },
            { num: '03', title: 'No Godfather Offer', body: 'No closing strategy. You get interest from an investor and then panic. There is no offer structure, no negotiation playbook.' },
            { num: '04', title: 'Weak Documentation', body: 'The real weakness is not the pitch deck. It is the legal documents, term sheets, and deal structure. Rajat Sir covers all of this.' },
          ].map(item => (
            <div key={item.num} style={{ display: 'flex', gap: '20px', marginBottom: '32px', alignItems: 'flex-start' }}>
              <span style={{ color: gold, fontSize: '32px', fontWeight: 900, opacity: 0.4, minWidth: '48px', lineHeight: 1 }}>{item.num}</span>
              <div>
                <h3 style={{ color: gold, fontSize: '16px', fontWeight: 700, marginBottom: '8px' }}>{item.title}</h3>
                <p style={{ color: '#bbb', lineHeight: 1.8 }}>{item.body}</p>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* BSCVI system */}
      <section style={{ padding: '60px 24px', maxWidth: '800px', margin: '0 auto' }}>
        <p style={{ color: gold, textTransform: 'uppercase', letterSpacing: '3px', fontSize: '12px', fontWeight: 700, marginBottom: '12px' }}>The System</p>
        <h2 style={{ fontSize: '28px', fontWeight: 800, marginBottom: '40px' }}>BSCVI 3.0 — <span style={{ color: gold }}>5 Stages to a Funded Startup</span></h2>
        {[
          { stage: '0', name: 'READINESS', desc: 'Free. Rajat Sir reviews your startup and tells you where you stand.', free: true },
          { stage: '1', name: 'IDENTIFY', desc: '10 investors who can actually fund your specific business.' },
          { stage: '2', name: 'APPROACH', desc: 'A personalised approach story for each of the 10 investors.' },
          { stage: '3', name: 'OFFER', desc: 'The Godfather Offer — structured for each interested investor.' },
          { stage: '4', name: 'CLOSE', desc: 'Documentation, term sheets, negotiation support, deal closure.' },
          { stage: '5', name: 'SUSTAIN', desc: 'Post-closure structuring and next round scouting.' },
        ].map(s => (
          <div key={s.stage} style={{ display: 'flex', gap: '16px', marginBottom: '16px', alignItems: 'flex-start', background: midGreen, borderRadius: '10px', padding: '16px 20px', border: `1px solid ${gold}${s.free ? '66' : '1a'}` }}>
            <span style={{ background: s.free ? gold : '#2a4a35', color: s.free ? darkGreen : gold, fontWeight: 900, fontSize: '14px', padding: '4px 10px', borderRadius: '6px', minWidth: '36px', textAlign: 'center', flexShrink: 0 }}>S{s.stage}</span>
            <div>
              <span style={{ color: gold, fontWeight: 700, fontSize: '13px', letterSpacing: '1px' }}>{s.name}</span>
              {s.free && <span style={{ color: darkGreen, background: gold, fontSize: '10px', fontWeight: 800, padding: '2px 6px', borderRadius: '4px', marginLeft: '8px' }}>FREE</span>}
              <p style={{ color: '#bbb', fontSize: '14px', marginTop: '4px', lineHeight: 1.6 }}>{s.desc}</p>
            </div>
          </div>
        ))}
      </section>

      {/* CTA */}
      <section style={{ background: midGreen, borderTop: `1px solid ${gold}22`, borderBottom: `1px solid ${gold}22`, padding: '60px 24px', textAlign: 'center' }}>
        <h2 style={{ fontSize: '28px', fontWeight: 800, marginBottom: '16px' }}>
          Stage 0 Is Free.<br /><span style={{ color: gold }}>Find Out Where You Stand.</span>
        </h2>
        <p style={{ color: '#888', marginBottom: '32px', fontSize: '16px' }}>
          7 questions. 10 minutes. Rajat Sir reviews every submission personally.
        </p>
        <Link href="/stage0" style={{ display: 'inline-block', background: gold, color: darkGreen, padding: '18px 48px', borderRadius: '8px', fontWeight: 800, fontSize: '17px', textDecoration: 'none', textTransform: 'uppercase', letterSpacing: '1px' }}>
          Apply to Work with Rajat Sir →
        </Link>
      </section>

      <footer style={{ padding: '24px', textAlign: 'center', color: '#555', fontSize: '13px' }}>
        © 2026 Veda Advisors | Rajat Rajkamal Agarwal | <a href="mailto:rajatkamalagarwal@gmail.com" style={{ color: '#666' }}>rajatkamalagarwal@gmail.com</a>
      </footer>
    </div>
  )
}
