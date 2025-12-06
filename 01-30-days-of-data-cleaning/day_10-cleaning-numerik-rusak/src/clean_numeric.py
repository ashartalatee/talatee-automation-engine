import pandas as pd
import re

def convert_to_number(value):
    if pd.isna(value):
        return value
    
    value = str(value).lower().strip()

    # ubah juta ke angka
    if "juta" in value:
        num = re.findall(f"\d+", value)
        return float(num[0]) * 1_000_000 if num else value
    
    # ubah ke ke ribuan
    if "k" in value:
        num = re.findall(r"\d+", value)
        return float(num[0]) * 1_000 if num else value
    
    # Hapus Rp, koma, spasi
    value = value.replace("rp", "").replace(",", "").strip()

    # Hapus semua selain angka dan titik
    value = re.sub(r"[^0-9.]", "", value)

    try:
        return float(value)
    except:
        return value

def clean_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:
    print("\n DATA SEBELUM CLEANING")
    print(df)

    for col in df.columns:
        if df[col].dtype == object:
            df[col] = df[col].apply(convert_to_number)
    
    print("\n DATA SETELAH CLEANING")
    print(df)

    return df