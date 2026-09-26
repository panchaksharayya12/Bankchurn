import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# Set page configuration
st.set_page_config(
    page_title="European Banking Churn Analytics",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for App-like experience
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.05rem;
        color: #475569;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border-radius: 12px;
        padding: 18px 20px;
        color: white;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        border: 1px solid rgba(255,255,255,0.1);
    }
    .metric-title {
        font-size: 0.82rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #94a3b8;
        font-weight: 600;
    }
    .metric-value {
        font-size: 1.85rem;
        font-weight: 700;
        margin-top: 4px;
        margin-bottom: 2px;
        color: #ffffff;
    }
    .metric-delta {
        font-size: 0.8rem;
        font-weight: 500;
    }
    .delta-high { color: #f87171; }
    .delta-low { color: #4ade80; }
    .delta-neutral { color: #cbd5e1; }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 10px 18px;
        border-radius: 8px;
        font-weight: 600;
    }
    div[data-testid="stSidebar"] {
        background-color: #f8fafc;
        border-right: 1px solid #e2e8f0;
    }
</style>
""", unsafe_allow_html=True)

# Data Loading with Cache
@st.cache_data
def load_and_preprocess_data():
    csv_path = Path(__file__).parent / "dataset.csv"
    if not csv_path.exists():
        # Fallback to current working directory
        csv_path = Path("dataset.csv")
    
    df = pd.read_csv(csv_path)
    
    # Feature Engineering
    # 1. Age Segmentation
    def categorize_age(age):
        if age < 30: return '<30'
        elif age <= 45: return '30–45'
        elif age <= 60: return '46–60'
        else: return '60+'
    df['AgeGroup'] = df['Age'].apply(categorize_age)
    
    # 2. Credit Score Bands
    def categorize_credit(score):
        if score < 580: return 'Low (<580)'
        elif score <= 669: return 'Medium (580-669)'
        else: return 'High (670+)'
    df['CreditScoreBand'] = df['CreditScore'].apply(categorize_credit)
    
    # 3. Tenure Lifecycles
    def categorize_tenure(t):
        if t <= 2: return 'New (0-2 yrs)'
        elif t <= 7: return 'Mid-term (3-7 yrs)'
        else: return 'Long-term (8-10 yrs)'
    df['TenureGroup'] = df['Tenure'].apply(categorize_tenure)
    
    # 4. Balance Segments
    # Zero: 0, Low: 0 < Balance < 119839.69, High: >= 119839.69
    high_bal_threshold = 119839.69
    def categorize_balance(b):
        if b == 0: return 'Zero Balance'
        elif b < high_bal_threshold: return 'Low Balance'
        else: return 'High Balance (≥€119.8k)'
    df['BalanceSegment'] = df['Balance'].apply(categorize_balance)
    
    # Labels
    df['ChurnLabel'] = df['Exited'].map({0: 'Retained', 1: 'Churned'})
    df['ActiveLabel'] = df['IsActiveMember'].map({1: 'Active', 0: 'Inactive'})
    df['CardLabel'] = df['HasCrCard'].map({1: 'Credit Card Holder', 0: 'No Card'})
    
    return df

df_raw = load_and_preprocess_data()

# Baseline Portfolio Constants
TOTAL_BASE_CUSTOMERS = len(df_raw)
BASE_CHURN_RATE = df_raw['Exited'].mean() * 100

# ================= SIDEBAR FILTERS =================
with st.sidebar:
    st.image("https://img.icons8.com/isometric/100/bank-building.png", width=64)
    st.markdown("### **Filter Controls**")
    st.caption("Refine customer segments across multiple dimensions.")
    
    # Geography
    all_geos = sorted(df_raw['Geography'].unique())
    selected_geos = st.multiselect("Geography", all_geos, default=all_geos)
    
    # Gender
    all_genders = sorted(df_raw['Gender'].unique())
    selected_genders = st.multiselect("Gender", all_genders, default=all_genders)
    
    # Activity
    all_activity = ['Active', 'Inactive']
    selected_activity = st.multiselect("Membership Status", all_activity, default=all_activity)
    
    # Age Groups
    age_order = ['<30', '30–45', '46–60', '60+']
    selected_age = st.multiselect("Age Cohort", age_order, default=age_order)
    
    # Balance Tier
    bal_order = ['Zero Balance', 'Low Balance', 'High Balance (≥€119.8k)']
    selected_balance = st.multiselect("Balance Segment", bal_order, default=bal_order)
    
    # Credit Score Band
    credit_order = ['Low (<580)', 'Medium (580-669)', 'High (670+)']
    selected_credit = st.multiselect("Credit Score Band", credit_order, default=credit_order)
    
    # Number of products
    all_prods = sorted(df_raw['NumOfProducts'].unique())
    selected_prods = st.multiselect("Bank Products Owned", all_prods, default=all_prods)
    
    st.markdown("---")
    if st.button("Reset All Filters", use_container_width=True):
        st.rerun()

# Apply Filters
df = df_raw[
    (df_raw['Geography'].isin(selected_geos)) &
    (df_raw['Gender'].isin(selected_genders)) &
    (df_raw['ActiveLabel'].isin(selected_activity)) &
    (df_raw['AgeGroup'].isin(selected_age)) &
    (df_raw['BalanceSegment'].isin(selected_balance)) &
    (df_raw['CreditScoreBand'].isin(selected_credit)) &
    (df_raw['NumOfProducts'].isin(selected_prods))
]

# Calculate Filtered Metrics
filtered_count = len(df)
if filtered_count > 0:
    filtered_churned = df['Exited'].sum()
    filtered_retained = filtered_count - filtered_churned
    filtered_churn_rate = (filtered_churned / filtered_count) * 100
    
    # High Value exposure in filtered view
    high_bal_churned = df[(df['BalanceSegment'] == 'High Balance (≥€119.8k)') & (df['Exited'] == 1)]
    high_bal_exposure = high_bal_churned['Balance'].sum() / 1e6
    
    # High value churn ratio in filtered view
    high_bal_total = len(df[df['BalanceSegment'] == 'High Balance (≥€119.8k)'])
    high_bal_churn_rate = (len(high_bal_churned) / high_bal_total * 100) if high_bal_total > 0 else 0
    
    # Germany Risk Index
    de_df = df[df['Geography'] == 'Germany']
    de_churn_rate = (de_df['Exited'].mean() * 100) if len(de_df) > 0 else 0
    de_risk_index = (de_churn_rate / BASE_CHURN_RATE) if BASE_CHURN_RATE > 0 else 0
else:
    filtered_churned = 0
    filtered_retained = 0
    filtered_churn_rate = 0
    high_bal_exposure = 0
    high_bal_churn_rate = 0
    de_risk_index = 0

# ================= MAIN HEADER =================
st.markdown('<div class="main-header">Customer Segmentation & Churn Pattern Analytics</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">European Banking Quantitative Attrition & Depositor Risk Intelligence Platform</div>', unsafe_allow_html=True)

# Top Dynamic KPIs Row
kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

with kpi1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Filtered Customers</div>
        <div class="metric-value">{filtered_count:,}</div>
        <div class="metric-delta delta-neutral">{filtered_count/TOTAL_BASE_CUSTOMERS*100:.1f}% of total portfolio</div>
    </div>
    """, unsafe_allow_html=True)

with kpi2:
    churn_diff = filtered_churn_rate - BASE_CHURN_RATE
    delta_class = "delta-high" if churn_diff > 0 else "delta-low"
    diff_sign = "+" if churn_diff > 0 else ""
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Observed Churn Rate</div>
        <div class="metric-value">{filtered_churn_rate:.2f}%</div>
        <div class="metric-delta {delta_class}">{diff_sign}{churn_diff:.2f}% vs baseline (20.37%)</div>
    </div>
    """, unsafe_allow_html=True)

with kpi3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">High-Value Churn Rate</div>
        <div class="metric-value">{high_bal_churn_rate:.2f}%</div>
        <div class="metric-delta delta-high">Accounts ≥ €119.8k</div>
    </div>
    """, unsafe_allow_html=True)

