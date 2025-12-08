import pandas as pd
from src.group_aggregate import group_and_aggregate

FILE_PATH = "DATA/sales_data.csv"

def main():
    df = pd.read_csv(FILE_PATH)
    print("\n DATA ASLI")
    print(df)

    df_grouped = group_and_aggregate(df)

    print("\n DATA SETELAH GROUPING & AGGREGATION")
    print(df_grouped)

    df_grouped.to_csv("data/sales_grouped.csv", index=False)
    print("\n File tersimpan: sales_grouped.csv")

if __name__ == "__main__":
    main()