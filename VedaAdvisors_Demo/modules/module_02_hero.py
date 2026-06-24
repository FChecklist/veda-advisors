"""
=============================================================================
MODULE 2: HERO SECTION (Section 1)
=============================================================================
GENERATES: fragments/fragment_02_hero.html

PURPOSE:
  The most important section — must stop the scroll.
  Full viewport height, dark background, Rajat Sir's image on right (desktop)
  or background layer (mobile). Text on the left.

CONTENT HIERARCHY (top to bottom):
  1. Small label: "STARTUP FUNDRAISING ADVISOR" (gold, uppercase)
  2. Main headline: "STOP CHASING INVESTORS. MAKE THEM CHASE YOU." (massive)
  3. Subline: About the 5-stage system and 400+ founders
  4. Provocative claim (gold, italic): About raising without MVP
  5. CTA button: "Find Out Why You're Not Getting Funded"
  6. Free/no-commitment text
  7. WhatsApp direct line
  8. Right side: Rajat Sir photo with credential badge overlay

DESIGN DECISIONS:
  - 100vh height to dominate the viewport
  - CSS-only diagonal pattern overlay (no external images needed)
  - Photo overlaps bottom of hero for editorial/premium feel
  - Gold glow around photo container
  - Credential badge overlaps the photo
  - Scroll indicator at bottom

IMAGE REFERENCES:
  - Primary: images/RAJAT Sir Image College.jpeg
  - Fallback: images/IMG_6215 (1).JPG

DEPENDENCIES: None (standalone fragment)
=============================================================================
"""

