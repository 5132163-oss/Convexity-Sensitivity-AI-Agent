import pandas as pd
from pathlib import Path


def calculate_key_rate_duration(data, key_rate_buckets):
    """
    Calculate portfolio exposure for each
    key-rate bucket.
    """

    total_value = data["Market_Value"].sum()

    krd_results = []

    for bucket in key_rate_buckets:

        bucket_data = data[
            data["KeyRateBucket"] == bucket
        ]

        if len(bucket_data) == 0:
            krd = 0
        else:
            krd = (
                bucket_data["Modified_Duration"]
                * bucket_data["Market_Value"]
            ).sum() / total_value

        krd_results.append({
            "Key_Rate_Bucket": bucket,
            "KRD": krd
        })

    return pd.DataFrame(krd_results)


if __name__ == "__main__":

    project_root = Path(__file__).resolve().parent.parent

    file_path = (
        project_root
        / "data"
        / "bond_portfolio.csv"
    )

    data = pd.read_csv(file_path)

    key_rate_buckets = [
        "1Y",
        "2Y",
        "3Y",
        "5Y",
        "7Y",
        "10Y",
        "15Y",
        "20Y",
        "30Y"
    ]

    if "KeyRateBucket" in data.columns:

        results = calculate_key_rate_duration(
            data,
            key_rate_buckets
        )

        print("Key Rate Duration Analysis")
        print("-" * 40)
        print(results)

    else:

        print("KeyRateBucket column is not available yet.")
        print(
            "Add the actual KRD bucket information "
            "when available."
        )
