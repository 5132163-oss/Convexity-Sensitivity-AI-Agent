import pandas as pd
import numpy as np
from pathlib import Path


def calculate_var(pnl_data, confidence=0.95):
    """
    Calculate historical VaR.
    """

    pnl = np.asarray(pnl_data, dtype=float)

    if len(pnl) < 2:
        return None

    var = np.percentile(
        pnl,
        (1 - confidence) * 100
    )

    return abs(var)


def calculate_cvar(pnl_data, confidence=0.95):
    """
    Calculate Conditional VaR (Expected Shortfall).
    """

    pnl = np.asarray(pnl_data, dtype=float)

    if len(pnl) < 2:
        return None

    var = np.percentile(
        pnl,
        (1 - confidence) * 100
    )

    losses = pnl[pnl <= var]

    if len(losses) == 0:
        return abs(var)

    return abs(losses.mean())


if __name__ == "__main__":

    project_root = Path(__file__).resolve().parent.parent

    file_path = (
        project_root
        / "data"
        / "monte_carlo_scenarios.csv"
    )

    data = pd.read_csv(file_path)

    pnl = data["Total_PnL"]

    print("VaR and CVaR Analysis")
    print("-" * 40)

    if len(pnl) < 2:

        print(
            "Insufficient P&L observations "
            "for meaningful VaR/CVaR estimation."
        )

        print(
            "Add the complete scenario dataset "
            "when available."
        )

    else:

        var_95 = calculate_var(
            pnl,
            0.95
        )

        cvar_95 = calculate
