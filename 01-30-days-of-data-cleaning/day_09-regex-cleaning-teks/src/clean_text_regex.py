import pandas as pd
import re

def remove_email(text):
    if pd.isna(text):
        return text
    return re.sub(r'\S+@\S+\./S+', '[EMAIL_REMOVED]', text)

def remove_phone(text):
    if pd.isna(text):
        return text
    return re.sub(r'\b(\+62|62|0)8[0-9]{7,11}\b', '[PHONE_REMOVED]', text)

def remove_special_chars(text):
    if pd.isna(text):
        return text
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)

def clean_text_regex(df: pd.DataFrame) -> pd.DataFrame:
    print("\n SEBELUM CLEANING REGEX")
    print(df.head())

    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].apply(remove_email)
        df[col] = df[col].apply(remove_phone)
        df[col] = df[col].apply(remove_special_chars)
        df[col] = df[col].str.strip().str.lower()

    print("\n SESUDAH CLEANING REGEX")
    print(df.head())

    return df