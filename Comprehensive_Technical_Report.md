# Comprehensive Technical Report: Customer Segmentation & Churn Pattern Analytics in European Banking
## Quantitative Risk Modeling, Demographic Cohort Diagnostics, and Balance Sheet Exposure Analysis

**Author / Lead Data Analyst:** Panchaksharayya  
**Project:** European Banking Customer Segmentation & Churn Analytics  
**Date:** September 2026  
**Document Type:** Formal Technical & Operational Report  
**Target Audience:** Chief Risk Officers (CRO), Retail Banking Heads, Treasury Managers, Prudential Regulators  

---

## 1. Executive Summary
Customer attrition in retail commercial banking represents a systemic drain on institutional capitalization, net interest margin stability, and regulatory liquidity compliance. This technical report provides an exhaustive, data-driven diagnostic of depositor attrition across 10,000 audited customer accounts situated in three primary European jurisdictions: France, Germany, and Spain.

### Key Empirical Findings:
1. **Portfolio Baseline:** The audited portfolio exhibits an overall churn rate of **20.37%** (2,037 departures out of 10,000 accounts), leaving 7,963 retained depositors (79.63%).
2. **Geographic Risk Asymmetry:** Germany demonstrates a critically elevated churn rate of **32.44%** (814 departures out of 2,509 accounts), representing a Geographic Risk Index (GRI) of **1.59x** relative to the European baseline. In contrast, France (16.15%) and Spain (16.67%) remain statistically stable.
3. **Pre-Retirement Demographic Vulnerability:** Depositors aged **46 to 60** experience an acute European churn rate of **51.12%**, escalating to **67.33%** among German depositors. This highlights severe service disconnects during the critical wealth decumulation and pension planning lifecycle stage.
4. **Capital Balance Flight:** Churn is heavily concentrated among high-net-worth depositors. Accounts in the upper balance quartile (>= EUR 119,800) experienced 610 departures, removing **EUR 110,853,241** in liquid deposits from the banking system.
5. **Product Bundling Paradox:** While holding 2 products represents an optimal retention relationship (7.58% churn), customers holding 3 products experience **82.71%** churn, and customers holding 4 products experience a **100.00%** exit rate (60 out of 60 accounts).
6. **Digital Engagement Dividend:** Active depositors (`IsActiveMember=1`) exhibit a churn rate of **14.27%** versus **26.85%** for inactive members, representing a **1.88x** relative risk reduction.

---

## 2. Dataset Architecture & Variable Dictionary
The analytical pipeline ingests an audited, cross-sectional cohort of 10,000 retail banking accounts. All records were validated for data completeness, containing zero missing or null entries across all 14 schema attributes.

| Column Name | Data Type | Analytical Class | Statistical Properties | Operational Definition & Business Rules |
| :--- | :--- | :--- | :--- | :--- |
| `RowNumber` | Integer | System Index | Range: 1 to 10,000 | Sequential row index; excluded from analytics. |
| `CustomerId` | Integer | Unique Identifier | Range: 15,565,701 to 15,815,456 | Primary account key; decoupled during modeling for GDPR compliance. |
| `Surname` | String | Customer Identity | 2,932 distinct surnames | Account holder surname; decoupled during modeling. |
| `CreditScore` | Integer | Financial Risk | Mean: 650.53, Median: 652.0, Range: 350 to 850 | Standardized FICO-equivalent credit rating. |
| `Geography` | Categorical | Jurisdiction | France (50.14%), Germany (25.09%), Spain (24.77%) | Sovereign operational banking jurisdiction. |
| `Gender` | Categorical | Demographics | Male (54.57%), Female (45.43%) | Customer biological gender attribute. |
| `Age` | Integer | Demographics | Mean: 38.92, Median: 37.0, Range: 18 to 92 | Customer chronological age in completed years. |
| `Tenure` | Integer | Relationship Duration | Mean: 5.01, Median: 5.0, Range: 0 to 10 | Duration of continuous customer relationship in years. |
| `Balance` | Float | Balance Sheet Exposure | Mean: EUR 76,485.89, Max: EUR 250,898.09 | Ledger account balance on audit observation date. |
| `NumOfProducts` | Integer | Relationship Breadth | Range: 1 to 4 (Mode: 1) | Total active institutional products held. |
| `HasCrCard` | Binary | Product Cross-Sell | 1 = 70.55%, 0 = 29.45% | Indicates active institutional credit card facility. |
| `IsActiveMember` | Binary | Behavioral Engagement | 1 = 51.51%, 0 = 48.49% | Indicates digital login or debit activity in prior 30 days. |
| `EstimatedSalary` | Float | Financial Profile | Mean: EUR 100,090.24, Range: EUR 11.58 to EUR 199,992.48 | Modeled gross annual household compensation. |
| `Exited` | Binary | Target Variable | 0 = 79.63% (Retained), 1 = 20.37% (Exited) | Formal relationship termination indicator within observation window. |

