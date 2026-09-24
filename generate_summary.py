import pandas as pd
import json

df = pd.read_csv('dataset.csv')

# Precompute data for web app
summary = {
    "total": len(df),
    "retained": int((df['Exited'] == 0).sum()),
    "churned": int((df['Exited'] == 1).sum()),
    "churn_rate": round(float(df['Exited'].mean() * 100), 2),
    "by_country": {},
    "by_age": {},
    "by_gender": {},
    "by_products": {},
    "by_balance": {},
    "by_activity": {},
    "country_age_matrix": {}
}

# Country
for c in ['France', 'Germany', 'Spain']:
    sub = df[df['Geography'] == c]
    summary["by_country"][c] = {
        "count": len(sub),
        "churned": int(sub['Exited'].sum()),
        "churn_rate": round(float(sub['Exited'].mean() * 100), 2),
        "mean_balance": round(float(sub['Balance'].mean()), 2),
        "gri": round(float(sub['Exited'].mean() / df['Exited'].mean()), 2)
    }

# Age
def age_g(a):
    if a < 30: return '<30'
    elif a <= 45: return '30–45'
    elif a <= 60: return '46–60'
    else: return '60+'
df['AgeGroup'] = df['Age'].apply(age_g)

for a in ['<30', '30–45', '46–60', '60+']:
    sub = df[df['AgeGroup'] == a]
    summary["by_age"][a] = {
        "count": len(sub),
        "churned": int(sub['Exited'].sum()),
        "churn_rate": round(float(sub['Exited'].mean() * 100), 2)
    }

# Gender
for g in ['Female', 'Male']:
    sub = df[df['Gender'] == g]
    summary["by_gender"][g] = {
        "count": len(sub),
        "churned": int(sub['Exited'].sum()),
        "churn_rate": round(float(sub['Exited'].mean() * 100), 2)
    }

# Products
for p in [1, 2, 3, 4]:
    sub = df[df['NumOfProducts'] == p]
    summary["by_products"][p] = {
        "count": len(sub),
        "churned": int(sub['Exited'].sum()),
        "churn_rate": round(float(sub['Exited'].mean() * 100), 2)
    }

# Activity
for act, label in [(1, 'Active'), (0, 'Inactive')]:
    sub = df[df['IsActiveMember'] == act]
    summary["by_activity"][label] = {
        "count": len(sub),
        "churned": int(sub['Exited'].sum()),
        "churn_rate": round(float(sub['Exited'].mean() * 100), 2)
    }

# Balance
def bal_g(b):
    if b == 0: return 'Zero Balance'
    elif b < 119839.69: return 'Low Balance'
    else: return 'High Balance (≥€119.8k)'
df['BalanceSegment'] = df['Balance'].apply(bal_g)

for b in ['Zero Balance', 'Low Balance', 'High Balance (≥€119.8k)']:
    sub = df[df['BalanceSegment'] == b]
    summary["by_balance"][b] = {
        "count": len(sub),
        "churned": int(sub['Exited'].sum()),
        "churn_rate": round(float(sub['Exited'].mean() * 100), 2),
        "churned_balance_sum": round(float(sub[sub['Exited'] == 1]['Balance'].sum() / 1e6), 2)
    }

# Country x Age Matrix
for a in ['<30', '30–45', '46–60', '60+']:
    summary["country_age_matrix"][a] = {}
    for c in ['France', 'Germany', 'Spain']:
        sub = df[(df['AgeGroup'] == a) & (df['Geography'] == c)]
        rate = round(float(sub['Exited'].mean() * 100), 2) if len(sub) > 0 else 0
        summary["country_age_matrix"][a][c] = rate

# Sample 100 customers for drill down
sample_cust = df[['CustomerId', 'Geography', 'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'IsActiveMember', 'CreditScore', 'EstimatedSalary', 'Exited']].head(100).to_dict(orient='records')
summary["customer_sample"] = sample_cust

with open('summary_stats.json', 'w') as f:
    json.dump(summary, f, indent=2)

print("Saved summary_stats.json successfully!")
