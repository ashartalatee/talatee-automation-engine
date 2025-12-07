import pandas as pd

def clean_after_merge(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Hapus duplikasi total
    df_no_dupe = df.drop_duplicates()
    print("\n Setelah hapus duplikasi total")
    print(df_no_dupe)

    # Rename / hapus kolom double jika ada
    cols = df_no_dupe.columns
    for col in cols:
        if col.endswith('_x') or col.endswith('_y'):
            new_col = col[:-2]
            if new_col not in cols:
                df_no_dupe.rename(col={col: new_col}, inplace=True)
            else:
                df_no_dupe.drop(columns=[col], inplace=True)

    
    print("\n Setelah fix kolom double")
    print(df_no_dupe)

    return df_no_dupe