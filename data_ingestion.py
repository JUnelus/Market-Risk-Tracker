import os
import requests
import sqlite3
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define API endpoint and parameters
api_endpoint = "https://www.alphavantage.co/query"
api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
symbol = "MSFT"  # Replace with the desired stock symbol
interval = "1min"  # Replace with the desired time interval

# Define database connection
db_name = "market_data.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS market_data (
        timestamp TEXT,
        open REAL,
        high REAL,
        low REAL,
        close REAL,
        volume INTEGER
    )
""")

# Retrieve market data from Alpha Vantage API
params = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": symbol,
    "interval": interval,
    "apikey": api_key
}
response = requests.get(api_endpoint, params=params)

# Parse JSON response
data = response.json()
time_series = data["Time Series (1min)"]

# Convert data to Pandas DataFrame
df = pd.DataFrame(time_series).T
df.columns = ["open", "high", "low", "close", "volume"]
df["timestamp"] = pd.to_datetime(df.index)

# Insert data into SQLite database
df.to_sql("market_data", conn, if_exists="append", index=False)

# Close database connection
conn.close()