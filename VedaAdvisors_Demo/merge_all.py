"""
=============================================================================
MERGE SCRIPT: Combines all 12 module fragments + CSS + JS into index.html
=============================================================================
OUTPUT: /home/z/my-project/VedaAdvisors_Demo/index.html

This script:
  1. Reads all 12 HTML fragments from the fragments/ directory
  2. Generates the COMPLETE CSS (design system from build prompt)
  3. Generates the JavaScript (scroll animations, counter, intersection observer)
  4. Assembles everything into one self-contained index.html
  5. Writes extensive comments throughout for reference

The CSS follows the EXACT design system from the build prompt:
  - Primary Background: #0D2B1F
  - Secondary Background: #1B3A2D
  - Accent Gold: #C9A84C
  - Text Primary: #FFFFFF
  - Font: Inter (400, 600, 700, 800, 900)
  - Mobile-first responsive design
  - Animations: fade-in on scroll, number counter, CTA pulse
=============================================================================
"""

import os

# ==============================================================================
# PATHS
# ==============================================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRAGMENTS_DIR = os.path.join(BASE_DIR, "fragments")
OUTPUT_PATH = os.path.join(BASE_DIR, "index.html")

# Fragment files in order
FRAGMENT_FILES = [
    "fragment_01_nav.html",       # Section 0: Navigation Bar
    "fragment_02_hero.html",      # Section 1: Hero
    "fragment_03_pain.html",      # Section 2: The Pain
    "fragment_04_numbers.html",   # Section 3: The Numbers
    "fragment_05_proof.html",     # Section 4: Proof Stories
    "fragment_06_bscvi.html",     # Section 5: BSCVI 3.0
    "fragment_07_rajat.html",     # Section 6: Rajat Sir
    "fragment_08_audience.html",  # Section 7: Who This Is For
    "fragment_09_filter.html",    # Section 8: The Filter
    "fragment_10_stage0.html",    # Section 9: Stage 0 Preview
    "fragment_11_global.html",    # Section 10: Global Reach
    "fragment_12_cta_footer.html" # Section 11+12: WhatsApp CTA + Footer
]