def generate_hero_html():
    """
    Generate the hero section HTML fragment.
    
    The hero is the single most important section for conversion.
    It must communicate:
    1. What this is (Startup Fundraising Advisory)
    2. The core promise (Stop Chasing, Make Them Chase You)
    3. Credibility (28 years, 400+ startups)
    4. A clear next action (CTA button)
    5. Personal connection (WhatsApp number, Rajat Sir photo)
    """
    
    html = '''
    <!-- ====================================================================
         SECTION 1: HERO
         ====================================================================
         WHY THIS IS THE MOST IMPORTANT SECTION:
         The hero has ONE job — stop the scroll. Every element is designed
         to create an emotional reaction: recognition of pain, curiosity
         about the system, and trust in Rajat Sir.

         LAYOUT STRATEGY:
         - Desktop: Two columns (60/40 split) — text left, photo right
         - Mobile: Single column — text first, photo below
         - Full viewport height (100vh) so it dominates the screen

         VISUAL ELEMENTS:
         - CSS-only diagonal grid pattern (no external images)
         - Gold accent line under label for visual hierarchy
         - Massive headline (72px desktop, 40px mobile) for impact
         - Rajat Sir photo with gold glow border (editorial feel)
         - Floating credential badge overlapping the photo
         - Animated scroll indicator at bottom

         CONTENT NOTES:
         - "STOP CHASING INVESTORS. MAKE THEM CHASE YOU." is the master 
           headline from the strategy document. Must appear exactly as-is.
         - The provocative claim about raising without MVP is from Section 2
           of the strategy doc. It challenges the founder's assumptions.
         - WhatsApp number (9650397480) is Rajat Sir's ONLY number.
         ==================================================================== -->
    <section id="hero" class="hero-section">
        
        <!-- CSS-ONLY DIAGONAL GRID PATTERN OVERLAY -->
        <!-- WHY: Creates visual texture without needing an external image.
             Repeating linear gradients at 45deg create a subtle grid
             that adds depth to the dark background. -->
        <div class="hero-pattern-overlay" aria-hidden="true"></div>

        <!-- HERO CONTAINER: Flex layout, 1200px max-width -->
        <div class="hero-container">
            
            <!-- ============================================================
                 LEFT SIDE: All text content
                 ============================================================
                 WHY LEFT: Western reading pattern (left-to-right) means
                 the eye lands on text first. The CTA is the goal, so
                 text gets the primary position.
                 ============================================================ -->
            <div class="hero-content">
                
                <!-- LABEL: Small caps, gold, letter-spacing -->
                <!-- WHY: Establishes the category immediately. "Startup
                     Fundraising Advisor" — NOT "Mentor" or "Coach".
                     This title is critical per the strategy document. -->
                <div class="hero-label">STARTUP FUNDRAISING ADVISOR</div>

                <!-- DECORATIVE GOLD LINE under label -->
                <!-- WHY: Creates visual separation between the label
                     and the headline. Adds a touch of premium branding. -->
                <div class="hero-label-line" aria-hidden="true"></div>

                <!-- MAIN HEADLINE: Massive, bold, white -->
                <!-- WHY: This is the #1 most important text on the entire
                     website. "STOP CHASING INVESTORS. MAKE THEM CHASE YOU."
                     It must be impossible to miss. 72px on desktop, 40px
                     on mobile. Weight 900 (black). Uppercase. -->
                <h1 class="hero-headline">
                    STOP CHASING<br>
                    <span class="hero-headline-accent">INVESTORS.</span><br>
                    MAKE THEM<br>
                    <span class="hero-headline-accent">CHASE YOU.</span>
                </h1>

                <!-- SUBLINE: Supporting text, muted color -->
                <!-- WHY: After the bold headline, the subline provides
                     context — mentions the system, 400+ founders, and
                     that this is built by someone who has done it. -->
                <p class="hero-subline">
                    A proven 5-stage system — built by someone<br class="hide-mobile">
                    who has done it and helped 400+ founders do it too.
                </p>

                <!-- PROVOCATIVE CLAIM: Gold colored, italic -->
                <!-- WHY: This challenges the founder's assumption that they
                     need a product/MVP/customers before raising. It's the
                     proprietary insight from Rajat Sir that nobody else says.
                     Creates cognitive dissonance → curiosity → engagement. -->
                <p class="hero-claim">
                    "You can raise funds without an MVP, without a product,
                    without customers — if you know the right investor."
                </p>

                <!-- PRIMARY CTA BUTTON -->
                <!-- WHY: The single most important interactive element on
                     the page. Must be gold (#C9A84C), large, with arrow.
                     Text: "Find Out Why You're Not Getting Funded →"
                     This wording creates urgency and personal relevance. -->
                <a 
                    href="#stage0" 
                    class="cta-primary hero-cta"
                    onclick="event.preventDefault(); alert('In the final version, this opens your personal portal where you complete Stage 0. Demo mode — coming soon.');"
                >
                    Find Out Why You're Not Getting Funded &rarr;
                </a>

                <!-- TRUST TEXT below CTA -->
                <!-- WHY: Reduces friction. Founders hesitate when they
                     think there's a catch. "Free. No credit card. No
                     commitment." removes all objections. -->
                <p class="hero-trust-text">Free. No credit card. No commitment.</p>

                <!-- WHATSAPP DIRECT LINE -->
                <!-- WHY: Some founders prefer WhatsApp over forms.
                     Giving the direct number builds trust — Rajat Sir
                     is accessible, not hidden behind a team. -->
                <div class="hero-whatsapp">
                    <a href="https://wa.me/919650397480" target="_blank" rel="noopener noreferrer">
                        &#128241; WhatsApp Rajat Sir directly: +91 9650397480
                    </a>
                </div>
            </div>

            <!-- ============================================================
                 RIGHT SIDE: Rajat Sir's Photo + Credential Badge
                 ============================================================
                 WHY: Rajat Sir IS the product. His face builds trust.
                 The photo must be large, commanding, and editorial.
                 - Gold glow border for premium feel
                 - Credential badge overlaps bottom of photo
                 - Photo slightly overlaps bottom of hero section
                 ============================================================ -->
            <div class="hero-image-wrapper">
                
                <!-- RAJAT SIR PHOTO -->
                <!-- IMAGE: RAJAT Sir Image College.jpeg (primary)
                     FALLBACK: IMG_6215 (1).JPG
                     WHY: College photo is more formal/commanding.
                     onerror switches to fallback if primary fails. -->
                <div class="hero-image-container">
                    <img 
                        src="images/RAJAT Sir Image College.jpeg"
                        alt="Rajat Sir — Startup Fundraising Advisor, TEDx Speaker, 28 Years Experience"
                        class="hero-image"
                        onerror="this.src='images/IMG_6215 (1).JPG';"
                    >
                    <!-- Gold glow border effect (pure CSS) -->
                    <!-- WHY: Creates a premium, editorial feel around the
                         photo. The gold color matches the brand palette. -->
                    <div class="hero-image-glow" aria-hidden="true"></div>
                </div>

                <!-- FLOATING CREDENTIAL BADGE -->
                <!-- WHY: Reinforces credibility without requiring the user
                     to scroll down to the numbers section. Positioned to
                     overlap the bottom of the photo for a layered effect. -->
                <div class="hero-credential-badge">
                    <div class="badge-item">&#127908; TEDx Speaker</div>
                    <div class="badge-item">28 Years Experience</div>
                    <div class="badge-item">400+ Startups Funded</div>
                </div>
            </div>
        </div>

        <!-- SCROLL INDICATOR at bottom of hero -->
        <!-- WHY: Tells users there's more content below. Animated
             bouncing arrow draws the eye downward. -->
        <div class="hero-scroll-indicator" aria-hidden="true">
            <div class="scroll-text">Scroll to discover</div>
            <div class="scroll-arrow">&#8595;</div>
        </div>
    </section>
    <!-- END OF SECTION 1: HERO -->
'''
    return html


if __name__ == "__main__":
    hero_html = generate_hero_html()
    output_path = "fragments/fragment_02_hero.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(hero_html)
    print(f"[MODULE 2] Hero section generated successfully!")
    print(f"[MODULE 2] Output: {output_path}")
    print(f"[MODULE 2] Size: {len(hero_html)} characters")