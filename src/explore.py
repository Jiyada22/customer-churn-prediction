import pandas as pd

df = pd.read_csv("data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("Shape:", df.shape) # ดูจำนวนแถวและคอลัมน์
print(df.head()) # ดูตัวอย่าง 5 แถวแรก
print(df.dtypes) # ดูชนิดข้อมูลของแต่ละคอลัมน์
print(df["Churn"].value_counts()) # ดูสัดส่วนลูกค้าที่ Churn