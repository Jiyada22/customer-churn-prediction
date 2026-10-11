import pandas as pd

#ใช้ตัวแปร df เก็บข้อมูล Customer-Churn -> อ่านข้อมูลจากไฟล์ CSV
df = pd.read_csv("data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# แปลงค่าในคอลัมน์ TotalCharges เป็นประเภทตัวเลข
converted = pd.to_numeric(df["TotalCharges"],errors="coerce")
print (converted)

# ค้นหาแถวที่มีค่า TotalCharges ไม่ถูกต้อง
bad_rows = df[converted.isna()]

# แสดงจำนวนแถวที่มีค่า TotalCharges ไม่ถูกต้อง
print ("Number of bad rows:", len(bad_rows))

# แสดงข้อมูลของแถวที่มีปัญหา (bad_rows)
print(bad_rows[["customerID","tenure","MonthlyCharges","TotalCharges"]])

# ตรวจสอบค่าของข้อมูลตัวแรก ใน TotalCharges ของ bad_rows
print(repr(bad_rows["TotalCharges"].iloc[0]))
