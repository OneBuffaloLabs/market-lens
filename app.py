import streamlit as st
from data_loader import fetch_stock_data

# --- App Configuration ---
st.set_page_config(page_title="Market Lens", page_icon="📈")

st.title("Market Lens 📈")
st.write("One Buffalo Labs - Financial Dashboard")

# --- Data Ingestion ---
st.header("Market Data Inspector")

# Define the tickers to fetch
target_tickers = ['AAPL', 'BTC-USD', 'GOOGL']

# Fetch the data
with st.spinner('Fetching market data...'):
    try:
        raw_data = fetch_stock_data(target_tickers)

        # Success Feedback
        st.success(f"Successfully loaded data for: {', '.join(target_tickers)}")

        # Display the Raw Data
        st.subheader("Raw Data Preview")
        st.write("This table shows the Open, High, Low, Close, and Volume data for the requested assets.")
        st.dataframe(raw_data)

    except Exception as e:
        st.error(f"Error fetching data: {e}")