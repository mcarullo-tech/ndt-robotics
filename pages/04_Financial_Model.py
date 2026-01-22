"""Interactive financial model: Baseline vs. Robotics scenarios."""

import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pandas as pd

from utils import set_page, add_footer

set_page()

st.title("💰 Interactive Financial Model")
st.markdown("Baseline vs. Robotics scenarios — adjust assumptions to explore sensitivity")
st.divider()

with st.expander("⚙️ Customize Assumptions (Edit & Explore)", expanded=True):
    tab_baseline, tab_robotics, tab_assumptions = st.tabs(["📋 Baseline Scenario", "🤖 Robotics Scenario", "⚠️ Risk Factors"])
    
    with tab_baseline:
        st.markdown("**Current State: Manual AU-E (No Investment)**")
        col_base1, col_base2 = st.columns(2)
        with col_base1:
            baseline_jobs = st.slider(
                "Jobs per year (manual)",
                min_value=5, max_value=30, value=12,
                help="Constrained by manual labor availability"
            )
            baseline_rev = st.slider(
                "Revenue per job (CAD)",
                min_value=50_000, max_value=200_000, value=120_000,
                step=5_000,
                help="Typical AU-E service rate"
            )
        with col_base2:
            baseline_exp = st.slider(
                "Expense per job (CAD)",
                min_value=10_000, max_value=100_000, value=40_000,
                step=5_000,
                help="Labor, equipment, overhead allocation"
            )
            baseline_shrink = st.slider(
                "Annual growth rate (%)",
                min_value=-20, max_value=20, value=-5,
                help="Without robotics, manual services typically decline"
            ) / 100

    with tab_robotics:
        st.markdown("**Investment Case: Two-Stage Robotics Implementation**")
        col_stage1, col_stage2 = st.columns(2)
        
        with col_stage1:
            st.markdown("**Stage 1: Impactor Tooling**")
            stage1_cost = st.number_input(
                "Stage 1 investment (CAD)",
                value=100_000,
                help="Precision impactor system: $100K baseline"
            )
            stage1_duration = st.slider(
                "Stage 1 duration (years)",
                min_value=0.1, max_value=2.0, value=0.5,
                step=0.1,
                help="6 months typical deployment"
            )
            uplift1 = st.slider(
                "Uplift after Stage 1 (%)",
                min_value=0, max_value=100, value=20,
                help="Typical: +20% throughput from improved consistency"
            ) / 100
        
        with col_stage2:
            st.markdown("**Stage 2: Full Robotic Platform**")
            stage2_cost = st.number_input(
                "Stage 2 investment (CAD)",
                value=300_000,
                help="Full robotic system: $300K baseline"
            )
            stage2_duration = st.slider(
                "Stage 2 duration (years)",
                min_value=0.5, max_value=3.0, value=1.5,
                step=0.1,
                help="12-18 months typical development & deployment"
            )
            uplift2 = st.slider(
                "Uplift after Stage 2 (%)",
                min_value=0, max_value=200, value=70,
                help="Typical: +50-70% throughput from full automation + premium pricing"
            ) / 100
        
        col_econ1, col_econ2 = st.columns(2)
        with col_econ1:
            rev_growth = st.slider(
                "Revenue growth post-robotics (%)",
                min_value=0, max_value=20, value=5,
                help="Premium pricing + market demand expansion"
            ) / 100
        with col_econ2:
            exp_reduction = st.slider(
                "Operating expense reduction (%)",
                min_value=0, max_value=50, value=25,
                help="Automation reduces cost-per-job by ~25-30%"
            ) / 100
    
    with tab_assumptions:
        st.markdown("""
        ### Key Risk Factors & Sensitivities
        
        **Our model assumes:**
        - Stage 1 delivers on technical specs (±2% force consistency)
        - Stage 2 achieves 70% capacity uplift (realistic for industrial automation)
        - Market tolerates 5-10% pricing premium for robotic systems
        - No major disruption to AU-E demand (mature market, stable)
        - Development timelines hold ±3 months
        
        **Model is most sensitive to:**
        1. **Job volume** — baseline forecast critical
        2. **Revenue per job** — pricing assumptions
        3. **Stage 2 uptime** — deployment delays push payback 6-12 months
        
        **Use the main sliders to stress-test these assumptions.**
        """)
    
    st.divider()
    discount_rate = st.slider(
        "💰 Discount rate for NPV calculation (%)",
        min_value=0, max_value=20, value=8,
        help="WACC proxy — 8% is typical for growth businesses"
    ) / 100

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

def calculate_irr(cashflows):
    """Calculate IRR using numpy-financial equivalent (simple bisection method)."""
    # Try to find IRR using Newton's method approximation
    try:
        from numpy_financial import irr
        irr_value = irr(cashflows)
        return irr_value if not np.isnan(irr_value) else None
    except:
        # Fallback: simple bisection method if numpy_financial not available
        def npv_at_rate(rate, cf):
            return np.sum(cf / (1 + rate)**np.arange(len(cf)))
        
        try:
            # Find IRR by bisection
            low, high = -0.99, 1.0
            for _ in range(100):
                mid = (low + high) / 2
                if npv_at_rate(mid, cashflows) > 0:
                    high = mid
                else:
                    low = mid
            return high if abs(npv_at_rate(high, cashflows)) < 1000 else None
        except:
            return None

