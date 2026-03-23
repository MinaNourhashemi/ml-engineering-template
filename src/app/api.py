from fastapi import FastAPI
import pandas as pd
import logging
import time

from src.app.model import load_model
from src.app.schemas import PredictionRequest, PredictionResponse
from src.app.db import get_engine, log_prediction, get_logs, init_db

app = FastAPI()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
logger = logging.getLogger(__name__)

model = load_model()
engine = get_engine()
init_db(engine)


@app.get("/logs")
def read_logs():
    logs = get_logs(engine)
    return {"logs": logs}


@app.post("/predict", response_model=PredictionResponse)
def predict(data: PredictionRequest):
    start = time.time()
    logger.info(f"event=request_received input={data.dict()}")

    X = pd.DataFrame([data.dict()])
    preds = model.predict(X)
    result = preds[0]

    end = time.time()
    latency = (end - start) * 1000

    log_prediction(engine, data.dict(), result, latency)

    logger.info(f"event=prediction_done output={result}")
    logger.info(f"event=latency latency_ms={latency:.2f}")

    return {"prediction": result}
