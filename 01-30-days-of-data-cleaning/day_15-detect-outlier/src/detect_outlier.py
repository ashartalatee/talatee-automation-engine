import pandas as pd

def detect_outliers_iqr(df: pd.DataFrame, column: str):
    df = df.copy()

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - (1.5 * IQR)
    upper_bound = Q3 + (1.5 * IQR)

    print(f"\n Batas Bawah : {lower_bound}")
    print(f" Batas Atas : {upper_bound}")

    df['outlier'] = (df[column] < lower_bound) | (df[column] > upper_bound)

    return df