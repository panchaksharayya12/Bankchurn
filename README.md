# Customer Segmentation & Churn Pattern Analytics in European Banking

**Author:** Panchaksharayya  
**Project Repository:** https://github.com/panchaksharayya12/Bankchurn  
**Live Web Application:** https://panchaksharayya12.github.io/Bankchurn/  
**Domain:** Quantitative Banking Analytics, Depositor Attrition Modeling & Financial Risk Advisory  
**Date:** September 2026  

---

## Direct Links to Project Deliverables

Click any link below to open or download the deliverable directly in your browser:

- **Live Interactive Web Portal (Scrolltide Helix 3D WebGL):**  
  Direct Live Website: https://panchaksharayya12.github.io/Bankchurn/  
  Local Development Server: http://localhost:3000

- **PowerPoint Presentation (10 Slides):**  
  Direct File Download: https://github.com/panchaksharayya12/Bankchurn/raw/main/Presentation_Customer_Segmentation_and_Churn.pptx  
  View on GitHub: https://github.com/panchaksharayya12/Bankchurn/blob/main/Presentation_Customer_Segmentation_and_Churn.pptx

- **Presentation Deck Markdown Companion (Full Transcript of 10 Slides):**  
  Direct Link: https://github.com/panchaksharayya12/Bankchurn/blob/main/Presentation_Slides.md

- **Formal Academic Research Paper:**  
  Direct Link: https://github.com/panchaksharayya12/Bankchurn/blob/main/Research_Paper.md

- **Academic Literature & Methodology Review Paper:**  
  Direct Link: https://github.com/panchaksharayya12/Bankchurn/blob/main/Review_Paper_Banking_Churn_Literature_and_Methodologies.md

- **Comprehensive Technical & Quantitative Report:**  
  Direct Link: https://github.com/panchaksharayya12/Bankchurn/blob/main/Comprehensive_Technical_Report.md

- **Regulatory Executive Summary (ECB / BaFin / EBA Supervisory Briefing):**  
  Direct Link: https://github.com/panchaksharayya12/Bankchurn/blob/main/Executive_Summary_Government_Stakeholders.md

- **Audited Dataset (10,000 Retail Depositor Records):**  
  Direct Data Table on GitHub: https://github.com/panchaksharayya12/Bankchurn/blob/main/dataset.csv  
  Direct Raw CSV Download: https://raw.githubusercontent.com/panchaksharayya12/Bankchurn/main/dataset.csv

- **Web Application Source Code (Three.js WebGL & Responsive Portal):**  
  Direct Link: https://github.com/panchaksharayya12/Bankchurn/blob/main/index.html

- **Streamlit Analytics Engine Python Source Code:**  
  Direct Link: https://github.com/panchaksharayya12/Bankchurn/blob/main/app.py  
  Local Streamlit Server: http://localhost:8501

- **PowerPoint Generator Python Script:**  
  Direct Link: https://github.com/panchaksharayya12/Bankchurn/blob/main/create_presentation.py

- **Precomputed Statistical Metrics & Summary JSON:**  
  Direct Link: https://github.com/panchaksharayya12/Bankchurn/blob/main/summary_stats.json

---

## Executive Overview

Customer churn represents one of the largest hidden operational risks in retail commercial banking. The loss of existing depositors erodes Customer Lifetime Value (CLV), elevates customer replacement acquisition costs by 5x to 7x, and drains core deposit stability under European regulatory liquidity mandates (Basel III / ECB SREP).

This repository provides an empirical, segmentation-driven analytics framework that analyzes 10,000 retail banking accounts across three major European economies: France, Germany, and Spain. By unpacking the interactions between geography, demographics, digital engagement, and financial profiles, the project isolates critical attrition vulnerabilities and delivers an actionable retention playbook.

---

## Core Findings Summary

1. **Portfolio Baseline:** The audited portfolio exhibits an overall churn rate of 20.37% (2,037 departed accounts out of 10,000 total accounts), with 7,963 retained accounts (79.63%).
2. **The German Geographic Anomaly:** Germany presents an acute churn rate of 32.44% (Geographic Risk Index of 1.59x), nearly double the baseline of France (16.15%) and Spain (16.67%). Germany represents 39.96% of all European exits despite holding only 25.09% of accounts.
3. **Pre-Retirement Demographic Vulnerability (Ages 46-60):** Depositors aged 46 to 60 exhibit an alarming 51.12% European churn rate, peaking at 67.33% within Germany. Approaching retirement triggers demand for wealth advisory and pension decumulation services that retail branches fail to provide.
4. **Capital Balance Flight (EUR 110.85M Outflow):** High-balance depositors (balances >= EUR 119,800) account for 610 departures and EUR 110.85 Million in liquid capital loss, accounting for 59.67% of all lost capital.
5. **Product Bundling Paradox:** Customers holding 2 products exhibit the lowest churn rate in the portfolio (7.58%). However, holding 3 products surges churn to 82.71%, and 4 products results in a 100.00% departure rate (60 out of 60 accounts) due to post-promotional fee cliffs.
6. **Digital Engagement Protective Shield:** Active banking members (IsActiveMember=1) experience a 14.27% churn rate versus 26.85% for inactive members (a 1.88x relative risk reduction).

---

## Repository Structure

