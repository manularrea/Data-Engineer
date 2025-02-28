import requests
import pandas as pd
from datetime import datetime

def fetch_realtime_data():
    """Fetch real-time BTC/USD price from Binance API"""
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    response = requests.get(url).json()

    return {'timestamp': datetime.now(), 'price': float(response['price'])}

# Save raw data
raw_data = fetch_realtime_data()
df = pd.DataFrame([raw_data])
df.to_csv("./storage/realtime_raw.csv", mode='a', header=False, index=False)
