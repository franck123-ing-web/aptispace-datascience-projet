import pandas as pd

def clean_data(df):

    # 1. normaliser timestamp (multi-format)
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce", dayfirst=True)

    # 2. supprimer valeurs manquantes critiques
    df = df.dropna(subset=["timestamp", "value"])

    # 3. conversion numérique (important)
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df = df.dropna(subset=["value"])

    # 4. supprimer anomalies extrêmes métier
    df = df[(df["value"] != -999) & (df["value"] != 999)]

    # 5. tri temporel
    df = df.sort_values("timestamp")

    return df