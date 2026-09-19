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

## 5. Risk Analysis Components
Duration
Duration measures the sensitivity of a bond's price to changes in interest rates.
Convexity
Convexity improves the estimation of bond price changes for larger interest-rate movements.
DV01
DV01 measures the approximate change in bond value for a one basis-point change in yield.
Key Rate Duration
Key Rate Duration analyzes sensitivity to movements at specific points of the yield curve.
Monte Carlo
Monte Carlo scenarios are used to analyze portfolio P&L under different yield-curve movements.
Stress Testing
Stress testing evaluates portfolio sensitivity under specified interest-rate shocks.
VaR and CVaR
VaR estimates potential loss at a selected confidence level.
CVaR estimates the average loss beyond the VaR threshold.
## 6. Machine Learning
The project includes a Random Forest regression model.
The implementation uses available bond risk variables to demonstrate the machine-learning workflow.
The current sample dataset contains only a small number of worked-example observations. Therefore, model performance should not be treated as statistically representative.
A larger actual bond dataset is required for meaningful model training and evaluation.
## 7. AI Risk Agent
The AI Risk Agent currently uses rule-based risk classification.
It classifies bonds into:
Low Risk
Medium Risk
High Risk
The classification is based on:
Modified Duration
Convexity
DV01
## 8. Dashboard
The Flask dashboard presents key portfolio metrics including:
Portfolio Market Value
Modified Duration
Convexity
DV01
Monte Carlo P&L
The dashboard provides a simple interface for viewing fixed-income portfolio risk information.
##9. Data Limitation
The project repository currently contains the supplied worked-example bond data.
The complete 300-bond portfolio and full historical yield-curve dataset are not included unless provided separately.
Therefore, historical yield-curve results and large-scale machine-learning performance should not be interpreted as final results until the complete datasets are available.
## 10. Conclusion
The project demonstrates a structured approach to fixed-income portfolio risk analysis using Python.
It combines financial risk metrics, scenario analysis, stress testing, machine learning, rule-based risk classification, and a web dashboard into one application.
