"""Investment Case: Why robotics transforms AU-E into an attractive opportunity."""

import streamlit as st
from utils import set_page, add_footer

set_page()

st.title("🎯 The Investment Case")
st.divider()

col1, col2 = st.columns([1.5, 1])

with col1:
    st.markdown(
        """
        ### The Investment Case

        - **We are not starting from zero** — AU‑E is an established, revenue‑generating service with consistent demand. The business already funds itself; no negative cash position at any point.
        - **The problem:** Manual AU‑E is labor‑limited, inconsistent, and unable to meet modern client expectations.
        - **The solution:** A $500K, two‑stage automation roadmap (Precision Impactor + Robotic Platform).
        - **The returns:** NPV $7.2M, IRR **165%** over 5 years driven by higher accuracy, greater accessibility, and reduced labor dependence.

        ---

        ### Why This Works

        | Factor | Why It Matters |
        |--------|----------------|
        | **Existing Market** | AU‑E already produces stable revenue — automation accelerates growth, not create it from scratch. |
        | **Market Timing** | Enterprise clients are actively seeking automated, high‑tech inspection solutions. |
        | **Proven Technology** | We’re integrating known robotics — not speculative R&D. |
        | **De‑Risked Rollout** | Stage 1 generates early gains and cash flow, reducing Stage 2 funding pressure. |
        | **Clear Value Story** | Better accuracy + deeper coverage = better client decisions and higher willingness to pay. |

        """
    )

with col2:
    st.image("images/BRO.png")

add_footer()
