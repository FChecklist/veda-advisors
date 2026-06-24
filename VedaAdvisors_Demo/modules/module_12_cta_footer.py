"""
=============================================================================
MODULE 12: WHATSAPP CTA (Section 11) + FOOTER (Section 12)
=============================================================================
GENERATES: fragments/fragment_12_cta_footer.html

PURPOSE:
  Section 11: WhatsApp CTA section (mid-page, not the floating button)
  Section 12: Footer with 3 columns + bottom bar
  Also includes the floating WhatsApp button (fixed, bottom-right)
=============================================================================
"""

def generate_cta_footer_html():
    """Generate WhatsApp CTA section + Footer + Floating WhatsApp button."""
    
    html = '''
    <!-- ====================================================================
         SECTION 11: WHATSAPP CTA — Direct Access Section
         ====================================================================
         WHY: Some founders prefer a quick WhatsApp chat before committing
         to the assessment. This section gives them that option.
         
         DESIGN: Centered card (max-width 600px) with dark green background
         and gold border. Green WhatsApp button inside.
         
         NOTE: The floating WhatsApp button is separate (see end of file).
         ==================================================================== -->
    <section id="whatsapp-cta" class="whatsapp-section">
        <div class="container">
            <div class="whatsapp-card">
                <div class="whatsapp-icon-large">&#128241;</div>
                <h2 class="whatsapp-headline">DIRECT ACCESS TO RAJAT SIR</h2>
                <p class="whatsapp-body">
                    Have a quick question before you apply?<br>
                    WhatsApp me directly. I respond personally.
                </p>
                <!-- GREEN WHATSAPP BUTTON -->
                <!-- WHY: #25D366 is WhatsApp brand green. This button
                     is the only non-gold CTA on the page — by design.
                     WhatsApp has its own visual identity. -->
                <a 
                    href="https://wa.me/919650397480" 
                    target="_blank" 
                    rel="noopener noreferrer"
                    class="whatsapp-button"
                >
                    &#9742; WhatsApp Rajat Sir &rarr; +91 9650397480
                </a>
            </div>
        </div>
    </section>
    <!-- END OF SECTION 11: WHATSAPP CTA -->


    <!-- ====================================================================
         SECTION 12: FOOTER
         ====================================================================
         WHY: The footer has 3 jobs:
         1. Brand reinforcement (logo + tagline)
         2. Navigation placeholders (links for final version)
         3. Contact information (WhatsApp, email, location)
         
         BOTTOM BAR: "This is not a course. This is not coaching..."
         — Reinforces the positioning one last time before the user leaves.
         
         DESIGN: Darkest background (#080F0A — near black).
         3 columns on desktop, stacked on mobile.
         ==================================================================== -->
    <footer id="footer" class="footer">
        <div class="container">
            <div class="footer-grid">
                
                <!-- COLUMN 1: Logo + Tagline -->
                <!-- WHY: Brand reinforcement. The tagline "Stop Chasing
                     Investors. Make Them Chase You." is the master headline.
                     Seeing it again at the bottom reinforces the message. -->
                <div class="footer-col">
                    <img 
                        src="images/MAIN - Short Logo Veda logo Slate Teak BG.png" 
                        alt="Veda Advisors" 
                        class="footer-logo"
                        onerror="this.style.display='none'; document.getElementById('footer-logo-text').style.display='block';"
                    >
                    <span id="footer-logo-text" class="footer-logo-fallback" style="display:none;">
                        VEDA<span class="gold-text">ADVISORS</span>
                    </span>
                    <p class="footer-tagline">"Stop Chasing Investors. Make Them Chase You."</p>
                    <p class="footer-copyright">&copy; 2026 Veda Advisors. All rights reserved.</p>
                </div>

                <!-- COLUMN 2: Quick Links (placeholders) -->
                <!-- WHY: These links will be active in the final version.
                     In the demo, they show an alert. -->
                <div class="footer-col">
                    <h4 class="footer-col-title">Quick Links</h4>
                    <ul class="footer-links">
                        <li><a href="#" onclick="event.preventDefault(); alert('Navigation active in final version.');">For Startup Founders</a></li>
                        <li><a href="#" onclick="event.preventDefault(); alert('Navigation active in final version.');">For Student Entrepreneurs</a></li>
                        <li><a href="#" onclick="event.preventDefault(); alert('Navigation active in final version.');">The BSCVI 3.0 System</a></li>
                        <li><a href="#" onclick="event.preventDefault(); alert('Navigation active in final version.');">Apply to Work with Rajat Sir</a></li>
                    </ul>
                </div>

                <!-- COLUMN 3: Contact Information -->
                <!-- WHY: WhatsApp is the #1 contact method. Email is backup.
                     Location (New Delhi) adds legitimacy. The graphy.com URL
                     is the current platform (being replaced). -->
                <div class="footer-col">
                    <h4 class="footer-col-title">Contact</h4>
                    <div class="footer-contact-item">
                        <span>&#128241; WhatsApp:</span>
                        <a href="https://wa.me/919650397480" target="_blank" rel="noopener noreferrer">+91 9650397480</a>
                    </div>
                    <div class="footer-contact-item">
                        <span>&#9993; Email:</span>
                        <a href="mailto:rajatkamalagarwal@gmail.com">rajatkamalagarwal@gmail.com</a>
                    </div>
                    <div class="footer-contact-item">
                        <span>&#128205; Location:</span>
                        <span>New Delhi, India</span>
                    </div>
                    <div class="footer-contact-item">
                        <span>&#127760; Current Platform:</span>
                        <a href="https://vedaadvisors.graphy.com" target="_blank" rel="noopener noreferrer">vedaadvisors.graphy.com</a>
                    </div>
                </div>
            </div>

            <!-- BOTTOM BAR: Positioning statement -->
            <!-- WHY: Last impression. Reinforces that this is NOT a course
                 or coaching platform. It's a system with a senior advisor.
                 This one line differentiates Veda Advisors from everything
                 else in the market. -->
            <div class="footer-bottom-bar">
                <p>This is not a course. This is not coaching. This is a system — with a senior advisor available to you every step of the way.</p>
            </div>
        </div>
    </footer>
    <!-- END OF SECTION 12: FOOTER -->


    <!-- ====================================================================
         FLOATING WHATSAPP BUTTON (Fixed, bottom-right, always visible)
         ====================================================================
         WHY: WhatsApp is Rajat Sir's primary contact channel.
         A floating button ensures it's always accessible regardless
         of where the user has scrolled to.
         
         DESIGN: Round green button (#25D366), bottom-right corner.
         Tooltip on hover: "Chat with Rajat Sir".
         Z-index 999 (below navbar at 1000).
         ==================================================================== -->
    <a 
        href="https://wa.me/919650397480" 
        target="_blank" 
        rel="noopener noreferrer"
        class="floating-whatsapp"
        aria-label="Chat with Rajat Sir on WhatsApp"
        title="Chat with Rajat Sir"
    >
        <!-- WhatsApp icon using Unicode/SVG -->
        <svg class="whatsapp-svg" viewBox="0 0 32 32" fill="white" width="28" height="28">
            <path d="M16.004 0h-.008C7.174 0 0 7.176 0 16c0 3.5 1.132 6.744 3.054 9.378L1.054 31.29l6.168-1.96A15.9 15.9 0 0016.004 32C24.826 32 32 24.822 32 16S24.826 0 16.004 0zm9.314 22.61c-.39 1.1-1.932 2.014-3.168 2.28-.846.18-1.95.324-5.66-1.216-4.748-1.97-7.806-6.81-8.042-7.126-.226-.316-1.888-2.514-1.888-4.8s1.196-3.41 1.62-3.876c.424-.466.926-.584 1.236-.584.31 0 .62.002.89.016.286.016.67-.108 1.048.8.39.932 1.332 3.25 1.45 3.486.118.236.196.512.04.826-.158.316-.236.512-.472.788-.236.276-.498.616-.71.826-.238.236-.484.492-.208.966.276.474 1.226 2.024 2.632 3.278 1.808 1.612 3.332 2.112 3.806 2.348.474.236.75.196 1.026-.118.276-.316 1.194-1.392 1.512-1.87.316-.478.632-.396 1.066-.238.434.158 2.744 1.294 3.214 1.53.47.236.782.354.9.55.118.196.118 1.122-.272 2.222z"/>
        </svg>
        <!-- Tooltip: appears on hover via CSS -->
        <span class="floating-whatsapp-tooltip">Chat with Rajat Sir</span>
    </a>
    <!-- END OF FLOATING WHATSAPP BUTTON -->
'''
    return html


if __name__ == "__main__":
    import os
    cta_footer_html = generate_cta_footer_html()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, "..", "fragments", "fragment_12_cta_footer.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(cta_footer_html)
    print(f"[MODULE 12] CTA + Footer section generated!")
    print(f"[MODULE 12] Size: {len(cta_footer_html)} characters")