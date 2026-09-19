import pandas as pd


def calculate_market_value(price, quantity):
    """
    Calculate market value from price and quantity.
    """
    return price * quantity


def calculate_dv01(modified_duration, market_value):
    """
    Estimate DV01 using modified duration.
    """
    return modified_duration * market_value * 0.0001


def duration_convexity_pnl(
    market_value,
    modified_duration,
    convexity,
    yield_change
):
    """
    Estimate P&L using duration and convexity.
    """

    duration_effect = (
        -modified_duration
        * yield_change
        * market_value
    )

    convexity_effect = (
        0.5
        * convexity
        * (yield_change ** 2)
        * market_value
    )

    total_pnl = duration_effect + convexity_effect

    return duration_effect, convexity_effect, total_pnl


if __name__ == "__main__":

    file_path = "data/bond_portfolio.csv"

    data = pd.read_csv(file_path)

    print("Bond Pricing and Risk Analysis")
    print("-" * 40)

    for _, bond in data.iterrows():

        duration_effect, convexity_effect, total_pnl = (
            duration_convexity_pnl(
                bond["Market_Value"],
                bond["Modified_Duration"],
                bond["Convexity"],
                0.01
            )
        )

        print("\nBond:", bond["Bond_ID"])
        print("Market Value:", bond["Market_Value"])
        print("DV01:", round(
            calculate_dv01(
                bond["Modified_Duration"],
                bond["Market_Value"]
            ), 4
        ))
        print("Duration Effect:", round(duration_effect, 2))
        print("Convexity Effect:", round(convexity_effect, 2))
        print("Total P&L:", round(total_pnl, 2))
