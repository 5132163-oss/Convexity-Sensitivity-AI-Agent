import pandas as pd
from pathlib import Path


def stress_test(
    market_value,
    duration,
    convexity,
    shift_bps
):
    """
    Estimate portfolio P&L under
    different interest-rate stress scenarios.
    """

    yield_change = shift_bps / 10000

    duration_effect = (
        -duration
        * yield_change
        * market_value
    )

    convexity_effect = (
        0.5
        * convexity
        * (yield_change ** 2)
        * market_value
    )

    total_pnl = (
        duration_effect
        + convexity_effect
    )

    return (
        duration_effect,
        convexity_effect,
        total_pnl
    )


if __name__ == "__main__":

    project_root = Path(__file__).resolve().parent.parent

    file_path = (
        project_root
        / "data"
        / "bond_portfolio.csv"
    )

    data = pd.read_csv(file_path)

    market_value = data["Market_Value"].sum()

    duration = (
        data["Modified_Duration"]
        * data["Portfolio_Weight"]
        / 100
    ).sum()

    convexity = (
        data["Convexity"]
        * data["Portfolio_Weight"]
        / 100
    ).sum()

    stress_scenarios = [
        -100,
        25,
        50,
        100,
        200,
        300
    ]

    print("Interest Rate Stress Testing")
    print("-" * 40)

    for shift in stress_scenarios:

        (
            duration_effect,
            convexity_effect,
            total_pnl
        ) = stress_test(
            market_value,
            duration,
            convexity,
            shift
        )

        print(
            "\nRate Shift:",
            shift,
            "bps"
        )

        print(
            "Duration Effect:",
            round(duration_effect, 2)
        )

        print(
            "Convexity Effect:",
            round(convexity_effect, 2)
        )

        print(
            "Total P&L:",
            round(total_pnl, 2)
        )
