import pandas as pd

# 读取数据文件
data_file = r"D:\big machine learning\Financial-Econometrics\HW_03\processed_data_v2.xlsx"

try:
    df = pd.read_excel(data_file)
    print("数据维度:", df.shape)
    print("\n所有列名:")
    for col in df.columns:
        print(f"  - {col}")
    
    # 查找包含"行业"、"Industry"、"Ind"的列
    print("\n包含'行业'、'Industry'、'Ind'的列:")
    industry_cols = [col for col in df.columns if any(x in col for x in ['行业', 'Industry', 'Ind', 'ind', 'INDUSTRY'])]
    for col in industry_cols:
        print(f"  - {col}")
        print(f"    样本值: {df[col].dropna().head(3).tolist()}")
        
except Exception as e:
    print(f"错误: {e}")
