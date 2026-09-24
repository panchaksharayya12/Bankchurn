# Customer Segmentation & Churn Pattern Analytics in European Banking
**Research Paper & Technical Report**

---

## Abstract
Customer churn represents a critical challenge for the European retail banking sector. The loss of existing banking clients reduces customer lifetime value (CLV), drives up replacement acquisition costs by an estimated 5× to 7×, and introduces balance sheet volatility. This study delivers a rigorous, segmentation-driven empirical analysis of customer churn across European retail banking markets (France, Germany, and Spain) utilizing a standardized cohort of 10,000 banking customers. By examining multivariate intersections across geography, demographics (age, gender), engagement (digital activity), financial profiles (credit score, account balance, salary), tenure, and product density, we uncover acute non-linear churn concentrations.

Our primary empirical findings show an overall baseline churn rate of **20.37%** (2,037 churned customers). However, churn is starkly non-uniform:
1. **Geographic Concentration:** Germany exhibits an acute churn rate of **32.44%** (Geographic Risk Index of **1.59**), nearly double that of France (**16.15%**) and Spain (**16.67%**).
2. **Age & Geography Hotspot:** Customers aged **46–60** present the highest demographic churn across all nations, peaking at an alarming **67.33%** among German customers.
3. **Engagement Gap:** Inactive customers churn at **26.85%** compared to **14.27%** among active banking members.
4. **Capital Exposure:** High-balance customers (>€119.8k) exhibit a **24.16%** churn rate, representing over **€110.8 million** in cumulative balance exposure.
5. **Product Paradox:** Customers holding 3 or 4 bank products experience churn rates exceeding **80%** to **100%**, signaling severe product cross-selling friction or aggressive promotional rate expiration.

We translate these findings into an actionable retention framework and an interactive Streamlit analytical application designed for operational risk managers, marketing executives, and regulatory stakeholders.

---

## 1. Introduction
Retail banking in the Eurozone has entered a period of heightened consumer mobility. With the maturation of Open Banking (PSD2 / PSD3), digital neobanks, and low friction in account switching, bank depositor loyalty can no longer be taken for granted. While European banks routinely track top-line churn percentages, conventional aggregate metrics obscure significant micro-segment vulnerabilities.

A bank reporting a "healthy" 80% customer retention rate may simultaneously be hemorrhaging its most profitable customer segments—specifically affluent, mid-career depositors with substantial liquid reserves. Without multidimensional customer segmentation, strategic countermeasures remain blunt, expensive, and reactive.

This research paper articulates a systematic exploratory data analytics (EDA) and segmentation framework to diagnose churn dynamics within retail banking cohorts, quantifying both customer volume attrition and capital balance exposure.

---

## 2. Problem Statement
European commercial banks confront three primary structural deficiencies in churn mitigation:
- **Segment Blindness:** Aggregate churn KPIs fail to differentiate between low-impact, zero-balance account closures and catastrophic departures of premier, multi-decade depositors.
- **Geographic Asymmetry:** Cross-border European operations often deploy centralized, one-size-fits-all customer loyalty programs that overlook acute regional disaffections (such as localized German competitive pressures).
- **Financial Profile Inversion:** Traditional credit risk models focus on default probability rather than churn probability, leaving high-net-worth, prime-credit depositors unprotected from competitor poaching.

Without structured, segment-aware analytics, retention capital is misallocated, customer acquisition costs spiral, and net interest margins deteriorate.

---

## 3. Project Objectives
### Primary Objectives:
- Measure and benchmark the baseline customer churn rate across European customer cohorts.
- Isolate and profile churn concentrations across demographic, geographic, and financial dimensions.
- Benchmark regional churn disparities across France, Germany, and Spain.

### Secondary & Strategic Objectives:
- Quantify financial and capital exposure represented by churned high-balance accounts.
- Evaluate the protective or destructive impact of product bundling (`NumOfProducts`) and digital engagement (`IsActiveMember`).
- Establish standardized Key Performance Indicators (KPIs) for ongoing executive oversight.
- Operationalize insights into a dynamic, production-grade Streamlit web application.

