import sqlite3
from matplotlib import ticker
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, root_mean_squared_error
import matplotlib.pyplot as plt


FEATURES = [
    "5-Day Moving Average",
    "20-Day Moving Average",
    "Daily Return",
    "5-Day Volatility",
]


def load_ticker_data(conn, ticker):
    df = pd.read_sql_query(
        """
        SELECT *
        FROM stock_prices
        WHERE Ticker = ?
        ORDER BY "Date"
        """,
        conn,
        params=(ticker,),
    )
    return df


def prepare_data(df):
    df = df.dropna(subset=FEATURES + ["Close"]).copy()
    df["Target"] = df["Close"].shift(-1)  # next day's closing price
    df = df.dropna(subset=["Target"])
    return df


def train_and_evaluate(df, ticker):
    X = df[FEATURES]
    y = df["Target"]

    # chronological split, never shuffle time series data
    split = int(len(df) * 0.8)
    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]

    model = LinearRegression()
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    
    baseline_preds = df["Close"].iloc[split:]   # today's close as the prediction for tomorrow

      
    model_mae = mean_absolute_error(y_test, preds)
    base_mae = mean_absolute_error(y_test, baseline_preds)
    model_rmse = root_mean_squared_error(y_test, preds)
    base_rmse = root_mean_squared_error(y_test, baseline_preds)

    improvement = (base_mae - model_mae) / base_mae * 100  # positive = model better

    print(f"[{ticker}] MAE  model: ${model_mae:.2f} | baseline: ${base_mae:.2f}")
    print(f"[{ticker}] RMSE model: ${model_rmse:.2f} | baseline: ${base_rmse:.2f}")
    print(f"[{ticker}] Model vs baseline (MAE): {improvement:+.1f}%")

    plt.figure(figsize=(10, 5))
    plt.plot(y_test.values, label="Actual")
    plt.plot(preds, label="Predicted")
    plt.title(f"{ticker}: Predicted vs Actual Next-Day Close")
    plt.xlabel("Trading day (test set)")
    plt.ylabel("Price ($)")
    plt.legend()
    plt.savefig(f"Data/processed/{ticker}_prediction_plot.png")
    plt.close()

    return model, model_mae, base_mae


def main():
    conn = sqlite3.connect("stock_data.db")
    tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]

    for ticker in tickers:
        df = load_ticker_data(conn, ticker)
        df = prepare_data(df)
        if len(df) < 30:
            print(f"[{ticker}] Not enough data, skipping")
            continue
        train_and_evaluate(df, ticker)

    conn.close()


if __name__ == "__main__":
    main()