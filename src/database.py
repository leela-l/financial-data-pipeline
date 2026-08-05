import sqlite3
# No pip install needed, sqlite3 is part of the Python standard library
from pathlib import Path
import pandas as pd

def main():
    conn = sqlite3.connect("stock_data.db")
    # Opens a connection to the SQLite database file named "stock_data.db"
    # If the file does not exist, it will be created

    PROCESSED_FOLDER = Path("Data/processed")

    for csv_file in PROCESSED_FOLDER.glob("*.csv"):
        
        print(f"Loading {csv_file.name} into database...")

        df = pd.read_csv(csv_file, index_col=0, parse_dates=True)
        # reads each CSV file into a pandas DataFrame

        ticker = csv_file.stem.replace("_processed", "")
        # creates a table name by removing the "_processed" suffix from the CSV file name

        df["Ticker"] = ticker
        # adds a new column to the DataFrame with the ticker symbol
    
        df.to_sql("stock_prices", conn, if_exists='append', index_label='Date', index=True)
        # writes the DataFrame to a SQL table in the SQLite database
        # if_exists='replace' means that if a table with the same name already exists, it will be replaced
        # index_label='Date' specifies that the index column should be labeled as 'Date' in the SQL table

    #tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn)
    # print(tables) CHECKS

    tables = pd.read_sql(
    "SELECT name FROM sqlite_master WHERE type='table';",
    conn)

    print(tables)



    conn.close()


if __name__ == "__main__":
    main()

