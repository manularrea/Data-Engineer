import pandas as pd
import sys
import os

# Ensure config directory is in Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../config")))

from database import save_dataframe  # Import database handler

# File paths
CLEANED_DATA_FILE = "./storage/batch_cleaned.csv"

# Load cleaned batch data
df = pd.read_csv(CLEANED_DATA_FILE)

# Convert published_date to datetime (if not already converted)
df["published_date"] = pd.to_datetime(df["published_date"], errors='coerce')

# Aggregate: Count number of articles per day
df_aggregated = df.groupby(df["published_date"].dt.date).size().reset_index(name="article_count")

# Rename columns
df_aggregated.rename(columns={"published_date": "date"}, inplace=True)

# Save aggregated batch data to database
save_dataframe(df_aggregated, "batch_cleaned")
print(f"✅ Aggregated batch data stored in SQLite.")
