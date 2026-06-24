import Link from 'next/link'

const gold = '#C9A84C'
const darkGreen = '#0D2B1F'
const midGreen = '#1B3A2D'

export const metadata = {
  title: 'Student Entrepreneurs — Startup Fundraising with Rajat Sir | Veda Advisors',
  description: 'Your idea deserves funding. Here\'s how to make investors take you seriously. Rajat Sir works with student entrepreneurs. Stage 0 is free.',
}

export default function StudentsPage() {
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
          For Student Entrepreneurs
        </p>
        <h1 style={{ fontSize: 'clamp(32px, 5vw, 52px)', fontWeight: 900, lineHeight: 1.15, marginBottom: '24px' }}>
          YOUR IDEA DESERVES FUNDING.<br />
          <span style={{ color: gold }}>HERE&apos;S HOW TO MAKE<br />INVESTORS TAKE YOU SERIOUSLY.</span>
        </h1>
        <p style={{ color: '#bbb', fontSize: '18px', lineHeight: 1.8, marginBottom: '32px', maxWidth: '620px' }}>
          Being a student is not a disadvantage. Not knowing the system is.
          Rajat Sir works with student entrepreneurs and teaches them the same system used by funded founders.
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

      {/* The myth */}
      <section style={{ background: midGreen, padding: '60px 24px' }}>
        <div style={{ maxWidth: '800px', margin: '0 auto' }}>
          <p style={{ color: gold, textTransform: 'uppercase', letterSpacing: '3px', fontSize: '12px', fontWeight: 700, marginBottom: '12px' }}>
            The Truth
          </p>
          <h2 style={{ fontSize: '28px', fontWeight: 800, marginBottom: '40px' }}>
            What Nobody Tells<br /><span style={{ color: gold }}>Student Entrepreneurs</span>
          </h2>
          {[
            { myth: 'You need an MVP to raise funds', truth: 'You can raise funds without an MVP, without a product, without a market, without customers — if you know how to identify the right investor for your specific idea.' },
            { myth: 'Investors don\'t take students seriously', truth: 'Investors fund conviction, clarity, and a system — not age. The problem is most students present ideas. Rajat Sir teaches you to present a deal.' },
            { myth: 'You need connections first', truth: 'You are one or two connections away from the right investor. The problem is not access. The problem is you don\'t know how to approach them correctly.' },
          ].map((item, i) => (
            <div key={i} style={{ marginBottom: '32px', background: darkGreen, borderRadius: '10px', padding: '24px', border: `1px solid ${gold}1a` }}>
              <p style={{ color: '#ff6b6b', fontSize: '13px', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '1px', marginBottom: '8px' }}>
                ✗ Myth: &quot;{item.myth}&quot;
              </p>
              <p style={{ color: '#bbb', lineHeight: 1.8, fontSize: '15px' }}>
                <span style={{ color: gold, fontWeight: 700 }}>Truth: </span>{item.truth}
              </p>
            </div>
          ))}
        </div>
      </section>

      {/* Rajat Sir bio short */}
      <section style={{ padding: '60px 24px', maxWidth: '800px', margin: '0 auto' }}>
        <div style={{ display: 'flex', gap: '32px', flexWrap: 'wrap', alignItems: 'center' }}>
          <img src="/images/Image 4 - Rajat.png" alt="Rajat Sir" style={{ width: '160px', height: '160px', objectFit: 'cover', borderRadius: '50%', border: `3px solid ${gold}` }} />
          <div style={{ flex: 1, minWidth: '260px' }}>
            <p style={{ color: gold, fontSize: '12px', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '2px', marginBottom: '8px' }}>Your Advisor</p>
            <h3 style={{ fontSize: '24px', fontWeight: 800, marginBottom: '12px' }}>Rajat Sir</h3>
            <p style={{ color: '#bbb', lineHeight: 1.8, fontSize: '15px' }}>
              TEDx Speaker. 28 years of experience. 400+ startups funded. 600+ founders mentored.
              He has raised funds for over two dozen of his own ventures — and now teaches founders to do the same.
            </p>
            <p style={{ color: gold, fontStyle: 'italic', marginTop: '16px', fontSize: '15px', lineHeight: 1.7 }}>
              &ldquo;I am 50 years old with 28 years of experience. I am the anchor where you confide your fears and discuss your options.&rdquo;
            </p>
          </div>
        </div>
      </section>

      {/* Stage 0 steps */}
      <section style={{ background: midGreen, padding: '60px 24px' }}>
        <div style={{ maxWidth: '800px', margin: '0 auto', textAlign: 'center' }}>
          <p style={{ color: gold, textTransform: 'uppercase', letterSpacing: '3px', fontSize: '12px', fontWeight: 700, marginBottom: '12px' }}>How It Works</p>
          <h2 style={{ fontSize: '28px', fontWeight: 800, marginBottom: '40px' }}>
            Three Steps. <span style={{ color: gold }}>No Payment Required Yet.</span>
          </h2>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '24px' }}>
            {[
              { step: '1', title: 'Fill Stage 0', body: '7 questions about your idea and where you are. Takes 10 minutes. Completely free.' },
              { step: '2', title: 'Get Rajat Sir\'s Email', body: 'He reads your answers personally and emails you an observation within 24 hours.' },
              { step: '3', title: 'Book Your Session', body: 'A free conversation. No commitment. Just Rajat Sir understanding your specific situation.' },
            ].map(s => (
              <div key={s.step} style={{ background: darkGreen, border: `1px solid ${gold}33`, borderRadius: '12px', padding: '28px 20px' }}>
                <div style={{ width: '48px', height: '48px', background: gold, borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 900, color: darkGreen, fontSize: '20px', margin: '0 auto 16px' }}>{s.step}</div>
                <h4 style={{ color: '#fff', fontWeight: 700, marginBottom: '8px' }}>{s.title}</h4>
                <p style={{ color: '#888', fontSize: '14px', lineHeight: 1.7 }}>{s.body}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section style={{ padding: '60px 24px', textAlign: 'center' }}>
        <h2 style={{ fontSize: '28px', fontWeight: 800, marginBottom: '16px' }}>
          Start Now.<br /><span style={{ color: gold }}>It&apos;s Free.</span>
        </h2>
        <p style={{ color: '#888', marginBottom: '32px', fontSize: '16px', maxWidth: '400px', margin: '0 auto 32px' }}>
          The only thing between you and your first investor conversation is Stage 0.
        </p>
        <Link href="/stage0" style={{ display: 'inline-block', background: gold, color: darkGreen, padding: '18px 48px', borderRadius: '8px', fontWeight: 800, fontSize: '17px', textDecoration: 'none', textTransform: 'uppercase', letterSpacing: '1px' }}>
          Begin Stage 0 — Free →
        </Link>
      </section>

      <footer style={{ padding: '24px', textAlign: 'center', color: '#555', fontSize: '13px', borderTop: `1px solid ${gold}11` }}>
        © 2026 Veda Advisors | Rajat Rajkamal Agarwal | <a href="mailto:rajatkamalagarwal@gmail.com" style={{ color: '#666' }}>rajatkamalagarwal@gmail.com</a>
      </footer>
    </div>
  )
}
