import pandas as pd
from src.clean_outliers_z import remove_outliers_zscore

FILE_PATH = "data/mini_outliers.csv"

def main():
    df = pd.read_csv(FILE_PATH)
    print("\n DATA ASLI")
    print(df)

    # Pastikan kolom numeric benar-benar numeric
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")

    df_clean = remove_outliers_zscore(df, "price", threshold=2.5)

    print("\n DATA SETELAH OUTLIERS REMOVED (Z-score)")
    print(df_clean)

if __name__ == "__main__":
    main()
