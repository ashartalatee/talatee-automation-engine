import pandas as pd
from src.clean_text_basic import clean_text_basic

FILE_PATH = "data/mini_text.csv"

def main():
    df = pd.read_csv(FILE_PATH)

    print("\n🔍 DATA ASLI")
    print(df)

    df_clean = clean_text_basic(df)

    print("\n✅ DATA SETELAH CLEAN")
    print(df_clean)

if __name__ == "__main__":
    main()
