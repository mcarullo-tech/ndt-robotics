"""NDT Robotics - Investor Dashboard Home."""

import streamlit as st
from utils import set_page, add_footer

set_page()

st.title("🤖 Reinventing Acousto-Ultrasonic Inspection Through Robotics")
st.subheader("A Two-Stage Automation Platform for the Next Era of AU-E")

st.divider()

st.markdown(
"""
## Welcome to NDT Robotics' Investor Dashboard

This interactive platform combines a **live investor pitch** with a **fully transparent financial model**.
Explore how robotics transforms AU-E from a manual service into a scalable, high-margin platform.

### 📊 Dashboard Navigation

Use the sidebar menu to explore our investment thesis:

1. **Problem** — Why manual AU-E is holding back the industry
2. **Opportunity** — How robotics creates a compelling opportunity
3. **Roadmap** — Our staged, de-risked development plan
4. **Financial Model** — Interactive scenarios & NPV analysis
5. **Investment Case** — Why this investment makes sense
6. **Contact** — Let's talk

---

### Key Highlights

"""
)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Investment Required", "$450K", "Across both stages")
with col2:
    st.metric("Projected Job Uplift", "+70%", "Year 2-3")
with col3:
    st.metric("Target Payback Period", "3-4 years", "At baseline pricing")

st.divider()

st.markdown(
"""
### 💡 Why This Matters

**AU-E is entering a critical inflection point.**

- Clients increasingly demand **automation** over manual methods
- Current manual inspection limits scalability and margins
- Robotics repositions AU-E as a **premium, high-tech service**
- First-mover advantage in automation = market leadership

### 🚀 Our Approach

We're not building a moonshot. We're executing a **pragmatic, two-stage plan**:

- **Stage 1**: Precision impactor tooling ($100K, 6 months) → immediate operational gains
- **Stage 2**: Full robotic platform ($300K, 1-2 years) → complete automation & market positioning

---

**Ready to explore the numbers?** Head to the Financial Model or reach out via the Contact page.
"""
)

add_footer()
