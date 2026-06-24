"""
=============================================================================
MODULE 8: WHO THIS IS FOR (Section 7) — Two Audience Cards
=============================================================================
GENERATES: fragments/fragment_08_audience.html

PURPOSE: Two cards — Startup Founders and Student Entrepreneurs.
  Each shows pain points (red X) and what changes (gold checkmark).
=============================================================================
"""

def generate_audience_html():
    """Generate the 'Is This For You?' section with two audience cards."""
    
    html = '''
    <!-- ====================================================================
         SECTION 7: WHO THIS IS FOR — Two Audience Cards
         ====================================================================
         WHY: Two distinct audiences from the strategy doc:
         1. Startup Founders — have a business, need capital
         2. Student Entrepreneurs — have an idea, want funding
         
         Same system. Same Rajat Sir. Same price. Different emotional entry.
         
         DESIGN: Each card shows pain (red X) → transformation (gold check).
         The red X items create recognition. The gold checks create hope.
         Gold divider separates pain from solution within each card.
         ==================================================================== -->
    <section id="audience" class="audience-section">
        <div class="container">
            <h2 class="section-headline">
                IS THIS <span class="gold-text">FOR YOU?</span>
            </h2>

            <div class="audience-grid">
                
                <!-- CARD 1: STARTUP FOUNDERS -->
                <!-- WHY: Primary audience. Have tried, failed, frustrated. -->
                <div class="audience-card">
                    <div class="audience-card-icon">&#128640;</div>
                    <h3 class="audience-card-title">STARTUP FOUNDERS</h3>
                    <p class="audience-card-sub">You have a business. You need capital.</p>
                    
                    <!-- PAIN POINTS (red X) -->
                    <!-- WHY: These mirror what founders are experiencing RIGHT NOW.
                         Recognition = engagement = conversion. -->
                    <div class="audience-pain-list">
                        <div class="audience-pain-item">
                            <span class="pain-x">&#10060;</span>
                            <span>Pitched investors. Got no response.</span>
                        </div>
                        <div class="audience-pain-item">
                            <span class="pain-x">&#10060;</span>
                            <span>Had meetings. Nothing moved.</span>
                        </div>
                        <div class="audience-pain-item">
                            <span class="pain-x">&#10060;</span>
                            <span>Don't know what you're doing wrong.</span>
                        </div>
                    </div>
                    
                    <!-- GOLD DIVIDER: separates pain from solution -->
                    <div class="audience-divider" aria-hidden="true"></div>
                    
                    <!-- WHAT CHANGES (gold check) -->
                    <!-- WHY: Shows the transformation. After pain, hope. -->
                    <div class="audience-solution-list">
                        <div class="audience-solution-item">
                            <span class="solution-check">&#9989;</span>
                            <span>Know exactly which 10 investors to approach</span>
                        </div>
                        <div class="audience-solution-item">
                            <span class="solution-check">&#9989;</span>
                            <span>Know exactly how to approach each one</span>
                        </div>
                        <div class="audience-solution-item">
                            <span class="solution-check">&#9989;</span>
                            <span>Have a Godfather Offer ready to close</span>
                        </div>
                    </div>
                    
                    <!-- AUDIENCE-SPECIFIC HEADLINE -->
                    <p class="audience-headline-italic">
                        "You've been pitching. Nothing has moved. Let's fix that."
                    </p>
                </div>

                <!-- CARD 2: STUDENT ENTREPRENEURS -->
                <!-- WHY: Secondary audience. Haven't tried yet — fear-based. -->
                <div class="audience-card">
                    <div class="audience-card-icon">&#127891;</div>
                    <h3 class="audience-card-title">STUDENT ENTREPRENEURS</h3>
                    <p class="audience-card-sub">You have an idea. You want funding.</p>
                    
                    <div class="audience-pain-list">
                        <div class="audience-pain-item">
                            <span class="pain-x">&#10060;</span>
                            <span>Investors don't take students seriously.</span>
                        </div>
                        <div class="audience-pain-item">
                            <span class="pain-x">&#10060;</span>
                            <span>Don't know where to start.</span>
                        </div>
                        <div class="audience-pain-item">
                            <span class="pain-x">&#10060;</span>
                            <span>Afraid to approach the wrong people.</span>
                        </div>
                    </div>
                    
                    <div class="audience-divider" aria-hidden="true"></div>
                    
                    <div class="audience-solution-list">
                        <div class="audience-solution-item">
                            <span class="solution-check">&#9989;</span>
                            <span>Understand how fundraising actually works</span>
                        </div>
                        <div class="audience-solution-item">
                            <span class="solution-check">&#9989;</span>
                            <span>Build your investor approach before you graduate</span>
                        </div>
                        <div class="audience-solution-item">
                            <span class="solution-check">&#9989;</span>
                            <span>Get a senior advisor who will listen — not dismiss</span>
                        </div>
                    </div>
                    
                    <p class="audience-headline-italic">
                        "Your idea deserves funding. Here's how to make investors take you seriously."
                    </p>
                </div>
            </div>
        </div>
    </section>
    <!-- END OF SECTION 7: WHO THIS IS FOR -->
'''
    return html


if __name__ == "__main__":
    import os
    aud_html = generate_audience_html()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, "..", "fragments", "fragment_08_audience.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(aud_html)
    print(f"[MODULE 8] Audience section generated!")
    print(f"[MODULE 8] Size: {len(aud_html)} characters")