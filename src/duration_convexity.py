import pandas as pd
from pathlib import Path


def calculate_risk_metrics(df):
    """
    Calculate portfolio contributions
    using duration, convexity and DV01.
    """

    df["Duration_Contribution"] = (
        df["Modified_Duration"]
        * df["Portfolio_Weight"]
        / 100
    )

    df["Convexity_Contribution"] = (
        df["Convexity"]
        * df["Portfolio_Weight"]
        / 100
    )

    return df


def calculate_price_change(
    market_value,
    duration,
    convexity,
    yield_change
):
    """
    Estimate P&L using duration and convexity.
    """

    pnl = (
        -duration
        * yield_change
        * market_value
        + 0.5
        * convexity
        * (yield_change ** 2)
        * market_value
    )

    return pnl


if __name__ == "__main__":

    # Project root/data path
    project_root = Path(__file__).resolve().parent.parent
    file_path = project_root / "data" / "bond_portfolio.csv"

    data = pd.read_csv(file_path)

    data = calculate_risk_metrics(data)

    print("Bond Portfolio Risk Analysis")
    print("-" * 40)

    print(
        data[
            [
                "Bond_ID",
                "Modified_Duration",
                "Convexity",
                "DV01",
                "Duration_Contribution",
                "Convexity_Contribution"
            ]
        ]
    )

    portfolio_duration = data[
        "Duration_Contribution"
    ].sum()

    portfolio_convexity = data[
        "Convexity_Contribution"
    ].sum()

    print("\nPortfolio Risk Metrics")
    print("-" * 40)

    print(
        "Modified Duration:",
        round(portfolio_duration, 4)
    )

    print(
        "Convexity:",
        round(portfolio_convexity, 4)
    )
