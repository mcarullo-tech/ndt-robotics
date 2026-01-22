import streamlit as st

def set_page():
    st.set_page_config(layout="wide")
    st.markdown(
        """
        <style>
        .block-container {max-width: 1100px; padding-top: 2rem;}
        h1, h2, h3 {font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;}
        </style>
        """,
        unsafe_allow_html=True,
    )
