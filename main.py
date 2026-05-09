from src.report_generator import generate_report
from src.visualization import (
    plot_closing_price,
    plot_moving_averages,
    plot_daily_returns,
    plot_return_distribution
)

from src.data_fetcher import fetch_stock_data, save_to_csv
from src.analysis import (
    clean_data,
    calculate_daily_returns,
    calculate_moving_averages,
    calculate_volatility,
    generate_summary
)

from datetime import datetime


def main():

    ticker = "AAPL"

    start_date = "2023-01-01"

    end_date = datetime.today().strftime('%Y-%m-%d')

    # Fetch stock data
    stock_data = fetch_stock_data(
        ticker,
        start_date,
        end_date
    )

    if stock_data is not None:

        # Save raw data
        save_to_csv(stock_data, ticker)

        # Clean data
        stock_data = clean_data(stock_data)

        # Calculate daily returns
        stock_data = calculate_daily_returns(stock_data)

        # Calculate moving averages
        stock_data = calculate_moving_averages(stock_data)

        # Calculate volatility
        volatility = calculate_volatility(stock_data)

        # Generate summary
        generate_summary(stock_data, volatility)

         # Generate visualizations
        plot_closing_price(stock_data, ticker)

        plot_moving_averages(stock_data, ticker)

        plot_daily_returns(stock_data, ticker)

        plot_return_distribution(stock_data, ticker)

         # Generate report
        generate_report(
            stock_data,
            ticker,
            volatility
        )
        
        # Save processed data
        stock_data.to_csv(
            f"outputs/{ticker}_processed_stock_data.csv"
        )

        print("\nProcessed data saved successfully!")


if __name__ == "__main__":
    main()