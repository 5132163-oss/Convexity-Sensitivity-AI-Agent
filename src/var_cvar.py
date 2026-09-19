import pandas as pd
import numpy as np


def calculate_var(pnl_data, confidence=0.95):
    """
    Calculate historical VaR.
    """

    pnl = np.array(pnl_data)

    var = np.percentile(
        pnl,
        (1 - confidence) * 100
    )

    return abs(var)


def calculate_cvar(pnl_data, confidence=0.95):
    """
    Calculate Conditional VaR (Expected Shortfall).
    """

    pnl = np.array(pnl_data)

    var = np.percentile(
        pnl,
        (1 - confidence) * 100
    )

    losses = pnl[pnl <= var]

    if len(losses) == 0:
        return abs(var)

    return abs(losses.mean())


if __name__ == "__main__":

    file_path = "data/monte_carlo_scenarios.csv"

    data = pd.read_csv(file_path)

    pnl = data["Total_PnL"]

    print("VaR and CVaR Analysis")
    print("-" * 40)

    var_95 = calculate_var(pnl, 0.95)
    cvar_95 = calculate_cvar(pnl, 0.95)

    print("95% VaR:", round(var_95, 2))
    print("95% CVaR:", round(cvar_95, 2))
