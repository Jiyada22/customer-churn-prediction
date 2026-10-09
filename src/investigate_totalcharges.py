import pandas as pd

#ใช้ตัวแปร df เก็บข้อมูล Customer-Churn
df = pd.read_csv("data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# 
converted = pd.to_numeric(df["TotalCharges"],errors="coerce")
print (converted)

#
bad_rows = df[converted.isna()]

print ("Number of bad rows:", len(bad_rows))
print(bad_rows[["customerID","tenure","MonthlyCharges","TotalCharges"]])
print(repr(bad_rows["TotalCharges"].iloc[0]))
