import pandas as pd


def calculate_risk_metrics(df):
    """
    Calculate basic portfolio risk metrics
    using the duration, convexity and DV01
    values available in the bond portfolio data.
    """

    df["Duration_Contribution"] = (
        df["Modified_Duration"] * df["Portfolio_Weight"] / 100
    )

    df["Convexity_Contribution"] = (
        df["Convexity"] * df["Portfolio_Weight"] / 100
    )

    df["DV01_Contribution"] = (
        df["DV01"] * df["Portfolio_Weight"] / 100
    )

    return df


def calculate_price_change(market_value, duration, convexity, yield_change):
    """
    Estimate bond price/P&L change using
    duration and convexity.
    """

    pnl = (
        -duration * yield_change * market_value
        + 0.5 * convexity * (yield_change ** 2) * market_value
    )

    return pnl


if __name__ == "__main__":

    file_path = "../data/bond_portfolio.csv"

    data = pd.read_csv(file_path)

    data = calculate_risk_metrics(data)

    print("Bond Portfolio Risk Analysis")
    print("-" * 40)

    print(data[
        [
            "Bond_ID",
            "Modified_Duration",
            "Convexity",
            "DV01",
            "Duration_Contribution",
            "Convexity_Contribution",
            "DV01_Contribution"
        ]
    ])

    portfolio_duration = data["Duration_Contribution"].sum()
    portfolio_convexity = data["Convexity_Contribution"].sum()
    portfolio_dv01 = data["DV01_Contribution"].sum()

    print("\nPortfolio Risk Metrics")
    print("-" * 40)
    print("Modified Duration:", round(portfolio_duration, 4))
    print("Convexity:", round(portfolio_convexity, 4))
    print("DV01:", round(portfolio_dv01, 4))
