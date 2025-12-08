import os
import pandas as pd
from src.validator import validate_dataframe

# ✅ BASE PATH (lokasi file ini)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ✅ AUTO CREATE OUTPUT FOLDER
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load raw data
data_path = os.path.join(BASE_DIR, "data", "raw", "sales_raw.csv")
df = pd.read_csv(data_path)

# Validate
valid_df, invalid_df = validate_dataframe(df)

# Save results
valid_df.to_csv(os.path.join(OUTPUT_DIR, "valid_data.csv"), index=False)
invalid_df.to_csv(os.path.join(OUTPUT_DIR, "invalid_data.csv"), index=False)

print("✅ Validation done")
print(f"✅ Valid rows   : {len(valid_df)}")
print(f"✅ Invalid rows : {len(invalid_df)}")
