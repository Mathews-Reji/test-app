import joblib


def predict(data):
    clf = joblib.load("lgbm_model.sav")
    return clf.predict(data)
