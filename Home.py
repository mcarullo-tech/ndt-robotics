"""NDT Robotics - Investor Dashboard Home."""

import streamlit as st
from utils import set_page, add_footer

set_page()

st.title("Reinventing Acousto-Ultrasonic Inspection Through Robotics")
st.subheader("A Two-Stage Automation Platform for the Next Era of AU-E")

st.divider()

st.markdown(
"""
## Welcome to NDT Robotics Investor Dashboard

An interactive financial platform showing how robotics transforms AU-E inspection into a scalable, high-margin business.

### Key Highlights
"""
)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Investment Required", "$500K", "Invested over 2 years")
with col2:
    st.metric("Internal Rate of Return", "165%", "Annualized over 5 years")
with col3:
    st.metric("Year 5 Advantage", "$1,225,600", "Annual cash flow improvement")

st.divider()

st.markdown(
"""
### Why This Matters

- NDT Inspection market is maturing; many competitors now offer robotic & AI integrated solutions.
- Manual AU-E is slow and plagued with error; clients demand accuracy to inform multi-million dollar decisions.
- Robotics repositions us as a premium, high-tech service provider.


### Our Two-Stage Plan

- **Stage 1**: Precision impactor tooling ($100K, 6 months) — immediate gains  
- **Stage 2**: Full robotic platform ($400K, 18 months) — complete automation

Use the sidebar to explore the Problem, Opportunity, Roadmap, Financial Model, and Investment Case.
"""
)

add_footer()
