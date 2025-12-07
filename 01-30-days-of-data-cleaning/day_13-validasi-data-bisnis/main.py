import pandas as pd
from src.validate_business import validate_business

FILE_PATH = "data/mini_business.csv"

def main():
    df = pd.read_csv(FILE_PATH)
    print("\n DATA ASLI")
    print(df)

    df_clean = validate_business(df)

    print("\n DATA SETELAH VALIDASI BISNIS")
    print(df_clean)

if __name__ == "__main__":
    main()