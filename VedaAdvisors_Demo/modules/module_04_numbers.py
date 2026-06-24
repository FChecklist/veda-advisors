"""
=============================================================================
MODULE 4: THE NUMBERS SECTION (Section 3)
=============================================================================
GENERATES: fragments/fragment_04_numbers.html

PURPOSE: Pure infographic — 3 large stats, no sentences.
  - 400+ STARTUPS FUNDED
  - 600+ FOUNDERS MENTORED  
  - 28 YEARS EXPERIENCE

DESIGN: Darker background (#111F17), gold 96px numbers, vertical dividers.
=============================================================================
"""

def generate_numbers_html():
    """Generate the stats/numbers infographic section."""
    
    # Stats data: (number, label, description)
    stats = [
        ("400+", "STARTUPS FUNDED", "Raised funds using this system"),
        ("600+", "FOUNDERS MENTORED", "From idea to investor meetings"),
        ("28", "YEARS EXPERIENCE", "In high stakes deals & negotiations")
    ]
    
    # Build stats HTML
    stats_html = ""
    for i, (num, label, desc) in enumerate(stats):
        stats_html += f'''
                <!-- STAT {i+1}: {label} -->
                <!-- WHY: Large gold numbers create instant credibility.
                     These are from the strategy document Section 1.
                     The counter animation (JS) will count up from 0. -->
                <div class="stat-item">
                    <div class="stat-number" data-target="{num.replace('+', '')}">{num}</div>
                    <div class="stat-label">{label}</div>
                    <div class="stat-desc">{desc}</div>
                </div>
'''
    
    html = f'''
    <!-- ====================================================================
         SECTION 3: THE NUMBERS — Pure Infographic
         ====================================================================
         WHY: Numbers build credibility faster than words. Three stats,
         each with a giant gold number. No paragraphs. Just impact.
         
         DESIGN: Darker background (#111F17) creates visual separation
         from the pain section above. Gold dividers between stats.
         Counter animation (JS in merge script) counts up from 0.
         ==================================================================== -->
    <section id="numbers" class="numbers-section">
        <div class="container">
            <div class="numbers-grid">
{stats_html}
            </div>
            
            <!-- TRIBE LINE + CTA -->
            <!-- WHY: "Join the tribe" creates belonging. The CTA here
                 is the 2nd appearance of the gold button on the page. -->
            <div class="numbers-cta-wrapper">
                <p class="numbers-tribe-text">"Join the tribe. Your startup could be next."</p>
                <a 
                    href="#stage0" 
                    class="cta-primary"
                    onclick="event.preventDefault(); alert('In the final version, this opens your personal portal where you complete Stage 0. Demo mode — coming soon.');"
                >
                    Start Free Assessment &rarr;
                </a>
            </div>
        </div>
    </section>
    <!-- END OF SECTION 3: THE NUMBERS -->
'''
    return html


if __name__ == "__main__":
    import os
    num_html = generate_numbers_html()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, "..", "fragments", "fragment_04_numbers.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(num_html)
    print(f"[MODULE 4] Numbers section generated!")
    print(f"[MODULE 4] Output: {output_path}")
    print(f"[MODULE 4] Size: {len(num_html)} characters")