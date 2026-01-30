"""Development Roadmap: Two-stage, de-risked execution plan."""

import streamlit as st
from utils import set_page, add_footer

set_page()

st.title("🛠️ Development Roadmap: Two-Stage, De-Risked Execution")
st.markdown("*Strategic phasing reduces risk while delivering early wins*")
st.divider()

col1, col2 = st.columns([1.5, 1])

with col1:
    st.markdown(
        """
        ### Stage 1: Precision Impactor (6-8 months, $100K)

        - **What:** Automated impact device replacing manual hammer strikes.
        - **Why it matters:** Immediate improvement in accuracy and repeatability; higher data quality is noticeable to clients and increases trust in reported results.
        - **Benefits:** Positions us as a high‑tech provider early; small but meaningful uplift in perceived value; generates incremental revenue that helps fund Stage 2.
        - **Risk Level:** Low — straightforward hardware development with fast deployment and site-time to build operational experience.
        
        ---

        ### Stage 2: Full Robotic Platform (12–18 months, $400K)

        - **What:** Industrial robotic arm + AU‑E integration + automation software.
        - **Why it matters:** Near‑total automation dramatically boosts accessibility (under-hearth, taphole, cooling plates), eliminates safety barriers, and expands coverage by 3–5×.
        - **Benefits:** Cuts inspection time by 30–50%, reduces outage duration, increases client uptime (high 6‑ to 7‑figure annual impact for smelters), and unlocks premium market positioning.
        - **Risk Level:** De‑risked — leverages proven robotic platforms and insights gained from Stage 1 deployment.
        
        ---
        
        ### Why Two Stages?
        
        1. Stage 1 delivers immediate accuracy and quality gains with minimal risk.
        2. Early uplift and improved client perception create cash flow that partially funds Stage 2.
        3. Stage 1 field experience reduces integration challenges in Stage 2.
        4. Stage 2 then delivers the full value: coverage, speed, safety, and premium positioning.
        """
    )

with col2:
    st.image("images/Designer (4).png")

add_footer()
