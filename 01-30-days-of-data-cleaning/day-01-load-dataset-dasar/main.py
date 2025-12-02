from src.load_data import load_dataset
from src.inspect import inspect_data

DATA_PATH = "data/mini_dataset.csv"

if __name__ == "__main__":
    data = load_dataset(DATA_PATH)
    inspect_data(data)