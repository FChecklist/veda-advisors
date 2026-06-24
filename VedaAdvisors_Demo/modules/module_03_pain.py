"""
=============================================================================
MODULE 3: THE PAIN SECTION (Section 2)
=============================================================================
GENERATES: fragments/fragment_03_pain.html

PURPOSE:
  Infographic section — Maximum Visual, Minimum Text.
  Shows the 4 reasons startups never raise funds.
  Each card has: large icon, bold title, ONE sentence max.
  Red left border (#E05252) on each card signals "wrong/danger".

CONTENT (from Strategy Doc Section 4):
  1. WRONG INVESTOR — Pitching everyone. Not every investor is your investor.
  2. WRONG APPROACH — Cold emails. LinkedIn spam. 3-year plans.
  3. NO CLOSING STRATEGY — Interest shown. Founder panics. Deal disappears.
  4. BLIND SPOT IN DOCUMENTATION — Deal dies after investor says yes.

DESIGN DECISIONS:
  - 2x2 grid on desktop, single column on mobile
  - Red left border creates visual "danger" signal per card
  - Dark green cards on darker background for depth
  - Bold Rajat Sir quote at bottom ties it all together

DEPENDENCIES: None (standalone fragment)
=============================================================================
"""

def generate_pain_html():
    """
    Generate the pain/diagnosis section HTML.
    
    This section leverages the psychology of recognition — founders
    must SEE THEMSELVES in at least one of these four cards.
    The red borders signal "this is wrong" without being aggressive.
    """
    
    # The 4 pain cards data — structured for easy maintenance
    # Each card: (emoji_icon, title, body_text)
    pain_cards = [
        (
            "&#127919;",  # 🎯 Target icon — represents aiming at wrong target
            "WRONG INVESTOR",
            "You're pitching everyone. Not every investor is your investor."
        ),
        (
            "&#128226;",  # 📢 Megaphone icon — represents shouting into void
            "WRONG APPROACH",
            "Cold emails. LinkedIn spam. 3-year plans. Investors stop listening."
        ),
        (
            "&#129309;",  # 🤝 Handshake icon — represents deal that never closes
            "NO CLOSING STRATEGY",
            "Interest shown. Founder panics. Deal disappears. No Godfather Offer."
        ),
        (
            "&#128196;",  # 📄 Document icon — represents legal blind spot
            "BLIND SPOT IN DOCUMENTATION",
            "The deal dies after investor says yes. Wrong papers. Wrong terms."
        )
    ]
    
    # Build each pain card HTML
    cards_html = ""
    for i, (icon, title, body) in enumerate(pain_cards):
        cards_html += f'''
                <!-- PAIN CARD {i+1}: {title} -->
                <!-- WHY: Each card addresses one of the 4 real reasons
                     startups fail to raise funds (from Rajat Sir's 
                     diagnosis of 600+ founders). Red left border signals
                     "this is what's wrong". -->
                <div class="pain-card">
                    <!-- Red left border: 4px solid #E05252 — danger color -->
                    <!-- WHY: Red universally signals "wrong/danger". Each
                         card is a mistake the founder is making. -->
                    <div class="pain-card-icon">{icon}</div>
                    <h3 class="pain-card-title">{title}</h3>
                    <p class="pain-card-body">{body}</p>
                </div>
'''
    
    html = f'''
    <!-- ====================================================================
         SECTION 2: THE PAIN — Why Most Startups Never Raise Funds
         ====================================================================
         WHY THIS SECTION EXISTS:
         Recognition is the most powerful conversion tool. When a founder
         reads these 4 cards and thinks "that's me" — they're hooked.
         This section is based on Rajat Sir's diagnosis of 600+ founders.

         DESIGN STRATEGY:
         - 2x2 grid on desktop → easy to scan
         - Single column on mobile → each card gets full attention
         - Red (#E05252) left borders → "this is wrong" signal
         - Maximum 1 sentence per card → no paragraphs, just impact
         - Rajat Sir quote at bottom → authoritative summary

         PSYCHOLOGY:
         The section starts with "And it has nothing to do with your idea."
         This is provocative — founders believe their idea is the problem.
         Reframing the problem creates an opening for the solution.
         ==================================================================== -->
    <section id="pain" class="pain-section">
        <div class="container">
            
            <!-- SECTION HEADLINE -->
            <!-- WHY: "WHY MOST STARTUPS NEVER RAISE FUNDS" — directly 
                 addresses the founder's biggest fear. The word "NEVER"
                 creates urgency. Two-line layout for visual impact. -->
            <h2 class="section-headline">
                WHY MOST STARTUPS<br>
                <span class="gold-text">NEVER RAISE FUNDS</span>
            </h2>
            
            <!-- SUB-HEADLINE (gold, italic) -->
            <!-- WHY: "And it has nothing to do with your idea." — this is
                 the hook. Every founder thinks their idea is the problem.
                 This reframes: it's the SYSTEM, not the idea. -->
            <p class="pain-subheadline">
                "And it has nothing to do with your idea."
            </p>

            <!-- 2x2 GRID OF PAIN CARDS -->
            <!-- WHY: Grid layout makes it scannable. Each card is 
                 self-contained — icon + title + one sentence. -->
            <div class="pain-grid">
{cards_html}
            </div>

            <!-- FULL-WIDTH STATEMENT BY RAJAT SIR -->
            <!-- WHY: After showing the problems, Rajat Sir delivers the
                 diagnosis: "The problem is not your startup. The problem
                 is the system." This transitions from pain to solution. -->
            <div class="pain-statement">
                <p class="pain-statement-text">
                    "The problem is not your startup.<br>
                    The problem is the system you are using to raise funds."
                </p>
                <p class="pain-statement-author">— Rajat Sir</p>
            </div>
        </div>
    </section>
    <!-- END OF SECTION 2: THE PAIN -->
'''
    return html


if __name__ == "__main__":
    import os
    pain_html = generate_pain_html()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, "..", "fragments", "fragment_03_pain.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(pain_html)
    print(f"[MODULE 3] Pain section generated successfully!")
    print(f"[MODULE 3] Output: {output_path}")
    print(f"[MODULE 3] Size: {len(pain_html)} characters")