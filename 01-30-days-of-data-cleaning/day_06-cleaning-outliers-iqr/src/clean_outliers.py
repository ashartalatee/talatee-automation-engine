import pandas as pd

def remove_outliers_iqr(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Bersihkan outlier numeric berdasarkan IQR
    """
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5* IQR
    upper_bound = Q3 + 1.5 * IQR

    print(f"\n {column} - Lower Bound: {lower_bound}, Upper Bound: {upper_bound}")

    df_clean = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    print(f"Jumlah baris setelah remove outliers: {len(df_clean)}")

    return df_clean