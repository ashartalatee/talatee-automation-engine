from src.load_data import load_dataset
from src.clean_types import convert_types

DATA_PATH = "data/mini_dataset.csv"

if __name__ == "__main__":
    df = load_dataset(DATA_PATH)
    df = convert_types(df)

    print("\n 5 Baris Pertama setelah konversi tipe:")
    print(df.head())