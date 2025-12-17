import yfinance as yf
import pandas as pd

def fetch_stock_data(tickers, period='1y'):
    """
    Fetches historical stock data for the given tickers using yfinance.

    Args:
        tickers (list or str): A single ticker or list of tickers (e.g., ['AAPL', 'BTC-USD']).
        period (str): The time period to download (e.g., '1y', '1mo', 'max').

    Returns:
        pd.DataFrame: A DataFrame containing the fetched market data.
    """
    # yfinance.download fetches data from Yahoo Finance
    # group_by='ticker' ensures the DataFrame is structured hierarchically if multiple tickers are used
    data = yf.download(tickers, period=period, group_by='ticker')

    return data