baseline_cf = baseline_cash_flow()
robotics_cf = robotics_cash_flow()

baseline_npv = npv(baseline_cf, discount_rate)
robotics_npv = npv(robotics_cf, discount_rate)

baseline_irr = calculate_irr(baseline_cf)
robotics_irr = calculate_irr(robotics_cf)

COLOR_BASELINE = '#0066CC'
COLOR_ROBOTICS = '#00C851'
COLOR_NEUTRAL = '#999999'

def format_cad(x, pos):
    """Format axis labels as CAD currency."""
    if x >= 1_000_000:
        return f"${x/1_000_000:.1f}M"
    elif x >= 1_000:
        return f"${x/1_000:.0f}K"
    else:
        return f"${x:.0f}"

st.divider()
st.subheader("📊 Financial Results")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(
        "Baseline NPV (5yr)",
        f"${round(baseline_npv/1000)*1000:,.0f}",
        help="Present value of manual AU-E, no investment"
    )
with col2:
    st.metric(
        "Robotics NPV (5yr)",
        f"${round(robotics_npv/1000)*1000:,.0f}",
        help="Present value of robotics investment strategy"
    )
with col3:
    npv_uplift = robotics_npv - baseline_npv
    st.metric(
        "NPV Uplift",
        f"${round(npv_uplift/1000)*1000:,.0f}",
        delta=f"+{round((npv_uplift/baseline_npv)*100)}%" if baseline_npv > 0 else "N/A",
        help="Value created by robotics investment"
    )

col4, col5, col6 = st.columns(3)
with col4:
    baseline_irr_pct = baseline_irr * 100 if baseline_irr else None
    st.metric(
        "Baseline IRR",
        f"{baseline_irr_pct:.1f}%" if baseline_irr_pct else "N/A",
        help="Internal Rate of Return for manual AU-E scenario"
    )
with col5:
    robotics_irr_pct = robotics_irr * 100 if robotics_irr else None
    st.metric(
        "Robotics IRR",
        f"{robotics_irr_pct:.1f}%" if robotics_irr_pct else "N/A",
        help="Internal Rate of Return for robotics investment scenario"
    )
with col6:
    if baseline_irr_pct and robotics_irr_pct:
        irr_diff = robotics_irr_pct - baseline_irr_pct
        st.metric(
            "IRR Improvement",
            f"{irr_diff:+.1f}%",
            help="IRR advantage of robotics scenario"
        )
    else:
        st.metric("IRR Improvement", "N/A")

tab1, tab2, tab3 = st.tabs(["Annual Cash Flow", "Cumulative Cash Flow", "Summary Table"])

