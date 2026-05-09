import pandas as pd
import numpy as np


def clean_data(data):
    """
    Clean stock market data
    """

    print("\nCleaning data...")

    # Remove missing values
    data = data.dropna()

    print("Missing values removed.")

    return data


def calculate_daily_returns(data):
    """
    Calculate daily percentage returns
    """

    print("\nCalculating daily returns...")

    data['Daily Return %'] = data['Close'].pct_change() * 100

    return data


def calculate_moving_averages(data):
    """
    Calculate moving averages
    """

    print("\nCalculating moving averages...")

    data['MA_20'] = data['Close'].rolling(window=20).mean()

    data['MA_50'] = data['Close'].rolling(window=50).mean()

    return data


def calculate_volatility(data):
    """
    Calculate stock volatility
    """

    print("\nCalculating volatility...")

    volatility = data['Daily Return %'].std()

    return volatility


def highest_lowest_analysis(data):
    """
    Find highest and lowest prices
    """

    highest_price = data['High'].max()

    lowest_price = data['Low'].min()

    return highest_price, lowest_price


def generate_summary(data, volatility):
    """
    Generate stock analysis summary
    """

    print("\n========== STOCK ANALYSIS SUMMARY ==========")

    latest_close = data['Close'].iloc[-1]

    average_close = data['Close'].mean()

    print(f"\nLatest Closing Price: {latest_close:.2f}")

    print(f"Average Closing Price: {average_close:.2f}")

    print(f"Volatility: {volatility:.2f}")

    highest_price, lowest_price = highest_lowest_analysis(data)

    print(f"Highest Price: {highest_price:.2f}")

    print(f"Lowest Price: {lowest_price:.2f}")

    print("\n============================================")