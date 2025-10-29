
## HW04-循环语句

对话标题：金融计量作业-HW05-循环语句练习

我刚教完学生 Stata 的程序基础，包括：local, global，循环语句和条件语句等。我想出一个作业，让学生使用循环语句等技巧，自行编写代码，验证 OLS 估计的无偏性。

大体思路：
1. 生成 P0 (population)：N=10000， $y = 10 + 0.5x + e$，e 和 x 都服从标准正态分布，二者不相关
2. 写一个循环：reps = 500 次，每次从 P0 中随机抽取 N = 120 个观察值，执行 reg y x 回归，记录 b_j = _b[x], 
- 列表统计 {b_j} 的均值，标准差，min, 5%, 25%, 50%, 75%, 95%, max 
- 图示无偏性
- 从理论上分析上述结果。Hint: 从 OLS 系数无偏性角度分析
3. 按照 step2 的方式得到 $\hat{beta}_j (j=1,2, \cdot, reps)$，但需要分别设定 N=100，500， 1000，对比：
- 三种情况下的 sd($\hat{beta}_j)
- 图示三种情况下的 $\hat{beta}_j 的密度函数图，用红色竖直虚线标注 $\beta_0=0.5$ 的位置
- 从理论上分析上述结果。
4. ……

你帮我编写一个逻辑清晰，表述简洁明了的习题吧

## HW05-OLS结果的输出和呈现

使用 `sysuse "nlsw88.dta", clear` 导入数据

1. 结果的表格呈现。自行编写代码，在 Stata 结果窗口中 (你的 .ipynb 文件的输出部分) 呈现以下结果 (黄色方框不属于自动输出任务，它只是提醒大家需要重点输出的内容)：
   - 注意：请勿进行手动复制粘贴，而是通过 Stata 代码实现自动化输出。 

![](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/aHR0cHM6Ly91cGxvYWQtaW1hZ2VzLmppYW5zaHUuaW8vdXBsb2FkX2ltYWdlcy83NjkyNzE0LTJlMTQyZGFhMDZmYzczYzYucG5n)

2. 将如下两个 OLS 回归 (M1 和 M2) 的系数估计值及置信区间采用图形方式呈现出来 (类似于下图中的点线图)，并做简要对比说明：
   - M1：`reg lnwage age grade married south exper tenure if race==1`
   - M2：`reg lnwage age grade married south exper tenure if race==2`
   - note: `lnwage` 变量需要你自行生成，如 `gen lnwage = ln(wage)`