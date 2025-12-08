import pandas as pd
from src.rules import valid_email, valid_age, valid_amount, valid_date


def validate_dataframe(df):
    valid_rows = []
    invalid_rows = []

    for index, row in df.iterrows():
        errors = []

        if not valid_email(row["email"]):
            errors.append("Invalid email")

        if not valid_age(row["age"]):
            errors.append("Invalid age")

        if not valid_amount(row["amount"]):
            errors.append("Invalid amount")

        if not valid_date(row["date"]):
            errors.append("Invalid date")

        if errors:
            row['errors'] = ", ".join(errors)
            invalid_rows.append(row)
        else:
            valid_rows.append(row)

    return pd.DataFrame(valid_rows), pd.DataFrame(invalid_rows)
