print("Starting data transformation...")
import pandas as pd
from pathlib import Path

RAW_FOLDER = Path("Data/raw")
PROCESSED_FOLDER = Path("Data/processed")

PROCESSED_FOLDER.mkdir(parents=True, exist_ok=True)


for csv_file in RAW_FOLDER.glob("*.csv"):
    df = pd.read_csv(csv_file)
    
    print(df.head())
    print(df.info())
    print(df.describe())