from pathlib import Path

from src.extract import main as extract
from src.transform import main as transform
from src.database import main as database
from src.queries import main as queries

def clean_previous_data():
    # Delete database
    db_file = Path("stock_data.db")
    if db_file.exists():
        db_file.unlink()
        print("Deleted old database")

    # Delete old CSV files
    folders = [
        Path("Data/raw"),
        Path("Data/processed")
    ]

    for folder in folders:
        if folder.exists():
            for file in folder.glob("*.csv"):
                file.unlink()
                print(f"Deleted {file}")

def main():
    clean_previous_data()
    print("Downloading stock data...")
    extract()

    print("Transforming data...")
    transform()

    print("Loading database...")
    database()

    print("Running SQL queries...")
    queries()

    print("Pipeline complete")

if __name__ == "__main__":
    main()