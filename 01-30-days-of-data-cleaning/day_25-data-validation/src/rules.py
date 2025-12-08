import re
from datetime import datetime

def valid_email(email):
    if not isinstance(email, str):
        return False
    pattern = r"[^@]+@[^@]+\.[^@]+"
    return re.match(pattern, email)

def valid_age(age):
    try:
        age = int(age)
        return 18 <= age <= 100
    except:
        return False

def valid_amount(amount):
    try:
        amount = float(amount)
        return amount > 0
    except:
        return False

def valid_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except:
        return False