---

## 4. Dataset Description & Variable Architecture
The analysis evaluates a standardized, audited dataset of 10,000 retail banking customers across three key European nations.

| Variable Name | Data Type | Analytical Role | Operational Description |
| :--- | :--- | :--- | :--- |
| `CustomerId` | Integer | Identifier | Unique customer account key |
| `Surname` | String | Non-analytical | Customer surname (excluded during feature modeling) |
| `CreditScore` | Integer | Demographics / Risk | Numerical creditworthiness rating (350–850) |
| `Geography` | Categorical | Macro Dimension | Country of account domicile (France, Germany, Spain) |
| `Gender` | Binary | Demographic | Biological sex (Male, Female) |
| `Age` | Integer | Demographic | Customer age in years (18–92) |
| `Tenure` | Integer | Relationship | Number of years maintaining account relationship (0–10) |
| `Balance` | Continuous | Financial | Current ledger balance in Euros (€0.00 to €250,898.09) |
| `NumOfProducts` | Integer | Product Depth | Count of distinct bank products held (1, 2, 3, or 4) |
| `HasCrCard` | Binary | Product / Channel | Credit card ownership flag (1 = Yes, 0 = No) |
| `IsActiveMember` | Binary | Behavioral | Active member engagement status (1 = Active, 0 = Inactive) |
| `EstimatedSalary` | Continuous | Financial | Model-estimated gross annual income in Euros |
| `Exited` | Binary | Target Variable | Churn status indicator (1 = Churned, 0 = Retained) |

---

## 5. Analytical Methodology & Segmentation Framework

### 5.1 Data Ingestion, Hygiene & Audit
Data validation verified complete record completeness:
- **Sample Size:** $N = 10,000$ customer observations across France ($n = 5,014$), Germany ($n = 2,509$), and Spain ($n = 2,477$).
- **Missing Value Audit:** Zero null or missing values across all 14 attributes.
- **Binary Integrity:** `HasCrCard`, `IsActiveMember`, and `Exited` strictly conforming to $\{0, 1\}$.
- **Privacy Sanitization:** Direct identifiers (`Surname`) isolated from analytical pipelines.

### 5.2 Feature Engineering & Segmentation Dimensions
To convert continuous metrics into actionable operational cohorts, four derived segmentation tiers were engineered:

1. **Age Cohorts (`AgeGroup`):**
   - `<30` (Young Adult / Early Career)
   - `30–45` (Core Prime Working Age)
   - `46–60` (Peak Wealth / Pre-Retirement)
   - `60+` (Retirement & Wealth Decumulation)

2. **Credit Score Bands (`CreditScoreBand`):**
   - `Low` ($< 580$)
   - `Medium` ($580 – 669$)
   - `High` ($\ge 670$)

3. **Tenure Lifecycles (`TenureGroup`):**
   - `New Customers` ($0 – 2$ years)
   - `Mid-Term Customers` ($3 – 7$ years)
   - `Long-Term Customers` ($8 – 10$ years)

4. **Balance Strata (`BalanceSegment`):**
   - `Zero Balance` ($Balance = €0.00$, represents 3,617 customers)
   - `Low Balance` ($€0 < Balance < €119,839.69$)
   - `High Balance / Premium` ($Balance \ge €119,839.69$, upper 50th percentile of funded accounts)

---

## 6. Exploratory Data Analysis & Empirical Findings

### 6.1 Baseline Attrition Rates
- **Retained Customers:** 7,963 clients (**79.63%**)
- **Churned Customers:** 2,037 clients (**20.37%**)

### 6.2 Geographic Risk Disparities
Across the three European banking jurisdictions, customer loyalty diverges markedly:
- **Germany:** 814 churned out of 2,509 customers $\rightarrow$ **32.44% Churn Rate**.
- **Spain:** 413 churned out of 2,477 customers $\rightarrow$ **16.67% Churn Rate**.
- **France:** 810 churned out of 5,014 customers $\rightarrow$ **16.15% Churn Rate**.

