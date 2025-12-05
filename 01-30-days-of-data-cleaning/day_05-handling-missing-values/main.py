import pandas as pd
from src.handle_missing import handle_missing

FILE_PATH = "../day_05-handling-missing-values/data/mini_missing_values.csv"

def main():
    df = pd.read_csv(FILE_PATH)

    print("\n DATASET ASLI")
    print(df)

    df_clean = handle_missing(df)

    print("\n DATASET SETELAH DIBERSIHKAN")
    print(df_clean)

if __name__ == "__main__":
    main()