import pandas as pd
from src.detect_outlier import detect_outliers_iqr

FILE_PATH = "data/raw_outliers.csv"

def main():
    df = pd.read_csv(FILE_PATH)

    print("\n DATA ASLI")
    print(df)

    df_checked = detect_outliers_iqr(df, "income")

    print("\n DATA DENGAN LABEL OUTLIER")
    print(df_checked)

    outliers = df_checked[df_checked["outlier"] == True]
    normal = df_checked[df_checked["outlier"] == False]

    print("\n DATA OUTLIER")
    print(outliers)

    print("\n DATA NORMAL")
    print(normal)

if __name__ == "__main__":
    main()