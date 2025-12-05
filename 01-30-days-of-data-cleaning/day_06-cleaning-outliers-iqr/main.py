import pandas as pd
from src.clean_outliers import remove_outliers_iqr

FILE_PATH = "data/mini_outliers.csv"

def main():
    df = pd.read_csv(FILE_PATH)
    print("\n DATA ASLI")
    print(df)

    df_clean = remove_outliers_iqr(df, "price")

    print("\n DATA SETELAH OUTLIERS REMOVED")
    print(df_clean)

if __name__ == "__main__":
    main()