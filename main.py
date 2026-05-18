import pandas as pd
from src.preprocessing import clean_data
from src.anomaly import zscore_anomalies, ml_anomalies
from src.visualization import plot_series, plot_anomalies

# Load
df = pd.read_csv("data/raw/housing.csv")

# Clean
df = clean_data(df)

# EDA simple
print(df.describe())

# Visualisation
plot_series(df)

# Z-score
df = zscore_anomalies(df)
plot_anomalies(df, "anomaly")

# ML anomaly
df = ml_anomalies(df)
plot_anomalies(df, "anomaly_ml")

print("Anomalies Z-score:", df["anomaly"].sum())
print("Anomalies ML:", df["anomaly_ml"].sum())