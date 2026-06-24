"""
=============================================================================
MODULE 1: NAVIGATION BAR (Section 0)
=============================================================================
GENERATES: fragments/fragment_01_nav.html

PURPOSE:
  Creates the fixed navigation bar that sits at the top of the page.
  - Fixed position, scrolls with page becoming slightly opaque via backdrop blur
  - Left side: Veda Advisors full logo
  - Right side: Single gold CTA button "Start Free Assessment"
  - Mobile: Hamburger menu with CTA always visible
  - Background: rgba(13, 43, 31, 0.95) with backdrop-filter: blur(10px)
  - Border bottom: 1px solid #2D4F3C
  - No other nav links — clean, minimal, one action only

DESIGN DECISIONS:
  - Fixed navbar is standard for conversion-focused landing pages
  - Single CTA reduces decision fatigue (conversion optimization principle)
  - Backdrop blur creates premium glass-morphism effect
  - Hamburger on mobile keeps layout clean on small screens
  - Z-index 1000 ensures navbar stays above all content

IMAGE REFERENCE:
  - Full logo: images/MAIN - Full Logo Veda full logo with Slate Teak BG.png
  - Short logo (mobile): images/MAIN - Short Logo Veda logo Slate Teak BG.png

DEPENDENCIES: None (standalone fragment)
=============================================================================
"""

def generate_nav_html():
    """
    Generate the navigation bar HTML fragment.
    
    Returns:
        str: Complete HTML string for the navigation bar section.
    
    The nav uses CSS Grid for layout on desktop and flexbox for mobile.
    The hamburger menu uses a checkbox hack for pure CSS toggling
    (no JavaScript required for mobile menu toggle).
    """

    # =========================================================================
    # NAVIGATION BAR HTML
    # =========================================================================
    # This is the complete navigation bar including:
    # 1. A label+checkbox for the mobile hamburger toggle (CSS-only approach)
    # 2. The nav container with logo on left, CTA on right
    # 3. Mobile slide-out menu
    # =========================================================================
    
    html = '''
    <!-- ====================================================================
         SECTION 0: NAVIGATION BAR
         ====================================================================
         WHY: The navbar is the first thing users see. It must be minimal,
         premium, and have exactly ONE call-to-action. No clutter, no links
         to nowhere. Just the brand and the action.

         DESIGN: Fixed position with backdrop blur for a glass-morphism
         effect. Gold CTA stands out against dark green background.
         On mobile, a hamburger menu reveals the CTA.

         IMAGES USED:
         - Desktop: Full logo (MAIN - Full Logo Veda full logo with Slate Teak BG.png)
         - Mobile: Short logo (MAIN - Short Logo Veda logo Slate Teak BG.png)
         ==================================================================== -->
    <nav id="main-nav" class="navbar">
        <!-- Container: max-width 1200px, centered with auto margins, padding for mobile -->
        <div class="nav-container">
            
            <!-- LEFT SIDE: Veda Advisors Logo -->
            <!-- WHY: Brand identity must be immediately visible. The logo 
                 appears on every screen the user visits. -->
            <!-- Using full logo on desktop, short logo on mobile (hidden via CSS) -->
            <a href="#" class="nav-logo" onclick="event.preventDefault();">
                <!-- Desktop logo: full version with background -->
                <img 
                    src="images/MAIN - Full Logo Veda full logo with Slate Teak BG.png" 
                    alt="Veda Advisors — Startup Fundraising Advisor" 
                    class="nav-logo-img nav-logo-desktop"
                    onerror="this.style.display='none'; document.getElementById('nav-logo-text').style.display='block';"
                >
                <!-- Mobile logo: shorter version for small screens -->
                <img 
                    src="images/MAIN - Short Logo Veda logo Slate Teak BG.png" 
                    alt="Veda Advisors" 
                    class="nav-logo-img nav-logo-mobile"
                    onerror="this.style.display='none';"
                >
                <!-- Fallback text logo if images fail to load -->
                <span id="nav-logo-text" class="nav-logo-fallback" style="display:none;">
                    VEDA<span class="gold-text">ADVISORS</span>
                </span>
            </a>

            <!-- RIGHT SIDE: Single CTA Button -->
            <!-- WHY: One action only. Conversion-focused design principle.
                 "Start Free Assessment" is the primary CTA used across the site.
                 Gold button on dark background creates maximum contrast. -->
            <a 
                href="#stage0" 
                class="nav-cta cta-primary"
                onclick="event.preventDefault(); alert('In the final version, this opens your personal portal where you complete Stage 0. Demo mode — coming soon.');"
            >
                Start Free Assessment
            </a>

            <!-- MOBILE HAMBURGER TOGGLE -->
            <!-- WHY: On mobile (<768px), the CTA button is hidden and
                 replaced by a hamburger menu that slides out a panel.
                 Uses checkbox hack for pure CSS toggle (no JS needed). -->
            <!-- Hidden checkbox that tracks hamburger state -->
            <input type="checkbox" id="nav-hamburger-check" class="nav-hamburger-check" aria-label="Toggle navigation menu">
            
            <!-- Hamburger icon (3 lines, becomes X when active via CSS) -->
            <label for="nav-hamburger-check" class="nav-hamburger" aria-label="Open menu">
                <span class="hamburger-line"></span>
                <span class="hamburger-line"></span>
                <span class="hamburger-line"></span>
            </label>

            <!-- MOBILE SLIDE-OUT MENU -->
            <!-- WHY: When hamburger is clicked, this panel slides in from right.
                 Contains the CTA button for mobile users. -->
            <div class="nav-mobile-menu">
                <!-- Mobile CTA: same as desktop but full-width on mobile -->
                <a 
                    href="#stage0" 
                    class="nav-mobile-cta cta-primary"
                    onclick="event.preventDefault(); alert('In the final version, this opens your personal portal where you complete Stage 0. Demo mode — coming soon.');"
                >
                    Start Free Assessment
                </a>
                <!-- WhatsApp link in mobile menu for quick access -->
                <a 
                    href="https://wa.me/919650397480" 
                    target="_blank" 
                    rel="noopener noreferrer"
                    class="nav-mobile-whatsapp"
                >
                    &#128241; WhatsApp Rajat Sir
                </a>
            </div>
        </div>
    </nav>
    <!-- END OF SECTION 0: NAVIGATION BAR -->
'''

    return html


# ==============================================================================
# MAIN EXECUTION
# ==============================================================================
# When this script is run directly, it generates the HTML fragment
# and saves it to the fragments/ directory.
# ==============================================================================
if __name__ == "__main__":
    # Generate the navigation HTML
    nav_html = generate_nav_html()
    
    # Save to fragments directory
    output_path = "fragments/fragment_01_nav.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(nav_html)
    
    # Print confirmation
    print(f"[MODULE 1] Navigation bar generated successfully!")
    print(f"[MODULE 1] Output: {output_path}")
    print(f"[MODULE 1] Size: {len(nav_html)} characters")