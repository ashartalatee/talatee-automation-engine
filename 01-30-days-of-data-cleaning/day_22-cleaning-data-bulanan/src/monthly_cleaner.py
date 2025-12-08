import pandas as pd
from pathlib import Path

def load_all_files(folder_path: str) -> pd.DataFrame:
    folder = Path(folder_path)
    all_files = folder.glob("*.csv")

    df_list = []

    for file in all_files:
        print(f" Memuat: {file.name}")
        df = pd.read_csv(file)
        df_list.append(df)

    combined_df = pd.concat(df_list, ignore_index=True)

    return combined_df


def clean_monthly_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Cleaning missing value
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df["amount"] = df["amount"].fillna(df["amount"].median())

    # Outlier flag
    Q1 = df["amount"].quantile(0.25)
    Q3 = df["amount"].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df["is_outlier"] = (df["amount"] < lower) | (df["amount"] > upper)

    return df
