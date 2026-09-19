# Convexity & Sensitivity AI Agent

## 1. Project Overview

The Convexity & Sensitivity AI Agent is a fixed-income portfolio risk analysis project.

It analyzes bond portfolio sensitivity to changes in interest rates and yield curves.

The project includes:

- Bond portfolio analysis
- Duration analysis
- Convexity analysis
- DV01 analysis
- Bond pricing
- Key Rate Duration
- Yield curve analysis
- Monte Carlo scenario analysis
- Stress testing
- VaR and CVaR
- Machine Learning
- Risk classification
- Flask dashboard

---

## 2. Objectives

The main objectives are:

1. Analyze bond portfolio risk.
2. Measure interest-rate sensitivity.
3. Calculate duration and convexity.
4. Analyze DV01 exposure.
5. Perform stress testing.
6. Analyze Monte Carlo scenarios.
7. Calculate VaR and CVaR.
8. Apply machine learning techniques.
9. Classify bond risk levels.
10. Present results through a dashboard.

---

## 3. Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Matplotlib
- Flask
- HTML
- CSS
- GitHub

---

## 4. Project Structure

```text
Convexity-Sensitivity-AI-Agent/
│
├── README.md
├── app.py
├── requirements.txt
│
├── data/
│   ├── bond_portfolio.csv
│   ├── yield_curve_history.csv
│   └── monte_carlo_scenarios.csv
│
├── src/
│   ├── duration_convexity.py
│   ├── monte_carlo.py
│   ├── yield_curve.py
│   ├── krd_analysis.py
│   ├── bond_pricing.py
│   ├── var_cvar.py
│   ├── ml_model.py
│   ├── stress_testing.py
│   └── ai_risk_agent.py
│
└── templates/
    └── dashboard.html
