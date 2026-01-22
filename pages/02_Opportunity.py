import streamlit as st
from utils import set_page

set_page()

st.title("The Opportunity: Robotics Makes AU-E Scalable and Sexy")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
    """
    **Robotics unlocks:**
    - Consistent, programmable impact force  
    - Faster inspections → more jobs per year  
    - Access to complex geometries  
    - A visually impressive system that attracts clients and conference attention  
    """
    )

with col2:
    st.image("images/robotic_arm.jpg", caption="Concept: robotic AU-E platform", use_column_width=True)

st.markdown(
"""
Robotics doesn't just improve AU-E — it **repositions** it as a premium, high-tech service.
"""
)
