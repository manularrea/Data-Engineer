import pandas as pd
import os
import subprocess


RAW_DATA_FILE = "./storage/realtime_raw.csv"
CLEANED_DATA_FILE = "./storage/realtime_cleaned.csv"

def process_realtime_data():
    """Clean and transform real-time BTC/USD data."""
    df = pd.read_csv(RAW_DATA_FILE)
    
    # Standardize timestamps
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # Handle missing values
    df.fillna(method="ffill", inplace=True)

    os.makedirs(os.path.dirname(CLEANED_DATA_FILE), exist_ok=True)

    # Save cleaned data
    df.to_csv(CLEANED_DATA_FILE, index=False)
    print("✅ Cleaned real-time data.")

process_realtime_data()