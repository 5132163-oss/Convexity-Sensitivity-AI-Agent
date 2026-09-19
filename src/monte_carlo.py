import pandas as pd


def calculate_scenario_pnl(row):
    """
    Calculate total P&L from duration and convexity effects.
    """

    total_pnl = row["Duration_PnL"] + row["Convexity_PnL"]

    return total_pnl


def run_monte_carlo_analysis(file_path):
    data = pd.read_csv(file_path)

    data["Calculated_Total_PnL"] = data.apply(
        calculate_scenario_pnl,
        axis=1
    )

    return data


if __name__ == "__main__":

    file_path = "../data/monte_carlo_scenarios.csv"

    results = run_monte_carlo_analysis(file_path)

    print("Monte Carlo Scenario Analysis")
    print("-" * 40)

    print(results)

    print("\nTotal P&L:")
    print(results["Calculated_Total_PnL"].sum())
