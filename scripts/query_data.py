import pandas as pd

from src.app.db import get_engine


def query_signals():
    engine = get_engine()
    df = pd.read_sql("SELECT * FROM signals", engine)
    print(df)


if __name__ == "__main__":
    query_signals()
