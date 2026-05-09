from datetime import datetime


def generate_report(data, ticker, volatility):
    """
    Generate stock analysis report
    """

    latest_close = data['Close'].iloc[-1]

    average_close = data['Close'].mean()

    highest_price = data['High'].max()

    lowest_price = data['Low'].min()

    average_return = data['Daily Return %'].mean()

    # Trend logic
    latest_ma20 = data['MA_20'].iloc[-1]

    latest_ma50 = data['MA_50'].iloc[-1]

    if latest_ma20 > latest_ma50:
        trend = "Bullish Trend 📈"
    else:
        trend = "Bearish Trend 📉"

    # Volatility interpretation
    if volatility < 1:
        risk_level = "Low Risk"
    elif volatility < 2:
        risk_level = "Moderate Risk"
    else:
        risk_level = "High Risk"

    report = f"""
==================================================
        STOCK MARKET ANALYSIS REPORT
==================================================

Ticker Symbol: {ticker}

Report Generated On:
{datetime.now()}

--------------------------------------------------
PRICE ANALYSIS
--------------------------------------------------

Latest Closing Price: {latest_close:.2f}

Average Closing Price: {average_close:.2f}

Highest Price: {highest_price:.2f}

Lowest Price: {lowest_price:.2f}

--------------------------------------------------
RETURN ANALYSIS
--------------------------------------------------

Average Daily Return: {average_return:.2f}%

Volatility: {volatility:.2f}

Risk Level: {risk_level}

--------------------------------------------------
TREND ANALYSIS
--------------------------------------------------

20-Day Moving Average: {latest_ma20:.2f}

50-Day Moving Average: {latest_ma50:.2f}

Current Trend: {trend}

--------------------------------------------------
FINAL INSIGHTS
--------------------------------------------------

1. The stock trend is identified using moving averages.

2. Volatility helps estimate market risk.

3. Daily returns indicate short-term performance.

4. Investors can use this analysis for educational
   research and market understanding.

==================================================
DISCLAIMER
==================================================

This project is created for educational purposes only.

This is NOT financial or investment advice.

==================================================
"""

    filename = f"reports/{ticker}_analysis_report.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(report)

    print(f"\nReport generated successfully: {filename}")