# Financial Data Pipeline

## Overview

This project downloads historical stock market data using Yahoo Finance,
transforms it with pandas, stores it in SQLite and performs SQL analysis.

## Technologies

- Python
- pandas
- SQLite
- Git
- GitHub

## Project structure

financial-data-pipeline/
│
├── Data/
│ ├── raw/ # Raw stock CSV files downloaded from the API
│ └── processed/ # Cleaned datasets with added useful features
│
├── src/
│ ├── extract.py # Extracts stock market data and saves raw CSV files
│ ├── transform.py # Cleans data and creates additional features
│ ├── database.py # Loads processed data into a SQLite database
│ └── queries.py # Runs SQL queries to analyse stock performance
│
├── main.py # Runs the complete ETL pipeline
├── stock_data.db # SQLite database containing processed stock data
├── requirements.txt # Python dependencies
└── README.md # Project documentation

## How to run

python main.py