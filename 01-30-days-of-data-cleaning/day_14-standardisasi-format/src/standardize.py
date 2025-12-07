import pandas as pd

def standardize_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # ORDER ID: JADIKAN 5 DIGIT
    df['order_id'] = df['order_id'].astype(str).str.strip().str.zfill(5)

    # CUSTOMER: rapikan nama
    df['customer'] = (
        df['customer']
        .astype(str)
        .str.strip()
    )

    # PRICE: pastikan integer bersih
    df['price'] = (
        df['price']
        .astype(str)
        .str.replace(" ", "")
        .astype(int)
    )

    print("\n DATA SETELAH STANDARDISASI")
    print(df)

    return df