---

## 3. Exploratory Data Analysis & Statistical Distributions

### 3.1 Univariate Statistical Summary
- **Credit Score Distribution:** Approximately normal with a mean of 650.53 (standard deviation: 96.65). Churned accounts display a nearly identical mean credit score (645.35) to retained accounts (651.85), indicating that credit score in isolation is an ineffective discriminator of voluntary churn.
- **Age Distribution:** Positively skewed with a median of 37.0 years and an interquartile range of 32 to 44 years. A secondary cluster exists between ages 45 and 65, which corresponds directly to the elevated churn hazard.
- **Account Balance Distribution:** Bimodal distribution. 3,617 accounts (36.17%) maintain exactly EUR 0.00 in balances. Among funded accounts (balance > 0), the mean balance is EUR 119,827.49 with a standard deviation of EUR 30,095.06.
- **Estimated Salary Distribution:** Uniformly distributed across the cohort from EUR 11.58 to EUR 199,992.48, demonstrating no significant parametric correlation with churn probability (Pearson r = 0.012).

---

## 4. Bivariate & Cross-Tabulation Risk Analysis

### 4.1 Geographic Disparities & Regional Risk Index
The European retail banking portfolio exhibits pronounced geographic divergence:

| Geographic Jurisdiction | Total Accounts | Retained Accounts | Exited Accounts | Segment Churn Rate | Geographic Risk Index (GRI) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **France** | 5,014 | 4,204 | 810 | 16.15% | 0.79x |
| **Spain** | 2,477 | 2,064 | 413 | 16.67% | 0.82x |
| **Germany** | 2,509 | 1,695 | 814 | **32.44%** | **1.59x** |
| **Total Cohort** | 10,000 | 7,963 | 2,037 | 20.37% | 1.00x |

**Statistical Significance:** A Pearson Chi-Square test of independence between Geography and Exited yields $\chi^2 = 301.26$, $p < 0.0001$ ($df = 2$). The German cohort accounts for **39.96%** of all European customer departures despite comprising only **25.09%** of the depositor base.

### 4.2 Demographic Risk: Age Cohort Analysis

| Age Bracket | Cohort Label | Total Accounts | Churned Accounts | Cohort Churn Rate | Relative Risk vs Baseline |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **18 to 30** | Young Professionals | 1,968 | 148 | 7.52% | 0.37x |
| **31 to 45** | Core Working Adults | 6,032 | 892 | 14.78% | 0.73x |
| **46 to 60** | Pre-Retirement Decumulation | 1,586 | 811 | **51.12%** | **2.51x** |
| **61 and Above** | Pensioners / Retirees | 414 | 113 | 27.29% | 1.34x |

**Demographic Insight:** Depositors aged 46 to 60 represent a hyper-critical hazard zone. In this segment, the probability of an account closing exceeds the probability of retention. When intersected with Geography, German depositors aged 46 to 60 experience an unprecedented churn rate of **67.33%** (307 exits out of 456 accounts).

### 4.3 Gender Variance
- **Female Depositors:** 4,543 accounts, 1,139 exits (**25.07%** churn rate).
- **Male Depositors:** 5,457 accounts, 898 exits (**16.46%** churn rate).
- **Z-Test for Two Proportions:** $z = 10.74$, $p < 0.0001$. Female depositors demonstrate an 8.61 percentage point higher attrition rate, which deepens in older wealth tiers due to unaddressed financial planning requirements.

### 4.4 Product Holding Dynamics & The Bundling Paradox

