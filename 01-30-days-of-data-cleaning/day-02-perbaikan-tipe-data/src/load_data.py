import pandas as pd

def load_dataset(filepath: str):
    print(f" Membaca data dari: {filepath}")
    df = pd.read_csv(filepath)
    return df