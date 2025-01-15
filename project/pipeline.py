import os
import pandas as pd
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILES = [
    os.path.join(BASE_DIR, "../data", "air_quality.csv"),
]

DATA_DIR = os.path.join(BASE_DIR, "../data")
DB_PATH = os.path.join(DATA_DIR, "air_quality.db")

def load_data(file_path):
    df = pd.read_csv(file_path)
    print(f"Loaded data from {file_path} with {len(df)} rows.")
    return df

def clean_data(df):
    df = df[df["Name"] == "Fine particles (PM 2.5)"]
    df = df[df["Geo Type Name"] == "UHF42"]
    df = df.drop(columns=["Message"], errors="ignore")
    df = df.dropna(how="all")  
    print(f"Data after cleaning has {len(df)} rows.")
    return df


def store_data(df, table_name, db_path):
    try:
        with sqlite3.connect(db_path) as conn:
            df.to_sql(table_name, conn, if_exists="replace", index=False)
            print(f"Stored {len(df)} rows in table {table_name}.")
    except Exception as e:
        print(f"Failed to store data in {table_name}: {e}")

def main():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    for i, file_path in enumerate(DATA_FILES, start=1):
        df = load_data(file_path)
        df = clean_data(df)
        store_data(df, f"dataset_{i}", DB_PATH)
    print("Data pipeline completed successfully.")

if __name__ == "__main__":
    main()
