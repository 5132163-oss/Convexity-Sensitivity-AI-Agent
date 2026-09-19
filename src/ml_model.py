import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np


def train_model(file_path):

    data = pd.read_csv(file_path)

    features = [
        "Modified_Duration",
        "Convexity",
        "DV01",
        "Price"
    ]

    X = data[features]
    y = data["Price"]

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

    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(
        mean_squared_error(y_test, predictions)
    )
    r2 = r2_score(y_test, predictions)

    return model, mae, rmse, r2


if __name__ == "__main__":

    file_path = "data/bond_portfolio.csv"

    model, mae, rmse, r2 = train_model(file_path)

    print("Machine Learning - Random Forest")
    print("-" * 40)
    print("MAE:", round(mae, 4))
    print("RMSE:", round(rmse, 4))
    print("R2 Score:", round(r2, 4))
