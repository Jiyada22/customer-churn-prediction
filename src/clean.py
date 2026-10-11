import pandas as pd
from pathlib import Path

RAW_PATH = "data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv"
OUTPUT_PATH = "data/processed/clean_data.csv"

# โหลดข้อมูลจากไฟล์ CSV
df = pd.read_csv(RAW_PATH)

# แปลง TotalCharges เป็นตัวเลข
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"],errors="coerce")

# เติม 0 ใน TotalCharges (ลูกค้าใหม่ที่ยังไม่มีค่า TotalCharges)
is_missing_new_customer = df["TotalCharges"].isna() & (df["tenure"] == 0)
print("Rows to fill with 0: ", is_missing_new_customer.sum())
df.loc[is_missing_new_customer, "TotalCharges"] = 0

# เช็คว่าค่าที่หายถูกเติมแล้วหรือยัง
assert df["TotalCharges"].isna().sum() == 0, "Unexpected missing TotalCharges found!"

print("TotalChages type is now:",df["TotalCharges"].dtype)


