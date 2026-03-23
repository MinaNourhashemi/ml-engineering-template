from sqlalchemy import create_engine, text


def get_engine():
    return create_engine("sqlite:///ml_pipeline.db")


def init_db(engine):
    with engine.connect() as conn:
        conn.execute(
            text("""
            CREATE TABLE IF NOT EXISTS inference_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                input TEXT,
                prediction TEXT,
                latency_ms REAL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        )
        conn.commit()


def log_prediction(engine, input_data, prediction, latency):
    with engine.connect() as conn:
        conn.execute(
            text("""
                INSERT INTO inference_logs (input, prediction, latency_ms)
                VALUES (:input, :prediction, :latency)
            """),
            {
                "input": str(input_data),
                "prediction": str(prediction),
                "latency": latency,
            },
        )
        conn.commit()


def get_logs(engine):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT input, prediction, latency_ms FROM inference_logs"))
        logs = []
        for row in result:
            logs.append(
                {
                    "input": row.input,
                    "prediction": row.prediction,
                    "latency_ms": row.latency_ms,
                }
            )
        return logs
