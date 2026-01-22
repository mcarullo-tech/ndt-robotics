import streamlit as st
from utils import set_page

set_page()

st.title("The Investment Case")

st.markdown(
"""
**Why this is a compelling investment:**

- Robotics turns AU-E from a shrinking service into a **growing, high-margin platform**
- The roadmap is **staged and de-risked**
- The financial model is **transparent and interactive**
- The technology becomes both a **capability** and a **marketing asset**
"""
)

st.markdown(
"""
Use the **Financial Model** page to explore:

- NPV uplift  
- Payback timing  
- Sensitivity to job volume, pricing, and uplift  
"""
)
