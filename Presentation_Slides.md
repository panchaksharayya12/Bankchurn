# Customer Segmentation and Churn Pattern Analytics in European Banking
## Executive Slide Presentation Deck (10 Slides)
**Presenter / Author:** Panchaksharayya  
**Affiliation:** Quantitative Banking Analytics & Financial Risk Advisory  
**Date:** September 2026  
**File Reference:** `Presentation_Customer_Segmentation_and_Churn.pptx`

---

## Slide 1: Title Slide

### Customer Segmentation and Churn Pattern Analytics in European Banking
*Empirical Analysis of Depositor Attrition, Demographic Vulnerabilities, and Capital Balance Flight Across 10,000 European Retail Accounts*

- **Author / Lead Analyst:** Panchaksharayya
- **Institutional Context:** Quantitative Banking Analytics & Financial Risk Advisory
- **Scope:** European Retail Banking (France, Germany, Spain)
- **Cohort Size:** 10,000 Audited Customer Accounts

---

## Slide 2: Executive Summary and Project Objectives

### Industry Context and Strategic Challenge
- **Rising Attrition in European Retail Banking:** Open Banking regulations (PSD2/PSD3) and aggressive fintech challenger banks have lowered account migration friction across the Eurozone.
- **The Limitations of Aggregate Metrics:** Standard enterprise reporting tracks aggregate churn (~20%), obscuring catastrophic flight within ultra-profitable micro-segments.
- **Balance Sheet and Liquidity Impact:** Customer attrition destroys Customer Lifetime Value (CLV), inflates replacement customer acquisition costs by 5x to 7x, and drains core deposit stability under Basel III Liquidity Coverage Ratio (LCR) guidelines.

### Primary Research and Analytical Scope
- **Empirical Baseline Quantification:** Conduct an exhaustive audit of 10,000 retail banking accounts across France, Germany, and Spain to establish empirical churn baselines.
- **Multi-Dimensional Segmentation:** Evaluate intersecting customer profiles spanning Geography, Age, Gender, Balance Tiers, Digital Engagement, and Product Breadth.
- **Capital Exposure Modeling:** Quantify exact Euro-denominated liquidity flight across high-balance account tiers rather than relying strictly on account counts.
- **Operational Deployment:** Formulate a concrete 4-Pillar Strategic Retention Playbook and deploy an interactive production scoring engine.

---

## Slide 3: Dataset Architecture and Exploratory Portfolio Overview

### Key Performance Indicators (Portfolio Level)
- **Total Depositor Records:** 10,000 audited accounts
- **Overall Churn Rate:** 20.37% (2,037 exited depositors)
- **Total Retained Cohort:** 79.63% (7,963 active depositors)
- **Portfolio Balance Audited:** EUR 764.86 Million (Mean: EUR 76,486)

### Feature Architecture & Data Validation
- **Demographic Attributes:** Age (18 to 92, Mean: 38.9), Gender (54.6% Male, 45.4% Female).
- **Geographic Jurisdictions:** France (5,014), Germany (2,509), Spain (2,477).
- **Credit Risk Profile:** Credit Score ranging from 350 to 850 (Mean: 650.5).
- **Relationship Tenure:** Customer tenure spans from 0 to 10 years (Mean: 5.0).
- **Product Density:** Holding between 1 and 4 institutional products.
- **Zero Missing Values:** Full completeness across all 10,000 rows and 14 raw variables.
- **Zero-Balance Depositor Cohort:** 36.17% (3,617 accounts) maintain 0.00 EUR balance (predominantly in France and Spain).

---

## Slide 4: Geographic Variance and the German Attrition Anomaly

### Regional Performance Summary
- **France:** 5,014 accounts | 16.15% churn rate | 810 departures | Geographic Risk Index (GRI): 0.79x (Stable Baseline)
- **Spain:** 2,477 accounts | 16.67% churn rate | 413 departures | Geographic Risk Index (GRI): 0.82x (Stable Cohort)
- **Germany:** 2,509 accounts | 32.44% churn rate | 814 departures | Geographic Risk Index (GRI): 1.59x (Critical Risk Zone)

