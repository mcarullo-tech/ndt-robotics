"""Opportunity Statement: How robotics transforms AU-E."""

import streamlit as st
from utils import set_page, add_footer

set_page()

st.title("✨ The Opportunity: Robotics Transforms AU-E")
st.divider()

col1, col2 = st.columns([1.5, 1])

with col1:
    st.markdown(
        """
        ### What Robotics Delivers
        
        **Technical:**
        - Precision-Level Accuracy: Remove human error and produce consistent and repeatable results.
        - Increased Accessibility: Robotic solutions allows us to access key areas previously inaccessible to humans.
        - Operational Efficiency: Inspections can be completed in less time and with less resources.
        

        **Business:**
        - Margin Expansion (83% vs. 67%) based on reduced operational costs
        - Projected uplift (2x in Year 5) from improved capabilities
        - Market Re-Positioning: Build confidence with existing clients, attract new clients with high-tech solutions.
        
        ### Unit Economics Transformation
        
        | Metric | Manual | Robotic | Change |
        |--------|--------|---------|--------|
        | **Jobs/year** | 15 | 30 | +100% |
        | **Revenue/job** | $120K | $150K | +25% |
        | **Margin** | 67% | 83% | +18 pts |
        | **Annual revenue** | $1.8M | $4.5M | +150% |
        
        **From niche and archaic technique to premium and scalable platform**
        """
    )

with col2:
    st.image("images/floaty_boaty.gif", width=800)


add_footer()
