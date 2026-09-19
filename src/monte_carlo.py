import pandas as pd
from pathlib import Path


def calculate_scenario_pnl(row):
    """
    Calculate total P&L from duration and convexity effects.
    """

    total_pnl = (
        row["Duration_PnL"]
        + row["Convexity_PnL"]
    )

    return total_pnl


def run_monte_carlo_analysis(file_path):
    """
    Load Monte Carlo scenario data
    and calculate scenario P&L.
    """

    data = pd.read_csv(file_path)

    data["Calculated_Total_PnL"] = data.apply(
        calculate_scenario_pnl,
        axis=1
    )

    return data


if __name__ == "__main__":

    project_root = Path(__file__).resolve().parent.parent

    file_path = (
        project_root
        / "data"
        / "monte_carlo_scenarios.csv"
    )

    results = run_monte_carlo_analysis(file_path)

    print("Monte Carlo Scenario Analysis")
    print("-" * 40)

    print(results)

    print("\nCalculated Total P&L:")

    print(
        round(
            results["Calculated_Total_PnL"].sum(),
            2
        )
    )
