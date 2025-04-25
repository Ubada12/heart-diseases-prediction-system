import pandas as pd

def get_data():
    data = pd.read_csv("model/cardio_train.csv")
    data["age"] = data["age"] / 365
    return data