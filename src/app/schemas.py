from pydantic import BaseModel


class PredictionRequest(BaseModel):
    feature: int


class PredictionResponse(BaseModel):
    prediction: str
