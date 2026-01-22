import streamlit as st
from utils import set_page

set_page()

st.title("The Problem: Manual AU-E Is Holding Us Back")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
    """
    - AU-E still relies on **manual hammer impacts**
    - Inconsistent force → inconsistent data
    - Clients increasingly expect **automation**
    - Manual methods look outdated in an AI/robotics world
    """
    )

with col2:
    st.image("images/manual_hammer.jpg", caption="Manual impact testing (illustrative)", use_column_width=True)

st.markdown(
"""
> We're doing precision ultrasonic work with a hammer.  
> It's slow, inconsistent, and visibly outdated.
"""
)