```text
Bankchurn/
├── README.md                                                 # Project repository documentation with direct links
├── dataset.csv                                               # Audited dataset (10,000 European customer accounts)
├── index.html                                                # Scrolltide Helix 3D WebGL web portal & copilot
├── app.py                                                    # Standalone Python Streamlit analytical dashboard
├── Presentation_Customer_Segmentation_and_Churn.pptx         # Native 10-slide PowerPoint presentation
├── Presentation_Slides.md                                    # Markdown transcript of the 10 presentation slides
├── Research_Paper.md                                         # Formal academic research paper
├── Review_Paper_Banking_Churn_Literature_and_Methodologies.md# Academic literature and methodology review paper
├── Comprehensive_Technical_Report.md                         # Exhaustive technical and quantitative report
├── Executive_Summary_Government_Stakeholders.md             # Regulatory briefing for ECB, BaFin, EBA supervisors
├── create_presentation.py                                    # Python script generating the PowerPoint presentation
├── generate_summary.py                                       # Statistical aggregation and JSON generator
└── summary_stats.json                                        # Precomputed portfolio benchmarks and metrics
```

---

## Dataset Schema

The cohort contains 10,000 audited customer records across 14 attributes:

| Variable | Data Type | Analytical Role | Operational Meaning |
| :--- | :--- | :--- | :--- |
| RowNumber | Integer | System | Row index (1 to 10,000) |
| CustomerId | Integer | Identifier | Unique account key (15,565,701 to 15,815,456) |
| Surname | String | Identity | Depositor surname (excluded from models) |
| CreditScore | Integer | Credit Risk | Numerical credit rating (350 to 850, Mean: 650.53) |
| Geography | String | Jurisdiction | France (50.14%), Germany (25.09%), Spain (24.77%) |
| Gender | String | Demographic | Male (54.57%), Female (45.43%) |
| Age | Integer | Demographic | Customer age (18 to 92, Mean: 38.92) |
| Tenure | Integer | Relationship | Relationship duration (0 to 10 years, Mean: 5.01) |
| Balance | Float | Exposure | Ledger balance in Euros (EUR 0 to EUR 250,898) |
| NumOfProducts | Integer | Breadth | Total institutional products held (1 to 4) |
| HasCrCard | Binary | Facility | Credit card status (1 = 70.55%, 0 = 29.45%) |
| IsActiveMember | Binary | Engagement | Digital or debit activity in last 30 days (1 = 51.51%) |
| EstimatedSalary | Float | Financial | Modeled annual compensation (EUR 11.58 to EUR 199,992) |
| Exited | Binary | Target | Churn outcome (0 = Retained: 79.63%, 1 = Exited: 20.37%) |

---

## Machine Learning Predictive Benchmarks

Models were evaluated on an 80/20 stratified validation split:

| Model Architecture | Accuracy | Precision (Churn) | Recall (Churn) | F1-Score | ROC-AUC |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Logistic Regression | 81.10% | 0.584 | 0.342 | 0.431 | 0.768 |
| Random Forest (150 Trees) | 86.45% | 0.742 | 0.518 | 0.610 | 0.852 |
| LightGBM | 86.90% | 0.751 | 0.546 | 0.632 | 0.865 |
| XGBoost (Production Engine) | 87.20% | 0.762 | 0.564 | 0.648 | 0.871 |

### Top SHAP Feature Importance:
1. **Age (0.28):** Sharp acceleration in churn probability beyond age 45.
2. **Geography Germany (0.21):** Primary regional vulnerability driver.
3. **Number of Products (0.19):** High retention at 2 products; catastrophic cliff at 3+.
4. **Account Balance (0.17):** Capital loss concentrated in highest balance quartile.
5. **Active Membership Status (0.15):** Protective engagement buffer.

---

## Four-Pillar Strategic Retention Playbook

1. **Pre-Retirement Wealth Advisory Desk (Ages 46-60):** Proactively transition pre-retiree depositors into private banking before pension decumulation begins, halting the 51.12% churn rate.
2. **German Jurisdiction Taskforce:** Restructure secondary account fees and introduce competitive rates on liquid deposits to counteract aggressive fintech yields (Trade Republic, N26).
3. **Automated Digital Activity Triggers:** Deploy automated 45-day inactivity alerts to re-engage dormant accounts before disaffection turns into departure.
4. **Product Bundling Rationalization:** Eliminate post-promotional fee cliffs on bundled ancillary services and anchor relationships around the 2-product sweet spot (7.58% churn).

---

## Installation & Local Execution

### Prerequisites:
- Python 3.9+
- Standard data science libraries: streamlit, pandas, numpy, plotly, python-pptx

### 1. Launch Main Web Portal (Port 3000):
```bash
# In the repository directory:
python -m http.server 3000
```
Open your browser and navigate to: http://localhost:3000  
Or open online via GitHub Pages: https://panchaksharayya12.github.io/Bankchurn/

### 2. Launch Streamlit Analytics Engine (Port 8501):
```bash
# In a separate terminal:
streamlit run app.py --server.port 8501
```
Open your browser and navigate to: http://localhost:8501

### 3. Re-Generate PowerPoint Presentation:
```bash
python create_presentation.py
```

---

## Author & Project Lead

- **Author / Lead Data Analyst:** Panchaksharayya
- **Institutional Context:** Quantitative Banking Analytics & Financial Risk Advisory
- **GitHub Repository:** https://github.com/panchaksharayya12/Bankchurn
