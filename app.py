import streamlit as st
import plotly.express as px
import pandas as pd
from data_loader import fetch_stock_data, calculate_portfolio_value

# --- Configuration ---
st.set_page_config(page_title="Market Lens", page_icon="📈", layout="wide")

# Hardcoded Mock Portfolio
# In a real app, this would come from a database or user input
MOCK_PORTFOLIO = {
    'AAPL': 50,      # 50 shares of Apple
    'BTC-USD': 0.5,  # 0.5 Bitcoin
    'NVDA': 20,      # 20 shares of Nvidia
    'TSLA': 30       # 30 shares of Tesla
}

st.title("Market Lens 📈")
st.caption("One Buffalo Labs - Portfolio Simulation")

# --- Sidebar ---
st.sidebar.header("Portfolio Settings")
st.sidebar.write("Current Holdings:")
st.sidebar.json(MOCK_PORTFOLIO)

# --- Main Execution ---
with st.spinner('Calculating portfolio value...'):
    try:
        # Fetch Data for Portfolio Assets
        tickers = list(MOCK_PORTFOLIO.keys())
        raw_data = fetch_stock_data(tickers)

        # Calculate Portfolio History
        total_value_series = calculate_portfolio_value(raw_data, MOCK_PORTFOLIO)

        # Current Stats
        current_total_value = total_value_series.iloc[-1]
        start_total_value = total_value_series.iloc[0]
        total_return = ((current_total_value - start_total_value) / start_total_value) * 100

        # --- Top Row Metrics ---
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Portfolio Value", f"${current_total_value:,.2f}")
        col2.metric("Total Return", f"{total_return:+.2f}%")
        col3.metric("Assets Tracked", len(tickers))

        st.divider()

        # --- Charts ---
        chart_col1, chart_col2 = st.columns([2, 1])

        with chart_col1:
            # Total Portfolio Value Chart
            st.subheader("Portfolio Performance (1 Year)")
            fig_history = px.line(
                total_value_series,
                title="Total Value Over Time",
                labels={"value": "Value ($)", "Date": "Date"}
            )
            # Add a filled area under the line for a "wealth" effect
            fig_history.update_traces(fill='tozeroy')
            st.plotly_chart(fig_history, use_container_width=True)

        with chart_col2:
            # Asset Allocation Pie Chart
            st.subheader("Asset Allocation")

            # Calculate current value per asset for the pie chart
            current_prices = {ticker: raw_data[ticker]['Close'].iloc[-1] for ticker in tickers}
            allocation_data = {
                'Asset': tickers,
                'Value': [price * MOCK_PORTFOLIO[t] for t, price in current_prices.items()]
            }
            df_allocation = pd.DataFrame(allocation_data)

            fig_pie = px.pie(
                df_allocation,
                values='Value',
                names='Asset',
                title="Current Allocation",
                hole=0.4 # Donut chart style
            )
            st.plotly_chart(fig_pie, use_container_width=True)

        # --- Detailed Data View ---
        with st.expander("View Portfolio Data"):
            st.dataframe(total_value_series.to_frame(name="Total Value"))

    except Exception as e:
        st.error(f"Error calculating portfolio: {e}")
        # Hint: If fetching fails, it's often because a ticker in the hardcoded list is invalid
        st.write("Debug info: Check if tickers in MOCK_PORTFOLIO are valid and reachable.")