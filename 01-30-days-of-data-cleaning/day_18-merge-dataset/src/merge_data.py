import pandas as pd

def merge_datasets(sales_df: pd.DataFrame, custumer_df: pd.DataFrame, how='left') -> pd.DataFrame:
    """
    Merge sales & custumer dataset
    how = left, right, inner, outer
    """

    print(f"\n MERGE TYPE: {how.upper()}")

    df_merged = pd.merge(sales_df, custumer_df, on="customer_id", how=how)

    print("\n HASIL MERGE")
    print(df_merged)

    return df_merged