from flask import Flask, render_template
import pandas as pd
from pathlib import Path

app = Flask(__name__)


def load_data():
    """
    Load project data from the data folder.
    """

    project_root = Path(__file__).resolve().parent

    bond_file = (
        project_root
        / "data"
        / "bond_portfolio.csv"
    )

    monte_carlo_file = (
        project_root
        / "data"
        / "monte_carlo_scenarios.csv"
    )

    bond_data = pd.read_csv(bond_file)

    monte_carlo_data = pd.read_csv(
        monte_carlo_file
    )

    return bond_data, monte_carlo_data


@app.route("/")
def home():

    bond_data, monte_carlo_data = load_data()

    # Total Portfolio Market Value
    total_market_value = (
        bond_data["Market_Value"].sum()
    )

    # Portfolio Modified Duration
    portfolio_duration = (
        bond_data["Modified_Duration"]
        * bond_data["Portfolio_Weight"]
        / 100
    ).sum()

    # Portfolio Convexity
    portfolio_convexity = (
        bond_data["Convexity"]
        * bond_data["Portfolio_Weight"]
        / 100
    ).sum()

    # Portfolio DV01
    portfolio_dv01 = (
        bond_data["DV01"]
        * bond_data["Quantity"]
    ).sum() / 100

    # Monte Carlo P&L
    total_pnl = (
        monte_carlo_data["Total_PnL"].sum()
    )

    return render_template(
        "dashboard.html",

        total_market_value=round(
            total_market_value,
            2
        ),

        portfolio_duration=round(
            portfolio_duration,
            4
        ),

        portfolio_convexity=round(
            portfolio_convexity,
            4
        ),

        total_dv01=round(
            portfolio_dv01,
            4
        ),

        total_pnl=round(
            total_pnl,
            2
        )
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
