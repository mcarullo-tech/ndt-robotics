# NDT Robotics Investor Dashboard - Quick Start Guide

## Running the Dashboard

```bash
streamlit run Home.py
```

The dashboard will open in your browser at `http://localhost:8501`

---

## 🎯 Customization Checklist

### 1. Contact Information (URGENT)
Edit `pages/06_Contact.py`:
- [ ] Replace `[Your Name/Company Name]` with your actual name
- [ ] Replace `[your.email@company.com]` with your email
- [ ] Replace `[+1 XXX-XXX-XXXX]` with your phone
- [ ] Replace `[linkedin.com/in/yourprofile]` with your LinkedIn
- [ ] Replace `[company.com]` with your website

### 2. Financial Model Assumptions
Edit `pages/04_Financial_Model.py`:
- [ ] Adjust baseline job volume (currently 12/year)
- [ ] Adjust revenue per job (currently $120K CAD)
- [ ] Adjust cost per job (currently $40K CAD)
- [ ] Adjust Stage 1 cost if different from $100K
- [ ] Adjust Stage 2 cost if different from $300K

### 3. Add Images
Create an `images/` folder and add:
- [ ] `manual_hammer.jpg` - Photo of manual hammer impact testing
- [ ] `robotic_arm.jpg` - Photo/rendering of robotic AU-E system

**Note:** If images aren't found, the app shows placeholders automatically.

### 4. Timeline & Roadmap
Edit `pages/03_Roadmap.py`:
- [ ] Update Stage 1 timeline if different from 6 months
- [ ] Update Stage 2 timeline if different from 12-18 months
- [ ] Update milestone dates (Q2 2026, Q3 2026, etc.)
- [ ] Adjust deliverables and impact metrics

### 5. Key Opportunity Numbers
Edit `pages/02_Opportunity.py`:
- [ ] Update unit economics table with your actual projections
- [ ] Update job volume assumptions
- [ ] Update pricing assumptions
- [ ] Update cost/margin assumptions

### 6. Investment Resources Links
Edit `pages/06_Contact.py`:
- [ ] Add link to your executive summary (1-page)
- [ ] Add link to detailed Excel financial model
- [ ] Add link to team bios/backgrounds
- [ ] Add link to case studies
- [ ] Add link to technical specifications

---

## 📊 Financial Model Guide

### How to Use the Interactive Model

1. **Baseline Scenario Tab**
   - Adjust jobs/year (default 12)
   - Adjust revenue and expense per job
   - Adjust growth/decline rate

2. **Robotics Scenario Tab**
   - Stage 1: Set cost, duration, and job uplift
   - Stage 2: Set cost, duration, and cumulative uplift
   - Economic factors: Revenue growth and expense reduction

3. **Risk Factors Tab**
   - Understand the key sensitivity drivers
   - Identifies assumptions your model depends on

4. **Results Tabs**
   - Annual Cash Flow: Year-by-year performance
   - Cumulative Cash Flow: Shows payback timing
   - Summary Table: Full numerical breakdown

### Interpreting Results

- **Baseline NPV**: Value with no investment (baseline for comparison)
- **Robotics NPV**: Value with $450K investment strategy
- **NPV Uplift**: The value created by the robotics investment
- **Payback Year**: When cumulative cash flow turns positive

---

## 🎨 Styling & Branding

All styling is centralized in `utils.py`:

```python
# Professional color scheme
--primary-color: #0066CC       # Blue
--success-color: #00C851       # Green
--background-light: #F8F9FA    # Light gray
```

To customize colors, edit the CSS in `utils.py` `set_page()` function.

---

## 🔑 Key Content Pages

| Page | File | Key Content |
|------|------|-------------|
| Home | `Home.py` | Dashboard overview, key metrics, intro |
| Problem | `01_Problem.py` | Why manual AU-E is limited |
| Opportunity | `02_Opportunity.py` | Why robotics transforms the business |
| Roadmap | `03_Roadmap.py` | Two-stage development plan |
| Financial Model | `04_Financial_Model.py` | Interactive financial scenarios |
| Investment Case | `05_Investment_Case.py` | Why this is a compelling investment |
| Contact | `06_Contact.py` | How to connect with you |

---

## 💡 Tips for Investors

### Present With Confidence

1. **Start on Home page** - Sets up the narrative
2. **Walk through Problem** - Establish the pain point
3. **Show Opportunity** - Paint the vision
4. **Explain Roadmap** - De-risked, staged approach
5. **Explore Financial Model** - Let them play with assumptions
6. **Summarize Investment Case** - 5 key points
7. **Close on Contact** - Next steps

### Interactive Features

- Let investors adjust financial assumptions in real time
- Show sensitivity to key drivers (job volume, pricing, etc.)
- Use this to have "what-if" conversations

### Red Flags to Address

- "What if Stage 2 delays by 6 months?" → Model shows 6-12 month payback delay
- "What if we only get 50% of the uplift?" → Adjust slider and recalculate
- "What if prices stay flat?" → Set revenue growth to 0% and show results

---

## 🚀 Deployment

### Local Testing
```bash
streamlit run Home.py
```

### Cloud Deployment (Streamlit Cloud)

1. Push repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Deploy from your GitHub repo
4. Share the public URL with investors

### Enterprise Deployment

- Streamlit can be deployed on AWS, Azure, or on-prem servers
- Consider authentication and data privacy for sensitive models

---

## 📞 Support & Customization

If you need to customize further:

- **Page content**: Edit the Markdown in each file
- **Financial assumptions**: Modify sliders in `04_Financial_Model.py`
- **Styling**: Edit CSS in `utils.py`
- **Add new pages**: Create new files in `pages/` folder following existing pattern
- **Change colors**: Update hex codes in `utils.py`

---

## ✅ Pre-Investor Checklist

- [ ] Contact information updated
- [ ] Financial assumptions reflect your actual projections
- [ ] Images added (or you're comfortable with placeholders)
- [ ] All links in Contact page are valid
- [ ] Tested locally and all interactive features work
- [ ] Roadmap timeline matches your actual plan
- [ ] Unit economics align with your business model
- [ ] You're comfortable explaining each assumption

---

**Good luck with your investment pitch! You've got this. 🚀**
