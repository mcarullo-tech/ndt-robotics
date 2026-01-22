import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy_financial as npf
import pandas as pd

from utils import set_page

set_page()

st.title("Live Financial Model: Baseline vs Robotics")

st.markdown("Adjust assumptions below and watch the model respond in real time.")

with st.expander("📊 Adjust Assumptions", expanded=False):
    col_base1, col_base2 = st.columns(2)
    col_robotics1, col_robotics2 = st.columns(2)
    
    with col_base1:
        st.subheader("Baseline AU-E")
        baseline_jobs = st.slider("Jobs per year", 5, 30, 12)
        baseline_rev = st.slider("Revenue per job (CAD)", 50_000, 200_000, 120_000, step=5_000)
    with col_base2:
        st.subheader("")
        baseline_exp = st.slider("Expense per job (CAD)", 10_000, 100_000, 40_000, step=5_000)
        baseline_shrink = st.slider("Annual shrink rate (%)", -20, 20, -5) / 100

    with col_robotics1:
        st.subheader("Robotics Development")
        stage1_cost = st.number_input("Stage 1 cost (CAD)", value=100_000)
        stage1_duration = st.slider("Stage 1 duration (years)", 0.1, 2.0, 0.5)
        stage2_cost = st.number_input("Stage 2 cost (CAD)", value=350_000)
        stage2_duration = st.slider("Stage 2 duration (years)", 0.5, 3.0, 1.5)
    with col_robotics2:
        st.subheader("")
        uplift1 = st.slider("Uplift after Stage 1 (%)", 0, 100, 20) / 100
        uplift2 = st.slider("Uplift after Stage 2 (%)", 0, 200, 50) / 100
        rev_growth = st.slider("Revenue growth (%)", 0, 20, 2) / 100
        exp_reduction = st.slider("Expense reduction (%)", 0, 50, 10) / 100

    discount_rate = st.slider("Discount rate for NPV (%)", 0, 20, 8) / 100

years = np.arange(0, 6)

def baseline_cash_flow():
    jobs = baseline_jobs
    flows = []
    for y in years:
        if y > 0:
            jobs *= (1 + baseline_shrink)
        revenue = jobs * baseline_rev
        expenses = jobs * baseline_exp
        flows.append(revenue - expenses)
    return np.array(flows)

def robotics_cash_flow():
    flows = []
    for y in years:
        if y < stage1_duration:
            jobs = baseline_jobs
        elif y < stage2_duration:
            jobs = baseline_jobs * (1 + uplift1)
        else:
            jobs = baseline_jobs * (1 + uplift1 + uplift2)

        revenue = jobs * baseline_rev * (1 + rev_growth)**y
        expenses = jobs * baseline_exp * (1 - exp_reduction)

        dev_cost = 0
        if y < stage1_duration:
            dev_cost += stage1_cost / stage1_duration
        if y < stage2_duration:
            dev_cost += stage2_cost / stage2_duration

        flows.append(revenue - expenses - dev_cost)
    return np.array(flows)

def npv(cashflows, rate):
    return np.sum(cashflows / (1 + rate)**years)

baseline_cf = baseline_cash_flow()
robotics_cf = robotics_cash_flow()

baseline_npv = npv(baseline_cf, discount_rate)
robotics_npv = npv(robotics_cf, discount_rate)

COLOR_BASELINE = '#0066CC'
COLOR_ROBOTICS = '#00C851'

def format_cad(x, pos):
    if x >= 1_000_000:
        return f"${x/1_000_000:.1f}M"
    elif x >= 1_000:
        return f"${x/1_000:.0f}K"
    else:
        return f"${x:.0f}"

col1, col2 = st.columns(2)
col1.metric("Baseline NPV (CAD)", f"{round(baseline_npv/1000)*1000:,.0f}")
col2.metric("Robotics NPV (CAD)", f"{round(robotics_npv/1000)*1000:,.0f}")

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(years, baseline_cf, label="Baseline", linewidth=3, color=COLOR_BASELINE)
ax.plot(years, robotics_cf, label="Robotics", linewidth=3, color=COLOR_ROBOTICS)
ax.yaxis.set_major_formatter(FuncFormatter(format_cad))
ax.set_xlabel("Year")
ax.set_ylabel("Cash Flow (CAD)")
ax.set_title("Annual Cash Flow Comparison")
ax.grid(True, linestyle="--", alpha=0.3)
ax.legend()
st.pyplot(fig)

fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.plot(years, np.cumsum(baseline_cf), label="Baseline", linewidth=3, color=COLOR_BASELINE)
ax2.plot(years, np.cumsum(robotics_cf), label="Robotics", linewidth=3, color=COLOR_ROBOTICS)
ax2.yaxis.set_major_formatter(FuncFormatter(format_cad))
ax2.set_xlabel("Year")
ax2.set_ylabel("Cumulative Cash Flow (CAD)")
ax2.set_title("Cumulative Cash Flow Comparison")
ax2.grid(True, linestyle="--", alpha=0.3)
ax2.legend()
st.pyplot(fig2)
