import logging
from db import insert_record, init_db
from data_generator import generate_dataset

logging.basicConfig(filename="logs/app.log", level=logging.INFO)

def ingest_synthetic_data(n_records=1000):
    init_db()
    data = generate_dataset(n_records)

    for rec in data:
        value = rec["value"]
        if value is None:
            value = 0
        insert_record(
            rec["country"],
            rec["date"],
            rec["metric"],
            float(value)
        )

    logging.info(f"Ingested {n_records} synthetic records.")
    return n_records
