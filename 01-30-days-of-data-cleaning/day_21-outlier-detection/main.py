import pandas as pd
from src.detect_outlier import detect_outliers

FILE_PATH = "data/sales_with_outlier.csv"

def main():
    df = pd.read_csv(FILE_PATH)

    print("\n DATA ASLI")
    print(df)

    df_outlier = detect_outliers(df, "amount")

    outliers = df_outlier[df_outlier["is_outlier"] == True]

    print("\n DATA OUTLIER")
    print(outliers)

    df_outlier.to_csv("data/sales_checked.csv", index=False)
    print("\n File tersimpan: sales_checked.csv")

if __name__ == "__main__":
    main()
