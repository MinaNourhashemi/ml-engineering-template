from sklearn.linear_model import LogisticRegression
import joblib


def train_model(X, y):
    model = LogisticRegression()
    model.fit(X, y)
    return model


def save_model(model, path="models/model.joblib"):
    joblib.dump(model, path)


def load_model(path="models/model.joblib"):
    return joblib.load(path)
