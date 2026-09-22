# Financial Data Pipeline

An ETL pipeline that downloads historical stock market data, cleans and transforms it with pandas, loads it into SQLite, and runs SQL analysis across multiple tickers. ML is used to train a baseline model to predict next day closing prices.

## Output Example
Deleted old database  
Deleted Data\raw\AAPL.csv  
Deleted Data\raw\AMZN.csv  
Deleted Data\raw\GOOGL.csv  
Deleted Data\raw\MSFT.csv  
Deleted Data\raw\TSLA.csv  
Deleted Data\processed\AAPL_processed.csv  
Deleted Data\processed\AMZN_processed.csv  
Deleted Data\processed\GOOGL_processed.csv  
Deleted Data\processed\MSFT_processed.csv  
Deleted Data\processed\TSLA_processed.csv  
Downloading stock data...  
Downloading stock data for AAPL  
Saved data for AAPL to Data/raw\AAPL.csv  
Downloading stock data for MSFT  
Saved data for MSFT to Data/raw\MSFT.csv  
Downloading stock data for GOOGL  
Saved data for GOOGL to Data/raw\GOOGL.csv  
Downloading stock data for AMZN  
Saved data for AMZN to Data/raw\AMZN.csv  
Downloading stock data for TSLA  
Saved data for TSLA to Data/raw\TSLA.csv  
Transforming data...  
Processing AAPL.csv...  
Dropped 0 duplicate rows  
Dropped 0 rows with missing values  
Added features: Daily Price Change, Daily Return, Daily Trading Range, 20-Day Moving Average, 5-Day Moving Average, 5-Day Volatility  
Saved processed data to Data\processed\AAPL_processed.csv  
Processing AMZN.csv...  
Dropped 0 duplicate rows  
Dropped 0 rows with missing values  
Added features: Daily Price Change, Daily Return, Daily Trading Range, 20-Day Moving Average, 5-Day Moving Average, 5-Day Volatility  
Saved processed data to Data\processed\AMZN_processed.csv  
Processing GOOGL.csv...  
Dropped 0 duplicate rows  
Dropped 0 rows with missing values  
Added features: Daily Price Change, Daily Return, Daily Trading Range, 20-Day Moving Average, 5-Day Moving Average, 5-Day Volatility  
Saved processed data to Data\processed\GOOGL_processed.csv  
Processing MSFT.csv...  
Dropped 0 duplicate rows  
Dropped 0 rows with missing values  
Added features: Daily Price Change, Daily Return, Daily Trading Range, 20-Day Moving Average, 5-Day Moving Average, 5-Day Volatility  
Saved processed data to Data\processed\MSFT_processed.csv  
Processing TSLA.csv...  
Dropped 0 duplicate rows  
Dropped 0 rows with missing values  
Added features: Daily Price Change, Daily Return, Daily Trading Range, 20-Day Moving Average, 5-Day Moving Average, 5-Day Volatility  
Saved processed data to Data\processed\TSLA_processed.csv  
Loading database...  
Loading AAPL_processed.csv into database...  
Loading AMZN_processed.csv into database...  
Loading GOOGL_processed.csv into database...  
Loading MSFT_processed.csv into database...  
Loading TSLA_processed.csv into database...  
           name  
0  stock_prices  
Running SQL queries...  
Ticker with highest average return: TSLA with avg return: 0.10299181992788116 %  
Ticker with highest average trading volume: TSLA with avg volume: 95228602.2310757  
Ticker with highest average closing price: MSFT with avg close: 365.86977055158275  
  
Number of trading days for each ticker:  
  AAPL: 1255  
  MSFT: 1255  
  GOOGL: 1255  
  AMZN: 1255  
  TSLA: 1255  
Performing machine learning predictions...  
[AAPL] Mean absolute error on next-day close prediction: $4.29  
[MSFT] Mean absolute error on next-day close prediction: $8.45  
[GOOGL] Mean absolute error on next-day close prediction: $6.83  
[AMZN] Mean absolute error on next-day close prediction: $5.05  
[TSLA] Mean absolute error on next-day close prediction: $11.02  
Pipeline complete  

## Overview

The pipeline runs in three stages:

1. **Extract** - downloads historical stock data for a list of tickers and saves it as raw CSV files
2. **Transform** - cleans each file (removes duplicates and missing values) and creates features (daily price change, daily return (%), daily trading range, and 5-day/20-day moving averages and volatility)
3. **Load** - writes the processed data for every ticker into a single SQLite table (`stock_prices`), tagging each row with its ticker

From there, `queries.py` runs SQL analysis across all tickers, and `model.py` trains a linear regression model as an extension beyond the core pipeline.

## Requirements

- Python 3.14
- pandas
- SQLite (`sqlite3`)
- scikit-learn
- Matplotlib


## Installation

```bash
git clone https://github.com/leela-l/financial-data-pipeline.git
cd financial-data-pipeline
pip install -r requirements.txt
```

## How to run

```bash
python main.py
```

This runs extract → transform → load. To run the SQL analysis or the prediction model separately:

```bash
python src/queries.py
python src/model.py
```

## ML Next Day Close Prediction

`model.py` trains a linear regression model per ticker to predict the next day's closing price, using same day features (5-day and 20-day moving averages, daily return, 5-day volatility).

The data is split chronologically (earliest 80% for training, most recent 20% for testing) rather than shuffled randomly since data is time dependent.

Prediction plots (actual vs. predicted close over the test period) are saved to `Data/processed/`.
