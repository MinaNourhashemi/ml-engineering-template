import pandas as pd

from src.app.db import get_engine
from sqlalchemy import text


def ingest_signals():
    df = pd.read_csv("data/signals.csv")
    engine = get_engine()
    with open("database/schema.sql") as f:
        sql = f.read()
    with engine.connect() as conn:
        conn.execute(text(sql))
        conn.commit()
    df.to_sql("signals", engine, if_exists="replace", index=False)
    print("Data ingested into database successfully.")


if __name__ == "__main__":
    ingest_signals()
