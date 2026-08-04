import pandas as pd
from pathlib import Path


# Path is a class in the pathlib module that provides an object-oriented interface for working with file system paths


def clean_data(df):
    """
    Clean the stock data DataFrame by removing duplicates and handling missing values.

    Parameters:
        df (DataFrame): Stock data DataFrame to clean."""
    
    df = df.sort_index(ascending=True)
    # sorts by date as date is the index of the DataFrame
    
    duplicates = df.duplicated().sum()

    df = df.drop_duplicates()

    print(f"Dropped {duplicates} duplicate rows")
    
     
    missing_rows = df.isnull().sum().sum()
    
    df = df.dropna()
    # drops the row with missing values in any columns
    
    print(f"Dropped {missing_rows} rows with missing values")

    return df

def add_features(df):
    """
    Add additional features to the stock data DataFrame.

    Parameters:
        df (DataFrame): Stock data DataFrame to add features to.
    """

    df["Daily Price Change"] = df["Close"] - df["Open"]
        # calculates the difference between the closing price and opening price for each day
    
    
    df["Daily Return"] = df["Close"].pct_change()* 100
        # finds percentage change between closing price today and yesterday
    
    
    df["Daily Trading Range"] = df["High"] - df["Low"]
        # calculates the difference between the highest and lowest price for each day
    
    
    df["20-Day Moving Average"] = df["Close"].rolling(window=20).mean()
        # calculates the rolling average closing price over the last 20 days

    print (f"Added features: Daily Price Change, Daily Return, Daily Trading Range, 20-Day Moving Average")

    return df


def save_processed_data(df, output_path):
    """
    Save the processed stock data DataFrame to a CSV file.

    Parameters:
        df (DataFrame): Processed stock data DataFrame to save.
        output_path (Path): Path to save the CSV file.
    """
    df.to_csv(output_path)
    print(f"Saved processed data to {output_path}")
      



def main():

    RAW_FOLDER = Path("Data/raw")
    # creates a Path object for folder

    PROCESSED_FOLDER = Path("Data/processed")

    PROCESSED_FOLDER.mkdir(parents=True, exist_ok=True)
    # creates the processed folder if it doesn't already exist


    for csv_file in RAW_FOLDER.glob("*.csv"):
        # uses the glob method of the Path object to find all CSV files in the raw folder

        print(f"Processing {csv_file.name}...")

        df = pd.read_csv(csv_file, index_col=0, parse_dates=True)
        # reads each CSV file into a pandas DataFrame
        # index_col=0 argument specifies that the first column should be used as the index 
        # parse_dates=True tells pandas to parse the index as dates
        
        df = clean_data(df)
        df = add_features(df)
        

        output_path = PROCESSED_FOLDER / f"{csv_file.stem}_processed.csv"
        # saves the processed DataFrame to a new CSV file in the processed folder, using the same name as the original file
    
        save_processed_data(df, output_path)


if __name__ == "__main__":
    main()














