"""Problem Statement: The limitations of manual AU-E."""

import streamlit as st
from utils import set_page, add_footer

set_page()

st.title("⚠️ The Problem: Manual AU-E Is Holding Us Back")
st.divider()

st.markdown(
    """
    ### Current Limitations
    
    - **Variable force** — operator-dependent impacts reduce consistency
    - **Limited throughput** — capped by manual labor
    - **Low client perception** — viewed as outdated, pre-automation
    - **Enterprise misalignment** — clients expect automated quality systems
    
    ### Business Impact
    
    | Metric | Current |
    |--------|--------|
    | **Jobs/year** | ~15 |
    | **Data consistency** | ±15% variance |
    | **Gross margin** | 67% |
    | **Growth potential** | Limited |
    
    **→ We're using a hammer to conduct precision ultrasonic analysis.**
    """
)

add_footer()
