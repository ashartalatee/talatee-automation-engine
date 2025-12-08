from src.monthly_cleaner import load_all_files, clean_monthly_data

DATA_FOLDER = "data/daily/"

def main():
    df = load_all_files(DATA_FOLDER)

    print("\n DATA DIGABUNG")
    print(df)

    cleaned_df = clean_monthly_data(df)

    print("\n DATA SETELAH CLEANING BULANAN")
    print(cleaned_df)

    cleaned_df.to_csv("data/monthly_cleaned.csv", index=False)

    print("\n File disimpan: data/monthly_cleaned.csv")

if __name__ == "__main__":
    main()
