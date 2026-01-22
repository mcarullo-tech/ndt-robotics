"""Contact page: Let's discuss the opportunity."""

import streamlit as st
from utils import set_page, add_footer

set_page()

st.title("📞 Let's Talk")
st.markdown("*Questions? Ready to explore this opportunity? Let's connect.*")
st.divider()

st.markdown(
    """
    ## Ready to Dive Deeper?
    
    If the vision resonates and the numbers make sense, we'd love to discuss:
    
    - **Technical details** — Stage 1 prototype, Stage 2 architecture
    - **Financial scenarios** — explore the model together, stress-test assumptions
    - **Team & execution** — our background in AU-E, robotics, and manufacturing
    - **Investment terms** — structure, milestones, fund deployment
    - **Timeline** — when do we start? What's the go/no-go criteria?
    
    ---
    
    ## Contact Information
    
    **[Your Name/Company Name]**
    - 📧 Email: [your.email@company.com]
    - 📱 Phone: [+1 XXX-XXX-XXXX]
    - 🔗 LinkedIn: [linkedin.com/in/yourprofile]
    - 🌐 Website: [company.com]
    
    ---
    
    ## What to Expect Next
    
    1. **Initial conversation** (30 min) — confirm fit and interest
    2. **Deep dive** (60 min) — walk through model, technical roadmap, team background
    3. **Reference calls** — speak with existing customers, technical advisors
    4. **Term discussion** — align on investment structure and milestones
    5. **Stage 1 kickoff** — begin building the future of AU-E together
    
    ---
    
    ## Investor Resources
    
    - 📋 **Executive summary** → [Link to 1-page overview]
    - 📈 **Detailed financial model** → [Link to Excel model]
    - 👥 **Team bios** → [Link to team background]
    - 🏆 **Case studies** → [Link to existing AU-E projects]
    - 📄 **Technical specs** → [Link to Stage 1/2 engineering plans]
    
    ---
    
    ## FAQ
    
    <details>
    <summary><strong>What's the minimum investment?</strong></summary>
    <p>Stage 1 can be funded independently at $100K, or both stages together at $450K.</p>
    </details>
    
    <details>
    <summary><strong>What's the cap table / equity structure?</strong></summary>
    <p>Let's discuss your preferred structure (equity, convertible, SAFE, etc.).</p>
    </details>
    
    <details>
    <summary><strong>When can Stage 1 start?</strong></summary>
    <p>With capital commitment, we can begin engineering in Q2 2026.</p>
    </details>
    
    <details>
    <summary><strong>Who are the competitors?</strong></summary>
    <p>AU-E remains largely manual. Robotics is an open space—first-mover advantage is real.</p>
    </details>
    
    <details>
    <summary><strong>What if the market doesn't adopt robotics?</strong></summary>
    <p>Stage 1 delivers value on its own (20% uplift, clear ROI). Stage 2 is the growth bet.</p>
    </details>
    """,
    unsafe_allow_html=True
)

st.divider()

st.markdown(
    """
    **Looking forward to the conversation.** Let's build something exceptional together.
    """
)

add_footer()

