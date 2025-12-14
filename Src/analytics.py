import pandas as pd
import matplotlib.pyplot as plt
from db import read_records

def _to_df(rows):
    return pd.DataFrame(rows, columns=["id", "country", "date", "metric", "value"]) \
           if rows else pd.DataFrame(columns=["id", "country", "date", "metric", "value"])

def get_filtered_data(country=None, metric=None, start_date=None, end_date=None):
    parts = []
    params = []

    if country:
        parts.append("country = ?")
        params.append(country)
    if metric:
        parts.append("metric = ?")
        params.append(metric)
    if start_date and end_date:
        parts.append("date BETWEEN ? AND ?")
        params.extend([start_date, end_date])

    query = " AND ".join(parts)
    rows = read_records(query, tuple(params))
    df = _to_df(rows)
    return df

def summary_stats(df):
    if df.empty:
        return {"count": 0, "mean": None, "min": None, "max": None}

    return {
        "count": int(len(df)),
        "mean": float(df["value"].mean()),
        "min": float(df["value"].min()),
        "max": float(df["value"].max())
    }

def plot_trend(df, title="Trend Over Time"):
    if df.empty:
        print("No data to plot.")
        return

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"])
    df = df.sort_values("date")

    plt.figure(figsize=(10, 5))
    plt.plot(df["date"], df["value"], marker="o")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
