"""Problem Statement: The limitations of manual AU-E."""

import streamlit as st
from utils import set_page, add_footer

set_page()

st.title("⚠️ The Problem: Manual AU-E Is Holding Us Back")
st.markdown("*Why the current approach limits growth and client confidence*")
st.divider()

col1, col2 = st.columns([1.2, 1], gap="large")

with col1:
    st.markdown(
        """
        ### Current State: Manual Inspection
        
        Today's AU-E (Acousto-Ultrasonic Evaluation) relies on:
        
        #### ❌ **The Core Issues**
        
        - **Manual hammer impacts** — operator-dependent, variable force
        - **Inconsistent data quality** — force variations reduce signal reliability
        - **Limited scalability** — throughput capped by manual labor
        - **Outdated perception** — clients view this as low-tech, pre-automation industry
        - **Operator fatigue** — repetitive impacts reduce consistency over long sessions
        - **Lack of repeatability** — difficult to compare results across time or operators
        
        ### Market Expectations Are Shifting
        
        - **Enterprise clients** now expect automation in precision testing
        - **Competitors** are exploring robotic solutions
        - **Industry trends** favor AI, robotics, and data-driven quality
        """
    )
    
with col2:
    # If image doesn't exist, show a placeholder
    try:
        st.image("images/manual_hammer.jpg", caption="Manual impact testing", width=None)
    except:
        st.info("📸 *Visual placeholder: Manual hammer impact system*")

st.divider()

st.markdown(
    """
    ### The Bottom Line
    
    > **We're conducting precision ultrasonic analysis with a hammer.**
    >
    > It works—but it's slow, inconsistent, and signals that AU-E is a *manual* service,
    > not a *precision* platform.
    
    ### What This Means for Business
    
    | Metric | Current (Manual) | Impact |
    |--------|------------------|--------|
    | **Jobs/year** | ~12 | Limited by labor |
    | **Data consistency** | ±15% variance | Limits QA confidence |
    | **Client perception** | Low-tech | Loses high-value clients |
    | **Competitive position** | Vulnerable | Others may move first |
    | **Growth ceiling** | ~20% annual | Difficult to exceed |
    
    ---
    
    **The opportunity is clear: robotics fixes all of these.**
    """
)

add_footer()
