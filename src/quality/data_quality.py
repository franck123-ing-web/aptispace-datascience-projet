import pandas as pd

def data_quality_score(df):

    score = 100

    missing_ratio = df.isnull().mean().mean()
    score -= missing_ratio * 40

    bad_values = df[df["value"].isin([-999, 999])].shape[0]
    score -= (bad_values / len(df)) * 30

    time_span = (df["timestamp"].max() - df["timestamp"].min()).days
    if time_span < 1:
        score -= 20

    std = df["value"].std()
    if std > df["value"].mean():
        score -= 10

    return max(0, round(score, 2))