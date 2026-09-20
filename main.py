from pathlib import Path

from src.extract import main as extract
from src.transform import main as transform
from src.database import main as database
from src.queries import main as queries

import logging


logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

def clean_previous_data():
    # Delete database
    db_file = Path("stock_data.db")
    if db_file.exists():
        db_file.unlink()
        logger.info("Deleted old database")

    # Delete old CSV files
    folders = [
        Path("Data/raw"),
        Path("Data/processed")
    ]

    for folder in folders:
        if folder.exists():
            for file in folder.glob("*.csv"):
                file.unlink()
                logger.info(f"Deleted {file}")

def main():
    clean_previous_data()
    logger.info("Downloading stock data...")
    extract()

    logger.info("Transforming data...")
    transform()

    logger.info("Loading database...")
    database()

    logger.info("Running SQL queries...")
    queries()

    logger.info("Pipeline complete")

if __name__ == "__main__":
    main()