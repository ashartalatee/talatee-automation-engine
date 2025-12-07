import pandas as pd
from src.clean_crm import clean_name, clean_email, clean_phone, clean_status

FILE_PATH = "data/raw_crm_data.csv"

def main():
    df = pd.read_csv(FILE_PATH)

    print("\n DATA ASLI")
    print(df)

    df["name_clean"] = df["name"].apply(clean_name)
    df["email_clean"] = df["email"].apply(clean_email)
    df["phone_clean"] = df["phone"].apply(clean_phone)
    df["status_clean"] = df["status"].apply(clean_status)

    print("\n DATA SETELAH CLEANING")
    print(df)

    df.to_csv("data/raw_crm_data.csv", index=False)
    print("\n File tersimpan sebagai: clean_crm_data.csv")

if __name__ == "__main__":
    main()