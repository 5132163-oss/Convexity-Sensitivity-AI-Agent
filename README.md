# Convexity & Sensitivity AI Agent

## Fixed-Income Portfolio Risk Analysis System

### Project Information

**Project Name:** Convexity & Sensitivity AI Agent  
**Student:** Yogita Patil  
**Course:** B.Sc. Computer Science  
**Academic Year:** 2026–2027  

---

## 1. Project Overview

The Convexity & Sensitivity AI Agent is a Python-based fixed-income portfolio risk analysis system.

The project analyzes the sensitivity of bond portfolios to changes in interest rates and yield curves.

It combines financial risk analysis, scenario analysis, machine learning, rule-based risk classification, and a Flask web dashboard.

---

## 2. Objectives

- Analyze bond portfolio risk.
- Calculate Modified Duration.
- Calculate Convexity.
- Analyze DV01.
- Perform Key Rate Duration analysis.
- Analyze yield-curve movements.
- Perform Monte Carlo scenario analysis.
- Perform interest-rate stress testing.
- Calculate VaR and CVaR.
- Demonstrate machine-learning workflow.
- Classify bond risk levels.
- Present portfolio metrics through a dashboard.

---

## 3. Main Components

### Bond Portfolio Analysis

The system stores bond-level information such as:

- Bond ID
- Issuer
- Modified Duration
- Convexity
- DV01
- Price
- Quantity
- Market Value
- Portfolio Weight

### Duration & Convexity

Duration measures the sensitivity of bond prices to changes in interest rates.

Convexity improves the estimation of price changes for larger interest-rate movements.

### DV01

DV01 measures the approximate change in bond value for a one basis-point change in yield.

### Key Rate Duration

Key Rate Duration analyzes portfolio sensitivity to movements at specific points of the yield curve.

### Monte Carlo Analysis

Monte Carlo scenarios are used to analyze portfolio P&L under different yield-curve movements.

### Stress Testing

Stress testing evaluates portfolio sensitivity under specified interest-rate shocks.

### VaR and CVaR

VaR estimates potential loss at a selected confidence level.

CVaR estimates the average loss beyond the VaR threshold.

### Machine Learning

The project includes a Random Forest regression model to demonstrate a machine-learning workflow using available bond risk variables.

### AI Risk Agent

The current AI Risk Agent uses rule-based risk classification.

It classifies bonds into:

- Low Risk
- Medium Risk
- High Risk

The classification uses:

- Modified Duration
- Convexity
- DV01

---

## 4. Dashboard

The project includes a Flask web dashboard.

The dashboard displays:

- Portfolio Market Value
- Modified Duration
- Convexity
- DV01
- Monte Carlo P&L

---

## 5. Technologies Used

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

## 6. Project Structure

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
├── templates/
│   └── dashboard.html
│
└── docs/
    └── PROJECT_DOCUMENTATION.md
 ## 7. Data Limitation

The current repository contains the supplied worked-example bond data.

The complete 300-bond portfolio and full historical yield-curve dataset are not included unless provided separately.

Therefore, historical yield-curve results and large-scale machine-learning performance should not be interpreted as final results until the complete datasets are available.

The machine-learning implementation is currently a technical demonstration because the sample dataset contains only a small number of observations.
## 8. Conclusion

The Convexity & Sensitivity AI Agent demonstrates a structured approach to fixed-income portfolio risk analysis using Python.

The project combines:

- Duration
- Convexity
- DV01
- Key Rate Duration
- Yield Curve Analysis
- Monte Carlo Analysis
- Stress Testing
- VaR and CVaR
- Machine Learning
- Risk Classification
- Flask Dashboard

into a single portfolio risk-analysis application.
## Author

**Yogita Patil**  
B.Sc. Computer Science  
Academic Year 2026–2027