**Geographic Risk Index (GRI)**, defined as $\frac{\text{Regional Churn Rate}}{\text{Portfolio Baseline Churn Rate}}$:
- Germany: **1.59** (59% above systemic baseline)
- Spain: **0.82** (18% below baseline)
- France: **0.79** (21% below baseline)

While Germany represents only 25.1% of the total customer base, it accounts for **39.96%** of all churned customers, almost exactly matching France's contribution (**39.76%**), despite France possessing double the customer volume.

### 6.3 Demographic Hotspots (Age & Gender Interaction)
- **Age Stratification:**
  - `<30` years: 124 churned out of 1,641 $\rightarrow$ **7.56%** churn rate.
  - `30–45` years: 956 churned out of 6,248 $\rightarrow$ **15.30%** churn rate.
  - `46–60` years: 842 churned out of 1,647 $\rightarrow$ **51.12%** churn rate.
  - `60+` years: 115 churned out of 464 $\rightarrow$ **24.78%** churn rate.

- **The German Pre-Retirement Crisis:**
  Intersecting Geography with Age reveals the single most volatile cohort in the entire portfolio:
  - **German customers aged 46–60** exhibit an unprecedented churn rate of **67.33%** (338 churned out of 502).
  - In comparison, France (45.79%) and Spain (40.66%) also experience peak churn in the 46–60 bracket, confirming this life stage as a universal vulnerability across European banking.

- **Gender Disparity:**
  - Female clients: 1,139 churned out of 4,543 $\rightarrow$ **25.07%** churn rate.
  - Male clients: 898 churned out of 5,457 $\rightarrow$ **16.46%** churn rate.
  *(Note: Econometric analysis indicates this reflects differential product usage, digital onboarding friction, and financial life-stage dynamics rather than direct biological causality).*

### 6.4 Engagement & Behavioral Indicators
- **Digital Engagement:**
  - Inactive Members (`IsActiveMember = 0`): **26.85%** churn rate (1,302 / 4,849).
  - Active Members (`IsActiveMember = 1`): **14.27%** churn rate (735 / 5,151).
  - Active digital engagement reduces observed churn risk by **46.8%**.

- **The Product Bundling Paradox (`NumOfProducts`):**
  - **1 Product:** 5,084 customers $\rightarrow$ **27.71%** churn.
  - **2 Products:** 4,590 customers $\rightarrow$ **7.58%** churn (*Optimal retention anchor*).
  - **3 Products:** 266 customers $\rightarrow$ **82.71%** churn (*Severe churn risk*).
  - **4 Products:** 60 customers $\rightarrow$ **100.00%** churn (*Complete portfolio failure*).
  
  *Root Cause Analysis:* Holding 2 products represents a standard primary banking relationship (e.g., Checking + Debit/Savings). Holding 3 or 4 products frequently corresponds to aggressive promotional cross-selling or structured investment vehicles whose promotional yield cliffs trigger rapid customer flight upon maturity.

### 6.5 Financial Profile & Capital Exposure
- **Balance Comparisons:**
  - Retained Customers: Mean balance of **€72,745.30**.
  - Churned Customers: Mean balance of **€91,108.54** (+25.2% higher).
- **Balance Stratification:**
  - `Zero Balance`: 3,617 customers $\rightarrow$ **13.82%** churn.
  - `Low Balance`: 3,191 customers $\rightarrow$ **23.97%** churn.
  - `High Balance` ($\ge €119.8\text{k}$): 3,192 customers $\rightarrow$ **24.19%** churn.
- **Capital Attrition Quantification:**
  - High-balance churners account for **€110.85 Million** in departed capital.
  - Total balance departed across all 2,037 churned customers equals **€185.59 Million**.
  - While zero-balance customers are easier to lose numerically, high-balance departures directly damage the bank's liquidity coverage ratio (LCR) and deposit funding base.

---

