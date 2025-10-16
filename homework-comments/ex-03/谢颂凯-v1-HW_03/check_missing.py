import pandas as pd
import numpy as np

base = r'd:\big machine learning\Financial-Econometrics\HW_03\CSMAR'

# 读取资产负债表
print("正在读取数据...")
bs1 = pd.read_excel(base + r'\资产负债表-2000-2010\跨表查询_沪深京股票(年频).xlsx')
bs2 = pd.read_excel(base + r'\资产负债表-2011-2024\跨表查询_沪深京股票(年频).xlsx')
bs = pd.concat([bs1, bs2])

print(f'\n资产负债表总行数: {len(bs)}')
print(f'资产负债表总列数: {len(bs.columns)}')

# 检查关键财务字段
fields = {
    '总资产': 'FS_Combas-A001000000',
    '总负债': 'FS_Combas-A002000000',
    '流动负债': 'FS_Combas-A002100000',
    '非流动负债': 'FS_Combas-A002200000',
    '货币资金': 'FS_Combas-A001101000',
    '短期借款': 'FS_Combas-A002101000',
    '长期借款': 'FS_Combas-A002201000',
    '所有者权益': 'FS_Combas-A003000000'
}

print('\n=== 原始数据字段缺失统计 ===')
for name, col in fields.items():
    if col in bs.columns:
        missing = bs[col].isna().sum()
        missing_pct = missing/len(bs)*100
        # 检查非数值类型
        non_numeric = pd.to_numeric(bs[col], errors='coerce').isna().sum()
        non_numeric_pct = non_numeric/len(bs)*100
        print(f'{name} ({col}):')
        print(f'  - 原始缺失: {missing} ({missing_pct:.2f}%)')
        print(f'  - 非数值/转换后缺失: {non_numeric} ({non_numeric_pct:.2f}%)')
    else:
        print(f'{name} ({col}): ✗ 字段不存在')

# 检查数据类型和特殊值
print('\n=== 数据类型检查 ===')
for name, col in list(fields.items())[:3]:
    if col in bs.columns:
        print(f'\n{name} ({col}):')
        print(f'  数据类型: {bs[col].dtype}')
        print(f'  唯一值数量: {bs[col].nunique()}')
        # 显示非数值的样本
        try:
            numeric_series = pd.to_numeric(bs[col], errors='coerce')
            non_numeric_mask = numeric_series.isna() & bs[col].notna()
            if non_numeric_mask.sum() > 0:
                print(f'  非数值样本 (前5个): {bs[col][non_numeric_mask].unique()[:5]}')
        except:
            pass

print('\n=== 分析完成 ===')
