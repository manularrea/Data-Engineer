import sqlite3
import os

DB_FILE = "../storage/market_data.db"

def get_connection():
    """Establish SQLite connection and create tables if they don’t exist."""
    os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS realtime_data (
            timestamp TEXT PRIMARY KEY,
            price REAL,
            moving_avg REAL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS batch_cleaned (
            date TEXT PRIMARY KEY,
            article_count INTEGER
        )
    """)

    conn.commit()
    return conn

def save_dataframe(df, table_name):
    """Save DataFrame to SQLite."""
    conn = get_connection()
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
