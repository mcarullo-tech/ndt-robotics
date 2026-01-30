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
        
        - **Limited Accuracy & Repeatability** - Human operator introduces variability in striking force and measurement location, both critical for accuracy.
        - **Accessibility Issues** — Key areas of interest to furnace operators are difficult or impossible to access.
        - **Scalability Challenges** — Heavy reliance on human operators limits growth potential; we will always be constrained by labor.
        - **Enterprise misalignment** — Clients expect high-tech precision solutions to inform multi-million dollar decisions.
        
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