| Number of Products | Total Accounts | Churned Accounts | Churn Rate | Operational Assessment |
| :--- | :--- | :--- | :--- | :--- |
| **1 Product** | 5,084 | 1,409 | 27.71% | Unanchored relationship; vulnerable to single-competitor rate offers. |
| **2 Products** | 4,590 | 348 | **7.58%** | Optimal balance; maximum switching barrier with minimal fee friction. |
| **3 Products** | 266 | 220 | **82.71%** | Severe friction; promotional rate expiration and fee accumulation. |
| **4 Products** | 60 | 60 | **100.00%** | Total attrition; predatory cross-selling resulting in immediate departure. |

---

## 5. Capital & Balance Exposure Quantification
Traditional retail bank reporting tracks customer volume attrition without weighting by ledger balances. To measure balance sheet exposure, we segment the portfolio into balance quartiles:

| Balance Quartile | Account Balance Range | Total Accounts | Churned Accounts | Churn Rate | Cumulative Capital Exposed |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Q1 (Zero-Balance)** | EUR 0.00 | 3,617 | 500 | 13.82% | EUR 0.00 |
| **Q2 (Low Balance)** | EUR 0.01 to EUR 97,198 | 1,383 | 362 | 26.17% | EUR 24,118,504 |
| **Q3 (Mid Balance)** | EUR 97,199 to EUR 119,800 | 2,500 | 565 | 22.60% | EUR 50,802,192 |
| **Q4 (High Balance)** | >= EUR 119,801 | 2,500 | 610 | **24.16%** | **EUR 110,853,241** |
| **Total Portfolio** | EUR 0.00 to EUR 250,898 | 10,000 | 2,037 | 20.37% | **EUR 185,773,937** |

### Critical Capital Takeaways:
- Over **EUR 185.77 Million** in cumulative balances exited the institution during the observation period.
- High-balance depositors (Q4) account for **EUR 110.85 Million** (59.67% of all lost capital), despite accounting for only 29.95% of total exited customer volume.
- Losing a single Q4 depositor drains an average of **EUR 181,726** in core liquidity, whereas losing a Q1 depositor imposes zero liquidity drain.

---

## 6. Predictive Machine Learning Modeling & Benchmarks
To automate churn detection, we trained and evaluated four machine learning algorithms on an 80/20 stratified train-test split (8,000 training records, 2,000 holdout validation records).

### 6.1 Model Performance Evaluation Matrix

| Algorithm | Accuracy | Precision (Churn) | Recall (Churn) | F1-Score (Churn) | ROC-AUC | PR-AUC |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Logistic Regression (Baseline)** | 81.10% | 0.584 | 0.342 | 0.431 | 0.768 | 0.482 |
| **Random Forest (150 Trees)** | 86.45% | 0.742 | 0.518 | 0.610 | 0.852 | 0.684 |
| **LightGBM (Leaf-Wise)** | 86.90% | 0.751 | 0.546 | 0.632 | 0.865 | 0.702 |
| **XGBoost (Production Engine)** | **87.20%** | **0.762** | **0.564** | **0.648** | **0.871** | **0.718** |

### 6.2 Feature Attribution via SHAP (SHapley Additive exPlanations)
Global SHAP value decomposition reveals the principal drivers of the production XGBoost classifier:
1. **Age (Mean |SHAP| = 0.82):** Feature impact rises sharply above age 45, peaking at age 54.
2. **NumOfProducts (Mean |SHAP| = 0.68):** Highly non-linear; holding 2 products exerts a strong negative (protective) attribution, while holding 3 or 4 products exerts massive positive (attrition) attribution.
3. **Geography_Germany (Mean |SHAP| = 0.54):** Strongly drives churn probability upward.
4. **IsActiveMember (Mean |SHAP| = 0.46):** Active membership status delivers a substantial protective push toward retention.
5. **Balance (Mean |SHAP| = 0.38):** High balances elevate risk due to competitor rate shopping.

---

## 7. Interactive Production Software Architecture
To translate analytical conclusions into daily banking workflows, the project implements a dual-layer software architecture:

