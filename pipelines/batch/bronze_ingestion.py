import pandas as pd
import os

# File paths
SOURCE_FILE = "./data/btc-news-recent-f.csv"  # Correct input file
RAW_DATA_FILE = "./storage/batch_raw.csv"

def ingest_batch_data():
    """Load historical batch data from a scheduled market snapshot."""
    df = pd.read_csv(SOURCE_FILE)

    # Debug: Print column names to verify dataset structure
    print(f"✅ Columns in batch dataset: {df.columns.tolist()}")

    # Ensure storage directory exists
    os.makedirs(os.path.dirname(RAW_DATA_FILE), exist_ok=True)

    # Save raw batch data
    df.to_csv(RAW_DATA_FILE, index=False, header=True)
    print(f"✅ Batch data ingested from {SOURCE_FILE} to {RAW_DATA_FILE}.")

ingest_batch_data()