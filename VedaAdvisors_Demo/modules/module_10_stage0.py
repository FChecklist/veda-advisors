"""
=============================================================================
MODULE 10: STAGE 0 PREVIEW (Section 9) — The Free Assessment Teaser
=============================================================================
GENERATES: fragments/fragment_10_stage0.html

PURPOSE: Shows what Stage 0 looks like — visual mockup of the form.
  Q1 visible and active, Q2-Q7 blurred/locked. Creates curiosity.
  3-step process at bottom.
=============================================================================
"""

def generate_stage0_html():
    """Generate the Stage 0 preview/teaser section."""
    
    # The 7 questions from Strategy Doc Section 10
    # Only Q1 is visible, rest are blurred
    questions = [
        ("1", "What is your startup called — and what problem does it solve?", True),
        ("2", "", False),  # Blurred
        ("3", "", False),
        ("4", "", False),
        ("5", "", False),
        ("6", "", False),
        ("7", "", False),
    ]
    
    questions_html = ""
    for num, text, is_visible in questions:
        if is_visible:
            questions_html += f'''
                    <!-- Q{num}: ACTIVE — Visible to user -->
                    <div class="stage0-question stage0-question-active">
                        <div class="stage0-question-number">Q{num}</div>
                        <div class="stage0-question-text">{text}</div>
                        <!-- Non-functional input field for visual only -->
                        <input type="text" class="stage0-input" placeholder="Your answer here..." readonly onclick="alert('In the final version, this opens your personal portal. Demo mode.');">
                    </div>
'''
        else:
            questions_html += f'''
                    <!-- Q{num}: LOCKED — Blurred/locked for curiosity -->
                    <div class="stage0-question stage0-question-locked">
                        <div class="stage0-question-number">Q{num}</div>
                        <div class="stage0-question-blur">&#128274; &#9679;&#9679;&#9679;&#9679;&#9679;&#9679;&#9679;</div>
                        <div class="stage0-locked-label">Unlocks when you start</div>
                    </div>
'''
    
    html = f'''
    <!-- ====================================================================
         SECTION 9: STAGE 0 PREVIEW — The Free Assessment Teaser
         ====================================================================
         WHY: This section SHOWS (doesn't tell) what Stage 0 is.
         By revealing Q1 and locking Q2-Q7, it creates massive curiosity.
         The founder thinks: "I want to know what the other questions are."
         
         DESIGN: A card that looks like a multi-step form.
         Q1 has an actual input field (non-functional in demo).
         Q2-Q7 are blurred with lock icons.
         
         PSYCHOLOGY: Partial information is more compelling than full info.
         The locked questions are the hook. "Unlocks when you start" 
         creates a desire to begin.
         ==================================================================== -->
    <section id="stage0" class="stage0-section">
        <div class="container">
            
            <h2 class="section-headline">
                START HERE.<br>
                <span class="gold-text">IT'S FREE.</span>
            </h2>
            <p class="section-subheadline">Stage 0 — The Startup Fundraising Readiness Assessment</p>

            <!-- FORM MOCKUP CARD -->
            <!-- WHY: Looks like a real form but is a visual preview only.
                 In the demo, clicking the input shows an alert. -->
            <div class="stage0-form-card">
                <!-- Form progress indicator -->
                <div class="stage0-progress">
                    <div class="stage0-progress-bar" style="width: 14%;"></div>
                    <span class="stage0-progress-text">1 of 7</span>
                </div>
                
                <!-- QUESTIONS LIST -->
                <div class="stage0-questions">
{questions_html}
                </div>
            </div>

            <!-- BELOW THE FORM PREVIEW -->
            <p class="stage0-teaser-text">
                7 questions. 10 minutes. Rajat Sir reviews every submission personally.
            </p>

            <!-- 3-STEP PROCESS -->
            <!-- WHY: Shows the journey after Stage 0:
                 1. Fill assessment → 2. Get Rajat Sir's email → 3. Book session
                 Makes the process feel simple and human. -->
            <div class="stage0-process-steps">
                <div class="process-step">
                    <div class="process-step-number">1</div>
                    <div class="process-step-text">Fill Stage 0</div>
                </div>
                <div class="process-step-arrow" aria-hidden="true">&rarr;</div>
                <div class="process-step">
                    <div class="process-step-number">2</div>
                    <div class="process-step-text">Get Rajat Sir's Email</div>
                </div>
                <div class="process-step-arrow" aria-hidden="true">&rarr;</div>
                <div class="process-step">
                    <div class="process-step-number">3</div>
                    <div class="process-step-text">Book Your Session</div>
                </div>
            </div>

            <!-- CTA BUTTON -->
            <a 
                href="#" 
                class="cta-primary"
                onclick="event.preventDefault(); alert('In the final version, this will open your personal portal. Demo mode — coming soon.');"
            >
                Begin Stage 0 — Free &rarr;
            </a>
        </div>
    </section>
    <!-- END OF SECTION 9: STAGE 0 PREVIEW -->
'''
    return html


if __name__ == "__main__":
    import os
    s0_html = generate_stage0_html()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, "..", "fragments", "fragment_10_stage0.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(s0_html)
    print(f"[MODULE 10] Stage 0 section generated!")
    print(f"[MODULE 10] Size: {len(s0_html)} characters")