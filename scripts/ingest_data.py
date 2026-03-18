import pandas as pd

from src.app.db import get_engine


def ingest_signals():
    df = pd.read_csv("data/signals.csv")
    engine = get_engine()
    df.to_sql("signals", engine, if_exists="replace", index=False)
    print("Data ingested into database successfully.")


if __name__ == "__main__":
    ingest_signals()