### Root Drivers of the German Banking Disparity
- **Volume Disproportion:** Germany contains only 25.09% of the customer base but accounts for 39.96% of all European churned depositors.
- **Interest Rate & Yield Sensitivity:** German retail depositors demonstrate rapid deposit reallocation toward high-yield digital neobanks (such as N26, Trade Republic, and ING DiBa).
- **Compounded Demographic Risk:** German depositors aged 46 to 60 experience a staggering 67.33% churn rate, representing the single highest risk intersection in the entire dataset.
- **Operational Implication:** A uniform European retention strategy is inherently flawed. Germany requires a dedicated regional retention desk and tailored yield preservation offerings.

---

## Slide 5: Demographic Vulnerability and the Pre-Retirement Crisis

### Churn Rate Distribution by Age Cohort
- **Age 18 to 30 (Young Professionals):** 1,968 accounts | 7.52% churn rate
- **Age 31 to 45 (Career Accumulators):** 6,032 accounts | 14.78% churn rate
- **Age 46 to 60 (Pre-Retirement Decumulation):** 1,586 accounts | 51.12% churn rate (Critical Attrition)
- **Age 61 and Above (Retirees / Pensioners):** 414 accounts | 27.29% churn rate

### Behavioral & Financial Drivers (Age 46-60)
- **Peak Net Worth Phase:** Depositors aged 46 to 60 control peak career earnings, substantial mortgage equity, and major investment portfolios.
- **Pension & Decumulation Planning:** Approaching retirement creates demand for consolidated wealth advisory, private banking services, and estate planning—services retail branches fail to provide.
- **Heightened Fee Sensitivity:** Unlike younger digital customers who tolerate account maintenance fees, pre-retirees actively switch institutions to eliminate custodial drag.
- **Gender Disparity Finding:** Female depositors in this bracket churn at 56.4% compared to 45.8% for males, indicating unmet needs in advisory engagement.

---

## Slide 6: Wealth Tier Dynamics and Capital Exposure Analysis

### Balance Tier Segmentation & Capital Flight
- **Zero-Balance Cohort (EUR 0.00):** 3,617 accounts | 13.82% churn rate | 500 exits | EUR 0.00 capital exposed
- **Moderate Balance (EUR 1 - 119.8k):** 3,883 accounts | 23.87% churn rate | 927 exits | EUR 74.92 Million capital exposed
- **Premier Capital Tier (>= EUR 119.8k):** 2,500 accounts | 24.16% churn rate | 610 exits | EUR 110.85 Million capital exposed

### Systemic Liquidity and Balance Sheet Vulnerability
- **The Fallacy of Unweighted Churn:** Traditional head-count metrics treat a 0.00 EUR balance account departure identically to a 200,000 EUR wealth exit.
- **EUR 110.85M Flight in Top Quartile:** 610 churned depositors held balances exceeding 119.8k EUR, pulling over 110.85 Million EUR in liquid deposits out of the institution.
- **LCR and Funding Stability Risk:** Under Basel III and ECB guidelines, rapid run-off of retail operational deposits strains short-term liquidity buffers and raises wholesale borrowing costs.

---

## Slide 7: Digital Engagement and the Product Bundling Paradox

### The Multi-Product Bundling Paradox
- **1 Product (Single Relationship):** 5,084 accounts | 27.71% churn rate
- **2 Products (Optimal Relationship):** 4,590 accounts | 7.58% churn rate (Lowest Attrition)
- **3 Products (Severe Attrition):** 266 accounts | 82.71% churn rate (Exited)
- **4 Products (Complete Catastrophe):** 60 accounts | 100.00% churn rate (60/60 Exited)

### Operational Explanation & Engagement Gap
- **Why 3 & 4 Products Collapse:** Aggressive promotional cross-selling packages teaser-rate cards, credit lines, and insurance. When introductory discounts expire, accumulated multi-product fees trigger abrupt relationship cancellations.
- **Customer Fatigue & Administrative Friction:** Managing disparate statements, regulatory disclaimers, and conflicting account minimums generates negative customer sentiment.
- **Digital Engagement Dividend:** Active members (`IsActiveMember=1`) churn at 14.27% compared to 26.85% for inactive members—a 1.88x relative risk reduction.
- **Strategic Sweet Spot:** Maintaining 2 deeply integrated core products maximizes switching barriers without inducing fee fatigue.

---

## Slide 8: Predictive Modeling and Machine Learning Benchmarks

