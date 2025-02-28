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
st.line_chart(df_realtime.set_index("timestamp")["price"])

# Batch Data
st.subheader("📊 Historical Moving Averages")
df_batch = fetch_data("batch_cleaned")
st.line_chart(df_batch.set_index("timestamp")["moving_avg"])
