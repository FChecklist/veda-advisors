'use client'

import { useState } from 'react'

const SUPABASE_URL = 'https://pcrjmlpuqsbocqfwoxod.supabase.co'
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBjcmptbHB1cXNib2NxZndveG9kIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODIzMTkxNTAsImV4cCI6MjA5Nzg5NTE1MH0.nH-nltFt8M3nJG_clP9Zw3_FsXtn-8mKrFeqdE414oU'

const questions = [
  { id: 'q1', label: 'What is your startup called — and what problem does it solve?' },
  { id: 'q2', label: 'Where are you right now?', type: 'select', options: ['Just an idea', 'Building MVP', 'Early revenue', 'Consistent revenue'] },
  { id: 'q3', label: 'Have you approached any investors yet?', type: 'select', options: ['No, not yet', 'Yes, but no results', 'Yes, got some interest', 'Yes, in active conversations'] },
  { id: 'q4', label: 'What is the one thing that worries you most about raising funds?' },
  { id: 'q5', label: 'How urgently do you need funding?', type: 'select', options: ['Exploring, no rush', 'Within 6 months', 'Within 3 months', 'Urgent — within 30 days'] },
  { id: 'q6', label: 'How much are you looking to raise — and what will you use it for?' },
  { id: 'q7', label: 'On a scale of 1–10, how ready is your startup to approach investors right now? And why?' },
]

