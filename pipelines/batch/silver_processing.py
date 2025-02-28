import pandas as pd
import os

# File paths
RAW_DATA_FILE = "./storage/batch_raw.csv"
CLEANED_DATA_FILE = "./storage/batch_cleaned.csv"

def process_batch_data():
    """Clean and transform historical batch data into a structured format."""
    df = pd.read_csv(RAW_DATA_FILE)

    # Standardize timestamps
    df["published_date"] = pd.to_datetime(df["published_date"], errors='coerce')

    # Drop rows with missing timestamps
    df.dropna(subset=["published_date"], inplace=True)

    # Extract relevant columns
    df_cleaned = df[["published_date", "title", "topic", "country"]]

    os.makedirs(os.path.dirname(CLEANED_DATA_FILE), exist_ok=True)

    # Save cleaned data
    df_cleaned.to_csv(CLEANED_DATA_FILE, index=False)
    print(f"✅ Cleaned batch data saved to {CLEANED_DATA_FILE}.")

process_batch_data()