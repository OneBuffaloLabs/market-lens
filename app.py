import streamlit as st
import plotly.express as px
from data_loader import fetch_stock_data, normalize_data, calculate_daily_returns

# --- App Configuration ---
st.set_page_config(page_title="Market Lens", page_icon="📈", layout="wide")

st.title("Market Lens 📈")

# --- Sidebar ---
st.sidebar.header("Configuration")
available_tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA', 'BTC-USD', 'ETH-USD', 'SPY']
selected_tickers = st.sidebar.multiselect(
    "Select Assets to Analyze",
    options=available_tickers,
    default=['AAPL', 'BTC-USD', 'GOOGL']
)

if selected_tickers:
    with st.spinner('Fetching market data...'):
        try:
            # 1. Fetch Data
            raw_data = fetch_stock_data(selected_tickers)

            # Handle Single Ticker vs Multi-Ticker Data Structure
            if len(selected_tickers) == 1:
                ticker = selected_tickers[0]
                close_prices = raw_data['Close'].to_frame(name=ticker)
                volume_data = raw_data['Volume'].to_frame(name=ticker)
                # Helper to access specific ticker data for metrics
                def get_ticker_data(t): return raw_data
            else:
                close_prices = raw_data.xs('Close', level=1, axis=1)
                volume_data = raw_data.xs('Volume', level=1, axis=1)
                def get_ticker_data(t): return raw_data[t]

            # Key Metrics Row (Task 4.4)
            st.header("Key Metrics")

            # Create a dynamic number of columns based on selection (max 4 per row recommended)
            cols = st.columns(len(selected_tickers))

            for idx, ticker in enumerate(selected_tickers):
                data = get_ticker_data(ticker)

                # Calculate Metrics
                current_price = data['Close'].iloc[-1]
                prev_price = data['Close'].iloc[-2]
                delta = ((current_price - prev_price) / prev_price) * 100
                ath = data['High'].max()

                # Display Metric
                with cols[idx]:
                    st.metric(
                        label=f"{ticker} (ATH: ${ath:,.2f})",
                        value=f"${current_price:,.2f}",
                        delta=f"{delta:+.2f}%"
                    )

            # Charts
            st.divider()

            # Chart 1: Price History (Normalized)
            # We use normalized data so BTC ($90k) and AAPL ($200) can be compared on one chart
            normalized_data = normalize_data(close_prices)

            st.subheader("Relative Price Performance")
            st.write("Performance relative to the start of the period (Base = 100).")

            fig_price = px.line(
                normalized_data,
                title="Price History (Normalized)",
                labels={"value": "Rebased Price (100)", "variable": "Asset"}
            )
            st.plotly_chart(fig_price, use_container_width=True)

            # Chart 2: Volume
            st.subheader("Trading Volume")
            fig_volume = px.area(
                volume_data,
                title="Daily Trading Volume",
                labels={"value": "Volume", "variable": "Asset"}
            )
            st.plotly_chart(fig_volume, use_container_width=True)

        except Exception as e:
            st.error(f"Error processing data: {e}")
            st.exception(e) # Prints the stack trace for easier debugging
else:
    st.info("Please select at least one ticker from the sidebar to begin.")