def generate_complete_css():
    """
    Generate the COMPLETE CSS for the entire website.
    
    This CSS implements the EXACT design system from the build prompt:
    - Color palette: dark green + gold + white
    - Typography: Inter font with specific weights
    - Spacing: 120px sections (desktop), 60px (mobile)
    - Responsive: 768px breakpoint for mobile
    - Animations: fade-in, counter, pulse
    - All component styles for every section
    """
    return '''
    /* ====================================================================
       COMPLETE CSS — VEDA ADVISORS DEMO WEBSITE
       ====================================================================
       DESIGN SYSTEM (from Build Prompt):
       - Primary BG: #0D2B1F (very dark green)
       - Secondary BG: #1B3A2D (dark green for cards)
       - Accent Gold: #C9A84C (CTAs, highlights, numbers)
       - Gold Light: #E8C96A (hover states)
       - Text Primary: #FFFFFF
       - Text Secondary: #B8C9BF (muted green-white)
       - Text Muted: #7A9E8A (labels, captions)
       - Border: #2D4F3C (subtle dark green)
       - Danger: #E05252 (wrong indicators)
       
       TYPOGRAPHY:
       - Font: Inter, fallback to Arial
       - H1: 72px/40px mobile, weight 900
       - H2: 48px/32px mobile, weight 800
       - Body: 18px/16px mobile, weight 400, line-height 1.7
       
       SPACING:
       - Section padding: 120px/60px mobile
       - Container max-width: 1200px
       - Card padding: 40px/24px mobile
       - Grid gap: 32px/16px mobile
       ==================================================================== */

    /* ====================================================================
       RESET & BASE STYLES
       ====================================================================
       WHY: CSS reset ensures consistent rendering across browsers.
       Box-sizing border-box makes padding behave predictably.
       Smooth scroll enables anchor link navigation.
       ==================================================================== */
    *, *::before, *::after {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    html {
        scroll-behavior: smooth; /* WHY: All anchor links smooth-scroll */
        font-size: 16px;
    }

    body {
        /* WHY: #0D2B1F is the primary background — very dark green,
             almost black-green. No white backgrounds anywhere. */
        background-color: #0D2B1F;
        color: #FFFFFF;
        font-family: 'Inter', 'Helvetica Neue', Arial, sans-serif;
        font-weight: 400;
        line-height: 1.7;
        overflow-x: hidden; /* Prevents horizontal scroll from animations */
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
    }

    /* Hide elements on mobile */
    .hide-mobile {
        display: block;
    }

    img {
        max-width: 100%;
        height: auto;
        display: block;
    }

    a {
        text-decoration: none;
        color: inherit;
        transition: color 0.3s ease;
    }

    /* ====================================================================
       UTILITY CLASSES
       ==================================================================== */
    .gold-text {
        color: #C9A84C; /* WHY: Gold is used ONLY for headlines, CTAs,
                           numbers, borders — not for body text */
    }

    .container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 24px; /* WHY: 24px side padding on mobile */
    }

    .section-headline {
        font-size: 48px;
        font-weight: 800;
        line-height: 1.1;
        text-align: center;
        margin-bottom: 16px;
        letter-spacing: -0.5px;
    }

    .section-subheadline {
        font-size: 18px;
        color: #B8C9BF;
        text-align: center;
        margin-bottom: 48px;
    }

    /* ====================================================================
       CTA BUTTON STYLES (from Build Prompt)
       ====================================================================
       WHY: The CTA button is the #1 conversion element. It must be:
       - Gold (#C9A84C) background
       - Dark text (#0D2B1F)
       - Large padding (18px 40px)
       - Bold (700 weight)
       - Subtle pulse animation
       - Hover: lighter gold (#E8C96A)
       ==================================================================== */
    .cta-primary {
        display: inline-block;
        background: #C9A84C;
        color: #0D2B1F;
        padding: 18px 40px;
        font-size: 18px;
        font-weight: 700;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        letter-spacing: 0.3px;
        /* Pulse animation — draws eye to the button */
        animation: cta-pulse 2.5s infinite;
    }

    .cta-primary:hover {
        background: #E8C96A;
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(201, 168, 76, 0.3);
    }

    /* CTA Pulse Animation — subtle gold glow */
    @keyframes cta-pulse {
        0% { box-shadow: 0 0 0 0 rgba(201, 168, 76, 0.4); }
        70% { box-shadow: 0 0 0 15px rgba(201, 168, 76, 0); }
        100% { box-shadow: 0 0 0 0 rgba(201, 168, 76, 0); }
    }

    /* ====================================================================
       NAVIGATION BAR (Section 0)
       ==================================================================== */
    .navbar {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        background: rgba(13, 43, 31, 0.95);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-bottom: 1px solid #2D4F3C;
        transition: all 0.3s ease;
    }

    .nav-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 24px;
        height: 72px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .nav-logo {
        display: flex;
        align-items: center;
    }

    .nav-logo-img {
        height: 48px;
        width: auto;
        object-fit: contain;
    }

    .nav-logo-desktop { display: block; }
    .nav-logo-mobile { display: none; }

    .nav-logo-fallback {
        font-size: 24px;
        font-weight: 800;
        letter-spacing: 1px;
    }

    .nav-cta {
        padding: 12px 28px;
        font-size: 15px;
    }

    /* Hamburger — hidden on desktop */
    .nav-hamburger-check { display: none; }
    .nav-hamburger {
        display: none; /* Shown on mobile */
    }
    .nav-mobile-menu { display: none; }

    /* ====================================================================
       HERO SECTION (Section 1)
       ====================================================================
       WHY: 100vh dominates the viewport. Two-column layout on desktop.
       CSS-only diagonal pattern creates visual texture.
       ==================================================================== */
    .hero-section {
        min-height: 100vh;
        display: flex;
        align-items: center;
        position: relative;
        padding-top: 72px; /* Account for fixed navbar */
        overflow: hidden;
    }

    /* CSS-ONLY DIAGONAL PATTERN OVERLAY */
    .hero-pattern-overlay {
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background:
            repeating-linear-gradient(
                45deg,
                transparent,
                transparent 40px,
                rgba(45, 79, 60, 0.08) 40px,
                rgba(45, 79, 60, 0.08) 41px
            ),
            repeating-linear-gradient(
                -45deg,
                transparent,
                transparent 40px,
                rgba(45, 79, 60, 0.08) 40px,
                rgba(45, 79, 60, 0.08) 41px
            );
        pointer-events: none;
        z-index: 0;
    }

    .hero-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 24px;
        display: grid;
        grid-template-columns: 1fr 0.85fr;
        gap: 48px;
        align-items: center;
        position: relative;
        z-index: 1;
    }

    .hero-content {
        padding: 40px 0;
    }

    .hero-label {
        font-size: 14px;
        font-weight: 600;
        color: #C9A84C;
        text-transform: uppercase;
        letter-spacing: 3px;
        margin-bottom: 16px;
    }

    .hero-label-line {
        width: 60px;
        height: 3px;
        background: #C9A84C;
        margin-bottom: 32px;
        border-radius: 2px;
    }

    .hero-headline {
        font-size: 72px;
        font-weight: 900;
        line-height: 1.0;
        letter-spacing: -1px;
        margin-bottom: 24px;
    }

    .hero-headline-accent {
        color: #C9A84C;
    }

    .hero-subline {
        font-size: 18px;
        color: #B8C9BF;
        line-height: 1.7;
        margin-bottom: 24px;
    }

    .hero-claim {
        font-size: 17px;
        color: #C9A84C;
        font-style: italic;
        margin-bottom: 32px;
        border-left: 3px solid #C9A84C;
        padding-left: 20px;
    }

    .hero-cta {
        margin-bottom: 12px;
    }

    .hero-trust-text {
        font-size: 14px;
        color: #7A9E8A;
        margin-bottom: 24px;
    }

    .hero-whatsapp a {
        font-size: 15px;
        color: #B8C9BF;
        transition: color 0.3s;
    }
    .hero-whatsapp a:hover { color: #C9A84C; }

    /* HERO IMAGE — Right side */
    .hero-image-wrapper {
        position: relative;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .hero-image-container {
        position: relative;
        border-radius: 16px;
        overflow: hidden;
    }

    .hero-image {
        width: 100%;
        max-width: 440px;
        height: 560px;
        object-fit: cover;
        border-radius: 16px;
    }

    .hero-image-glow {
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        border-radius: 16px;
        box-shadow: 0 0 40px rgba(201, 168, 76, 0.15), inset 0 0 40px rgba(201, 168, 76, 0.05);
        border: 2px solid rgba(201, 168, 76, 0.3);
        pointer-events: none;
    }

    .hero-credential-badge {
        position: absolute;
        bottom: -20px;
        left: 20px;
        right: 20px;
        background: rgba(13, 43, 31, 0.95);
        border: 1px solid #C9A84C;
        border-radius: 12px;
        padding: 16px 20px;
        backdrop-filter: blur(10px);
    }

    .badge-item {
        font-size: 14px;
        font-weight: 600;
        color: #FFFFFF;
        padding: 4px 0;
    }

    /* SCROLL INDICATOR */
    .hero-scroll-indicator {
        position: absolute;
        bottom: 32px;
        left: 50%;
        transform: translateX(-50%);
        text-align: center;
    }

    .scroll-text {
        font-size: 12px;
        color: #7A9E8A;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 8px;
    }

    .scroll-arrow {
        font-size: 24px;
        color: #C9A84C;
        animation: scroll-bounce 2s infinite;
    }

    @keyframes scroll-bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(8px); }
        60% { transform: translateY(4px); }
    }

    /* ====================================================================
       PAIN SECTION (Section 2)
       ==================================================================== */
    .pain-section {
        padding: 120px 0;
        background: #0D2B1F;
    }

    .pain-subheadline {
        font-size: 20px;
        color: #C9A84C;
        font-style: italic;
        text-align: center;
        margin-bottom: 48px;
    }

    .pain-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 24px;
        max-width: 900px;
        margin: 0 auto 48px;
    }

    .pain-card {
        background: #1B3A2D;
        border-left: 4px solid #E05252;
        border-radius: 12px;
        padding: 32px;
        box-shadow: 0 4px 24px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
    }

    .pain-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 32px rgba(0,0,0,0.4);
    }

    .pain-card-icon {
        font-size: 48px;
        margin-bottom: 16px;
    }

    .pain-card-title {
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 8px;
        color: #FFFFFF;
    }

    .pain-card-body {
        font-size: 15px;
        color: #B8C9BF;
        line-height: 1.6;
    }

    .pain-statement {
        text-align: center;
        max-width: 700px;
        margin: 0 auto;
        padding: 32px;
        border-top: 1px solid #2D4F3C;
    }

    .pain-statement-text {
        font-size: 24px;
        font-weight: 600;
        line-height: 1.4;
        color: #FFFFFF;
    }

    .pain-statement-author {
        font-size: 16px;
        color: #C9A84C;
        margin-top: 12px;
    }

    /* ====================================================================
       NUMBERS SECTION (Section 3)
       ====================================================================
       WHY: Darker background (#111F17) creates visual separation.
       Gold 96px numbers for impact. Vertical dividers between stats.
       ==================================================================== */
    .numbers-section {
        padding: 120px 0;
        background: #111F17;
    }

    .numbers-grid {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 0;
        text-align: center;
        position: relative;
        max-width: 900px;
        margin: 0 auto 48px;
    }

    /* Vertical gold dividers between stats */
    .numbers-grid > .stat-item:not(:last-child)::after {
        content: '';
        position: absolute;
        right: 0;
        top: 10%;
        height: 80%;
        width: 1px;
        background: rgba(201, 168, 76, 0.3);
    }

    .stat-item {
        position: relative;
        padding: 24px;
    }

    .stat-number {
        font-size: 96px;
        font-weight: 900;
        color: #C9A84C;
        line-height: 1;
        margin-bottom: 8px;
    }

    .stat-label {
        font-size: 16px;
        font-weight: 600;
        color: #FFFFFF;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 8px;
    }

    .stat-desc {
        font-size: 14px;
        color: #7A9E8A;
    }

    .numbers-cta-wrapper {
        text-align: center;
    }

    .numbers-tribe-text {
        font-size: 18px;
        color: #B8C9BF;
        font-style: italic;
        margin-bottom: 24px;
    }

    /* ====================================================================
       PROOF STORIES SECTION (Section 4)
       ==================================================================== */
    .proof-section {
        padding: 120px 0;
        background: #0D2B1F;
    }

    .proof-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 32px;
        max-width: 900px;
        margin: 0 auto 48px;
    }

    .proof-card {
        background: #1B3A2D;
        border-top: 4px solid #C9A84C;
        border-radius: 12px;
        padding: 32px;
        box-shadow: 0 4px 24px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
    }

    .proof-card:hover {
        transform: translateY(-4px);
    }

    .proof-badge {
        display: inline-block;
        background: rgba(201, 168, 76, 0.15);
        color: #C9A84C;
        font-size: 12px;
        font-weight: 600;
        padding: 4px 12px;
        border-radius: 4px;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 16px;
    }

    .proof-startup-name {
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 12px;
    }

    .proof-amount {
        font-size: 48px;
        font-weight: 900;
        color: #C9A84C;
        line-height: 1.1;
        margin-bottom: 4px;
    }

    .proof-amount-usd {
        font-size: 16px;
        color: #7A9E8A;
        margin-bottom: 16px;
    }

    .proof-founder {
        font-size: 16px;
        color: #B8C9BF;
        margin-bottom: 16px;
    }

    .proof-quote {
        font-size: 15px;
        color: #B8C9BF;
        font-style: italic;
        border-top: 1px solid #2D4F3C;
        padding-top: 16px;
        line-height: 1.6;
    }

    .proof-closing {
        text-align: center;
        font-size: 18px;
        color: #B8C9BF;
        font-style: italic;
    }

    /* ====================================================================
       BSCVI 3.0 SYSTEM SECTION (Section 5)
       ====================================================================
       WHY: The journey map is horizontal on desktop with a gold dashed
       connecting line. Each stop is a numbered circle.
       ==================================================================== */
    .bscvi-section {
        padding: 120px 0;
        background: #111F17;
    }

    .bscvi-subheadline {
        font-size: 20px;
        color: #C9A84C;
        font-style: italic;
        text-align: center;
        margin-bottom: 60px;
    }

    .journey-map {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        position: relative;
        max-width: 1100px;
        margin: 0 auto 40px;
        padding: 0 20px;
    }

    /* Gold dashed connecting line */
    .journey-line {
        position: absolute;
        top: 30px;
        left: 50px;
        right: 50px;
        height: 2px;
        background: repeating-linear-gradient(
            90deg,
            #C9A84C,
            #C9A84C 8px,
            transparent 8px,
            transparent 16px
        );
        z-index: 0;
    }

    .journey-stop {
        flex: 1;
        text-align: center;
        position: relative;
        z-index: 1;
        padding: 0 8px;
    }

    .journey-stop-circle {
        width: 60px;
        height: 60px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        font-weight: 900;
        margin: 0 auto 16px;
        background: #1B3A2D;
        border: 3px solid #C9A84C;
        color: #FFFFFF;
        transition: all 0.3s ease;
    }

    .journey-stop-free {
        background: #C9A84C;
        color: #0D2B1F;
        box-shadow: 0 0 20px rgba(201, 168, 76, 0.3);
    }

    .journey-stop-label {
        font-size: 16px;
        font-weight: 700;
        color: #FFFFFF;
        margin-bottom: 4px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .journey-stop-sub {
        font-size: 13px;
        color: #B8C9BF;
        margin-bottom: 8px;
    }

    .journey-badge {
        display: inline-block;
        background: rgba(45, 79, 60, 0.5);
        color: #7A9E8A;
        font-size: 11px;
        font-weight: 600;
        padding: 2px 10px;
        border-radius: 4px;
        margin-bottom: 12px;
    }

    .journey-badge-free {
        background: rgba(201, 168, 76, 0.2);
        color: #C9A84C;
    }

    .journey-stop-desc {
        font-size: 13px;
        color: #7A9E8A;
        line-height: 1.5;
        max-width: 150px;
        margin: 0 auto;
    }

    .bscvi-note {
        text-align: center;
        margin-bottom: 32px;
    }

    .bscvi-note p {
        font-size: 16px;
        color: #B8C9BF;
        margin-bottom: 4px;
    }

    .bscvi-cta-wrapper {
        text-align: center;
    }

    /* ====================================================================
       RAJAT SIR SECTION (Section 6)
       ==================================================================== */
    .rajat-section {
        padding: 120px 0;
        background: #0D2B1F;
    }

    .rajat-grid {
        display: grid;
        grid-template-columns: 0.9fr 1.1fr;
        gap: 48px;
        align-items: start;
    }

    .rajat-photo-wrapper {
        position: relative;
        border-radius: 16px;
        overflow: hidden;
    }

    .rajat-photo {
        width: 100%;
        height: 500px;
        object-fit: cover;
        border-radius: 16px;
    }

    .rajat-photo-glow {
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        border-radius: 16px;
        border: 2px solid rgba(201, 168, 76, 0.3);
        box-shadow: 0 0 30px rgba(201, 168, 76, 0.1);
        pointer-events: none;
    }

    .rajat-photo-credential-strip {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        background: rgba(13, 43, 31, 0.9);
        padding: 12px 20px;
        font-size: 13px;
        color: #B8C9BF;
        text-align: center;
        letter-spacing: 1px;
    }

    .rajat-content {
        padding-top: 16px;
    }

    .rajat-label {
        font-size: 14px;
        font-weight: 600;
        color: #C9A84C;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 16px;
    }

    .rajat-headline {
        font-size: 48px;
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 24px;
    }

    .rajat-paragraph p {
        font-size: 16px;
        color: #B8C9BF;
        margin-bottom: 12px;
        line-height: 1.7;
    }

    .confidentiality-box {
        background: rgba(201, 168, 76, 0.05);
        border: 2px solid #C9A84C;
        border-radius: 12px;
        padding: 24px;
        margin: 32px 0;
        text-align: center;
    }

    .confidentiality-icon {
        font-size: 32px;
        margin-bottom: 8px;
    }

    .confidentiality-text {
        font-size: 18px;
        font-weight: 600;
        color: #FFFFFF;
    }

    .confidentiality-author {
        font-size: 14px;
        color: #C9A84C;
        margin-top: 8px;
    }

    .rajat-badges-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 12px;
        margin-bottom: 32px;
    }

    .rajat-badge {
        background: #1B3A2D;
        border: 1px solid #2D4F3C;
        border-radius: 8px;
        padding: 16px;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .badge-icon {
        font-size: 24px;
    }

    .badge-text {
        font-size: 13px;
        color: #B8C9BF;
        font-weight: 500;
    }

    .rajat-cta-subtext {
        font-size: 14px;
        color: #7A9E8A;
        margin-top: 12px;
    }

    /* ====================================================================
       AUDIENCE SECTION (Section 7)
       ==================================================================== */
    .audience-section {
        padding: 120px 0;
        background: #111F17;
    }

    .audience-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 32px;
        max-width: 900px;
        margin: 0 auto;
    }

    .audience-card {
        background: #1B3A2D;
        border-radius: 12px;
        padding: 40px;
        box-shadow: 0 4px 24px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
    }

    .audience-card:hover {
        transform: translateY(-4px);
    }

    .audience-card-icon {
        font-size: 48px;
        margin-bottom: 16px;
    }

    .audience-card-title {
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 4px;
    }

    .audience-card-sub {
        font-size: 15px;
        color: #7A9E8A;
        margin-bottom: 24px;
    }

    .audience-pain-list {
        margin-bottom: 16px;
    }

    .audience-pain-item {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 8px 0;
        font-size: 15px;
        color: #B8C9BF;
    }

    .pain-x { font-size: 16px; flex-shrink: 0; }

    .audience-divider {
        height: 1px;
        background: #C9A84C;
        margin: 20px 0;
        opacity: 0.5;
    }

    .audience-solution-list {
        margin-bottom: 20px;
    }

    .audience-solution-item {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 8px 0;
        font-size: 15px;
        color: #FFFFFF;
    }

    .solution-check { color: #C9A84C; font-size: 16px; flex-shrink: 0; }

    .audience-headline-italic {
        font-size: 16px;
        color: #C9A84C;
        font-style: italic;
        border-top: 1px solid #2D4F3C;
        padding-top: 16px;
        line-height: 1.5;
    }

    /* ====================================================================
       FILTER SECTION (Section 8)
       ====================================================================
       WHY: Even darker background (#0A1A10), centered, max-width 700px.
       Creates intimate, serious, exclusive tone.
       ==================================================================== */
    .filter-section {
        padding: 120px 0;
        background: #0A1A10;
    }

    .filter-content {
        max-width: 700px;
        margin: 0 auto;
        text-align: center;
    }

    .filter-quote-mark {
        font-size: 120px;
        color: #C9A84C;
        line-height: 0.6;
        opacity: 0.3;
        margin-bottom: 16px;
    }

    .filter-headline {
        font-size: 48px;
        font-weight: 800;
        margin-bottom: 24px;
    }

    .filter-body {
        font-size: 18px;
        color: #B8C9BF;
        margin-bottom: 8px;
    }

    .filter-body-emphasis {
        font-size: 20px;
        color: #B8C9BF;
        margin-bottom: 40px;
    }

    .filter-checklist, .filter-antilist {
        text-align: left;
        margin-bottom: 32px;
    }

    .filter-list-title {
        font-size: 16px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 16px;
    }

    .filter-check-item, .filter-anti-item {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 8px 0;
        font-size: 16px;
        color: #B8C9BF;
    }

    .filter-check-icon { font-size: 18px; font-weight: 700; flex-shrink: 0; }
    .filter-anti-icon { font-size: 16px; flex-shrink: 0; }

    .filter-cta-subtext {
        font-size: 14px;
        color: #7A9E8A;
        margin-top: 16px;
    }

    /* ====================================================================
       STAGE 0 PREVIEW SECTION (Section 9)
       ==================================================================== */
    .stage0-section {
        padding: 120px 0;
        background: #0D2B1F;
    }

    .stage0-form-card {
        max-width: 600px;
        margin: 0 auto 32px;
        background: #1B3A2D;
        border: 1px solid #2D4F3C;
        border-radius: 16px;
        padding: 32px;
        box-shadow: 0 4px 24px rgba(0,0,0,0.3);
    }

    .stage0-progress {
        position: relative;
        height: 6px;
        background: #2D4F3C;
        border-radius: 3px;
        margin-bottom: 32px;
        overflow: hidden;
    }

    .stage0-progress-bar {
        height: 100%;
        background: #C9A84C;
        border-radius: 3px;
        transition: width 0.3s;
    }

    .stage0-progress-text {
        position: absolute;
        right: 0;
        top: -24px;
        font-size: 13px;
        color: #7A9E8A;
    }

    .stage0-questions {
        display: flex;
        flex-direction: column;
        gap: 12px;
    }

    .stage0-question {
        background: #0D2B1F;
        border-radius: 8px;
        padding: 20px;
        border: 1px solid #2D4F3C;
    }

    .stage0-question-active {
        border-color: #C9A84C;
    }

    .stage0-question-number {
        font-size: 12px;
        font-weight: 700;
        color: #C9A84C;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 8px;
    }

    .stage0-question-text {
        font-size: 16px;
        color: #FFFFFF;
        margin-bottom: 12px;
        font-weight: 500;
    }

    .stage0-input {
        width: 100%;
        background: #1B3A2D;
        border: 1px solid #2D4F3C;
        border-radius: 6px;
        padding: 12px 16px;
        color: #FFFFFF;
        font-size: 15px;
        font-family: inherit;
        outline: none;
        transition: border-color 0.3s;
    }

    .stage0-input:focus {
        border-color: #C9A84C;
    }

    .stage0-question-locked {
        opacity: 0.4;
        cursor: not-allowed;
    }

    .stage0-question-blur {
        font-size: 18px;
        color: #7A9E8A;
        letter-spacing: 4px;
    }

    .stage0-locked-label {
        font-size: 12px;
        color: #7A9E8A;
        margin-top: 4px;
    }

    .stage0-teaser-text {
        text-align: center;
        font-size: 16px;
        color: #B8C9BF;
        margin-bottom: 32px;
    }

    .stage0-process-steps {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 16px;
        margin-bottom: 32px;
        flex-wrap: wrap;
    }

    .process-step {
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .process-step-number {
        width: 32px;
        height: 32px;
        border-radius: 50%;
        background: #C9A84C;
        color: #0D2B1F;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        font-size: 14px;
        flex-shrink: 0;
    }

    .process-step-text {
        font-size: 14px;
        color: #B8C9BF;
        font-weight: 500;
    }

    .process-step-arrow {
        color: #C9A84C;
        font-size: 20px;
    }

    /* ====================================================================
       GLOBAL REACH SECTION (Section 10)
       ==================================================================== */
    .global-section {
        padding: 120px 0;
        background: #111F17;
    }

    .global-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 24px;
        max-width: 800px;
        margin: 0 auto 32px;
    }

    .global-card {
        background: #1B3A2D;
        border: 1px solid #2D4F3C;
        border-radius: 12px;
        padding: 24px;
        text-align: center;
        transition: all 0.3s ease;
    }

    .global-card:hover {
        transform: translateY(-4px);
        border-color: #C9A84C;
    }

    .global-flag {
        font-size: 40px;
        margin-bottom: 12px;
    }

    .global-region {
        font-size: 15px;
        font-weight: 700;
        color: #FFFFFF;
        margin-bottom: 4px;
    }

    .global-status {
        font-size: 13px;
        color: #7A9E8A;
    }

    .global-language-note {
        text-align: center;
        font-size: 15px;
        color: #7A9E8A;
    }

    /* ====================================================================
       WHATSAPP CTA SECTION (Section 11)
       ==================================================================== */
    .whatsapp-section {
        padding: 80px 0;
        background: #0D2B1F;
    }

    .whatsapp-card {
        max-width: 600px;
        margin: 0 auto;
        background: #1B3A2D;
        border: 2px solid #C9A84C;
        border-radius: 16px;
        padding: 48px 40px;
        text-align: center;
    }

    .whatsapp-icon-large {
        font-size: 48px;
        margin-bottom: 16px;
    }

    .whatsapp-headline {
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 12px;
    }

    .whatsapp-body {
        font-size: 16px;
        color: #B8C9BF;
        margin-bottom: 24px;
        line-height: 1.6;
    }

    .whatsapp-button {
        display: inline-block;
        background: #25D366;
        color: white;
        padding: 16px 32px;
        border-radius: 8px;
        font-size: 16px;
        font-weight: 600;
        transition: all 0.3s ease;
    }

    .whatsapp-button:hover {
        background: #20BA5A;
        transform: translateY(-2px);
    }

    /* ====================================================================
       FOOTER (Section 12)
       ====================================================================
       WHY: Darkest background (#080F0A — near black). 3 columns.
       Bottom bar reinforces positioning one last time.
       ==================================================================== */
    .footer {
        padding: 80px 0 0;
        background: #080F0A;
        border-top: 1px solid #2D4F3C;
    }

    .footer-grid {
        display: grid;
        grid-template-columns: 1.2fr 1fr 1fr;
        gap: 48px;
        padding-bottom: 48px;
    }

    .footer-logo {
        height: 40px;
        width: auto;
        object-fit: contain;
        margin-bottom: 12px;
    }

    .footer-logo-fallback {
        font-size: 20px;
        font-weight: 800;
    }

    .footer-tagline {
        font-size: 15px;
        color: #B8C9BF;
        font-style: italic;
        margin-bottom: 8px;
    }

    .footer-copyright {
        font-size: 13px;
        color: #7A9E8A;
    }

    .footer-col-title {
        font-size: 16px;
        font-weight: 700;
        margin-bottom: 16px;
        color: #FFFFFF;
    }

    .footer-links {
        list-style: none;
    }

    .footer-links li {
        margin-bottom: 10px;
    }

    .footer-links a {
        font-size: 14px;
        color: #B8C9BF;
        transition: color 0.3s;
    }

    .footer-links a:hover {
        color: #C9A84C;
    }

    .footer-contact-item {
        display: flex;
        flex-direction: column;
        margin-bottom: 12px;
        font-size: 14px;
        color: #B8C9BF;
    }

    .footer-contact-item a {
        color: #C9A84C;
        font-weight: 500;
    }

    .footer-contact-item a:hover {
        color: #E8C96A;
    }

    .footer-bottom-bar {
        border-top: 1px solid #2D4F3C;
        padding: 24px 0;
        text-align: center;
    }

    .footer-bottom-bar p {
        font-size: 14px;
        color: #7A9E8A;
        font-style: italic;
        max-width: 700px;
        margin: 0 auto;
    }

    /* ====================================================================
       FLOATING WHATSAPP BUTTON
       ====================================================================
       WHY: Always accessible regardless of scroll position.
       Bottom-right corner. Round green button with SVG icon.
       Tooltip on hover.
       ==================================================================== */
    .floating-whatsapp {
        position: fixed;
        bottom: 24px;
        right: 24px;
        width: 56px;
        height: 56px;
        background: #25D366;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 999;
        box-shadow: 0 4px 16px rgba(37, 211, 102, 0.4);
        transition: all 0.3s ease;
    }

    .floating-whatsapp:hover {
        transform: scale(1.1);
        box-shadow: 0 6px 24px rgba(37, 211, 102, 0.5);
    }

    .floating-whatsapp-tooltip {
        position: absolute;
        right: 68px;
        background: #0D2B1F;
        color: #FFFFFF;
        padding: 8px 16px;
        border-radius: 6px;
        font-size: 13px;
        white-space: nowrap;
        opacity: 0;
        pointer-events: none;
        transition: opacity 0.3s;
        border: 1px solid #2D4F3C;
    }

    .floating-whatsapp:hover .floating-whatsapp-tooltip {
        opacity: 1;
    }

    .whatsapp-svg {
        flex-shrink: 0;
    }

    /* ====================================================================
       FADE-IN ON SCROLL ANIMATION
       ====================================================================
       WHY: Elements fade in as the user scrolls to them.
       Uses Intersection Observer (JS below). Elements start invisible
       and become visible when they enter the viewport.
       ==================================================================== */
    .fade-in {
        opacity: 0;
        transform: translateY(20px);
        transition: opacity 0.6s ease, transform 0.6s ease;
    }

    .fade-in.visible {
        opacity: 1;
        transform: translateY(0);
    }

    /* ====================================================================
       MOBILE RESPONSIVE STYLES (< 768px)
       ====================================================================
       WHY: "Mobile first — global audience scrolls on phone."
       All grids become single column. Font sizes reduce.
       Navigation becomes hamburger. CTA buttons full width.
       ==================================================================== */
    @media (max-width: 768px) {
        .hide-mobile { display: none; }

        .section-headline { font-size: 32px; }
        .section-subheadline { font-size: 16px; margin-bottom: 32px; }

        /* NAV MOBILE */
        .nav-cta { display: none; }
        .nav-hamburger {
            display: flex;
            flex-direction: column;
            gap: 5px;
            cursor: pointer;
            padding: 8px;
            z-index: 1001;
        }
        .hamburger-line {
            width: 24px;
            height: 2px;
            background: #FFFFFF;
            transition: all 0.3s ease;
            border-radius: 1px;
        }
        .nav-hamburger-check:checked ~ .nav-mobile-menu {
            display: flex;
            flex-direction: column;
            gap: 16px;
            padding: 24px;
        }
        .nav-mobile-menu {
            position: fixed;
            top: 72px;
            left: 0;
            right: 0;
            background: rgba(13, 43, 31, 0.98);
            backdrop-filter: blur(10px);
            padding: 0 24px;
            border-bottom: 1px solid #2D4F3C;
            z-index: 999;
        }
        .nav-mobile-cta { 
            display: block; 
            text-align: center; 
            width: 100%;
            animation: none;
        }
        .nav-mobile-whatsapp {
            display: block;
            text-align: center;
            padding: 12px;
            color: #25D366;
            font-size: 15px;
            border: 1px solid #25D366;
            border-radius: 8px;
        }

        /* HERO MOBILE */
        .hero-container {
            grid-template-columns: 1fr;
            gap: 32px;
            padding-top: 24px;
            padding-bottom: 24px;
        }
        .hero-headline { font-size: 40px; }
        .hero-image { max-width: 320px; height: 400px; }
        .hero-credential-badge {
            position: relative;
            bottom: auto; left: auto; right: auto;
            margin-top: 16px;
        }

        /* PAIN MOBILE */
        .pain-section { padding: 60px 0; }
        .pain-grid { grid-template-columns: 1fr; }

        /* NUMBERS MOBILE */
        .numbers-section { padding: 60px 0; }
        .numbers-grid {
            grid-template-columns: 1fr;
            gap: 32px;
        }
        .numbers-grid > .stat-item:not(:last-child)::after {
            display: none;
        }
        .stat-number { font-size: 56px; }

        /* PROOF MOBILE */
        .proof-section { padding: 60px 0; }
        .proof-grid { grid-template-columns: 1fr; }
        .proof-amount { font-size: 36px; }

        /* BSCVI MOBILE — vertical stack */
        .bscvi-section { padding: 60px 0; }
        .journey-map {
            flex-direction: column;
            align-items: center;
            gap: 24px;
        }
        .journey-line {
            top: 30px;
            bottom: 30px;
            left: 50%;
            right: auto;
            width: 2px;
            height: auto;
            background: repeating-linear-gradient(
                180deg,
                #C9A84C,
                #C9A84C 8px,
                transparent 8px,
                transparent 16px
            );
        }

        /* RAJAT SIR MOBILE */
        .rajat-section { padding: 60px 0; }
        .rajat-grid { grid-template-columns: 1fr; }
        .rajat-photo { height: 350px; }
        .rajat-headline { font-size: 32px; }

        /* AUDIENCE MOBILE */
        .audience-section { padding: 60px 0; }
        .audience-grid { grid-template-columns: 1fr; }

        /* FILTER MOBILE */
        .filter-section { padding: 60px 0; }
        .filter-headline { font-size: 32px; }

        /* STAGE 0 MOBILE */
        .stage0-section { padding: 60px 0; }
        .stage0-process-steps { flex-direction: column; gap: 12px; }
        .process-step-arrow { transform: rotate(90deg); }

        /* GLOBAL MOBILE */
        .global-section { padding: 60px 0; }
        .global-grid { grid-template-columns: 1fr 1fr; }

        /* FOOTER MOBILE */
        .footer-grid { grid-template-columns: 1fr; gap: 32px; }
        .cta-primary { 
            display: block; 
            text-align: center; 
            width: 100%;
            animation: none;
        }
    }

    /* Extra small screens (< 400px) */
    @media (max-width: 400px) {
        .hero-headline { font-size: 34px; }
        .global-grid { grid-template-columns: 1fr; }
        .rajat-badges-grid { grid-template-columns: 1fr; }
    }
'''


