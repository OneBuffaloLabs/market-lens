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
    """
    return df / df.iloc[0] * 100

def calculate_daily_returns(df):
    """
    Calculates the daily percentage change.
    """
    return df.pct_change()

def calculate_portfolio_value(historical_data, portfolio_composition):
    """
    Calculates the total value of the portfolio over time.

    Args:
        historical_data (pd.DataFrame): MultiIndex DF containing 'Close' prices.
        portfolio_composition (dict): Dictionary of {ticker: quantity}.

    Returns:
        pd.Series: A single series representing the total portfolio value over time.
    """
    portfolio_value = pd.DataFrame()

    # Handle the MultiIndex structure
    # If we only have one asset, yfinance structure is flat. If multiple, it's (Ticker, PriceType).
    is_multi_index = isinstance(historical_data.columns, pd.MultiIndex)

    for ticker, quantity in portfolio_composition.items():
        if is_multi_index:
            try:
                # Extract Close price for specific ticker
                price_series = historical_data.xs('Close', level=1, axis=1)[ticker]
            except KeyError:
                # Fallback if ticker structure is different (sometimes happens with single col slices)
                price_series = historical_data[ticker]['Close']
        else:
            # Single asset case
            price_series = historical_data['Close']

        # Value = Price * Quantity
        portfolio_value[ticker] = price_series * quantity

    # Sum across the row to get total value for that day
    return portfolio_value.sum(axis=1)