import pandas as pd
import numpy as np
from pathlib import Path

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def train_model(file_path):

    data = pd.read_csv(file_path)

    # Required features available in the current dataset
    features = [
        "Modified_Duration",
        "Convexity",
        "DV01"
    ]

    target = "Price"

    # Check required columns
    required_columns = features + [target]

    missing_columns = [
        column
        for column in required_columns
        if column not in data.columns
    ]

    if missing_columns:

        raise ValueError(
            "Missing columns: "
            + ", ".join(missing_columns)
        )

    # Check dataset size
    if len(data) < 10:

        print(
            "Insufficient observations for "
            "meaningful machine-learning training."
        )

        print(
            "Current observations:",
            len(data)
        )

        print(
            "Please add the complete bond portfolio "
            "dataset before training the model."
        )

        return None

    X = data[features]
    y = data[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(
        y_test,
        predictions
    )

    rmse = np.sqrt(
        mean_squared_error(
            y_test,
            predictions
        )
    )

    r2 = r2_score(
        y_test,
        predictions
    )

    return model, mae, rmse, r2


if __name__ == "__main__":

    project_root = Path(__file__).resolve().parent.parent

    file_path = (
        project_root
        / "data"
        / "bond_portfolio.csv"
    )

    result = train_model(file_path)

    if result is not None:

        model, mae, rmse, r2 = result

        print("\nMachine Learning - Random Forest")
        print("-" * 40)

        print(
            "MAE:",
            round(mae, 4)
        )

        print(
            "RMSE:",
            round(rmse, 4)
        )

        print(
            "R2 Score:",
            round(r2, 4)
        )
