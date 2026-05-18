import matplotlib.pyplot as plt

def plot_series(df):
    plt.figure(figsize=(10,5))
    plt.plot(df["timestamp"], df["value"])
    plt.title("Time series")
    plt.show()


def plot_anomalies(df, col):
    plt.figure(figsize=(10,5))

    plt.plot(df["timestamp"], df["value"])

    anomalies = df[df[col] == True]
    plt.scatter(anomalies["timestamp"], anomalies["value"], color="red")

    plt.title(f"Anomalies ({col})")
    plt.show()