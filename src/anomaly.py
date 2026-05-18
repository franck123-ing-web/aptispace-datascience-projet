import numpy as np
from sklearn.ensemble import IsolationForest

def zscore_anomalies(df):
    mean = df["value"].mean()
    std = df["value"].std()

    df["z_score"] = (df["value"] - mean) / std
    df["anomaly"] = np.abs(df["z_score"]) > 3

    return df


def ml_anomalies(df):
    model = IsolationForest(contamination=0.05, random_state=42)

    df["anomaly_ml"] = model.fit_predict(df[["value"]])
    df["anomaly_ml"] = df["anomaly_ml"] == -1

    return df