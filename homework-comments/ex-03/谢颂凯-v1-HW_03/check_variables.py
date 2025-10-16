import pandas as pd

# 读取dta文件
df = pd.read_stata(r"D:\big machine learning\Financial-Econometrics\HW_03\CSMAR\final_merged_data_v1.dta")

print(f"数据形状: {df.shape}")
print(f"\n变量列表 (共{len(df.columns)}个):")
print(df.columns.tolist())

print("\n查找包含特定关键词的变量:")
print("\n包含'A00'的变量 (资产负债表):")
asset_vars = [col for col in df.columns if 'A00' in str(col)]
print(asset_vars[:20])  # 显示前20个

print("\n包含'B00'的变量 (利润表):")
income_vars = [col for col in df.columns if 'B00' in str(col)]
print(income_vars[:20])

print("\n包含'Shr'或'shr'的变量 (股权):")
share_vars = [col for col in df.columns if 'shr' in str(col).lower()]
print(share_vars)

print("\n前3行数据:")
print(df.head(3))
