import pandas as pd
from scipy import stats

def remove_outliers_zscore(df: pd.DataFrame, column: str, threshold: float = 3.0) -> pd.DataFrame:
    """
    Bersihkan outlier numeric berdasarkan Z-score
    """
    df_clean = df.copy()
    z_scores = stats.zscore(df_clean[column].astype(float))
    abs_z_scores = abs(z_scores)

    df_clean = df_clean[abs_z_scores < threshold]

    print(f"\n {column} - Z-score threshold: {threshold}")
    print(f"Jumlah baris setelah remove outliers: {len(df_clean)}")

    return df_clean