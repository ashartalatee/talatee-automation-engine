import pandas as pd
from src.clean_text_regex import clean_text_regex

FILE_PATH = "data/mini_text_dirty.csv"

def main():
    df = pd.read_csv(FILE_PATH)

    print("\n DATA ASLI")
    print(df)

    df_clean = clean_text_regex(df)

    print("\n DATA SETELAH REGEX CLEAN")
    print(df_clean)

if __name__ == "__main__":
    main()