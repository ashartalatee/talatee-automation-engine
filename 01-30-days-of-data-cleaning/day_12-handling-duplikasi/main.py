import pandas as pd
from src.handle_duplicates import remove_duplicates

FILE_PATH = "data/mini_duplicates.csv"

def main():
    df = pd.read_csv(FILE_PATH)
    print("\n DATA ASLI")
    print(df)

    # Hapus duplicate berdasarkan semua kolom
    df_clean = remove_duplicates(df)

    print("\n DATA SETELAH REMOVE DUPLICATES")
    print(df_clean)

if __name__ == "__main__":
    main()