with tab1:
    st.markdown("**Annual Operating Cash Flow: Baseline vs. Robotics**")
    fig, ax = plt.subplots(figsize=(14, 6))
    
    # Add stage indicators
    ax.axvspan(0, stage1_duration, alpha=0.1, color='#FF6B6B', label='Stage 1: Impactor')
    ax.axvspan(stage1_duration, stage2_duration, alpha=0.1, color='#FFA500', label='Stage 2: Full Robot')
    
    # Plot lines with professional styling
    ax.plot(years, baseline_cf, label="Baseline (Manual)", linewidth=4, marker='o', markersize=10,
            color=COLOR_BASELINE, markerfacecolor=COLOR_BASELINE, markeredgewidth=2, markeredgecolor='white')
    ax.plot(years, robotics_cf, label="Robotics Scenario", linewidth=4, marker='s', markersize=10,
            color=COLOR_ROBOTICS, markerfacecolor=COLOR_ROBOTICS, markeredgewidth=2, markeredgecolor='white')
    
    # Break-even line
    ax.axhline(y=0, color='#333333', linestyle='-', linewidth=2, alpha=0.8, zorder=1)
    
    ax.set_title("Annual Operating Cash Flow Comparison", fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel("Year", fontsize=12, fontweight='bold')
    ax.set_ylabel("Annual Cash Flow (CAD)", fontsize=12, fontweight='bold')
    ax.yaxis.set_major_formatter(FuncFormatter(format_cad))
    ax.set_xticks([0, 1, 2, 3, 4, 5])
    ax.set_xticklabels(['Year 0', 'Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5'])
    
    ax.grid(True, linestyle="--", alpha=0.25, linewidth=0.8)
    ax.legend(fontsize=11, loc='best', framealpha=0.98, shadow=True, edgecolor='black', ncol=2)
    
    # Professional styling
    fig.patch.set_facecolor('white')
    ax.set_facecolor('#f5f5f5')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    st.pyplot(fig)
    
    st.markdown("""**Interpretation:**
    - Baseline: Flat or declining (mature manual service)
    - Robotics: Ramps up as stages complete, then outperforms baseline significantly
    - **Green shading**: Stage 1 deployment period
    - **Orange shading**: Stage 2 development/deployment period
    - Dashed line: Break-even point ($0 cash flow)
    """)

with tab2:
    st.markdown("**Cumulative Cash Flow: The Payback Story**")
    cumsum_baseline = np.cumsum(baseline_cf)
    cumsum_robotics = np.cumsum(robotics_cf)
    
    fig2, ax2 = plt.subplots(figsize=(14, 6))
    
    # Add stage indicators
    ax2.axvspan(0, stage1_duration, alpha=0.1, color='#FF6B6B', label='Stage 1: Impactor')
    ax2.axvspan(stage1_duration, stage2_duration, alpha=0.1, color='#FFA500', label='Stage 2: Full Robot')
    
    # Area fills for context
    ax2.fill_between(years, cumsum_baseline, alpha=0.15, color=COLOR_BASELINE)
    ax2.fill_between(years, cumsum_robotics, alpha=0.15, color=COLOR_ROBOTICS)
    
    # Plot lines with professional styling
    ax2.plot(years, cumsum_baseline, label="Baseline (Manual)", linewidth=4, marker='o', markersize=10,
             color=COLOR_BASELINE, markerfacecolor=COLOR_BASELINE, markeredgewidth=2, markeredgecolor='white')
    ax2.plot(years, cumsum_robotics, label="Robotics Scenario", linewidth=4, marker='s', markersize=10,
             color=COLOR_ROBOTICS, markerfacecolor=COLOR_ROBOTICS, markeredgewidth=2, markeredgecolor='white')
    
    # Bold break-even line
    ax2.axhline(y=0, color='#333333', linestyle='-', linewidth=2.5, alpha=0.8, zorder=2)
    
    # Highlight payback with improved visualization
    for i in range(len(years)-1):
        if cumsum_robotics[i] < 0 and cumsum_robotics[i+1] > 0:
            payback_year = years[i] + (abs(cumsum_robotics[i]) / (cumsum_robotics[i+1] - cumsum_robotics[i]))
            # Large circle at payback
            ax2.plot(payback_year, 0, marker='o', markersize=16, color='#FF3B30', zorder=5, 
                    markeredgewidth=3, markeredgecolor='#8B0000')
            ax2.annotate(
                f'💰 Payback: Yr {payback_year:.1f}',
                xy=(payback_year, 0),
                xytext=(payback_year + 0.6, cumsum_robotics[-1]*0.35),
                arrowprops=dict(arrowstyle='->', color='#FF3B30', lw=2.5),
                fontsize=11,
                fontweight='bold',
                color='#FF3B30',
                bbox=dict(boxstyle='round,pad=0.6', facecolor='#FFFF00', alpha=0.85, edgecolor='#FF3B30', linewidth=2)
            )
            break
    
    ax2.set_title("Cumulative Cash Flow: Payback Timeline", fontsize=16, fontweight='bold', pad=20)
    ax2.set_xlabel("Year", fontsize=12, fontweight='bold')
    ax2.set_ylabel("Cumulative Cash Flow (CAD)", fontsize=12, fontweight='bold')
    ax2.yaxis.set_major_formatter(FuncFormatter(format_cad))
    ax2.set_xticks([0, 1, 2, 3, 4, 5])
    ax2.set_xticklabels(['Year 0', 'Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5'])
    
    ax2.grid(True, linestyle="--", alpha=0.25, linewidth=0.8)
    ax2.legend(fontsize=11, loc='upper left', framealpha=0.98, shadow=True, edgecolor='black', ncol=2)
    
    # Professional styling
    fig2.patch.set_facecolor('white')
    ax2.set_facecolor('#f5f5f5')
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    
    plt.tight_layout()
    st.pyplot(fig2)
    st.markdown("""**Key Takeaway:**
    - **Red shaded area**: Negative cumulative cash flow (recovery period with investment)
    - **Green shaded area**: Positive cumulative cash flow (profit zone)
    - **Bold line**: Break-even point - crossing this is payback
    - **Green shading on X-axis**: Stage 1 deployment (6 months)
    - **Orange shading on X-axis**: Stage 2 development/deployment (12-18 months)
    - **Red circle**: Exact payback point when investment is fully recovered
    """)

with tab3:
    st.markdown("**Financial Summary Table**")
    
    summary_data = {
        "Year": [int(y) for y in years],
        "Baseline CF (K)": [f"${x/1000:.0f}" for x in baseline_cf],
        "Robotics CF (K)": [f"${x/1000:.0f}" for x in robotics_cf],
        "Cumsum Baseline (K)": [f"${x/1000:.0f}" for x in np.cumsum(baseline_cf)],
        "Cumsum Robotics (K)": [f"${x/1000:.0f}" for x in np.cumsum(robotics_cf)],
    }
    
    df_summary = pd.DataFrame(summary_data)
    st.dataframe(df_summary, use_container_width=True, hide_index=True)

st.divider()
add_footer()
