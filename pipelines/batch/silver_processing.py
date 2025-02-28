import pandas as pd
import os

# File paths
RAW_DATA_FILE = "./storage/batch_raw.csv"
CLEANED_DATA_FILE = "./storage/batch_cleaned.csv"

# Load batch data
df = pd.read_csv(RAW_DATA_FILE)

# Debug: Print column names to verify structure
print(f"✅ Columns in batch dataset: {df.columns.tolist()}")

# Ensure 'published_date' column exists (acts as timestamp)
expected_column = "published_date"
if expected_column not in df.columns:
    raise KeyError(f"❌ Column '{expected_column}' not found. Found columns: {df.columns.tolist()}")

# Convert published_date to datetime
df["published_date"] = pd.to_datetime(df["published_date"], errors='coerce')

# Drop rows where conversion failed
df.dropna(subset=["published_date"], inplace=True)

# Extract only relevant columns for further processing
df_cleaned = df[["published_date", "title", "topic", "country"]]

# Ensure storage directory exists
os.makedirs(os.path.dirname(CLEANED_DATA_FILE), exist_ok=True)

# Save cleaned data
df_cleaned.to_csv(CLEANED_DATA_FILE, index=False)
print(f"✅ Cleaned batch data saved to {CLEANED_DATA_FILE}.")
