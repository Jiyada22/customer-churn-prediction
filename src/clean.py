import pandas as pd
from pathlib import Path

RAW_PATH = "data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv"
OUTPUT_PATH = "data/processed/clean_data.csv"

# โหลดข้อมูลจากไฟล์ CSV
df = pd.read_csv(RAW_PATH)

# แปลง TotalCharges เป็นตัวเลข
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"].astype(str).str.strip(), errors="coerce")

# ตรวจสอบคจำนวนค่าว่าง
print("Missing TotalCharges : ", df["TotalCharges"].isna().sum())

#ตรวจสอบแถวที่มีค่าว่าง
missing_rows = df[df["TotalCharges"].isna()]

print("\nRows with missing TotalCharges : ")
print(missing_rows[["customerID","tenure","MonthlyCharges","TotalCharges"]])

# เติม 0 ให้ลูกค้าใหม่ที่ยังไม่มีค่า TotalCharges
is_missing_new_customer = (df["TotalCharges"].isna() & (df["tenure"] == 0))

df.loc[is_missing_new_customer,"TotalCharges"] = 0

# ตรวจสอบผลลัพธ์หลังจากเติมค่า
print("\nRows filled with 0 : ",is_missing_new_customer.sum())
print("Remaining Missing values : ", df["TotalCharges"].isna().sum())
print("TotalCharges data type : ", df["TotalCharges"].dtype)

# ตรวจสอบว่าค่าว่างทั้งหมดถูกเติมแล้วหรือไม่
assert df["TotalCharges"].isna().sum() == 0, "Unexpected missing values in TotalCharges found!"
print("TotalCharges validation passed.")

#-------------------------------------------------------
# แปลงค่าของคอลัมน์ Churn เป็นตัวเลข (Yes=1, No=0)
df["Churn"] = df["Churn"].map({"Yes":1, "No":0})

# ตรวจสอบค่าที่แปลงแล้ว
print("\nChurn values:")
print(df["Churn"].value_counts(dropna=False))
print("\nChurn dtype : ", df["Churn"].dtype)

# ตรวจสอบว่ามีค่าที่แปลงไม่ได้หรือไม่
assert df["Churn"].notna().all(), "Unexpected Churn values found!"