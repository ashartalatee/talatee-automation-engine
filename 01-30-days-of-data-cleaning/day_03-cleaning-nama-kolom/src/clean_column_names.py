import pandas as pd
import re

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Bersihkan & standarkan nama kolom
    """
    print("\n BEFORE:")
    print(df.columns)

    new_cols = []

    for col in df.columns:
        col = col.strip()                   # hapus spasi depan-belakang
        col = col.lower()                   # huruf kecil
        col = re.sub(r"[^\w/s]", "", col) # hapus simbol
        col = re.sub(r"\s+", "_", col) # ganti spasi jadi_
        new_cols.append(col)

    df.columns = new_cols
    print("\n AFTER:")
    print(df.columns)

    return df