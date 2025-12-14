import os
import pandas as pd
import logging

logging.basicConfig(filename="logs/app.log", level=logging.INFO)

def export_to_csv(df, filepath: str):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df.to_csv(filepath, index=False)
    logging.info(f"Exported to {filepath}")
