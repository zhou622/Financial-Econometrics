import pandas as pd

# 检查基本信息年度表
basic_info_file = r"D:\big machine learning\Financial-Econometrics\HW_03\CSMAR\上市公司基本信息年度表\STK_LISTEDCOINFOANL.xlsx"

try:
    df = pd.read_excel(basic_info_file, nrows=10)
    print("基本信息年度表列名:")
    for i, col in enumerate(df.columns, 1):
        print(f"{i:3d}. {col}")
    
    # 查找行业相关列
    print("\n\n可能的行业列:")
    industry_cols = [col for col in df.columns if any(x in str(col).lower() for x in ['行业', 'industry', 'ind', 'sector', 'nnind'])]
    for col in industry_cols:
        print(f"  - {col}")
        print(f"    前3个值: {df[col].dropna().head(3).tolist()}")
        
except Exception as e:
    print(f"错误: {e}")
