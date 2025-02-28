import streamlit as st
import pandas as pd
import sqlite3

DB_FILE = "./storage/market_data.db"

st.title("📊 BTC/USD Market Dashboard")

def fetch_data(table):
    """Fetch data from SQLite."""
    conn = sqlite3.connect(DB_FILE)
    df = pd.read_sql(f"SELECT * FROM {table}", conn)
    conn.close()
    return df

# Real-Time Data
st.subheader("📈 Real-Time BTC/USD Price")
df_realtime = fetch_data("realtime_data")

# Ensure "timestamp" exists before setting index
if "timestamp" in df_realtime.columns:
    df_realtime["timestamp"] = pd.to_datetime(df_realtime["timestamp"])
    st.line_chart(df_realtime.set_index("timestamp")["price"])
else:
    st.error("❌ 'timestamp' column missing in real-time data.")

# Batch Data
st.subheader("📊 Historical Moving Averages")
df_batch = fetch_data("batch_cleaned")

# Ensure "date" exists before setting index
if "date" in df_batch.columns:  
    df_batch["date"] = pd.to_datetime(df_batch["date"])
    st.line_chart(df_batch.set_index("date")["daily_change"])
else:
    st.error("❌ 'date' column missing in batch data.")