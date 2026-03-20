# import logging


# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s | %(levelname)s | %(message)s",
# )

# logger = logging.getLogger(__name__)


# def train_model() -> None:
#     logger.info("event=training_started model=dummy_model")
#     logger.info("event=training_finished status=success")


import pandas as pd

from src.app.db import get_engine
from src.app.model import train_model, save_model


def load_data():
    engine = get_engine()
    df = pd.read_sql("SELECT * FROM signals", engine)

    # feature ساده (dummy)
    df["feature"] = df["subject_id"]

    X = df[["feature"]]
    y = df["label"]

    return X, y


def run_training():
    X, y = load_data()
    model = train_model(X, y)
    save_model(model)
    print("Model trained successfully!")


if __name__ == "__main__":
    run_training()
