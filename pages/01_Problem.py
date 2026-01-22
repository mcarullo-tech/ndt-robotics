"""Problem Statement: The limitations of manual AU-E."""

import streamlit as st
from utils import set_page, add_footer

set_page()

st.title("⚠️ The Problem: Manual AU-E Is Holding Us Back")
st.divider()

col1, col2 = st.columns([1.5, 1])

with col1:
    st.markdown(
        """
        ### Current Limitations
        
        - **Limited Accuracy** — inconsistent impact force affects data quality
        - **Accessibility Issues** — key areas of interest are unreachable for operators
        - **Scalability Challenges** — manual processes limit growth potential
        - **Enterprise misalignment** — clients expect automated quality systems
        
        ### Business Impact
        
        | Metric | Current |
        |--------|--------|
        | **Jobs/year** | ~15 |
        | **Data consistency** | ±15% variance |
        | **Gross margin** | 65% |
        | **Growth potential** | Limited |
        
        **→ We're using a hammer to conduct precision NDT analysis.**
        """
    )

with col2:
    st.image("images/gingy_coat.png")

add_footer()
