
import sys
import os


PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)




import sqlite3
import pandas as pd
import pytest
from pathlib import Path

import db as db_module
import data_generator as generator
import ingestion as ingestion_module
import data_cleaner as cleaner
import analytics as analytics_module
import utils as utils_module


@pytest.fixture(scope="function")
def tmp_db_path(tmp_path):
    db_path = tmp_path / "test_ph.db"
    db_module.set_db(str(db_path))
    if os.path.exists(db_module.DB_NAME):
        os.remove(db_module.DB_NAME)
    db_module.init_db()
    yield str(db_path)
    if os.path.exists(db_module.DB_NAME):
        os.remove(db_module.DB_NAME)


def test_generate_synthetic_record():
    rec = generator.generate_synthetic_record()
    assert isinstance(rec, dict)
    assert "country" in rec
    assert "date" in rec
    assert "metric" in rec


def test_generate_dataset_length():
    ds = generator.generate_dataset(20)
    assert len(ds) == 20


def test_ingestion(tmp_db_path):
    ingestion_module.ingest_synthetic_data(15)
    rows = db_module.read_records()
    assert len(rows) == 15


def test_crud(tmp_db_path):
    db_module.insert_record("X", "2023-01-01", "metric", 10)
    rows = db_module.read_records("country = ?", ("X",))
    assert len(rows) == 1

    rec_id = rows[0][0]
    db_module.update_record(rec_id, 200)
    updated = db_module.read_records("id = ?", (rec_id,))[0]
    assert updated[4] == 200

    db_module.delete_record(rec_id)
    rows2 = db_module.read_records("country = ?", ("X",))
    assert len(rows2) == 0


def test_clean_dataframe():
    df = pd.DataFrame({
        "country": ["A", None],
        "date": ["2020-01-01", "bad-date"],
        "metric": ["m1", "m2"],
        "value": ["10", "bad"]
    })

    cleaned = cleaner.clean_dataframe(df)
    assert cleaned["country"].iloc[1] == "Unknown"
    assert not pd.isna(cleaned["value"].iloc[1])


def test_filter_and_summary(tmp_db_path):
    db_module.insert_record("UK", "2023-01-01", "vacc", 50)
    db_module.insert_record("UK", "2023-02-01", "vacc", 70)

    df = analytics_module.get_filtered_data(country="UK", metric="vacc")
    assert len(df) == 2

    stats = analytics_module.summary_stats(df)
    assert stats["mean"] == pytest.approx(60)


def test_export_to_csv(tmp_db_path, tmp_path):
    db_module.insert_record("X", "2023-01-01", "m", 10)
    df = analytics_module.get_filtered_data()
    out = tmp_path / "test_export.csv"

    utils_module.export_to_csv(df, str(out))
    assert out.exists()

    loaded = pd.read_csv(out)
    assert len(loaded) == len(df)


def test_plot_trend_runs(tmp_db_path):
    import matplotlib
    matplotlib.use("Agg")  # avoid GUI popup

    from analytics import plot_trend

    df = pd.DataFrame({
        "date": ["2020-01-01", "2020-02-01"],
        "value": [10, 50]
    })

    plot_trend(df, title="Test Trend")  
