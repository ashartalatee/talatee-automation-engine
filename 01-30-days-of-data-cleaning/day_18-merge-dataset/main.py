import pandas as pd
from src.merge_data import merge_datasets

SALES_FILE = "data/sales.csv"
CUSTOMER_FILE = "data/customer.csv"

def main():
    sales_df = pd.read_csv(SALES_FILE)
    customer_df = pd.read_csv(CUSTOMER_FILE)

    print("\n DATA SALES")
    print(sales_df)

    print("\n DATA CUSTOMER")
    print(customer_df)

    df_merged = merge_datasets(sales_df, customer_df, how='left')

    df_merged.to_csv("data/merged_data.csv", index=False)
    print("\n File tersimpan: merged_data.csv")

if __name__ == "__main__":
    main()