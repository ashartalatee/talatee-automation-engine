import pandas as pd
from src.clean_dates import clean_date_column

FILE_PATH = "data/mini_dates.csv"

def main():
    # Ambil hanya kolom penting (hindari kolom ekstra)
    df = pd.read_csv(FILE_PATH, usecols=['order_id','customer','date'])

    print("\n DATA ASLI")
    print(df)

    df_clean = clean_date_column(df, "date")

    print("\n DATA SETELAH CLEAN TANGGAL")
    print(df_clean)

if __name__ == "__main__":
    main()
