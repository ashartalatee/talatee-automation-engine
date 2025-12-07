import pandas as pd

def validate_business(df: pd.DataFrame) -> pd.DataFrame:
    """
    Validasi logika bisnis:
    - Quantity > 0
    - Price > 0
    - Flag data bermasalah
    """

    df = df.copy()

    df['flag_qty'] = df['quantity'] <= 0
    df['flag_price'] = df['price'] <= 0
    df['flag_any'] = df['flag_qty'] | df['flag_price']

    print("\n VALIDASI DATA BISNIS")
    print(df)

    # Opsi: hapus data yang bermasalah
    df_clean = df[~df['flag_any']].drop(columns=['flag_qty','flag_price','flag_any'])

    print("\n DATA SETELAH VALIDASI & HAPUS DATA INVALID")
    print(df_clean)

    return df_clean