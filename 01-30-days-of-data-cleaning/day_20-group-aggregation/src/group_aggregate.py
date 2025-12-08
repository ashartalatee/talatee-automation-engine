import pandas as pd

def group_and_aggregate(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Group by customer & date
    grouped = df.groupby(['customer', 'date'], as_index=False).agg({
        'amount': 'sum',
        'product': 'count' # Jumlah transaksi
    })
    
    grouped.rename(columns={'product': 'transaction'}, inplace=True)

    print("\n HASIL GROUP & AGGREGATE")
    print(grouped)

    return grouped