"""
=============================================================================
MODULE 5: PROOF STORIES SECTION (Section 4)
=============================================================================
GENERATES: fragments/fragment_05_proof.html

PURPOSE: Two case study cards — Chaitanya (UElement, ₹15Cr) and Abhinav (ARC Electric, ₹3Cr)
=============================================================================
"""

def generate_proof_html():
    """Generate the two proof/case study cards."""
    
    # Case study data from Strategy Doc Section 6
    case_studies = [
        {
            "badge": "CASE STUDY #1",
            "startup": "UElement",
            "amount_inr": "&#8377;15 CRORE RAISED",
            "amount_usd": "(~$1.8 Million)",
            "founder": "Chaitanya",
            "quote": "Working with Rajat Sir changed how we approached every investor conversation. — Chaitanya, Founder, UElement"
        },
        {
            "badge": "CASE STUDY #2",
            "startup": "ARC Electric",
            "amount_inr": "&#8377;3 CRORE RAISED",
            "amount_usd": "(~$360,000)",
            "founder": "Abhinav",
            "quote": "The BSCVI 3.0 system gave us clarity we never had before. We knew exactly who to call. — Abhinav, Founder, ARC Electric"
        }
    ]
    
    cards_html = ""
    for cs in case_studies:
        cards_html += f'''
                <!-- {cs['badge']}: {cs['startup']} -->
                <div class="proof-card">
                    <div class="proof-badge">{cs['badge']}</div>
                    <h3 class="proof-startup-name">{cs['startup']}</h3>
                    <div class="proof-amount">{cs['amount_inr']}</div>
                    <div class="proof-amount-usd">{cs['amount_usd']}</div>
                    <div class="proof-founder">&#128100; {cs['founder']}</div>
                    <p class="proof-quote">"{cs['quote'].split(' — ')[0]}" — {cs['founder']}, Founder, {cs['startup']}</p>
                </div>
'''
    
    html = f'''
    <!-- ====================================================================
         SECTION 4: PROOF STORIES — Founders Who Did It
         ====================================================================
         WHY: Social proof is the #2 conversion driver (after pain recognition).
         Two real founders. Real money raised. Specific amounts.
         Format: Name · Startup · Amount · One line quote.
         Short. Specific. Real.
         ==================================================================== -->
    <section id="proof" class="proof-section">
        <div class="container">
            <h2 class="section-headline">
                FOUNDERS WHO<br>
                <span class="gold-text">DID IT</span>
            </h2>
            <p class="section-subheadline">Real founders. Real investors. Real money raised.</p>
            
            <div class="proof-grid">
{cards_html}
            </div>
            
            <!-- CLOSING LINE: These are not exceptions -->
            <p class="proof-closing">"These are not exceptions. This is what the system does."</p>
        </div>
    </section>
    <!-- END OF SECTION 4: PROOF STORIES -->
'''
    return html


if __name__ == "__main__":
    import os
    proof_html = generate_proof_html()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, "..", "fragments", "fragment_05_proof.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(proof_html)
    print(f"[MODULE 5] Proof section generated!")
    print(f"[MODULE 5] Size: {len(proof_html)} characters")