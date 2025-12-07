import pandas as pd
from src.clean_after_merge import clean_after_merge

FILE_PATH = "data/merged_sample.csv"

def main():
    df = pd.read_csv(FILE_PATH)
    print("\n📂 DATA ASLI")
    print(df)

    df_clean = clean_after_merge(df)

    print("\n✅ DATA SETELAH CLEAN AFTER MERGE")
    print(df_clean)

    df_clean.to_csv("data/clean_merged.csv", index=False)
    print("\n💾 File tersimpan: clean_merged.csv")

if __name__ == "__main__":
    main()
