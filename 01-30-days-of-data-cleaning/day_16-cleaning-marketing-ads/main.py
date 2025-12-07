import pandas as pd
from src.clean_ads import clean_ctr, clean_spend

FILE_PATH = "data/raw_ads_data.csv"

def main():
    df = pd.read_csv(FILE_PATH)

    print("\n DATA ASLI")
    print(df)

    df["ctr_clean"] = df["ctr"].apply(clean_ctr)
    df["spend_clean"] = df["spend"].apply(clean_spend)

    print("\n DATA SETELAH CLEANING")
    print(df)

    df.to_csv("data/raw_ads_data.csv", index=False)
    print("\n File tersimpan sebagai: clean_ads_data.csv")

if __name__ == "__main__":
    main()