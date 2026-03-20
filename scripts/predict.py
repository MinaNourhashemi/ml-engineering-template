import pandas as pd

from src.app.model import load_model


def predict():
    model = load_model()

    X = pd.DataFrame({"feature": [101, 102, 103]})

    preds = model.predict(X)

    print("Predictions:", preds)


if __name__ == "__main__":
    predict()
