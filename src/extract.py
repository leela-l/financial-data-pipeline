import yfinance as yf
import pandas as pd
import os


TICKERS = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']

def download_stock_data(tickers, period = "5y"):
    """
    Download historical stock data for the given tickers and date range.

    Parameters:
        tickers (list): List of stock tickers.
        period (str): Period for which to download data.
    """

    print(f"Downloading stock data for {tickers}")

    data = yf.download(tickers, period=period)

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    return data


def save_data_to_csv(data, ticker, folder='Data/raw'):
    """
    Save the stock data to a CSV file.

    Parameters:
        data (DataFrame): Stock data to save.
        ticker (str): Stock ticker.
        folder (str): Folder to save the CSV file in.
    """
    if not os.path.exists(folder):
        os.makedirs(folder)

    # can also use os.makedirs(folder, exist_ok=True)
    
    file_path = os.path.join(folder, f"{ticker}.csv")
    # Could just do folder + "/" + f"{ticker}.csv" but os.path.join is more robust and cross-platform
    data.to_csv(file_path)
    print(f"Saved data for {ticker} to {file_path}")


def main():
    for ticker in TICKERS:
        data = download_stock_data(ticker)
        save_data_to_csv(data, ticker)


if __name__ == "__main__":
    main()

