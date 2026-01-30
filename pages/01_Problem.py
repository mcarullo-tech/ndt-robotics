"""Problem Statement: The limitations of manual AU-E."""

import streamlit as st
from utils import set_page, add_footer

set_page()

st.title("⚠️ The Problem: Manual AU-E Is Holding Us Back")
st.divider()

col1, col2 = st.columns([1.5, 1])

with col1:
    # Regular left-aligned bullets (recommended for readability)
    st.markdown(
        """
        ### Current Limitations
        
        - **Limited Accuracy & Repeatability** — Human operator introduces variability in striking force and measurement location, both critical for accuracy.
        - **Accessibility Issues** — Key areas of interest to furnace operators are difficult or impossible to access.
        - **Scalability Challenges** — Heavy reliance on human operators limits growth potential; we will always be constrained by labor.
        - **Enterprise misalignment** — Clients expect high-tech precision solutions to inform multi-million dollar decisions.
        """
    )

    # Centered quote
    st.markdown(
        """
        <div style="
            margin-top: 10px;
            text-align: center;
            font-size: 1.6rem;
            line-height: 1.6;
            font-style: italic;
            color: #ffffff;
        ">
            “We’re using a hammer to conduct precision NDT analysis??”
        </div>
        <div style="text-align:center; font-size: 1.2rem; color:#888; margin-top: 6px;">
            — Internal stakeholder
        </div>
        """,
        unsafe_allow_html=True
    )

    # OPTIONAL: If you truly want centered bullets (less common for UX),
    # wrap them in a centered div and constrain width for readability:
    # st.markdown(
    #     '''
    #     <div style="text-align:center; margin: 0 auto; max-width: 680px;">
    #         <ul style="list-style-position: inside; padding-left: 0;">
    #             <li><b>Limited Accuracy & Repeatability</b> — Operator variability in force & location.</li>
    #             <li><b>Accessibility Issues</b> — Critical areas unsafe/impossible for humans.</li>
    #             <li><b>Scalability Challenges</b> — Growth constrained by labor.</li>
    #             <li><b>Enterprise misalignment</b> — Premium clients expect precision tech.</li>
    #         </ul>
    #     </div>
    #     ''',
    #     unsafe_allow_html=True
    # )

with col2:
    # Center the image in its column
    st.markdown(
        """
        <div style="display:flex; justify-content:center; align-items:center;">
            <img src="images/hammering.JPG" style="max-width:100%; height:auto; border-radius:6px;" />
        </div>
        """,
        unsafe_allow_html=True
    )
    # Or simpler (not perfect in all themes):
    # st.image("images/hammering.JPG", use_column_width=True)

add_footer()