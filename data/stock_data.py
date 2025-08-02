
import yfinance as yf
from datetime import datetime

def fetch_stock_data(ticker: str, start_date: str, end_date: str):
    #fetching stock data using yfinance
    df = yf.download(ticker, start=start_date, end=end_date)
    df.reset_index(inplace=True)
    df['Date'] = df['Date'].dt.date
    return df[['Date', 'Close']]

df = fetch_stock_data("AAPL", "2023-01-01", datetime.now().strftime("%Y-%m-%d"))
