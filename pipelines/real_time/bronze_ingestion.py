import requests
import pandas as pd
from datetime import datetime
import os
import subprocess
from apscheduler.schedulers.background import BackgroundScheduler

# Bronze: Simulate periodic API calls (e.g., every 30 seconds) to ingest raw BTC/USD market data

RAW_DATA_FILE = "./storage/realtime_raw.csv"

def fetch_realtime_data():
    """Fetch BTC/USD real-time price, volume, and order book data from Binance API."""
    url = "https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT"  # Full market data
    response = requests.get(url).json()
    
    data = {
        'timestamp': datetime.now(),
        'price': float(response['lastPrice']),
        'volume': float(response['volume']),
        'high_price': float(response['highPrice']),
        'low_price': float(response['lowPrice'])
    }
    
    df = pd.DataFrame([data])

    os.makedirs(os.path.dirname(RAW_DATA_FILE), exist_ok=True)
    
    # Append new data
    df.to_csv(RAW_DATA_FILE, mode='a', header=not os.path.exists(RAW_DATA_FILE), index=False)
    print(f"✅ Fetched: {data}")

fetch_realtime_data()