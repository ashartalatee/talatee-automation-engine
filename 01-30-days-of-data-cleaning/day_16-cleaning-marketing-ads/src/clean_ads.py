import pandas as pd
import re

def clean_ctr(value):
    if pd.isna(value):
        return None
    
    value = str(value).replace("%", "").replace(",", ".")
    return float(value)

def clean_spend(value):
    if pd.isna(value):
        return None

    value = str(value).lower().strip()

    # hapus rp dan spasi
    value = value.replace("rp", "").replace(" ", "")

    # jika pakai k (30k)
    if "k" in value:
        value = value.replace("k", "")
        return float(value) * 1000

    # Hapus titik ribuan (50.000 -> 50000)
    value = value.replace(".", "")

    # Hapus koma sisa
    value = value.replace(",", "")

    return float(value)
