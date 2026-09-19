import pandas as pd


def classify_risk(duration, convexity, dv01):
    """
    Simple rule-based risk classification
    based on interest-rate sensitivity.
    """

    if duration >= 10 or convexity >= 150 or dv01 >= 0.10:
        return "High Risk"

    elif duration >= 5 or convexity >= 50 or dv01 >= 0.05:
        return "Medium Risk"

    else:
        return "Low Risk"


def generate_risk_report(data):

    reports = []

    for _, bond in data.iterrows():

        risk = classify_risk(
            bond["Modified_Duration"],
            bond["Convexity"],
            bond["DV01"]
        )

        reports.append({
            "Bond_ID": bond["Bond_ID"],
            "Risk_Level": risk,
            "Modified_Duration": bond["Modified_Duration"],
            "Convexity": bond["Convexity"],
            "DV01": bond["DV01"]
        })

    return pd.DataFrame(reports)


if __name__ == "__main__":

    file_path = "data/bond_portfolio.csv"

    data = pd.read_csv(file_path)

    report = generate_risk_report(data)

    print("AI Risk Agent")
    print("-" * 40)
    print(report)
