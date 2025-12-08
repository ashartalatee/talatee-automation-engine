import re
import pandas as pd


def clean_price(value):
    if pd.isna(value):
        return 0

    value = str(value).lower().strip()

    if "k" in value:
        number = re.findall(r"\d+", value)[0]
        return float(number) * 1000

    cleaned = re.sub(r"[^\d]", "", value)

    if cleaned == "":
        return 0

    return float(cleaned)


def clean_category(value):
    value = str(value).strip().lower()

    mapping = {
        "elektronik": "Elektronik",
        "electronic": "Elektronik",
        "minuman": "Minuman",
        "drink": "Minuman"
    }

    return mapping.get(value, value.title())


def clean_qty(value):
    if pd.isna(value):
        return 0

    value = int(value)

    if value < 0:
        return 0

    return value
