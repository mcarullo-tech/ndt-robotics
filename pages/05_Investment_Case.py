"""Investment Case: Why robotics transforms AU-E into an attractive opportunity."""

import streamlit as st
from utils import set_page, add_footer

set_page()

st.title("🎯 The Investment Case: Why This Matters")
st.markdown("*A pragmatic path to transforming AU-E into a high-margin, defensible platform*")
st.divider()

st.markdown(
    """
    ## Executive Summary
    
    **The Problem:** Manual AU-E is hitting a growth ceiling — labor-constrained, data-inconsistent, and visibly outdated.
    
    **The Opportunity:** A two-stage robotics investment ($450K total) transforms AU-E from a commodity service 
    into a premium, scalable platform generating 3x+ revenue and 4x+ EBITDA by Year 3.
    
    **The Investment:** 
    - **Stage 1** ($100K, 6 mo) → immediate operational gains, validates demand
    - **Stage 2** ($300K, 12-18 mo) → market leadership, 70%+ throughput uplift
    
    **The Returns:** NPV of $1.2M+ over 5 years, payback in Year 2-3, strategic asset for exit or scale.
    
    ---
    """
)

st.subheader("✅ Why This Is Compelling")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        ### 📈 Market Dynamics
        
        **Tailwinds:**
        - Enterprise clients demand automation
        - AU-E is a stable, growing NDT segment
        - Robotics cost curve improving 15-20% annually
        - First-mover can establish the standard
        
        **No major disruption risk:**
        - AU-E is mature, proven technology
        - Not competing with emerging tech
        - Clear customer base & pricing power
        """
    )

with col2:
    st.markdown(
        """
        ### 💰 Unit Economics
        
        **Baseline (Manual):**
        - 12 jobs/year @ $120K = $1.44M revenue
        - Margin: 67% → $960K EBITDA
        - Growth: Flat/declining
        
        **Robotics (Year 3+):**
        - 30 jobs/year @ $150K = $4.5M revenue
        - Margin: 83% → $3.7M EBITDA
        - ROI on $450K: **8-10x in 5 years**
        """
    )

with col3:
    st.markdown(
        """
        ### 🛡️ De-Risking
        
        **Two-stage approach:**
        - Stage 1 validates market demand
        - Stage 1 ROI funds most of Stage 2
        - Proven robotics tech (not R&D)
        - Existing customer relationships
        
        **Exit optionality:**
        - Attractive to industrial OEMs
        - Appealing to NDT consolidators
        - Self-funding by Year 3
        """
    )

st.divider()

st.subheader("📋 Investment Thesis: Five Key Points")

with st.expander("1️⃣ Market Timing — The Inflection Is Now", expanded=True):
    st.markdown(
        """
        - Enterprise manufacturers increasingly specify robotic inspection systems
        - AU-E is proving its ROI in aerospace, automotive, and renewables
        - Current competitors are slow to automate — first-mover advantage is real
        - Tech cost curve for industrial robotics + vision systems is favorable
        
        **We are at the moment when automation becomes table-stakes in AU-E.**
        """
    )

with st.expander("2️⃣ Pragmatic Execution — Not a Moonshot"):
    st.markdown(
        """
        - Stage 1 uses proven electromechanical impact technology (off-the-shelf, <$100K)
        - Stage 2 integrates proven industrial robotics (Kuka, ABB, Fanuc)
        - No fundamental R&D risk — integration and application development
        - Team has experience in AU-E, robotics, and manufacturing
        
        **We're not inventing new technology—we're applying proven tech to a new market.**
        """
    )

with st.expander("3️⃣ Financial Efficiency — Capital Works Hard"):
    st.markdown(
        """
        - $100K Stage 1 investment breaks even in 18 months
        - Stage 1 cash generation partially funds Stage 2
        - Total $450K investment generates $1.2M+ NPV in 5 years
        - Payback achieved by Year 3, with significant upside after
        
        **This is disciplined capital deployment with clear ROI milestones.**
        """
    )

with st.expander("4️⃣ Competitive Moat — First Wins the Market"):
    st.markdown(
        """
        - First automated AU-E platform establishes reference customers
        - Software/data analytics become defensible over time
        - Service expertise is hard to replicate
        - Pricing power as premium, automated solution
        
        **In a fragmented market, the first professional platform wins.**
        """
    )

with st.expander("5️⃣ Exit Readiness — Multiple Paths to Value"):
    st.markdown(
        """
        **Acquisition targets:**
        - Tier-1 NDT companies (Eddyfi, Olympus, Sonatest) seeking robotics capabilities
        - Industrial equipment manufacturers (ABB, Fanuc) seeking AU-E domain
        - Private equity rolls for consolidation plays
        
        **Organic growth path:**
        - Self-funding by Year 3 enables geographic expansion
        - Software subscriptions create recurring revenue
        - Multiple can expand beyond AU-E to other NDT modalities
        
        **By Year 5, multiple exit paths available.**
        """
    )

st.divider()

st.subheader("🎬 Next Steps")

st.markdown(
    """
    1. **Review the financial model** — use the interactive dashboard to stress-test assumptions
    2. **Understand the roadmap** — ask questions about technical execution & timelines
    3. **Validate the team** — we're experienced in AU-E, robotics, and scaling hardware businesses
    4. **Discuss investment terms** — let's align on stage gates, milestones, and fund deployment
    
    ---
    
    **Ready to move forward?** Head to the Contact page to schedule a deeper discussion.
    """
)

add_footer()
