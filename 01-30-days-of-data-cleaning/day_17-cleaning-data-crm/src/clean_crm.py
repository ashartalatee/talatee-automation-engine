import pandas as pd
import re

# Berishkan nama
def clean_name(name):
    if pd.isna(name):
        return None
    
    return str(name).strip().title()

# Bersihkan email
def clean_email(email):
    if pd.isna(email):
        return None
    
    if "@" not in email or "." not in email:
        return None
    
    return email.strip().lower()

# Bersihkan phone
def clean_phone(phone):
    if pd.isna(phone):
        return None
    
    phone = re.sub(r"\D", "", str(phone))
    return phone if len(phone) >= 10 else None

# Standarisasi status
def clean_status(status):
    if pd.isna(status):
        return "unknown"
    
    status = status.strip().lower()

    if "lead" in status:
        return "Lead"
    if "prospect" in status:
        return "prospect"
    if "deal" in status or "close" in status:
        return "Deal"
    if "lost" in status:
        return "Lost"
    
    return "Other"