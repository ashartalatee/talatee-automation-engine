import pandas as pd

def detect_outliers(df: pd.DataFrame, column: str) -> pd.DataFrame:
    df = df.copy()

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    print(f"\n Batas bawah: {lower}")
    print(f" Batas atas : {upper}")

    df["is_outlier"] = (df[column] < lower) | (df[column] > upper)

    print("\n Data dengan flag outlier:")
    print(df)

    return df
