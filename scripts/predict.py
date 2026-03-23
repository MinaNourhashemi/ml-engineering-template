# import pandas as pd
# import time
# import logging

# from src.app.model import load_model
# from src.app.db import get_engine, log_prediction

# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s | %(levelname)s | %(message)s",
# )

# logger = logging.getLogger(__name__)


# @app.post("/predict", response_model=PredictionResponse)
# def predict(data: PredictionRequest):
#     start = time.time()
#     logger.info(f"event=request_received input={data.dict()}")

#     X = pd.DataFrame([data.dict()])
#     preds = model.predict(X)
#     result = preds[0]

#     end = time.time()
#     latency = (end - start) * 1000

#     # 👇 این خط مهمه
#     log_prediction(engine, data.dict(), result, latency)

#     logger.info(f"event=prediction_done output={result}")
#     logger.info(f"event=latency latency_ms={latency:.2f}")

#     return {"prediction": result}


# if __name__ == "__main__":
#     predict()


import pandas as pd
import time
import logging

from src.app.model import load_model
from src.app.db import get_engine, log_prediction

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

model = load_model()
engine = get_engine()

data = {"feature": 101}

start = time.time()

X = pd.DataFrame([data])
preds = model.predict(X)
result = preds[0]

latency = time.time() - start

log_prediction(engine, data, result, latency)

logger.info(f"Prediction: {result}")