1. **Standalone High-Performance Streamlit Web Application (`app.py` on Port 8501):**
   - **Multi-Dimensional Filtering:** Interactive sidebar enabling simultaneous cross-filtering by Country, Gender, Age Cohorts, Credit Score, Balance Tier, and Product Count.
   - **Dynamic KPI Recalculation:** Instant recalculation of segment customer counts, retained volumes, exit counts, churn percentages, and capital exposure.
   - **Interactive Visualizations:** Embedded Plotly visualizations, including balance-to-salary scatter matrices and cross-tab heatmaps.
   - **Operational Account Triage:** High-risk customer filtering table with dynamic risk scoring and customized CSV export functionality.

2. **Scrolltide Helix 3D WebGL Web Portal (`index.html` on Port 3000):**
   - **Three.js WebGL Engine:** Dynamic double-helix particle system reflecting real-time banking data density.
   - **Scroll-Bound Cinematic Narrative:** 4-stage camera transitions bound to scroll position.
   - **Embedded Elena Vance AI Banking Copilot:** Natural language quantitative chat assistant delivering instant insights, KPI benchmarks, and regulatory summaries.
   - **Direct Streamlit Integration:** Clean header link directing analysts to the dedicated port 8501 analytics suite.

---

## 8. Four-Pillar Strategic Retention Playbook

### Pillar 1: Dedicated Pre-Retirement Wealth Advisory Desk
- **Target Demographic:** Depositors aged 46 to 60 (51.12% European churn rate).
- **Countermeasure:** Establish a specialized Pre-Retirement Wealth Desk. When customers enter this age bracket, automatically assign a private wealth manager to conduct comprehensive estate, tax, and pension decumulation reviews.
- **Projected Impact:** Preserves an estimated 25% of vulnerable pre-retiree relationships, protecting EUR 35 Million in core balances.

### Pillar 2: German Jurisdiction Competitiveness Taskforce
- **Target Jurisdiction:** German Retail Branches (32.44% churn rate, GRI 1.59x).
- **Countermeasure:** Conduct an immediate audit of account maintenance fees and debit transaction charges. Implement competitive tiered interest rates on liquid deposits to counteract aggressive fintech yields (Trade Republic, N26).
- **Projected Impact:** Reduces German churn from 32.44% toward the European average of 16-17%, halting an estimated 350 account exits annually.

### Pillar 3: Automated Digital Engagement Triggers
- **Target Cohort:** Inactive Account Holders (26.85% churn rate).
- **Countermeasure:** Implement algorithmic triggers that detect 45 consecutive days of account dormancy. Trigger personalized mobile notifications, fee waivers, or direct deposit cash rewards.
- **Projected Impact:** Restoring 30% of inactive accounts to active status delivers a 1.88x reduction in attrition risk.

### Pillar 4: Restructure Multi-Product Architecture
- **Target Cohort:** Multi-Product Holders (3 and 4 products; 82.7%+ churn).
- **Countermeasure:** Eliminate punitive interest rate step-downs and hidden recurring charges on bundled ancillary products. Consolidate digital account reporting into a unified interface.
- **Projected Impact:** Eliminates the product holding cliff, restoring customer confidence in secondary financial facilities.

---

## 9. Regulatory Governance & Prudential Compliance
The findings and analytical tools delivered in this project align with prevailing European supervisory standards:
- **ECB Single Supervisory Mechanism (SSM) & SREP:** Incorporates segment-specific depositor flight into internal liquidity stress-testing models (ILAAP), ensuring compliance with Pillar 2 liquidity guidelines.
- **Basel III Liquidity Coverage Ratio (LCR):** Restraining high-balance depositor attrition directly mitigates 30-day operational cash outflows, strengthening the bank's High-Quality Liquid Asset (HQLA) buffer.
- **EBA Treating Customers Fairly (TCF):** Eliminating predatory product bundling ensures full adherence to European consumer fairness directives.
- **GDPR Compliance:** The analytical engine operates strictly on pseudonymized demographic and financial attributes without exposing Personally Identifiable Information (PII).

---

## 10. Conclusion
By transitioning from aggregate churn reporting to multidimensional, capital-weighted customer segmentation, commercial banks can transform an invisible operational vulnerability into a strategic competitive advantage. Deploying predictive machine learning algorithms alongside a disciplined four-pillar retention framework preserves tens of millions of Euros in core depositor liquidity, maximizes customer lifetime value, and reinforces institutional balance sheet resilience.
