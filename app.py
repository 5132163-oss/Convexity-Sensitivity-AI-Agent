from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)


def load_data():
    bond_file = "data/bond_portfolio.csv"
    monte_carlo_file = "data/monte_carlo_scenarios.csv"

    bond_data = pd.read_csv(bond_file)
    monte_carlo_data = pd.read_csv(monte_carlo_file)

    return bond_data, monte_carlo_data


@app.route("/")
def home():

    bond_data, monte_carlo_data = load_data()

    total_market_value = bond_data["Market_Value"].sum()

    portfolio_duration = (
        bond_data["Modified_Duration"]
        * bond_data["Portfolio_Weight"]
        / 100
    ).sum()

    portfolio_convexity = (
        bond_data["Convexity"]
        * bond_data["Portfolio_Weight"]
        / 100
    ).sum()

    total_dv01 = (
        bond_data["DV01"]
        * bond_data["Portfolio_Weight"]
        / 100
    ).sum()

    total_pnl = monte_carlo_data["Total_PnL"].sum()

    return render_template(
        "dashboard.html",
        total_market_value=round(total_market_value, 2),
        portfolio_duration=round(portfolio_duration, 4),
        portfolio_convexity=round(portfolio_convexity, 4),
        total_dv01=round(total_dv01, 4),
        total_pnl=round(total_pnl, 2)
    )


if __name__ == "__main__":
    app.run(debug=True)
