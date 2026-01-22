"""Development Roadmap: Two-stage, de-risked execution plan."""

import streamlit as st
from utils import set_page, add_footer

set_page()

st.title("🛠️ Development Roadmap: Two-Stage, De-Risked Execution")
st.markdown("*Strategic phasing reduces risk while delivering early wins*")
st.divider()

st.markdown(
    """
    ## Strategic Philosophy
    
    Our roadmap is **deliberately staged**—not a moonshot. Each stage:
    - Delivers real business value
    - Funds (partially) the next stage
    - Reduces technical and market risk
    - Proves the business model incrementally
    
    ---
    """
)

# Stage 1
st.subheader("🔧 Stage 1: Precision Impactor Tooling (Fast Win)")

col1, col2 = st.columns([1.5, 1], gap="large")

with col1:
    st.markdown(
        """
        ### Deliverables
        
        - **Precision impact system** → replaces manual hammer
        - **Force calibration & feedback control** → ±2% consistency
        - **Integration with existing AU-E hardware** → minimal operational change
        - **Operator training & documentation** → smooth deployment
        
        ### Impact (Year 1)
        
        - **+20% job capacity** within existing labor constraints
        - **+30% data consistency** → higher client confidence
        - **Early revenue boost** → validates product-market fit
        - **Funding for Stage 2** → proven ROI attracts capital
        
        ### Timeline & Budget
        - **Duration:** 6 months (Q2-Q3 2026)
        - **Investment:** $100K CAD
        - **Expected ROI:** 60% within 12 months
        - **Risk Level:** 🟢 Low (proven electromechanical technology)
        """
    )

with col2:
    st.info(
        """**Stage 1 Quick Facts**

✓ Proven technology
✓ Fast deployment (6 mo)
✓ Minimal integration risk
✓ Immediate revenue impact
✓ Funds Stage 2"""
    )

st.divider()

# Stage 2
st.subheader("🤖 Stage 2: Full Robotic Platform (Market Leadership)")

col3, col4 = st.columns([1.5, 1], gap="large")

with col3:
    st.markdown(
        """
        ### Deliverables
        
        - **Industrial robotic arm integration** (6-axis, ~500KG payload)
        - **Custom AU-E probe end-effector** → specialized probe mounting
        - **Motion control software** → path planning & repeatability
        - **AI-powered inspection sequencing** → optimized scanning patterns
        - **Cloud data pipeline** → real-time analytics & trend reporting
        - **Conference-ready demonstration system** → marketing & sales asset
        
        ### Impact (Year 2-3)
        
        - **+170% job capacity** through automation
        - **+25% pricing premium** due to premium positioning
        - **+83% gross margin** vs. baseline manual
        - **$3.1M annual EBITDA** (vs. $960K manual)
        - **Strategic asset** — attracts partnerships, acquirers, or IPO readiness
        
        ### Timeline & Budget
        - **Duration:** 12-18 months (Q4 2026 - Q2 2027)
        - **Investment:** $300K CAD
        - **Expected ROI:** 4:1 within 3 years
        - **Risk Level:** 🟡 Medium (integration complexity, but robotics proven)
        """
    )

with col4:
    st.info(
        """**Stage 2 Quick Facts**

✓ Builds on Stage 1
✓ Proven robotics + custom integration
✓ Industry 4.0 positioning
✓ High-margin revenue stream
✓ Strategic moat"""
    )

st.divider()

# Timeline visualization
st.subheader("📅 Investment Timeline")

st.markdown(
    """
    ```
    Q2 2026          Q4 2026          Q2 2027          Q2 2028
    |                |                |                |
    [==== Stage 1 ===|                |                |
         6 mo, $100K |                |                |
                     [===== Stage 2 ======|                |
                         12-18 mo, $300K |                |
                                        [== Revenue Growth ==]|
    ```
    
    ### Key Milestones
    
    - **M1 (Q2 2026):** Stage 1 prototype complete, initial testing
    - **M2 (Q3 2026):** Stage 1 deployment, customer pilot
    - **M3 (Q4 2026):** Stage 2 engineering begins, Stage 1 ROI measured
    - **M4 (Q2 2027):** Stage 2 robotic system integration complete
    - **M5 (Q3 2027):** Stage 2 production deployment, market launch
    - **M6 (2028+):** Scale operations, expand customer base, explore growth capital or exit
    """
)

st.divider()

st.markdown(
    """
    ## Why This Plan Works
    
    1. **De-risked execution** — proven tech at each stage
    2. **Funding efficiency** — Stage 1 generates cash to fund Stage 2
    3. **Market validation** — Stage 1 proves customer demand before big Stage 2 bet
    4. **Competitive advantage** — early-mover in robotic AU-E
    5. **Optionality** — success at Stage 1 attracts partners, capital, or acquirers for Stage 2
    
    This is a **pragmatic, capital-efficient path** to transforming AU-E into a high-margin, scalable platform.
    """
)

add_footer()
