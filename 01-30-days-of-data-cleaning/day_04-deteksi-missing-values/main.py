import pandas as pd
from src.detect_missing import detect_missing_values

FILE_PATH = "data/mini_missing_values.csv"

def main():
    df = pd.read_csv(FILE_PATH)

    print("\n DATASET ASLI")
    print(df)

    detect_missing_values(df)

if __name__ == "__main__":
    main()