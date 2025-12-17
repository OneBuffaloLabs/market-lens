import yfinance as yf
import pandas as pd

def fetch_stock_data(tickers, period='1y'):
    """
    Fetches historical stock data for the given tickers using yfinance.
    """
    if not tickers:
        return pd.DataFrame()

    # group_by='ticker' ensures the DataFrame is structured hierarchically
    data = yf.download(tickers, period=period, group_by='ticker')
    return data

def normalize_data(df):
    """
    Normalizes the data so all assets start at 100.
    This allows for easy relative comparison between assets of different prices.

    Formula: (Price_t / Price_0) * 100
    """
    # Vectorized operation: Divide the whole dataframe by the first row
    # This single line replaces loop-heavy logic found in other languages.
    return df / df.iloc[0] * 100

def calculate_daily_returns(df):
    """
    Calculates the daily percentage change.
    """
    return df.pct_change()