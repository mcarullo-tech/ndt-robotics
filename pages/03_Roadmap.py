import streamlit as st
from utils import set_page

set_page()

st.title("Two-Stage Development Roadmap")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Stage 1 — Impactor Tooling")
    st.markdown(
    """
    - Cost: ~**$100k CAD**  
    - Timeline: **6 months**  
    - Immediate accuracy + speed gains  
    - Direct uplift in job volume  
    """
    )

with col2:
    st.subheader("Stage 2 — Full Robotic Platform")
    st.markdown(
    """
    - Cost: ~**$300k** (CAD-equivalent)  
    - Timeline: **1–2 years**  
    - Full automation + reach  
    - Conference-ready showcase system  
    """
    )

st.markdown(
"""
This is a **de-risked, staged engineering plan** — not a moonshot.
"""
)
