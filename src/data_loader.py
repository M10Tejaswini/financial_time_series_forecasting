import yfinance as yf
import pandas as pd

def load_stock_data(ticker: str, start="2018-01-01", end="2023-12-31") -> pd.DataFrame:
    data = yf.download(ticker, start=start, end=end)
    data = data[['Close']]
    return data