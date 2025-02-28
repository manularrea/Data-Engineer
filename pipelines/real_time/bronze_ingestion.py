import requests
import pandas as pd
from datetime import datetime
import os
from apscheduler.schedulers.background import BackgroundScheduler

RAW_DATA_FILE = "./storage/realtime_raw.csv"

def fetch_realtime_data():
    """Fetch BTC/USD real-time price from Binance API every 30 seconds."""
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    response = requests.get(url).json()
    
    data = {'timestamp': datetime.now(), 'price': float(response['price'])}
    df = pd.DataFrame([data])

    os.makedirs(os.path.dirname(RAW_DATA_FILE), exist_ok=True)
    df.to_csv(RAW_DATA_FILE, mode='a', header=not os.path.exists(RAW_DATA_FILE), index=False)
    print(f"✅ Fetched: {data}")

# Run every 30 seconds
scheduler = BackgroundScheduler()
scheduler.add_job(fetch_realtime_data, 'interval', seconds=30)
scheduler.start()

# Keep script running
while True:
    pass
