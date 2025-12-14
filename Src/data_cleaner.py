import pandas as pd

def clean_dataframe(df: pd.DataFrame):
    if df.empty:
        return df

    df["country"] = df["country"].fillna("Unknown")
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["metric"] = df["metric"].fillna("unknown")
    df["value"] = pd.to_numeric(df["value"], errors="coerce").fillna(0)

    return df
