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
        - Consistent force (±5% vs. ±15% manual)
        - 3-5x throughput increase
        - Removes operator dependency
        
        **Business:**
        - Premium pricing ($150K vs. $120K per job)
        - Margin expansion (83% vs. 67%)
        - Enterprise client positioning
        
        ### Unit Economics Transformation
        
        | Metric | Manual | Robotic | Change |
        |--------|--------|---------|--------|
        | **Jobs/year** | 15 | 30 | +100% |
        | **Revenue/job** | $120K | $150K | +25% |
        | **Margin** | 65% | 83% | +18 pts |
        | **Annual revenue** | $1.8M | $4.5M | +150% |
        
        **→ From niche and archaic technique to premium and scalable platform**
        """
    )

with col2:
    st.info("📸 **Image Placeholder**\n\nRobotic AU-E Platform")


add_footer()
