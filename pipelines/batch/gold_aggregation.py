import pandas as pd
import sys
import os

# Dynamically find the project root
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, os.path.join(PROJECT_ROOT, "config"))

from database import save_dataframe  # Import database handler

# File paths
CLEANED_DATA_FILE = "./storage/batch_cleaned.csv"

def aggregate_batch_data():
    """Generate trend analyses & perform data quality checks."""
    df = pd.read_csv(CLEANED_DATA_FILE)

    # Convert published_date to datetime (if not already converted)
    df["published_date"] = pd.to_datetime(df["published_date"], errors='coerce')

    # Aggregate article count per day
    df_aggregated = df.groupby(df["published_date"].dt.date).size().reset_index(name="article_count")

    # Rename columns
    df_aggregated.rename(columns={"published_date": "date"}, inplace=True)

    # **Trend Analysis: Calculate daily article trends**
    df_aggregated["daily_change"] = df_aggregated["article_count"].pct_change().fillna(0) * 100  # % Change

    # **Data Quality Checks**
    if df_aggregated["article_count"].isnull().sum() > 0:
        print("⚠️ Warning: Missing article count data detected!")

    # Save aggregated batch data to SQLite
    save_dataframe(df_aggregated, "batch_cleaned")
    print("✅ Aggregated batch data stored in SQLite.")

aggregate_batch_data()
print(f"✅ Aggregated batch data stored in SQLite.")
