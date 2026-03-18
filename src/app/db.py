from sqlalchemy import create_engine


def get_engine():
    engine = create_engine("sqlite:///ml_pipeline.db")
    return engine
