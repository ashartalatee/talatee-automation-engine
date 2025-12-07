import pandas as pd
from src.standardize import standardize_data

FILE_PATH = "data/raw_format.csv"

def main():
    df = pd.read_csv(FILE_PATH)

    print("\n DATA SEBELUM STANDARDISASI")
    print(df)

    df_clean = standardize_data(df)

    print("\n DATA SIAP PAKAI (STANDARD)")
    print(df_clean)

if __name__ == "__main__":
    main()