with kpi4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Germany Risk Index</div>
        <div class="metric-value">{de_risk_index:.2f}×</div>
        <div class="metric-delta delta-high">{'+59% excess risk' if de_risk_index > 1 else 'Within baseline'}</div>
    </div>
    """, unsafe_allow_html=True)

with kpi5:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">High-Balance Exposure</div>
        <div class="metric-value">€{high_bal_exposure:.1f}M</div>
        <div class="metric-delta delta-neutral">Capital at risk ({len(high_bal_churned)} accounts)</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

if filtered_count == 0:
    st.warning("⚠️ No customers match the selected filter criteria. Please broaden your selection in the sidebar.")
    st.stop()

# Navigation Tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "Churn Overview",
    "Geographic Analysis",
    "Demographics & Tenure",
    "High-Value & Products",
    "Customer Drill-Down",
    "Full Research Paper",
    "️ Supervisory Briefing"
])

# ================= TAB 1: CHURN OVERVIEW =================
with tab1:
    st.subheader("Executive Churn & Portfolio Retention Summary")
    st.markdown("Comprehensive view of retail customer retention dynamics and primary attrition vectors.")
    
    col_a, col_b = st.columns([1.1, 1.4])
    
    with col_a:
        # Donut Chart
        labels = ['Retained', 'Churned']
        values = [filtered_retained, filtered_churned]
        colors = ['#10b981', '#ef4444']
        
        fig_donut = go.Figure(data=[go.Pie(
            labels=labels,
            values=values,
            hole=0.62,
            marker_colors=colors,
            textinfo='label+percent',
            insidetextorientation='horizontal',
            hoverinfo='label+value+percent'
        )])
        fig_donut.update_layout(
            title_text="Portfolio Retention vs Churn Distribution",
            title_x=0.1,
            height=360,
            margin=dict(t=50, b=20, l=20, r=20),
            showlegend=True,
            legend=dict(orientation="h", yanchor="bottom", y=-0.1, xanchor="center", x=0.5)
        )
        st.plotly_chart(fig_donut, use_container_width=True)
    
    with col_b:
        st.markdown("#### Primary Empirical Drivers Identified")
        st.markdown("""
        - **German Jurisdictional Fragility:** Germany generates **32.44%** churn (GRI 1.59), contributing **39.96%** of all churned clients despite representing only 25% of customers.
        - **Pre-Retirement Vulnerability (46–60):** The 46–60 age group registers an unprecedented **51.12%** churn portfolio-wide, and surges to **67.33%** in Germany.
        - ⚡ **Digital Dormancy Penalty:** Inactive members exhibit **26.85%** churn versus **14.27%** for active members—a **46.8% reduction in churn** when digital engagement is maintained.
        - ⚠️ **The Multi-Product Paradox:** Holding 2 products provides peak retention (**7.58%** churn), while holding 3 or 4 products triggers catastrophic flight (**82.7%** and **100%** churn respectively).
        - **High-Value Capital Drain:** Churned high-balance accounts account for **€110.85M** in departed balances, threatening core deposit stability.
        """)

    st.markdown("---")
    st.markdown("#### KPI Summary Scorecard")
    kpi_summary = pd.DataFrame({
        "KPI Name": [
            "Overall Churn Rate",
            "High-Value Churn Ratio",
            "Germany Geographic Risk Index (GRI)",
            "Inactive Member Churn Rate",
            "Active Member Churn Rate",
            "Pre-Retiree Churn Rate (46–60)",
            "High-Balance Capital Exposure"
        ],
        "Portfolio Result": [
            "20.37%",
            "24.16%",
            "1.59",
            "26.85%",
            "14.27%",
            "51.12%",
            "€110.85 Million"
        ],
        "Strategic Meaning": [
            "Baseline attrition across all 10,000 customers",
            "Observed churn among accounts with balance ≥ €119.8k",
            "Germany churn rate relative to overall portfolio baseline",
            "Observed churn among digitally inactive account holders",
            "Observed churn among digitally engaged account holders",
            "Peak demographic attrition rate across Europe",
            "Aggregate balance drain across churned high-balance accounts"
        ]
    })
    st.dataframe(kpi_summary, use_container_width=True, hide_index=True)

# ================= TAB 2: GEOGRAPHIC ANALYSIS =================
with tab2:
    st.subheader("Geographic Churn Benchmarking: France, Germany & Spain")
    
    geo_stats = df.groupby('Geography').agg(
        Total=('Exited', 'count'),
        Churned=('Exited', 'sum'),
        ChurnRate=('Exited', lambda x: x.mean() * 100),
        MeanBalance=('Balance', 'mean')
    ).reset_index()
    geo_stats['GRI'] = geo_stats['ChurnRate'] / BASE_CHURN_RATE
    geo_stats['ChurnContribution'] = (geo_stats['Churned'] / geo_stats['Churned'].sum() * 100) if geo_stats['Churned'].sum() > 0 else 0

    c1, c2 = st.columns(2)
    with c1:
        fig_geo_rate = px.bar(
            geo_stats,
            x='Geography',
            y='ChurnRate',
            color='Geography',
            color_discrete_map={'France': '#3b82f6', 'Germany': '#ef4444', 'Spain': '#f59e0b'},
            text=geo_stats['ChurnRate'].apply(lambda x: f"{x:.2f}%"),
            title="Observed Churn Rate by Country (%)"
        )
        fig_geo_rate.add_hline(y=BASE_CHURN_RATE, line_dash="dash", line_color="black", annotation_text="Baseline (20.37%)")
        fig_geo_rate.update_layout(height=380, showlegend=False)
        st.plotly_chart(fig_geo_rate, use_container_width=True)

    with c2:
        fig_geo_contrib = px.pie(
            geo_stats,
            names='Geography',
            values='Churned',
            color='Geography',
            color_discrete_map={'France': '#3b82f6', 'Germany': '#ef4444', 'Spain': '#f59e0b'},
            title="Share of Total Churned Customers (%)",
            hole=0.45
        )
        fig_geo_contrib.update_layout(height=380)
        st.plotly_chart(fig_geo_contrib, use_container_width=True)

    st.markdown("#### Geographic Risk Summary")
    st.dataframe(
        geo_stats.style.format({
            'Total': '{:,.0f}',
            'Churned': '{:,.0f}',
            'ChurnRate': '{:.2f}%',
            'MeanBalance': '€{:,.2f}',
            'GRI': '{:.2f}×',
            'ChurnContribution': '{:.2f}%'
        }),
        use_container_width=True,
        hide_index=True
    )

# ================= TAB 3: DEMOGRAPHICS & TENURE =================
with tab3:
    st.subheader("Demographic & Lifecycle Patterns")
    
    col_d1, col_d2 = st.columns(2)
    
    with col_d1:
        # Age group churn
        age_stats = df.groupby('AgeGroup', observed=True).agg(
            Total=('Exited', 'count'),
            ChurnRate=('Exited', lambda x: x.mean() * 100)
        ).reindex(age_order).reset_index()
        
        fig_age = px.bar(
            age_stats,
            x='AgeGroup',
            y='ChurnRate',
            color='ChurnRate',
            color_continuous_scale='Reds',
            text=age_stats['ChurnRate'].apply(lambda x: f"{x:.2f}%"),
            title="Churn Rate by Age Group (%)"
        )
        fig_age.update_layout(height=360, coloraxis_showscale=False)
        st.plotly_chart(fig_age, use_container_width=True)
    
    with col_d2:
        # Gender Churn
        gender_stats = df.groupby('Gender').agg(
            Total=('Exited', 'count'),
            ChurnRate=('Exited', lambda x: x.mean() * 100)
        ).reset_index()
        
        fig_gender = px.bar(
            gender_stats,
            x='Gender',
            y='ChurnRate',
            color='Gender',
            color_discrete_map={'Female': '#ec4899', 'Male': '#3b82f6'},
            text=gender_stats['ChurnRate'].apply(lambda x: f"{x:.2f}%"),
            title="Churn Rate by Gender (%)"
        )
        fig_gender.update_layout(height=360, showlegend=False)
        st.plotly_chart(fig_gender, use_container_width=True)

    st.markdown("#### Geography × Age Cohort Cross-Tabulation (The German 46–60 Hotspot)")
    heatmap_data = df.pivot_table(index='AgeGroup', columns='Geography', values='Exited', aggfunc=lambda x: x.mean() * 100).reindex(age_order)
    
    fig_heat = px.imshow(
        heatmap_data,
        labels=dict(x="Country", y="Age Cohort", color="Churn Rate (%)"),
        x=heatmap_data.columns,
        y=heatmap_data.index,
        color_continuous_scale="YlOrRd",
        text_auto=".1f",
        title="Cross-Jurisdictional Churn Matrix: Geography vs Age Cohort (%)"
    )
    fig_heat.update_layout(height=360)
    st.plotly_chart(fig_heat, use_container_width=True)
    
    st.info("**Key Finding:** German customers aged 46–60 exhibit an alarming **67.33% churn rate**, making this sub-segment the single highest churn concentration across all retail banking operations.")

# ================= TAB 4: HIGH VALUE & PRODUCTS =================
with tab4:
    st.subheader("High-Value Depositor Risk & The Product Paradox")
    
    c_p1, c_p2 = st.columns(2)
    
    with c_p1:
        # Product Churn Paradox
        prod_stats = df.groupby('NumOfProducts').agg(
            Count=('Exited', 'count'),
            ChurnRate=('Exited', lambda x: x.mean() * 100)
        ).reset_index()
        
        fig_prod = px.bar(
            prod_stats,
            x='NumOfProducts',
            y='ChurnRate',
            color='ChurnRate',
            color_continuous_scale='Reds',
            text=prod_stats['ChurnRate'].apply(lambda x: f"{x:.1f}%"),
            title="The Product Paradox: Churn Rate by Number of Bank Products (%)"
        )
        fig_prod.update_layout(height=360, coloraxis_showscale=False)
        st.plotly_chart(fig_prod, use_container_width=True)
        st.caption("2 products deliver peak loyalty (7.58% churn). 3 products churn at 82.7%, and 4 products churn at 100%.")

    with c_p2:
        # Balance Segment Churn
        bal_stats = df.groupby('BalanceSegment', observed=True).agg(
            Count=('Exited', 'count'),
            ChurnRate=('Exited', lambda x: x.mean() * 100)
        ).reindex(bal_order).reset_index()
        
        fig_bal = px.bar(
            bal_stats,
            x='BalanceSegment',
            y='ChurnRate',
            color='BalanceSegment',
            color_discrete_sequence=['#94a3b8', '#38bdf8', '#f97316'],
            text=bal_stats['ChurnRate'].apply(lambda x: f"{x:.2f}%"),
            title="Churn Rate by Balance Segment (%)"
        )
        fig_bal.update_layout(height=360, showlegend=False)
        st.plotly_chart(fig_bal, use_container_width=True)

    st.markdown("#### High-Value Depositors: Balance vs Estimated Salary Distribution")
    scatter_sample = df.sample(min(1500, len(df)), random_state=42)
    fig_scatter = px.scatter(
        scatter_sample,
        x='EstimatedSalary',
        y='Balance',
        color='ChurnLabel',
        color_discrete_map={'Retained': '#10b981', 'Churned': '#ef4444'},
        size='Age',
        hover_data=['Geography', 'CreditScore', 'NumOfProducts'],
        title="Depositor Ledger: Balance vs Annual Salary (Sampled, Colored by Churn)",
        labels={'EstimatedSalary': 'Estimated Annual Salary (€)', 'Balance': 'Account Balance (€)'}
    )
    fig_scatter.update_layout(height=420)
    st.plotly_chart(fig_scatter, use_container_width=True)

# ================= TAB 5: CUSTOMER DRILL-DOWN =================
with tab5:
    st.subheader("Customer Level Risk Triage & Data Drill-Down")
    st.markdown("Filter and export high-risk accounts for branch-level retention outreach.")
    
    triage_col1, triage_col2 = st.columns([1, 2])
    with triage_col1:
        only_high_risk = st.checkbox("Show Only Critical Priority Accounts (Germany + Age 46–60 or Balance ≥ €120k Churned)", value=False)
    
    if only_high_risk:
        display_df = df[((df['Geography'] == 'Germany') & (df['AgeGroup'] == '46–60')) | ((df['BalanceSegment'] == 'High Balance (≥€119.8k)') & (df['Exited'] == 1))]
    else:
        display_df = df
        
    st.markdown(f"**Showing {len(display_df):,} matching customer accounts:**")
    
    preview_cols = ['CustomerId', 'Geography', 'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'IsActiveMember', 'CreditScore', 'EstimatedSalary', 'ChurnLabel']
    st.dataframe(display_df[preview_cols], use_container_width=True, height=400)
    
    # CSV Download
    csv_data = display_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Filtered Customer Dataset (CSV)",
        data=csv_data,
        file_name="european_banking_churn_filtered.csv",
        mime="text/csv",
        use_container_width=True
    )

# ================= TAB 6: FULL RESEARCH PAPER =================
with tab6:
    st.subheader("Complete Research Paper & Analytical Methodology")
    research_paper_path = Path(__file__).parent / "Research_Paper.md"
    if research_paper_path.exists():
        with open(research_paper_path, 'r', encoding='utf-8') as f:
            paper_content = f.read()
        st.markdown(paper_content)
    else:
        st.info("Research paper markdown file is located at `Research_Paper.md` in the project root.")

# ================= TAB 7: SUPERVISORY BRIEFING =================
with tab7:
    st.subheader("Supervisory Executive Briefing for Government & Regulatory Bodies")
    exec_summary_path = Path(__file__).parent / "Executive_Summary_Government_Stakeholders.md"
    if exec_summary_path.exists():
        with open(exec_summary_path, 'r', encoding='utf-8') as f:
            exec_content = f.read()
        st.markdown(exec_content)
    else:
        st.info("Executive summary markdown file is located at `Executive_Summary_Government_Stakeholders.md` in the project root.")

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: #94a3b8; font-size: 0.85rem;'>© 2026 European Central Banking Research · Customer Segmentation & Churn Analytics Platform · Built for Production Deployment</div>", unsafe_allow_html=True)
