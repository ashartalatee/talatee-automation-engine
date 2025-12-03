import pandas as pd
from src.clean_column_names import clean_column_names

FILE_PATH = "data/messy_column_names.csv"

def main():
    df = pd.read_csv(FILE_PATH)

    print("\n  DATA ASLI:")
    print(df.head())

    df_clean = clean_column_names(df)

    print("\n DATA SETELAH CLEAN:")
    print(df_clean.head())

if __name__ == "__main__":
    main()