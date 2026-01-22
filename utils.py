"""Utility functions for NDT Robotics investor dashboard."""

import streamlit as st


def set_page() -> None:
    """Configure Streamlit page settings with professional styling."""
    st.set_page_config(
        page_title="NDT Robotics | Investor Dashboard",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    st.markdown(
        """
        <style>
            /* Professional color scheme and typography */
            :root {
                --primary-color: #0066CC;
                --success-color: #00C851;
                --warning-color: #FF9500;
                --danger-color: #FF3B30;
                --background-light: #F8F9FA;
                --border-color: #E0E6ED;
            }
            
            .block-container {
                max-width: 1200px;
                padding-top: 2rem;
                padding-left: 2rem;
                padding-right: 2rem;
            }
            
            h1, h2, h3, h4, h5, h6 {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', sans-serif;
                font-weight: 600;
                letter-spacing: -0.5px;
            }
            
            h1 {
                font-size: 2.5rem;
                margin-bottom: 1rem;
                color: #0066CC;
            }
            
            h2 {
                font-size: 1.8rem;
                margin-top: 2rem;
                margin-bottom: 1rem;
                color: #1a1a1a;
            }
            
            /* Professional metric cards */
            [data-testid="metric-container"] {
                background-color: #F8F9FA;
                padding: 1.5rem;
                border-radius: 8px;
                border: 1px solid #E0E6ED;
            }
            
            /* Button styling */
            .stButton > button {
                border-radius: 6px;
                padding: 0.5rem 1.5rem;
                font-weight: 500;
            }
            
            /* Dividers */
            hr {
                margin: 2rem 0;
                border-color: #E0E6ED;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def add_footer() -> None:
    """Add a professional footer to pages."""
    st.markdown(
        """
        <hr style='margin-top: 3rem; border: 1px solid #E0E6ED;'>
        <p style='text-align: center; color: #666; font-size: 0.9rem; margin-top: 2rem;'>
        <strong>NDT Robotics</strong> | Reinventing Acousto-Ultrasonic Inspection<br>
        © 2026 NDT Robotics. All rights reserved.
        </p>
        """,
        unsafe_allow_html=True,
    )