export default function Stage0Page() {
  const [step, setStep] = useState(0) // 0 = intro, 1-7 = questions, 8 = contact, 9 = done
  const [answers, setAnswers] = useState<Record<string, string>>({})
  const [contact, setContact] = useState({ name: '', email: '', whatsapp: '' })
  const [submitting, setSubmitting] = useState(false)
  const [error, setError] = useState('')

  const totalSteps = questions.length + 1 // 7 questions + contact
  const progress = step === 0 ? 0 : Math.round((step / totalSteps) * 100)

  function handleAnswer(value: string) {
    const q = questions[step - 1]
    setAnswers(prev => ({ ...prev, [q.id]: value }))
  }

  function canProceed() {
    if (step === 0) return true
    if (step <= questions.length) return !!answers[questions[step - 1].id]?.trim()
    return contact.name.trim() && contact.email.trim()
  }

  function next() {
    if (!canProceed()) return
    setStep(s => s + 1)
    setError('')
  }

  function back() {
    setStep(s => Math.max(0, s - 1))
    setError('')
  }

  async function submit() {
    if (!contact.name.trim() || !contact.email.trim()) {
      setError('Please fill in your name and email.')
      return
    }
    setSubmitting(true)
    setError('')
    try {
      const payload = {
        name: contact.name.trim(),
        email: contact.email.trim(),
        whatsapp: contact.whatsapp.trim() || null,
        startup_stage: answers.q2 || null,
        revenue_status: answers.q2 || null,
        funding_asked: answers.q6 || null,
        investor_conversations: answers.q3 || null,
        biggest_challenge: answers.q4 || null,
        how_heard: null,
        status: 'new',
      }
      // Store all 7 answers as a JSON note in biggest_challenge field
      const fullAnswers = JSON.stringify({ ...answers, ...contact })
      Object.assign(payload, { biggest_challenge: fullAnswers })

      const res = await fetch(`${SUPABASE_URL}/rest/v1/stage0_submissions`, {
        method: 'POST',
        headers: {
          'apikey': SUPABASE_ANON_KEY,
          'Authorization': `Bearer ${SUPABASE_ANON_KEY}`,
          'Content-Type': 'application/json',
          'Prefer': 'return=minimal',
        },
        body: JSON.stringify(payload),
      })
      if (res.ok) {
        setStep(9)
      } else {
        const err = await res.text()
        setError('Submission failed. Please try WhatsApp instead.')
        console.error(err)
      }
    } catch {
      setError('Network error. Please try WhatsApp instead.')
    } finally {
      setSubmitting(false)
    }
  }

  const s = { background: '#0D2B1F', minHeight: '100vh', fontFamily: 'Inter, sans-serif', color: '#fff', padding: '0' }
  const gold = '#C9A84C'
  const darkGreen = '#0D2B1F'
  const midGreen = '#1B3A2D'

  // DONE state
  if (step === 9) return (
    <div style={s}>
      <nav style={{ background: darkGreen, borderBottom: `1px solid ${gold}22`, padding: '16px 24px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <a href="/" style={{ textDecoration: 'none' }}>
          <img src="/images/MAIN - Short Logo Veda logo Slate Teak BG.png" alt="Veda Advisors" style={{ height: '40px' }} />
        </a>
      </nav>
      <div style={{ maxWidth: '600px', margin: '80px auto', padding: '0 24px', textAlign: 'center' }}>
        <div style={{ fontSize: '56px', marginBottom: '24px' }}>✅</div>
        <h1 style={{ color: gold, fontSize: '28px', fontWeight: 800, marginBottom: '16px', textTransform: 'uppercase', letterSpacing: '1px' }}>
          Stage 0 Submitted
        </h1>
        <p style={{ color: '#ccc', fontSize: '18px', lineHeight: 1.7, marginBottom: '32px' }}>
          Rajat Sir will personally review your answers and email you within 24 hours.
        </p>
        <div style={{ background: midGreen, border: `1px solid ${gold}44`, borderRadius: '12px', padding: '24px', marginBottom: '32px' }}>
          <p style={{ color: gold, fontWeight: 700, marginBottom: '8px', textTransform: 'uppercase', letterSpacing: '1px', fontSize: '13px' }}>What happens next</p>
          <p style={{ color: '#ccc', lineHeight: 1.8, fontSize: '15px' }}>
            <strong style={{ color: '#fff' }}>Email 1:</strong> Acknowledgement from Rajat Sir (within a few hours)<br />
            <strong style={{ color: '#fff' }}>Email 2:</strong> Personalised observation + book your free session (within 24 hrs)<br />
            <strong style={{ color: '#fff' }}>Session:</strong> Free, no commitment. Just a conversation.
          </p>
        </div>
        <p style={{ color: '#888', fontSize: '14px', marginBottom: '24px' }}>
          Have an urgent question? WhatsApp Rajat Sir directly.
        </p>
        <a href="https://wa.me/919650397480" target="_blank" rel="noopener"
          style={{ display: 'inline-block', background: '#25D366', color: '#fff', padding: '14px 32px', borderRadius: '8px', fontWeight: 700, textDecoration: 'none', fontSize: '16px' }}>
          📱 WhatsApp Rajat Sir
        </a>
      </div>
    </div>
  )

  const currentQ = step >= 1 && step <= 7 ? questions[step - 1] : null
  const currentAnswer = currentQ ? (answers[currentQ.id] || '') : ''

  return (
    <div style={s}>
      {/* Nav */}
      <nav style={{ background: darkGreen, borderBottom: `1px solid ${gold}22`, padding: '16px 24px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <a href="/" style={{ textDecoration: 'none' }}>
          <img src="/images/MAIN - Short Logo Veda logo Slate Teak BG.png" alt="Veda Advisors" style={{ height: '40px' }} />
        </a>
        <span style={{ color: gold, fontSize: '13px', fontWeight: 600, textTransform: 'uppercase', letterSpacing: '1px' }}>
          Stage 0 — Free Assessment
        </span>
      </nav>

      {/* Progress bar */}
      {step > 0 && (
        <div style={{ background: '#0a2218', height: '4px' }}>
          <div style={{ background: gold, height: '100%', width: `${progress}%`, transition: 'width 0.3s ease' }} />
        </div>
      )}

      <div style={{ maxWidth: '640px', margin: '0 auto', padding: '40px 24px 80px' }}>

        {/* INTRO */}
        {step === 0 && (
          <div>
            <p style={{ color: gold, textTransform: 'uppercase', letterSpacing: '3px', fontSize: '12px', fontWeight: 700, marginBottom: '24px' }}>
              Stage 0 — Free Readiness Assessment
            </p>
            <h1 style={{ fontSize: '36px', fontWeight: 900, lineHeight: 1.2, marginBottom: '20px' }}>
              START HERE.<br /><span style={{ color: gold }}>IT&apos;S FREE.</span>
            </h1>
            <p style={{ color: '#bbb', fontSize: '17px', lineHeight: 1.8, marginBottom: '32px' }}>
              7 questions. 10 minutes. Rajat Sir reviews every submission personally and emails you within 24 hours.
            </p>
            <div style={{ background: midGreen, border: `1px solid ${gold}33`, borderRadius: '12px', padding: '20px 24px', marginBottom: '32px' }}>
              {[
                'Startup called — and what problem it solves',
                'Where you are right now (idea / building / revenue)',
                'Whether you have approached investors',
                'Your biggest fear about fundraising',
                'How urgently you need funding',
                'How much you are raising — and what for',
                'Your honest readiness score out of 10',
              ].map((q, i) => (
                <div key={i} style={{ display: 'flex', gap: '12px', marginBottom: i < 6 ? '12px' : 0, alignItems: 'flex-start' }}>
                  <span style={{ color: gold, fontWeight: 700, fontSize: '13px', minWidth: '24px' }}>Q{i + 1}</span>
                  <span style={{ color: '#ccc', fontSize: '14px' }}>{q}</span>
                </div>
              ))}
            </div>
            <button onClick={next}
              style={{ background: gold, color: darkGreen, padding: '16px 40px', borderRadius: '8px', fontWeight: 800, fontSize: '17px', border: 'none', cursor: 'pointer', width: '100%', textTransform: 'uppercase', letterSpacing: '1px' }}>
              Begin Stage 0 — Free →
            </button>
            <p style={{ color: '#666', fontSize: '13px', textAlign: 'center', marginTop: '16px' }}>
              No payment. No spam. Just Rajat Sir reading your answers.
            </p>
          </div>
        )}

        {/* QUESTIONS 1-7 */}
        {step >= 1 && step <= 7 && currentQ && (
          <div>
            <p style={{ color: gold, fontSize: '13px', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '2px', marginBottom: '8px' }}>
              Question {step} of 7
            </p>
            <h2 style={{ fontSize: '22px', fontWeight: 700, lineHeight: 1.4, marginBottom: '32px' }}>
              {currentQ.label}
            </h2>
            {currentQ.type === 'select' ? (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                {currentQ.options?.map(opt => (
                  <button key={opt} onClick={() => { handleAnswer(opt); setTimeout(next, 150) }}
                    style={{
                      padding: '16px 20px', borderRadius: '8px', textAlign: 'left', fontSize: '15px', fontWeight: 500,
                      cursor: 'pointer', transition: 'all 0.15s',
                      background: currentAnswer === opt ? gold : midGreen,
                      color: currentAnswer === opt ? darkGreen : '#fff',
                      border: `1px solid ${currentAnswer === opt ? gold : gold + '33'}`,
                    }}>
                    {opt}
                  </button>
                ))}
              </div>
            ) : (
              <textarea
                value={currentAnswer}
                onChange={e => handleAnswer(e.target.value)}
                placeholder="Type your answer here..."
                rows={4}
                style={{
                  width: '100%', background: midGreen, border: `1px solid ${gold}44`, borderRadius: '8px',
                  color: '#fff', fontSize: '16px', padding: '16px', resize: 'vertical', outline: 'none',
                  fontFamily: 'Inter, sans-serif', lineHeight: 1.6, boxSizing: 'border-box',
                }}
                onKeyDown={e => { if (e.key === 'Enter' && e.metaKey) next() }}
              />
            )}
            <div style={{ display: 'flex', gap: '12px', marginTop: '24px' }}>
              {step > 1 && (
                <button onClick={back}
                  style={{ padding: '14px 24px', background: 'transparent', border: `1px solid ${gold}44`, color: '#888', borderRadius: '8px', cursor: 'pointer', fontSize: '14px' }}>
                  ← Back
                </button>
              )}
              {currentQ.type !== 'select' && (
                <button onClick={next} disabled={!canProceed()}
                  style={{ flex: 1, padding: '14px 24px', background: canProceed() ? gold : '#2a4a35', color: canProceed() ? darkGreen : '#666', borderRadius: '8px', cursor: canProceed() ? 'pointer' : 'default', fontWeight: 700, fontSize: '15px', border: 'none' }}>
                  {step === 7 ? 'Last step →' : 'Next →'}
                </button>
              )}
            </div>
          </div>
        )}

        {/* CONTACT STEP */}
        {step === 8 && (
          <div>
            <p style={{ color: gold, fontSize: '13px', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '2px', marginBottom: '8px' }}>
              Almost done
            </p>
            <h2 style={{ fontSize: '22px', fontWeight: 700, lineHeight: 1.4, marginBottom: '8px' }}>
              Where should Rajat Sir send his response?
            </h2>
            <p style={{ color: '#888', fontSize: '14px', marginBottom: '32px' }}>
              He reviews every submission personally and replies within 24 hours.
            </p>
            {(['name', 'email', 'whatsapp'] as const).map(field => (
              <div key={field} style={{ marginBottom: '16px' }}>
                <label style={{ display: 'block', color: gold, fontSize: '12px', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '1px', marginBottom: '8px' }}>
                  {field === 'name' ? 'Your Name *' : field === 'email' ? 'Email Address *' : 'WhatsApp Number (optional)'}
                </label>
                <input
                  type={field === 'email' ? 'email' : 'text'}
                  value={contact[field]}
                  onChange={e => setContact(prev => ({ ...prev, [field]: e.target.value }))}
                  placeholder={field === 'name' ? 'Full name' : field === 'email' ? 'your@email.com' : '+91 98765 43210'}
                  style={{
                    width: '100%', background: midGreen, border: `1px solid ${gold}44`, borderRadius: '8px',
                    color: '#fff', fontSize: '16px', padding: '14px 16px', outline: 'none', boxSizing: 'border-box',
                    fontFamily: 'Inter, sans-serif',
                  }}
                />
              </div>
            ))}
            {error && <p style={{ color: '#ff6b6b', fontSize: '14px', marginBottom: '16px' }}>{error}</p>}
            <div style={{ display: 'flex', gap: '12px', marginTop: '8px' }}>
              <button onClick={back}
                style={{ padding: '14px 24px', background: 'transparent', border: `1px solid ${gold}44`, color: '#888', borderRadius: '8px', cursor: 'pointer', fontSize: '14px' }}>
                ← Back
              </button>
              <button onClick={submit} disabled={submitting || !canProceed()}
                style={{ flex: 1, padding: '14px 24px', background: canProceed() && !submitting ? gold : '#2a4a35', color: canProceed() && !submitting ? darkGreen : '#666', borderRadius: '8px', cursor: canProceed() ? 'pointer' : 'default', fontWeight: 800, fontSize: '15px', border: 'none', textTransform: 'uppercase', letterSpacing: '1px' }}>
                {submitting ? 'Submitting...' : 'Submit to Rajat Sir →'}
              </button>
            </div>
            <p style={{ color: '#555', fontSize: '12px', textAlign: 'center', marginTop: '16px' }}>
              Your answers are confidential. What you share stays with Rajat Sir.
            </p>
          </div>
        )}
      </div>
    </div>
  )
}
