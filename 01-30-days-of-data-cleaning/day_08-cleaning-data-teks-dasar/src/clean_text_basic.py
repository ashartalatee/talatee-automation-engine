import pandas as pd

def clean_text_basic(df: pd.DataFrame) -> pd.DataFrame:
    """
    Bersihkan data teks:
    - lowercase
    - strip spasi
    - replace karakter khusus (contoh: ganti multiple spasi)
    """

    print("\n📌 SEBELUM CLEAN")
    print(df.head())

    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.strip()       # hapus spasi depan-belakang
        df[col] = df[col].str.lower()       # lowercase
        df[col] = df[col].str.replace(r"\s+", " ", regex=True)  # ganti multiple spasi dengan 1

    print("\n✅ SESUDAH CLEAN")
    print(df.head())

    return df
