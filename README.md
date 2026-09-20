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

This runs the full pipeline. It downloads historical stock data, cleans and transforms it with pandas, loads it into a local SQLite database (`stock_data.db`), and executes the SQL analysis queries.