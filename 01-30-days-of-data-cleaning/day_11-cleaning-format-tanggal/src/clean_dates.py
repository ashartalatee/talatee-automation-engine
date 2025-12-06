import pandas as pd
from datetime import datetime

def parse_flexible_date(date_str):
    """
    Parse tanggal dengan berbagai format menjadi YYYY-MM-DD
    """
    formats = [
        "%Y-%m-%d",    # 2024-01-01
        "%d/%m/%y",    # 01/02/24
        "%d/%m/%Y",    # 01/02/2024
        "%Y.%m.%d",    # 2024.04.04
        "%d-%b-%Y",    # 05-May-2024
        "%B %d, %Y"    # March 3, 2025
    ]
    for fmt in formats:
        try:
            return datetime.strptime(str(date_str), fmt)
        except:
            continue
    return pd.NaT

def clean_date_column(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Bersihkan & standarkan tanggal ke format YYYY-MM-DD
    """
    print("\n SEBELUM CLEANING")
    print(df[column])

    df[column] = df[column].apply(parse_flexible_date)

    print("\n SESUDAH CLEANING")
    print(df[column])

    return df
