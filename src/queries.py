import sqlite3
import pandas as pd


def main():
    conn = sqlite3.connect("stock_data.db")

    tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']


    # Average return
    avg_returns = {}
    # Average trading volume
    avg_volumes = {}
    # Average closing price
    avg_closing_prices = {}
    # Number of trading days
    trading_days = {}

    for ticker in tickers:
        result_av_returns = pd.read_sql_query(
            f"""
            SELECT AVG("Daily Return") as avg_return
            FROM stock_prices
            WHERE Ticker = ?
            """,
            conn,
            params=(ticker,)
        )

        avg_returns[ticker] = result_av_returns['avg_return'][0]

        result_avg_volumes = pd.read_sql_query(
                """
                SELECT AVG("Volume") as avg_volume
                FROM stock_prices
                WHERE Ticker = ?
                """,
                conn,
                params=(ticker,)
            )
        
        avg_volumes[ticker] = result_avg_volumes['avg_volume'][0]

        result_avg_closing_prices = pd.read_sql_query(
                """
                SELECT AVG("Close") as avg_close
                FROM stock_prices
                WHERE Ticker = ?
                """,
                conn,
                params=(ticker,)
            )
        
        avg_closing_prices[ticker] = result_avg_closing_prices['avg_close'][0]

        result_trading_days = pd.read_sql_query(
                """
                SELECT COUNT(*) as trading_days
                FROM stock_prices
                WHERE Ticker = ?
                """,
                conn,
                params=(ticker,)
            )
        
        trading_days[ticker] = result_trading_days['trading_days'][0]




    best_ticker = max(avg_returns, key=avg_returns.get)

    print(
        f"Ticker with highest average return: {best_ticker} "
        f"with avg return: {avg_returns[best_ticker]} %"
    )

    highest_volume_ticker = max(avg_volumes, key=avg_volumes.get)

    print(
        f"Ticker with highest average trading volume: {highest_volume_ticker} "
        f"with avg volume: {avg_volumes[highest_volume_ticker]}"
    ) 


    highest_closing_price_ticker = max(avg_closing_prices, key=avg_closing_prices.get)

    print(
        f"Ticker with highest average closing price: {highest_closing_price_ticker} "
        f"with avg close: {avg_closing_prices[highest_closing_price_ticker]}"
    )


    print("\nNumber of trading days for each ticker:")
    for ticker, days in trading_days.items():
        print(f"  {ticker}: {days}")


    conn.close()


if __name__ == "__main__":
    main()