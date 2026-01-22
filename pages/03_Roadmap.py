"""Development Roadmap: Two-stage, de-risked execution plan."""

import streamlit as st
from utils import set_page, add_footer

set_page()

st.title("🛠️ Development Roadmap: Two-Stage, De-Risked Execution")
st.markdown("*Strategic phasing reduces risk while delivering early wins*")
st.divider()

col1, col2 = st.columns([1.5, 1])

with col1:
    st.markdown(
        """
        ### Stage 1: Precision Impactor (6 months, $100K)
        
        - **What:** Automated impact system replacing manual hammer  
        - **Impact:** **+20%** capacity, validates market demand  
        - **ROI:** Payback in 12-18 months  
        
        ---

        ### Stage 2: Full Robotic Platform (12-18 months, $400K)

        - **What:** Industrial robotic arm + AU-E integration + AI software  
        - **Impact:** **+150%** capacity, premium market positioning
        - **ROI:** Strategic asset for scalable growth
        
        ---
        
        ### Why Two Stages?
        
        1. Stage 1 can be deployed quickly for early benefits
        2. Stage 1 cash partially funds Stage 2
        3. Proven technologies—not R&D risk
        4. Demonstrate progress to stakeholders
        """
    )

with col2:
    st.info("📸 **Image Placeholder**\n\nRoadmap Timeline/Milestones")

add_footer()