### Model Evaluation on 80/20 Stratified Validation Split
- **Logistic Regression (Baseline):** Accuracy: 81.1% | ROC-AUC: 0.768 | Recall (Churn): 34.2%
- **Random Forest Classifier:** Accuracy: 86.4% | ROC-AUC: 0.852 | Recall (Churn): 51.8%
- **LightGBM Gradient Booster:** Accuracy: 86.9% | ROC-AUC: 0.865 | Recall (Churn): 54.6%
- **XGBoost Classifier (Production):** Accuracy: 87.2% | ROC-AUC: 0.871 | Recall (Churn): 56.4% | F1-Score: 0.638

### Top Model Feature Importance (SHAP / Gini)
1. **Age (Weight: 0.28):** Non-linear escalation between ages 45 and 60.
2. **Geography Germany (Weight: 0.21):** Primary geographical exit predictor.
3. **Number of Products (Weight: 0.19):** Severe cliff at 3+ products.
4. **Account Balance (Weight: 0.17):** Flight concentration in top quartile.
5. **Active Membership Status (Weight: 0.15):** Strong retention shield.

### Operational Triage Integration
- **Real-Time Streamlit Scoring:** Deployed via Python/Streamlit engine on port 8501.
- **Risk Stratification:** Scores depositors into Low (<20%), Medium (20-50%), and Critical (>50%) flight hazard buckets.
- **Batch Export:** Generates actionable CSV rosters for branch manager interventions.
- **Intervention Window:** Triggers retention actions 60-90 days prior to formal account closure.

---

## Slide 9: Four-Pillar Strategic Retention Playbook

### Pillar 1: Pre-Retirement Wealth Advisory Desk
- **Target:** Depositors aged 46 to 60 (51.12% Churn)
- Assign dedicated private wealth relationship managers before depositors enter pension decumulation.
- Bundle tax optimization, estate structuring, and preferential term deposit yields.
- Counteract female pre-retiree attrition (56.4%) with personalized wealth planning seminars.

### Pillar 2: German Jurisdiction Taskforce
- **Target:** German Depositors (32.44% Churn)
- Audit secondary account maintenance fees and debit card surcharges.
- Introduce competitive rate tiers on core liquid savings to defend against neobanks.
- Establish localized Berlin/Munich customer retention desks with fast-track escalation.

### Pillar 3: Digital Activity Incentivization
- **Target:** Inactive Accounts (26.85% Churn)
- Deploy automated 45-day inactivity alerts across mobile app and debit transactions.
- Offer direct deposit cashback incentives and recurring bill pay setup rewards.
- Transition passive single-product depositors into daily operational bank users.

### Pillar 4: Product Bundling Rationalization
- **Target:** 3+ Product Holders (82.7%+ Churn)
- Eliminate punitive post-promotional fee cliffs on bundled credit and insurance lines.
- Consolidate account statements into unified digital relationship overviews.
- Focus relationship growth on the 2-product sweet spot (7.58% churn) rather than forced cross-selling.

---

## Slide 10: Regulatory Governance, Economic Impact and Conclusions

### Regulatory & Supervisory Alignment
- **ECB SREP & ICAAP Integration:** European Central Bank supervisors evaluate operational deposit stability under Pillar 2 capital guidelines. Segment-specific depositor flight must be integrated into liquidity stress testing.
- **Basel III Liquidity Standards (LCR & NSFR):** Mitigating the EUR 110.85M flight among high-balance retail depositors directly strengthens the 30-day Liquidity Coverage Ratio buffer.
- **Consumer Protection & TCF Compliance:** Eliminating deceptive teaser rates and multi-product fee cliffs ensures strict compliance with European Banking Authority (EBA) Treating Customers Fairly principles.
- **GDPR Compliant Architecture:** Predictive modeling and scoring are conducted on pseudonymized data pipelines without PII exposure.

### Economic Value & Project Conclusions
- **Projected Economic Return:** A 15% reduction in high-balance attrition preserves an estimated EUR 16.6 Million in core liquidity and EUR 1.8 Million in annual net interest income.
- **Executive Transformation:** Shifts banking management from passive reactive attrition reporting to proactive, algorithmic depositor relationship preservation.
- **Repository Artifacts:** Complete audited codebase, interactive Helix web portal, Streamlit analytical app, research papers, and technical reports available in the repository.
- **Lead Analyst:** Panchaksharayya | Quantitative Banking Analytics & Financial Risk Advisory
