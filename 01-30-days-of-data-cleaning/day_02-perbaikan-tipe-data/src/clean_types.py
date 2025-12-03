import pandas as pd

def convert_types(df):
    """
    Perbaiki tipe data:
    - order_date datetime
    - total_price numeric
    - age numeric
    """
    # Convert order_date ke datetime
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

    # Convert total_price ke numeric
    df['total_price'] = pd.to_numeric(df['total_price'], errors='coerce')

    # Convert age ke numeric
    df['age'] = pd.to_numeric(df['age'], errors='coerce')

    print("\n Tipe data setelah konversi:")
    print(df.dtypes)
    return df