
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

## HW06-Bootstrap 方法练习

Mroz, T. A. (1987). The Sensitivity of an Empirical Model of Married Women’s Hours of Work to Economic and Statistical Assumptions. Econometrica, 55(4), 765. [Link](https://doi.org/10.2307/1911029), [-PDF-](https://gattonweb.uky.edu/Faculty/Ziliak/Mroz_1987.pdf), [-PDF2-](https://eml.berkeley.edu/~cle/e250a_f13/mroz-paper.pdf), [Google](<https://scholar.google.com/scholar?q=The Sensitivity of an Empirical Model of Married Women’s Hours of Work to Economic and Statistical Assumptions>), [-cited-](https://scholar.google.com/scholar?cites=14972433787391365635&as_sdt=2005&sciodt=0,5&hl=zh-CN)


![Mroz-1987-Table04](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/Mroz-1987-Table04.png)


我刚在 金融计量经济学 课程中教完学生 Bootstrap，讲授了 Bootstrap 的基本原理，如何使用Bootstrap 进行组间系数差异检验。

请帮我出几道习题供学生练习。

1. 使用 webuse morz.dta, clear  导入数据，设定模型 `lnwage` 对 `exper`, `expersq`, `educ`, `age` 的回归，让学生对比如下三种设定下的标准误有何差别：
- i.i.d 假设下的经典标准误
- Heteroskedasticity-robust 标准误，White (1980)
- Cluster-robust 标准误，以 `age` 为 cluster (建议使用 `reghdfe` 命令执行回归)
- 二维 Cluster-robust 标准误，以 `age` 和 `educ` 为 cluster (建议使用 `reghdfe` 命令执行回归)
- Bootstrap 标准误，使用 `vce(bootstrap, reps(1000) seed(12345))`
- Jackknife 标准误，使用 `vce(jackknife)`

1. 设定模型 `lnwage` 对 `exper`, `expersq`, `educ`, `age` 的回归，让学生使用 Bootstrap 方法进行组间系数差异检验。可以使用 `ssc install bdiff, replace` 安装 `bdiff` 命令。然后检验 `educ` 变量在 `inlf==0` 和 `inlf==1` 两组样本中的系数差异是否显著。

2. 设定模型 `lnwage` 对 `exper`, `expersq`, `educ`, `age` 的回归，让学生使用 Bootstrap 方法 (reps=1000) 构建 R2 的 95% 置信区间，并绘制 R2 的 Bootstrap 分布直方图。给出解释。


## HW07-Hansen (1999) 面板门槛模型

Hansen, B. E. (1999). Threshold effects in non-dynamic panels: Estimation, testing, and inference. Journal of Econometrics, 93(2), 345–368. [Link](https://doi.org/10.1016/S0304-4076(99)00025-1), [PDF](http://sci-hub.ren/10.1016/S0304-4076(99)00025-1), [-PDF2-](https://users.ssc.wisc.edu/~bhansen/papers/joe_99.pdf), [Google](<https://scholar.google.com/scholar?q=Threshold effects in non-dynamic panels: Estimation, testing, and inference>). [-cited-](https://scholar.google.com/scholar?cites=2645204791588266977&as_sdt=2005&sciodt=0,5&hl=zh-CN), [Slides-wild bootstrap](https://www.stata.com/meeting/china19_Shanghai/slides/china19_Wang2.pdf)

- Data: <https://github.com/lianxhcn/data/raw/refs/heads/main/hansen1999.dta>

```stata
use "https://github.com/lianxhcn/data/raw/refs/heads/main/hansen1999.dta", clear
des
```


## HW08-经济金融领域顶刊论文复现

1. 顶刊论文复现代码和数据链接整理

请按照如下列表整理经济和金融领域顶级期刊是否提供了论文的代码和数据链接。将结果以缩进列表 (list) 的形式写在下面：

- American Economic Review (AER)
  - website: <https://www.aeaweb.org/journals/aer>
  - 是否提供数据和代码链接：是
  - e.g., 
 

1. 请浏览经济和金融领域顶级期刊（如 AER, JPE, QJE, Econometrica, JF, RFS, JFE 等）最近两年内 (2024-2025 年) 发表的论文，选择一篇包含实证分析的文章进行复现。



我是教授「金融计量」课程的老师，经过两周的学习，学生已经掌握了一些基本实证分析方法和技巧。我想布置一个作业，让学生自行检索后了解如下信息：

1. 经济学和金融学的 Top Journals 有哪些？5+4
2. 这些期刊是否提供论文的代码和数据链接？如果提供，链接在哪里？请学生整理成一个列表。
3. 选择一篇包含实证分析的文章，下载作者提供的复现资料到本地，尝试运行代码，并撰写一份简要的复现报告，包括：
   - 原文的引文信息 （作者、标题、期刊、年份等），建议采用如下格式：
     - `Authors, Title, Journal, Year, Volume (Issue): Pages. [-Link-](), [-PDF-](), [-Google Scholar-]().`
     - e.g., 

- 参考资料：
  - 连享会, 2020, [连享会：论文重现复现网站大全](https://www.lianxh.cn/details/232.html).
  - 汇总了各个期刊的复现资料要求和数据存储平台：[EJD: Find Economic Articles with Data](https://ejd.econ.mathematik.uni-ulm.de/)

参见 连享会, 2020, [连享会：论文重现复现网站大全](https://www.lianxh.cn/details/232.html).

-   Mendeley 平台: [Discover Mendeley Data](https://data.mendeley.com/)
-   密歇根大学的 ICPSR: [ICPSR Data](https://www.icpsr.umich.edu/icpsrweb/)
-   哈佛大学的 IQSS: [Harvard Dataverse](https://dataverse.harvard.edu/)
-   Sebastian Kranz（Ulm University）: [Find Economic Articles with Data](https://ejd.econ.mathematik.uni-ulm.de/)
    -   包含 8000 多篇经济金融论文，可检索软件类型、期刊名称等。