"""Opportunity Statement: How robotics transforms AU-E."""

import streamlit as st
from utils import set_page, add_footer

set_page()

st.title("✨ The Opportunity: Robotics Transforms AU-E")
st.divider()

col1, col2 = st.columns([1.5, 1])

with col1:
    st.markdown(
        """
        ### What Robotics Delivers
        
        **Technical Benefits**
        - **Higher Accuracy** — Robotics eliminates strike variability and human error, producing consistent, repeatable data with higher confidence.
        - **Improved Accessibility** — Robots can access critical areas that are unsafe or physically impossible for human operators.
        - **Greater Coverage** — More surface area can be inspected in the same outage window, reducing blind spots in life prediction and reline planning.
        - **Operational Efficiency** — Faster inspections with fewer people involved, reducing outage time and resource requirements.

        **Client Value**
        - **Reduced Risk of Unplanned Reline** — Accessing previously unreachable areas can reveal early-stage wear that would otherwise go undetected, potentially saving millions in emergency downtime.
        - **Optimized Campaign Life** — More accurate thickness data allows operators to safely extend furnace life without increasing risk exposure.
        - **Targeted Maintenance** — Higher-resolution inspection enables precision repairs instead of conservative full‑area replacements, reducing maintenance cost.
        - **Shorter Outage Windows** — Faster robotic scans reduce furnace downtime, directly translating into higher production uptime and revenue.
        
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
            “From niche and archaic technique to premium and scalable platform”
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.image("images/floaty_boaty.gif", width=800)


add_footer()
