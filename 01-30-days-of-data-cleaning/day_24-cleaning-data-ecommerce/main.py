import pandas as pd
from src.ecommerce_cleaner import clean_price, clean_category, clean_qty

FILE_PATH = "data/ecommerce_raw.csv"

def main():
    df = pd.read_csv(FILE_PATH)

    print("\n DATA ASLI")
    print(df)

    df["harga_bersih"] = df["harga"].apply(clean_price)
    df["kategori_bersih"] = df["kategori"].apply(clean_category)
    df["qty_bersih"] = df["qty"].apply(clean_qty)

    print("\n DATA SETELAH DIBERSIHKAN")
    print(df)

    df.to_csv("data/ecommerce_clean.csv", index=False)

    print("\n File disimpan: data/ecommerce_clean.csv")


if __name__ == "__main__":
    main()
