import pandas as pd
from src.clean_numeric import clean_numeric_columns

FILE_PATH = "data/mini_numeric_dirty.csv"

def main():
    df = pd.read_csv(FILE_PATH)

    df_clean = clean_numeric_columns(df)

    print("\n FINAL RESULT")
    print(df_clean)
    print("\n Tipe Data Sekarang:")
    print(df_clean.dtypes)

if __name__ == "__main__":
    main()