def generate_javascript():
    """
    Generate the JavaScript for the website.
    
    Three JS features (all vanilla, no libraries):
    1. Intersection Observer — fade-in on scroll
    2. Number counter animation — stats count up from 0
    3. Navbar scroll effect (optional enhancement)
    """
    return '''
    /* ====================================================================
       JAVASCRIPT — VEDA ADVISORS DEMO WEBSITE
       ====================================================================
       Three features only (all vanilla JS, no libraries):
       1. Intersection Observer — fade-in elements on scroll
       2. Number Counter — animate stats from 0 to target value
       3. Smooth scroll for anchor links (backup for older browsers)
       ==================================================================== */

    // Wait for DOM to be ready
    document.addEventListener("DOMContentLoaded", function() {

        // ==================================================================
        // 1. FADE-IN ON SCROLL (Intersection Observer)
        // ==================================================================
        // WHY: Elements with class "fade-in" start invisible (opacity: 0).
        // When they enter the viewport, the "visible" class is added,
        // triggering a CSS transition (opacity + translateY).
        // This creates a premium, subtle animation without any JS library.
        // ==================================================================
        var fadeElements = document.querySelectorAll(
            ".pain-card, .proof-card, .journey-stop, .audience-card, " +
            ".rajat-photo-wrapper, .rajat-content, .filter-content, " +
            ".stage0-form-card, .global-card, .whatsapp-card, " +
            ".stat-item, .hero-content, .hero-image-wrapper, .pain-statement"
        );

        // Add fade-in class to all target elements
        fadeElements.forEach(function(el) {
            el.classList.add("fade-in");
        });

        // Intersection Observer: watches elements and adds "visible" class
        // when they enter the viewport (with 10% threshold)
        var observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add("visible");
                    // Once visible, stop observing (no need to re-animate)
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.1,    // Trigger when 10% of element is visible
            rootMargin: "0px 0px -40px 0px"  // Slight offset for better timing
        });

        // Observe each element
        fadeElements.forEach(function(el) {
            observer.observe(el);
        });


        // ==================================================================
        // 2. NUMBER COUNTER ANIMATION
        // ==================================================================
        // WHY: Stats (400+, 600+, 28) count up from 0 when the numbers
        // section enters the viewport. Creates visual interest and
        // draws attention to the credibility numbers.
        // ==================================================================
        var statNumbers = document.querySelectorAll(".stat-number[data-target]");
        var counterObserver = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    // Start counter animation
                    animateCounter(entry.target);
                    counterObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.3 });

        statNumbers.forEach(function(el) {
            counterObserver.observe(el);
        });

        /**
         * Animate a number from 0 to target value.
         * @param {HTMLElement} element - The stat-number element
         * Uses requestAnimationFrame for smooth 60fps animation.
         * Duration: 2 seconds. Easing: ease-out.
         */
        function animateCounter(element) {
            var target = parseInt(element.getAttribute("data-target"));
            var hasPlus = element.textContent.includes("+");
            var duration = 2000; // 2 seconds
            var startTime = null;

            function step(timestamp) {
                if (!startTime) startTime = timestamp;
                var progress = Math.min((timestamp - startTime) / duration, 1);
                // Ease-out cubic: fast start, slow end
                var eased = 1 - Math.pow(1 - progress, 3);
                var current = Math.floor(eased * target);
                element.textContent = current + (hasPlus ? "+" : "");
                if (progress < 1) {
                    requestAnimationFrame(step);
                } else {
                    element.textContent = target + (hasPlus ? "+" : "");
                }
            }

            requestAnimationFrame(step);
        }


        // ==================================================================
        // 3. MOBILE NAVIGATION: Close menu when a link is clicked
        // ==================================================================
        // WHY: On mobile, after clicking a CTA in the hamburger menu,
        // the menu should close automatically.
        // ==================================================================
        var mobileMenuLinks = document.querySelectorAll(".nav-mobile-menu a");
        var hamburgerCheck = document.getElementById("nav-hamburger-check");
        
        mobileMenuLinks.forEach(function(link) {
            link.addEventListener("click", function() {
                if (hamburgerCheck) {
                    hamburgerCheck.checked = false;
                }
            });
        });

    }); // END DOMContentLoaded
'''


