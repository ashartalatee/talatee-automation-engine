import pandas as pd

def detect_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Deteksi nilai kosong (missing values) dan persentasenya
    """

    print("\n INFO DATA")
    print(df.info())

    print("\n JUMLAH MISSING PER KOLOM")
    print(df.isna().sum())

    missing_percent = (df.isna().sum() / len(df)) * 100

    print("\n PERSENTASE MISSING (%)")
    print(missing_percent)

    return missing_percent