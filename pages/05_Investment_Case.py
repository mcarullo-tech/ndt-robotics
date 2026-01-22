"""Investment Case: Why robotics transforms AU-E into an attractive opportunity."""

import streamlit as st
from utils import set_page, add_footer

set_page()

st.title("🎯 The Investment Case")
st.divider()

col1, col2 = st.columns([1.5, 1])

with col1:
    st.markdown(
        """
        ### The Opportunity
        
        - **Problem:** Manual AU-E is labor-constrained, inconsistent, and outdated  
        - **Solution:** $500K investment in two-stage robotics platform  
        - **Returns:** NPV $7.2M, IRR **165%** over 5 years 

        ---
        
        ### Why This Works
        
        | Factor | Why It Matters |
        |--------|---------|
        | **Market timing** | Enterprise clients demand automation now |
        | **Proven tech** | Not R&D—integration of existing robotics |
        | **Strong returns** | NPV $7.2M, IRR **165%** over 5 years |
        | **De-risked plan** | Stage 1 funds Stage 2; early wins |
        
        ---
        
        ### Financial Summary
        
        **Stage 1 ($100K, 6 mo):**
        - **+20%** capacity, validates market demand
        - Payback in 12-18 months
        - Generates cash for Stage 2

        **Stage 2 ($400K, 12-18 mo):**
        - **+150%** capacity, premium positioning
        - Strategic asset for growth
        """
    )

with col2:
    st.info("📸 **Image Placeholder**\n\nInvestment Returns & Growth Trajectory")

add_footer()
