import pandas as pd
import sqlite3
import os
import sys 

# Dynamically find the project root
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, os.path.join(PROJECT_ROOT, "config"))

from database import save_dataframe

CLEANED_DATA_FILE = "./storage/realtime_cleaned.csv"

def aggregate_realtime_data():
    """Compute moving averages, volume summaries, and perform data quality checks."""
    df = pd.read_csv(CLEANED_DATA_FILE)

    # Compute 5-point moving average for price & volume
    df['moving_avg_price'] = df['price'].rolling(window=5).mean()
    df['moving_avg_volume'] = df['volume'].rolling(window=5).mean()

    # **Data Quality Checks**
    if df['price'].isnull().sum() > 0:
        print("⚠️ Warning: Missing price data detected!")
    if df['volume'].isnull().sum() > 0:
        print("⚠️ Warning: Missing volume data detected!")

    # Save aggregated data to SQLite
    save_dataframe(df, "realtime_data")
    print("✅ Aggregated real-time data stored in SQLite.")

aggregate_realtime_data()
 