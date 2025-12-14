import sqlite3
from typing import Tuple, List

DB_NAME = "public_health.db"

def set_db(path: str):
    global DB_NAME
    DB_NAME = path

def get_conn():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_conn()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS health_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            country TEXT,
            date TEXT,
            metric TEXT,
            value REAL
        )
    """)
    conn.commit()
    conn.close()

def insert_record(country: str, date: str, metric: str, value: float):
    conn = get_conn()
    c = conn.cursor()
    c.execute("""
        INSERT INTO health_data (country, date, metric, value)
        VALUES (?, ?, ?, ?)
    """, (country, date, metric, value))
    conn.commit()
    conn.close()

def read_records(filter_query: str = "", params: Tuple = ()):
    conn = get_conn()
    c = conn.cursor()
    q = "SELECT id, country, date, metric, value FROM health_data"
    if filter_query:
        q += " WHERE " + filter_query
    c.execute(q, params)
    rows = c.fetchall()
    conn.close()
    return rows

def update_record(record_id: int, value: float):
    conn = get_conn()
    c = conn.cursor()
    c.execute("UPDATE health_data SET value = ? WHERE id = ?", (value, record_id))
    conn.commit()
    conn.close()

def delete_record(record_id: int):
    conn = get_conn()
    c = conn.cursor()
    c.execute("DELETE FROM health_data WHERE id = ?", (record_id,))
    conn.commit()
    conn.close()
