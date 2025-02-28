import pandas as pd
import sqlite3
import os
from config.database import save_dataframe

CLEANED_DATA_FILE = "./storage/realtime_cleaned.csv"

df = pd.read_csv(CLEANED_DATA_FILE)
df['moving_avg'] = df['price'].rolling(window=5).mean()

save_dataframe(df, "realtime_data")
print("✅ Aggregated real-time data stored in SQLite.")
