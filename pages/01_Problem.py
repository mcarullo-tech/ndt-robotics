"""Problem Statement: The limitations of manual AU-E."""

import streamlit as st
from utils import set_page, add_footer

set_page()

st.title("⚠️ The Problem: Manual AU-E Is Holding Us Back")
st.divider()

# --- Add CSS once, to create a flex box that centers content vertically ---
st.markdown(
    """
    <style>
      /* Adjust this to the vertical height you want both columns to share */
      .vcenter-block {
          display: flex;
          flex-direction: column;
          justify-content: center;   /* vertical centering */
          min-height: 460px;         /* make both columns tall enough to center within */
      }
      /* Optional: horizontally center content inside the flex box */
      .vcenter-block.center-h {
          align-items: center;
          text-align: center;
      }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns([1.5, 1])

with col1:
    st.markdown('<div class="vcenter-block">', unsafe_allow_html=True)

    st.markdown(
        """
        ### Current Limitations
        
        - **Limited Accuracy & Repeatability** — Human operator introduces variability in striking force and measurement location, both critical for accuracy.
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
            text-align: center;
        ">
            “We’re using a hammer to conduct precision NDT analysis??”
        </div>
        <div style="text-align:center; font-size: 1.2rem; color:#888; margin-top: 6px;">
            — Internal stakeholder
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)  # close vcenter-block

with col2:
    # Wrap the image in the same vertical-centering block.
    st.markdown('<div class="vcenter-block center-h">', unsafe_allow_html=True)
    st.image("images/hammering.JPG", use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

add_footer()