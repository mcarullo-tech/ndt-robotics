"""NDT Robotics - Investor Dashboard Home."""

import streamlit as st
from utils import set_page, add_footer

set_page()

st.title("Reinventing AU-E Inspection Through Robotics")
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
    st.metric("Total Investment Required", "$550K", "Invested over 2 years")
with col2:
    st.metric("Internal Rate of Return", "972%", "Annualized over 5 years")
with col3:
    st.metric("Year 5 Advantage", "$3,360,000", "Annual cash flow improvement")

st.divider()

st.markdown(
"""
### Why This Matters

- The NDT inspection market is maturing, and enterprise clients now expect high‑tech, automated solutions.
- We position ourselves as the “gold standard” of furnace NDT and charge premium prices, but the on-site experience still looks manual and low‑tech.
- This creates a clear mismatch between what clients expect from a premium provider and what we currently deliver.
- Clients are aware that robotic and AI‑integrated inspection systems exist, and they increasingly expect that level of sophistication.
- Meanwhile, our patent has expired, and low-cost, low-tech competitors keep entering the market.
- These competitors appear “good enough” compared to our current execution, making it harder to defend premium pricing without upgrading our technology.

### Our Two-Stage Plan

- **Stage 1**: Precision impactor tooling ($150K, 8-12 months) — immediate gains  
- **Stage 2**: Full robotic platform ($400K, 12-18 months) — complete automation

Use the sidebar to explore the Problem, Opportunity, Roadmap, Financial Model, and Investment Case.
"""
)

add_footer()
