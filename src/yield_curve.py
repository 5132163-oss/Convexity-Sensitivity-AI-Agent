import pandas as pd


def load_yield_curve(file_path):
    """
    Load yield curve history data.
    """

    data = pd.read_csv(file_path)

    return data


def summarize_yield_curve(data):
    """
    Create a basic summary of yield curve data.
    """

    summary = data.groupby("Tenor_Years")["Yield"].agg(
        ["min", "max", "mean"]
    ).reset_index()

    return summary


if __name__ == "__main__":

    file_path = "../data/yield_curve_history.csv"

    data = load_yield_curve(file_path)

    print("Yield Curve Analysis")
    print("-" * 40)

    print("Number of records:", len(data))

    # The current project dataset contains the required
    # column structure but no historical observations yet.
    if data["Yield"].notna().any():

        summary = summarize_yield_curve(data)

        print("\nYield Curve Summary:")
        print(summary)

    else:

        print("\nNo historical yield observations available yet.")
        print("Please add the actual yield-curve dataset when available.")
