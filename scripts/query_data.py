from sqlalchemy import text
from src.app.db import get_engine


def query_logs():
    engine = get_engine()

    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM inference_logs"))

        for row in result:
            print(row)


if __name__ == "__main__":
    query_logs()