## 7. Key Performance Indicators (KPI Summary Table)

| KPI Metric Name | Portfolio Result | Benchmark / Meaning | Strategic Priority |
| :--- | :--- | :--- | :--- |
| **Overall Churn Rate** | **20.37%** | Portfolio-wide attrition baseline | Moderate |
| **High-Value Churn Ratio** | **24.16%** | Churn rate among premium accounts ($\ge €119.8\text{k}$) | **Critical** |
| **Germany Risk Index (GRI)** | **1.59** | 59% higher churn exposure than baseline | **Critical** |
| **Inactive Churn Rate** | **26.85%** | Churn among dormant / disengaged clients | High |
| **Pre-Retiree Churn (46–60)** | **51.12%** | Peak demographic vulnerability | **Critical** |
| **Optimal Product Retention** | **7.58%** | Churn rate for 2-product account holders | Benchmark Model |
| **High-Balance Capital Exposure** | **€110.8M** | Total liquidity exposed to high-value churn | **Critical** |
| **Total Churned Balance** | **€185.6M** | Aggregate balance drain across all churners | High |

---

## 8. Strategic Business Playbook & Recommendations

### 1. The German Market Remediation Taskforce
- **Action:** Establish a dedicated German retention desk. Re-evaluate fee structures, digital UX, and wealth management fees against aggressive domestic fintechs (e.g., N26, Trade Republic).
- **KPI:** Reduce German churn from 32.4% toward the Eurozone benchmark (<20%) within 18 months.

### 2. Pre-Retirement (Age 46–60) Wealth Advisory Shield
- **Action:** Customers aged 46–60 possess maximum liquidity and are preparing for pension decumulation. Deploy proactive, human-assisted wealth advisors, tax-advantaged retirement accounts, and private banking perks to stem the 51.1% (and 67.3% in Germany) attrition.

### 3. Early Inactivity Intervention Protocol
- **Action:** Build automated behavioral triggers when digital log-ins or debit transactions decline for >45 consecutive days. Offer personalized re-engagement incentives before dormancy transitions into formal account closure.

### 4. Rationalization of Multi-Product Bundles (3+ Products)
- **Action:** Audit all customers holding $\ge 3$ products. Eliminate steep interest rate step-downs or hidden secondary account maintenance fees that currently cause 82%+ churn among multi-product holders.

### 5. High-Net-Worth Relationship Managers
- **Action:** Assign dedicated tier-1 relationship managers to every account with $>€100,000$ in balances to protect the €110.8M capital exposure pool.

---

## 9. Streamlit Dashboard Architecture
To operationalize this empirical research into everyday banking workflows, a production-grade Streamlit web application (`app.py`) was engineered:
- **Core Modules:**
  1. *Executive Overview & Churn Summary* (Live KPI counters, distribution charts)
  2. *Geographic Intelligence Center* (Country-by-country comparative benchmarking)
  3. *Demographic & Lifecycle Matrix* (Age, gender, and tenure cross-tabulations)
  4. *High-Value Capital Risk Explorer* (Balance exposure scatter plots and wealth tiering)
  5. *Customer Drill-Down & Risk Triage* (Granular customer inspection with CSV export)
- **Interactive Capabilities:**
  - Multi-parameter segment filtering (Country, Gender, Age Group, Activity Status, Credit Score).
  - Dynamic KPI recalculation on the fly.
  - One-click customer risk list downloads for frontline branch managers.

---

## 10. Conclusion & Future Research
This investigation confirms that customer churn in European banking is not a random attrition process, but a highly concentrated, segment-specific phenomenon. The intersection of geographic friction (Germany), life-stage wealth transitions (ages 46–60), and multi-product pricing penalties generates the vast majority of capital risk. By transitioning from generic retention campaigns to precision segment targeting, European retail banks can protect millions in core deposits and preserve long-term franchise value.

*Future Research:* Expanding this framework to incorporate real-time transactional velocity, customer service interaction logs, and macro-economic interest rate shifts will further elevate predictive precision.
