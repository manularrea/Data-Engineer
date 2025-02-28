import pandas as pd
import os

# File paths
SOURCE_FILE = "./data/btc-news-recent-f.csv"  # Correct input file
RAW_DATA_FILE = "./storage/batch_raw.csv"

# Load historical data
df = pd.read_csv(SOURCE_FILE)

# Print column names for debugging
print(f"✅ Columns found in dataset: {df.columns.tolist()}")

# Ensure storage directory exists
os.makedirs(os.path.dirname(RAW_DATA_FILE), exist_ok=True)

# Save raw batch data with headers
df.to_csv(RAW_DATA_FILE, index=False, header=True)
print(f"✅ Batch data ingested from {SOURCE_FILE} to {RAW_DATA_FILE}.")
