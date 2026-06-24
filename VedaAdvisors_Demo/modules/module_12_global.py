"""
=============================================================================
MODULE 11: GLOBAL REACH (Section 10) — Simple Infographic
=============================================================================
GENERATES: fragments/fragment_11_global.html

PURPOSE: 4 region cards showing global presence.
  India, UAE & Middle East, Southeast Asia, United Kingdom.
=============================================================================
"""

def generate_global_html():
    """Generate the global reach section."""
    
    # Region data from Strategy Doc Section 14
    regions = [
        ("&#127470;&#127475;", "India", "Accepting applications"),
        ("&#127462;&#127466;", "UAE & Middle East", "Accepting applications"),
        ("&#127480;&#127468;", "Southeast Asia", "Accepting applications"),
        ("&#127468;&#127463;", "United Kingdom", "Accepting applications"),
    ]
    
    cards_html = ""
    for flag, name, status in regions:
        cards_html += f'''
                <div class="global-card">
                    <div class="global-flag">{flag}</div>
                    <div class="global-region">{name}</div>
                    <div class="global-status">{status}</div>
                </div>
'''
    
    html = f'''
    <!-- ====================================================================
         SECTION 10: GLOBAL REACH — Global Advisory, Personal Attention
         ====================================================================
         WHY: The strategy document emphasizes this is NOT just an Indian
         coaching platform. It's a global advisory. These 4 regions are
         the priority markets (Section 14): UAE, Southeast Asia, UK, India.
         
         DESIGN: 4 simple cards with flags, region names, and status.
         Clean, minimal. No clutter.
         ==================================================================== -->
    <section id="global" class="global-section">
        <div class="container">
            <h2 class="section-headline">
                GLOBAL ADVISORY.<br>
                <span class="gold-text">PERSONAL ATTENTION.</span>
            </h2>
            <p class="section-subheadline">Rajat Sir works with founders from across the world.</p>

            <div class="global-grid">
{cards_html}
            </div>

            <!-- LANGUAGE NOTE -->
            <!-- WHY: Clarifies that sessions are in English and all
                 time zones are accommodated. Removes a common objection
                 for international founders. -->
            <p class="global-language-note">
                All sessions are in English. All time zones accommodated.
            </p>
        </div>
    </section>
    <!-- END OF SECTION 10: GLOBAL REACH -->
'''
    return html


if __name__ == "__main__":
    import os
    global_html = generate_global_html()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, "..", "fragments", "fragment_11_global.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(global_html)
    print(f"[MODULE 11] Global section generated!")
    print(f"[MODULE 11] Size: {len(global_html)} characters")