def merge_all():
    """
    Main merge function:
    1. Reads all 12 HTML fragments
    2. Wraps them in complete HTML structure with CSS and JS
    3. Writes the final index.html
    """
    
    # Read all fragments
    fragments_content = []
    for i, filename in enumerate(FRAGMENT_FILES, 1):
        filepath = os.path.join(FRAGMENTS_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        fragments_content.append(content)
        print(f"  [MERGE] Read fragment {i}/12: {filename} ({len(content)} chars)")
    
    # Combine all fragment HTML
    all_sections_html = "\n".join(fragments_content)
    
    # Generate CSS and JS
    css = generate_complete_css()
    js = generate_javascript()
    
    # Assemble the complete HTML document
    complete_html = f'''<!DOCTYPE html>
<!--
============================================================================
VEDA ADVISORS — COMPLETE DEMO WEBSITE
============================================================================
FILE: index.html
VERSION: 1.0 | June 2026
CREATED BY: Python module-based generation system (12 modules)

WHAT THIS IS:
  A single self-contained HTML file that works on any laptop.
  No internet required for layout. No server needed.
  Just double-click and open in any browser.

HOW IT WAS BUILT:
  - 12 Python modules (modules/module_01_nav.py through module_12_cta_footer.py)
  - Each module generates an HTML fragment saved to fragments/
  - This merge script (merge_all.py) combines all fragments with CSS + JS
  - Every section has extensive comments explaining WHY decisions were made

DESIGN SYSTEM:
  - Primary Background: #0D2B1F (very dark green)
  - Secondary Background: #1B3A2D (dark green cards)
  - Accent Gold: #C9A84C (CTAs, highlights, numbers)
  - Text: #FFFFFF (primary), #B8C9BF (secondary), #7A9E8A (muted)
  - Font: Inter (400, 600, 700, 800, 900)
  - Mobile-first responsive at 768px breakpoint

SECTIONS (in order):
  Section 0:  Navigation Bar (fixed, glass-morphism)
  Section 1:  Hero (100vh, Rajat Sir photo, master headline)
  Section 2:  The Pain (4 reason cards, red borders)
  Section 3:  The Numbers (400+, 600+, 28 years — gold stats)
  Section 4:  Proof Stories (UElement ₹15Cr, ARC Electric ₹3Cr)
  Section 5:  BSCVI 3.0 System (journey map, 6 stops)
  Section 6:  Rajat Sir (personal section, confidentiality promise)
  Section 7:  Who This Is For (founders + students)
  Section 8:  The Filter (exclusive, checklist + anti-checklist)
  Section 9:  Stage 0 Preview (form teaser, Q1 visible)
  Section 10: Global Reach (India, UAE, SE Asia, UK)
  Section 11: WhatsApp CTA (direct access section)
  Section 12: Footer (3 columns + bottom bar)

IMAGES EXPECTED (in images/ folder):
  - MAIN - Full Logo Veda full logo with Slate Teak BG.png
  - MAIN - Short Logo Veda logo Slate Teak BG.png
  - RAJAT Sir Image College.jpeg
  - IMG_6215 (1).JPG
  - IMG_6287.JPG

CONTACT: rajatkamalagarwal@gmail.com | WhatsApp: +91 9650397480
============================================================================
-->
<html lang="en">
<head>
    <!-- ====================================================================
         META TAGS
         ====================================================================
         WHY: viewport for responsive, charset for special characters,
         description for SEO (even in demo), title for browser tab.
         ==================================================================== -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Veda Advisors — Stop Chasing Investors. Make Them Chase You. Startup Fundraising Advisory by Rajat Sir with a proven 5-stage system. 400+ startups funded.">
    <title>Veda Advisors — Startup Fundraising Advisor | Rajat Sir</title>
    
    <!-- FAVICON (short logo) -->
    <link rel="icon" type="image/png" href="images/MAIN - Short Logo Veda logo Slate Teak BG.png">

    <!-- ====================================================================
         GOOGLE FONTS: Inter
         ====================================================================
         WHY: Inter is the specified font from the design system.
         Weights: 400 (body), 600 (captions), 700 (titles), 800 (headlines), 900 (hero).
         Falls back to Arial if offline (per build prompt).
         ==================================================================== -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap" rel="stylesheet">

    <!-- ====================================================================
         COMPLETE STYLESHEET
         ====================================================================
         All CSS is inline (in this <style> tag) so the file is self-contained.
         Every CSS rule has a comment explaining its purpose.
         ==================================================================== -->
    <style>
{css}
    </style>
</head>
<body>

    <!-- ====================================================================
         ALL SECTIONS — Merged from 12 module fragments
         ====================================================================
         Each section below was generated by a separate Python module:
         module_01_nav.py → fragment_01_nav.html (Section 0: Nav)
         module_02_hero.py → fragment_02_hero.html (Section 1: Hero)
         module_03_pain.py → fragment_03_pain.html (Section 2: Pain)
         module_04_numbers.py → fragment_04_numbers.html (Section 3: Numbers)
         module_05_proof.py → fragment_05_proof.html (Section 4: Proof)
         module_06_bscvi.py → fragment_06_bscvi.html (Section 5: BSCVI)
         module_07_rajat.py → fragment_07_rajat.html (Section 6: Rajat Sir)
         module_08_audience.py → fragment_08_audience.html (Section 7: Audience)
         module_09_filter.py → fragment_09_filter.html (Section 8: Filter)
         module_10_stage0.py → fragment_10_stage0.html (Section 9: Stage 0)
         module_12_global.py → fragment_11_global.html (Section 10: Global)
         module_12_cta_footer.py → fragment_12_cta_footer.html (Section 11+12)
         ==================================================================== -->

{all_sections_html}

    <!-- ====================================================================
         JAVASCRIPT
         ====================================================================
         Three features (all vanilla JS, no external libraries):
         1. Intersection Observer — fade-in elements on scroll
         2. Number counter — animate stats from 0 to target
         3. Mobile nav close on link click
         ==================================================================== -->
    <script>
{js}
    </script>

</body>
</html>
'''

    # Write the complete HTML file
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(complete_html)
    
    print(f"\n{'='*60}")
    print(f"[MERGE COMPLETE] index.html generated successfully!")
    print(f"[OUTPUT] {OUTPUT_PATH}")
    print(f"[SIZE] {len(complete_html):,} characters ({len(complete_html)//1024} KB)")
    print(f"[FRAGMENTS] 12 modules merged")
    print(f"[CSS] {len(css):,} characters")
    print(f"[JS] {len(js):,} characters")
    print(f"{'='*60}")


if __name__ == "__main__":
    merge_all()