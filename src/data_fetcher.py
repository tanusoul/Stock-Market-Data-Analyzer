import yfinance as yf
import pandas as pd
from datetime import datetime


def fetch_stock_data(ticker, start_date, end_date):
    """
    Fetch stock market data using Yahoo Finance
    """

    print(f"\nFetching data for {ticker}...")

    stock = yf.download(
        ticker,
        start=start_date,
        end=end_date
    )

    # Fix multi-level columns if present
    if isinstance(stock.columns, pd.MultiIndex):
        stock.columns = stock.columns.get_level_values(0)

    if stock.empty:
        print("No data found.")
        return None

    print("\nData fetched successfully!")
    print(stock.head())

    return stock


def save_to_csv(data, ticker):
    """
    Save stock data to CSV
    """

    filename = f"data/{ticker}_stock_data.csv"

    data.to_csv(filename)

    print(f"\nData saved to: {filename}")


if __name__ == "__main__":

    ticker = "AAPL"

    start_date = "2023-01-01"

    end_date = datetime.today().strftime('%Y-%m-%d')

    stock_data = fetch_stock_data(
        ticker,
        start_date,
        end_date
    )

    if stock_data is not None:
        save_to_csv(stock_data, ticker)