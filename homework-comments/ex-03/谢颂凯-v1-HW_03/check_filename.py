import os

path = r"D:\big machine learning\Financial-Econometrics\HW_03\CSMAR\CSMAR常用变量-2000-2024"
files = os.listdir(path)

for f in files:
    if "常用变量" in f and f.endswith(".dta"):
        print(f"文件名: {f}")
        print(f"文件名的字节表示: {f.encode('utf-8')}")
        print(f"正确的路径应该是:")
        print(f'use "D:\\big machine learning\\Financial-Econometrics\\HW_03\\CSMAR\\CSMAR常用变量-2000-2024\\{f}", clear')
