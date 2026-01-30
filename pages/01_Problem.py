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
        
        - **Inconsistent Accuracy** — Manual striking introduces variability in force, angle, and location, reducing confidence in the data.
        - **Restricted Access** — Critical furnace zones are unsafe or physically unreachable, leaving major data gaps.
        - **Labor‑Limited Throughput** — Inspection speed and capacity depend entirely on human operators; scaling requires more people, not better productivity.
        - **Misaligned With Client Expectations** — Enterprise clients making multi‑million‑dollar decisions now expect automated, high‑precision inspection tools, not manual hammer-based workflows.
        
        """
    )

    st.markdown(
        """
        <div style="
            margin-top: 10px;
            font-size: 1.6rem;
            line-height: 1.6;
            font-style: italic;
            color: #ffffff;
        ">
            “We’re using a hammer to conduct precision NDT analysis??”
        </div>
        <div style="font-size: 1.2rem; color:#888; margin-top: 6px;">
            — Internal stakeholder
        </div>
        """,
        unsafe_allow_html=True
    )



with col2:
    st.image("images/hammering.JPG")

add_footer()
