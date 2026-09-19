import pandas as pd


def calculate_key_rate_duration(data, key_rate_buckets):
    """
    Calculate the portfolio exposure for each
    key-rate bucket.
    """

    krd_results = []

    total_value = data["Market_Value"].sum()

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

    file_path = "data/bond_portfolio.csv"

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

    # Run only when KeyRateBucket exists in the dataset.
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
        print("Add the actual KRD bucket information when available.")
