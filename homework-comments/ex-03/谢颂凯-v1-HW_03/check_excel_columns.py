import pandas as pd

# 查看资产负债表文件的列名
print("=== 资产负债表 2011-2024 ===")
df1 = pd.read_excel(r"D:\big machine learning\Financial-Econometrics\HW_03\CSMAR\资产负债表-2011-2024\跨表查询_沪深京股票(年频).xlsx", nrows=0)
print("列名:")
for col in df1.columns:
    print(f"  {col}")

print("\n=== 利润表现金流量表 2011-2024 ===")
df2 = pd.read_excel(r"D:\big machine learning\Financial-Econometrics\HW_03\CSMAR\利润表-现金流量表-2011-2024\跨表查询_沪深京股票(年频).xlsx", nrows=0)
print("列名:")
for col in df2.columns:
    print(f"  {col}")

print("\n=== CSMAR常用变量 ===")
df3 = pd.read_excel(r"D:\big machine learning\Financial-Econometrics\HW_03\CSMAR\CSMAR常用变量-2000-2024\常用变量查询（年度）.xlsx", nrows=0)
print("列名:")
for col in df3.columns:
    print(f"  {col}")
