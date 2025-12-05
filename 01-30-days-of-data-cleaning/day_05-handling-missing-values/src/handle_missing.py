import pandas as pd

def handle_missing(df: pd.DataFrame) -> pd.DataFrame:
    """
    Tangani missing values dengan:
    - Drop baris yang terlalu banyak kosong
    - Isi numeric dengan mean
    - Isi text dengan mode
    """

    print("\n SEBELUM:")
    print(df.isna().sum())

    # DROP BARIS YANG KEHILANGAN LEBIH DARI 2 DATA
    df = df.dropna(thresh=len(df.columns) - 2)

    # Fill numeric dengan MEAN
    for col in ['price', 'quantity']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            mean_value = df[col].mean()
            df[col] = df[col].fillna(mean_value)

    # Fill text dengan MODE
    for col in ['customer', 'email']:
        if col in df.columns:
            mode_value = df[col].mode()
            if not mode_value.empty:
                df[col] = df[col].fillna(mode_value[0])

    print("\n SESUDAH:")
    print(df.isna().sum())

    return df