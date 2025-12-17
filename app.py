import streamlit as st
from data_loader import fetch_stock_data, normalize_data, calculate_daily_returns

# --- App Configuration ---
st.set_page_config(page_title="Market Lens", page_icon="📈", layout="wide")

st.title("Market Lens 📈")
st.write("One Buffalo Labs - Financial Dashboard")

# --- Sidebar Configuration ---
st.sidebar.header("Configuration")

# Sidebar Multiselect
available_tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA', 'BTC-USD', 'ETH-USD', 'SPY']
selected_tickers = st.sidebar.multiselect(
    "Select Assets to Analyze",
    options=available_tickers,
    default=['AAPL', 'BTC-USD', 'GOOGL']
)

# --- Main Analysis ---
if selected_tickers:
    with st.spinner('Fetching market data...'):
        try:
            # Fetch Data
            raw_data = fetch_stock_data(selected_tickers)

            # Extract just the 'Close' prices for cleaner analysis
            # We handle the MultiIndex structure (Ticker -> OHLCV)
            if len(selected_tickers) > 1:
                close_prices = raw_data.xs('Close', level=1, axis=1)
            else:
                # Handle single ticker case where structure might differ slightly
                # Re-indexing to ensure it's a DataFrame
                close_prices = raw_data['Close'].to_frame(name=selected_tickers[0])

            # Apply Transformations
            normalized_data = normalize_data(close_prices)
            daily_returns = calculate_daily_returns(close_prices)

            # Display Data
            st.header("Market Analysis")

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Normalized Prices (Base 100)")
                st.write("Rebased to 100 at start of period for direct comparison.")
                st.dataframe(normalized_data.tail())

            with col2:
                st.subheader("Daily Returns (%)")
                st.write("Day-over-day percentage change.")
                st.dataframe(daily_returns.tail())

        except Exception as e:
            st.error(f"Error processing data: {e}")
else:
    st.info("Please select at least one ticker from the sidebar to begin.")