"""Opportunity Statement: How robotics transforms AU-E."""

import streamlit as st
from utils import set_page, add_footer

set_page()

st.title("✨ The Opportunity: Robotics Unlocks Scalability & Premium Positioning")
st.markdown("*Transforming AU-E from a manual service into a high-margin, automatable platform*")
st.divider()

col1, col2 = st.columns([1.2, 1], gap="large")

with col1:
    st.markdown(
        """
        ### Why Robotics Changes Everything
        
        Robotics isn't just an incremental improvement—it's a **strategic repositioning** of AU-E.
        
        #### ✅ **Technical Advantages**
        
        - **Consistent, programmable impact** — force repeatable within ±2%
        - **Faster inspection cycles** — 3-5x throughput vs. manual
        - **Complex geometry access** — reaches areas manual testing cannot
        - **Data standardization** — enables trend analysis and predictive QA
        - **Operator independence** — removes fatigue and human error
        - **Scalability** — same system can handle 10x more jobs annually
        
        #### 💰 **Business Advantages**
        
        - **Higher margins** — premium pricing for "Industry 4.0" solutions
        - **Recurring revenue** — software, maintenance, and calibration services
        - **Enterprise sales** — attracts large OEMs and Tier-1 manufacturers
        - **Conference visibility** — cutting-edge robotics attracts media and partnerships
        - **Defensible moat** — first-mover establishes the standard
        """
    )
    
with col2:
    try:
        st.image("images/robotic_arm.jpg", caption="Robotic AU-E platform concept", width=None)
    except:
        st.info("📸 *Visual placeholder: Robotic AU-E system*")

st.divider()

st.markdown(
    """
    ### Market Positioning
    
    **Before Robotics:**  
    "Manual service provider offering commodity AU-E testing"
    
    **After Robotics:**  
    "High-tech platform provider offering AI-enabled, scalable quality assurance"
    
    ---
    
    ### The Unit Economics Transform
    
    | Metric | Manual AU-E | Robotic AU-E | Change |
    |--------|-------------|--------------|--------|
    | **Jobs/year** | 12 | 25-35 | +170-190% |
    | **Revenue/job** | $120K | $150K+ | +25% (premium pricing) |
    | **Cost/job** | $40K | $25K | -37% (automation) |
    | **Gross margin** | 67% | 83% | +16 pts |
    | **Annual revenue** | $1.44M | $3.75M | +161% |
    | **Annual EBITDA** | ~$960K | ~$3.1M | +223% |
    
    ---
    
    ### This Is Not Incremental
    
    Robotics transforms AU-E from a **labor-constrained service** into a **capital-enabled, scalable platform**.
    It's a different business model, serving different customers, at different price points.
    """
)

add_footer()
