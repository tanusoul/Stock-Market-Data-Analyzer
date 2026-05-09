import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date


st.set_page_config(
    page_title="Stock Market Data Analyzer",
    layout="wide"
)

st.title("📈 Stock Market Data Analyzer")

st.markdown("""
Analyze stock market trends, moving averages,
returns, and volatility using Python.
""")


# Sidebar Inputs
st.sidebar.header("User Input")

ticker = st.sidebar.text_input(
    "Enter Stock Ticker",
    "AAPL"
)

start_date = st.sidebar.date_input(
    "Start Date",
    date(2023, 1, 1)
)

end_date = st.sidebar.date_input(
    "End Date",
    date.today()
)


# Fetch Data
@st.cache_data
def load_data(ticker, start, end):

    data = yf.download(
        ticker,
        start=start,
        end=end
    )

    # Fix multi-level columns
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    return data


data = load_data(
    ticker,
    start_date,
    end_date
)


if data.empty:

    st.error("No stock data found.")

else:

    st.subheader(f"{ticker} Stock Data")

    st.dataframe(data.tail())

    # Moving averages
    data['MA_20'] = data['Close'].rolling(20).mean()

    data['MA_50'] = data['Close'].rolling(50).mean()

    # Daily returns
    data['Daily Return %'] = (
        data['Close'].pct_change() * 100
    )

    # Metrics
    latest_close = data['Close'].iloc[-1]

    highest_price = data['High'].max()

    lowest_price = data['Low'].min()

    volatility = data['Daily Return %'].std()

    # Display metrics
    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Latest Close",
        f"{latest_close:.2f}"
    )

    col2.metric(
        "Highest Price",
        f"{highest_price:.2f}"
    )

    col3.metric(
        "Lowest Price",
        f"{lowest_price:.2f}"
    )

    col4.metric(
        "Volatility",
        f"{volatility:.2f}"
    )

    # Closing price chart
    st.subheader("📊 Closing Price Chart")

    fig1, ax1 = plt.subplots(figsize=(12, 5))

    ax1.plot(data['Close'])

    ax1.set_title(f"{ticker} Closing Price")

    st.pyplot(fig1)

    # Moving averages chart
    st.subheader("📈 Moving Average Analysis")

    fig2, ax2 = plt.subplots(figsize=(12, 5))

    ax2.plot(data['Close'], label='Close')

    ax2.plot(data['MA_20'], label='20-Day MA')

    ax2.plot(data['MA_50'], label='50-Day MA')

    ax2.legend()

    st.pyplot(fig2)

    # Daily returns chart
    st.subheader("📉 Daily Returns")

    fig3, ax3 = plt.subplots(figsize=(12, 5))

    ax3.plot(data['Daily Return %'])

    ax3.set_title("Daily Return Percentage")

    st.pyplot(fig3)

    # Final insights
    st.subheader("🧠 Final Insights")

    if data['MA_20'].iloc[-1] > data['MA_50'].iloc[-1]:
        st.success("Bullish Trend Detected 📈")
    else:
        st.warning("Bearish Trend Detected 📉")

    if volatility < 1:
        st.info("Low Risk Stock")
    elif volatility < 2:
        st.info("Moderate Risk Stock")
    else:
        st.error("High Risk Stock")


st.markdown("---")

st.caption(
    "Educational Project Only | Not Financial Advice"
)