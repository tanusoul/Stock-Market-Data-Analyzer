import matplotlib.pyplot as plt
import seaborn as sns


# Set chart style
sns.set_style("darkgrid")


def plot_closing_price(data, ticker):
    """
    Plot stock closing price
    """

    plt.figure(figsize=(12, 6))

    plt.plot(data['Close'], label='Closing Price')

    plt.title(f"{ticker} Closing Price")

    plt.xlabel("Date")

    plt.ylabel("Price")

    plt.legend()

    filename = f"images/{ticker}_closing_price.png"

    plt.savefig(filename)

    plt.close()

    print(f"Closing price chart saved: {filename}")


def plot_moving_averages(data, ticker):
    """
    Plot moving averages
    """

    plt.figure(figsize=(12, 6))

    plt.plot(data['Close'], label='Closing Price')

    plt.plot(data['MA_20'], label='20-Day MA')

    plt.plot(data['MA_50'], label='50-Day MA')

    plt.title(f"{ticker} Moving Averages")

    plt.xlabel("Date")

    plt.ylabel("Price")

    plt.legend()

    filename = f"images/{ticker}_moving_averages.png"

    plt.savefig(filename)

    plt.close()

    print(f"Moving average chart saved: {filename}")


def plot_daily_returns(data, ticker):
    """
    Plot daily returns
    """

    plt.figure(figsize=(12, 6))

    plt.plot(data['Daily Return %'])

    plt.title(f"{ticker} Daily Returns")

    plt.xlabel("Date")

    plt.ylabel("Daily Return %")

    filename = f"images/{ticker}_daily_returns.png"

    plt.savefig(filename)

    plt.close()

    print(f"Daily returns chart saved: {filename}")


def plot_return_distribution(data, ticker):
    """
    Plot return distribution
    """

    plt.figure(figsize=(10, 6))

    sns.histplot(
        data['Daily Return %'].dropna(),
        bins=50,
        kde=True
    )

    plt.title(f"{ticker} Return Distribution")

    plt.xlabel("Daily Return %")

    filename = f"images/{ticker}_return_distribution.png"

    plt.savefig(filename)

    plt.close()

    print(f"Return distribution chart saved: {filename}")