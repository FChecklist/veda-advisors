"""
=============================================================================
MODULE 6: BSCVI 3.0 SYSTEM (Section 5) — The Journey Map
=============================================================================
GENERATES: fragments/fragment_06_bscvi.html

PURPOSE: The most important infographic — visual journey map with 6 stops.
  STOP 0 (FREE) → STOP 1 (IDENTIFY) → STOP 2 (APPROACH) →
  STOP 3 (OFFER) → STOP 4 (CLOSE) → STOP 5 (SUSTAIN)

DESIGN: Horizontal road on desktop, vertical on mobile.
  Gold dashed connecting line, numbered circles, badges.
=============================================================================
"""

def generate_bscvi_html():
    """Generate the BSCVI 3.0 System journey map."""
    
    # Journey stages data from Strategy Doc Section 3
    stages = [
        ("0", "READINESS", "Free Assessment", "FREE", 
         "Understand where your startup stands today", True),
        ("1", "IDENTIFY", "Find Your Investor", "Stage 1",
         "Build a list of 10 investors who will actually fund your specific business", False),
        ("2", "APPROACH", "Reach Your Investor", "Stage 2",
         "Write a personalised approach strategy for each of your 10 investors", False),
        ("3", "OFFER", "The Godfather Offer", "Stage 3",
         "Structure an offer the investor cannot refuse", False),
        ("4", "CLOSE", "Documentation & Deal", "Stage 4",
         "Navigate term sheets, negotiations, and close the deal correctly", False),
        ("5", "SUSTAIN", "Grow the Relationship", "Stage 5",
         "Manage investors, plan next round, build long-term relationships", False),
    ]
    
    stops_html = ""
    for num, name, sub, badge, desc, is_free in stages:
        # Free stage gets gold circle, others get dark green with gold border
        circle_class = "journey-stop-circle journey-stop-free" if is_free else "journey-stop-circle"
        badge_class = "journey-badge journey-badge-free" if is_free else "journey-badge"
        
        stops_html += f'''
                <!-- JOURNEY STOP {num}: {name} -->
                <!-- WHY: Each stop is one complete deliverable.
                     Stage 0 is FREE (gold circle) — the hook.
                     Other stages are locked/dark — creates curiosity. -->
                <div class="journey-stop" data-stage="{num}">
                    <div class="{circle_class}">{num}</div>
                    <div class="journey-stop-label">{name}</div>
                    <div class="journey-stop-sub">{sub}</div>
                    <div class="{badge_class}">{badge}</div>
                    <div class="journey-stop-desc">{desc}</div>
                </div>
'''
    
    html = f'''
    <!-- ====================================================================
         SECTION 5: THE BSCVI 3.0 SYSTEM — The Journey Map
         ====================================================================
         WHY: This is the CORE PRODUCT. The journey map must be visually
         stunning — it's what makes Veda Advisors unique.
         
         DESIGN: 
         - Horizontal on desktop (gold dashed line connecting 6 stops)
         - Vertical on mobile (stacked with line running down)
         - Stop 0 is gold (FREE) — stands out as the entry point
         - Other stops are dark with gold border — premium, locked feel
         - Connecting arrow line creates visual progression
         
         CONTENT: Each stop has: number, name, subtitle, badge, description.
         Maximum 5 words explanation per the "Less English. More Infographic"
         principle from the strategy document.
         ==================================================================== -->
    <section id="bscvi" class="bscvi-section">
        <div class="container">
            <h2 class="section-headline">
                THE <span class="gold-text">BSCVI 3.0</span> SYSTEM
            </h2>
            <p class="bscvi-subheadline">
                "Raising funds is High Stakes Negotiation.<br>
                And like any negotiation — it has a system."
            </p>

            <!-- JOURNEY MAP: Horizontal on desktop, vertical on mobile -->
            <div class="journey-map">
{stops_html}
                <!-- CONNECTING LINE (visual only, drawn via CSS) -->
                <div class="journey-line" aria-hidden="true"></div>
            </div>

            <!-- IMPORTANT NOTE below journey map -->
            <!-- WHY: Reassures founders that Stage 0 is free, they move
                 at their own pace, and each stage is 1-on-1 with Rajat Sir -->
            <div class="bscvi-note">
                <p>You start at Stage 0 — <span class="gold-text">free</span>. You move forward only when you are ready.</p>
                <p>Each stage is one-on-one with Rajat Sir. Your pace. Your journey.</p>
            </div>

            <!-- CTA: 3rd appearance of gold button -->
            <div class="bscvi-cta-wrapper">
                <a 
                    href="#stage0" 
                    class="cta-primary"
                    onclick="event.preventDefault(); alert('In the final version, this opens your personal portal where you complete Stage 0. Demo mode — coming soon.');"
                >
                    Start at Stage 0 — It's Free &rarr;
                </a>
            </div>
        </div>
    </section>
    <!-- END OF SECTION 5: BSCVI 3.0 SYSTEM -->
'''
    return html


if __name__ == "__main__":
    import os
    bscvi_html = generate_bscvi_html()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, "..", "fragments", "fragment_06_bscvi.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(bscvi_html)
    print(f"[MODULE 6] BSCVI section generated!")
    print(f"[MODULE 6] Size: {len(bscvi_html)} characters")