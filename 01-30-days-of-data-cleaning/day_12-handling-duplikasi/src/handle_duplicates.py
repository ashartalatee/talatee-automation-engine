import pandas as pd

def remove_duplicates(df: pd.DataFrame, subset=None) -> pd.DataFrame:
    """
    Hapus baris duplikat
    - subset: list kolom yang diperiksa duplikat (optional)
    """

    print("\n SEBELUM REMOVE DUPLICATES")
    print(df)

    # Deteksi duplikat
    dupe_rows = df.duplicated(subset=subset)
    print("\n Baris duplikat (True = duplikat)")
    print(dupe_rows)

    # Hapus duplikat
    df_clean = df.drop_duplicates(subset=subset, keep='first')

    print("\n SESUDAH REMOVE DUPLICATES")
    print(df_clean)

    return df_clean