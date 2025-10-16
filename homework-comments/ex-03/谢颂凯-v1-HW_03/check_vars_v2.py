import pandas as pd
import sys

try:
    # 尝试读取dta文件
    print("正在读取数据文件...")
    df = pd.read_stata(r"D:\big machine learning\Financial-Econometrics\HW_03\CSMAR\final_merged_data_v1.dta", 
                       iterator=True)
    
    # 只读取变量名,不读取全部数据
    varlist = df.variable_labels()
    varnames = df.varlist
    
    print(f"\n共有 {len(varnames)} 个变量\n")
    
    # 筛选关键变量
    print("资产负债表相关变量(A开头):")
    for var in varnames:
        if var.startswith('A0'):
            print(f"  {var}")
            if len([v for v in varnames if v.startswith('A0') and varnames.index(v) <= varnames.index(var)]) >= 30:
                print("  ... (更多变量)")
                break
    
    print("\n利润表相关变量(B开头):")
    for var in varnames:
        if var.startswith('B0'):
            print(f"  {var}")
            if len([v for v in varnames if v.startswith('B0') and varnames.index(v) <= varnames.index(var)]) >= 20:
                print("  ... (更多变量)")
                break
    
    print("\n股权相关变量:")
    for var in varnames:
        if 'shr' in var.lower() or 'Shr' in var:
            print(f"  {var}")
    
    print("\n其他关键变量:")
    keywords = ['stock_code', 'year', 'LISTINGDATE', 'Symbol']
    for var in varnames:
        if var in keywords or any(k in var for k in keywords):
            print(f"  {var}")
    
except Exception as e:
    print(f"错误: {e}")
    print("\n尝试使用chunksize读取...")
    try:
        df_chunk = pd.read_stata(r"D:\big machine learning\Financial-Econometrics\HW_03\CSMAR\final_merged_data_v1.dta",
                                 chunksize=1)
        for chunk in df_chunk:
            print(f"\n变量列表:")
            for i, col in enumerate(chunk.columns):
                print(col, end=', ')
                if (i+1) % 10 == 0:
                    print()
            break
    except Exception as e2:
        print(f"第二次尝试也失败: {e2}")
