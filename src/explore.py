#Data Profiling

import pandas as pd
# แสดงทุกคอลัมน์
pd.set_option('display.max_columns', None) 

df = pd.read_csv("data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("========================= Data Overview - ตรวจสอบภาพรวมข้อมูล =========================")
print("Total Records (จำนวนแถวทั้งหมด) : ",len(df))

# ดูจำนวนแถวและคอลัมน์
print("Shape (แถว , คอลัมน์ ) : ", df.shape) 

# ดูชนิดข้อมูลของแต่ละคอลัมน์
print(df.dtypes.to_string() + "\n") 

# ดูตัวอย่าง 5 แถวแรก
print(df.head()) 

#ดูข้อมูลแต่ละคอลัมน์เก็บอะไรบ้าง ที่ไม่ซ้ำกัน
for col in df.columns:
    print(f"\n{col} :")
    print(df[col].unique())

print("-"*50 +"\n")

print("========================= Missing Values - ตรวจสอบค่าว่าง =========================")
# ตรวจสอบ Missing Values
print("Null Records per column :\n",df.isnull().sum()) 
print("Total Missing Values :", df.isnull().sum().sum())

print("\nBlank Values per column :")
blank_counts = df.select_dtypes(include=["object"]).apply(lambda col: col.str.strip().eq("").sum())
print(blank_counts)
print("\nTotal Blank Values :", blank_counts.sum())
print("-"*50 +"\n")

print("========================= Duplicate Records - ตรวจสอบข้อมูลซ้ำ ========================="  )
# ตรวจสอบ Duplicate Records
print("Duplicate Records :", df.duplicated().sum()) 

# ตรวจสอบ Duplicate customerID (Primary Key)
print("Duplicate customerID :", df["customerID"].duplicated().sum()) 
print("-"*50 +"\n")

#print(df["Churn"].value_counts()) # ดูสัดส่วนลูกค้าที่ Churn (ที่เลิกใช้งาน)