# FE 课程报告备选主题

>Note (`2025/12/23 9:16`)：    
大家好，我会陆续发布一些选题，供大家参考和选择。目前已经发布的选题如下，大家可以先浏览一下，看看对哪一个选题感兴趣。我将于 12.26 日组织大家确认选题。

- 有些文献的 PDF 链接对应的是 working paper 版本，大家可以根据需要自行寻找最终发表版本。
  - 【PDF】文件夹：存放了部分选题的 PDF 文档
- 部分论文的复现资料：[点击查看](https://www.jianguoyun.com/p/DYgReTcQtKiFCBip6p4GIAA)
- 参考：[Top论文复现及中文精要](https://www.jianguoyun.com/p/DVlZ9DYQtKiFCBil9O4EIAA)
  - 这是一些已经完成的复现报告，大家的课程报告基本上按此风格撰写即可。

[toc]

---

# T1. Wang-2024-EE

- Wang, Z., Zhang, T., Ren, X., & Shi, Y. (**2024**). AI adoption rate and corporate green innovation efficiency: Evidence from Chinese energy companies. **Energy Economics**, 132, 107499. [Link](https://doi.org/10.1016/j.eneco.2024.107499), [PDF](https://file-lianxh.oss-cn-shenzhen.aliyuncs.com/Refs/2026-Spring/Wang_2024_AI_adoption_rate_and_corporate_green_innovation.pdf), [Google](<https://scholar.google.com/scholar?q=AI adoption rate and corporate green innovation efficiency: Evidence from Chinese energy companies>), [cited](https://scholar.google.com/scholar?cites=3084301341760475150&as_sdt=2005&sciodt=0,5&hl=zh-CN), [Replication](https://ars.els-cdn.com/content/image/1-s2.0-S014098832400207X-mmc1.zip)。
  - 该文只有一个 `.do` 文档和一个 `.dta` 文档，可以一键执行到底。

# T2. Cepni-2024-EE
- Cepni, O., Şensoy, A., & Yılmaz, M. H. (**2024**). Climate change exposure and cost of equity. **Energy Economics**, 130, 107288. [Link](https://doi.org/10.1016/j.eneco.2023.107288), [PDF](https://file-lianxh.oss-cn-shenzhen.aliyuncs.com/Refs/2026-Spring/Cepni_2024_Climate_change_exposure_and_cost_of_equity.pdf), [Google](<https://scholar.google.com/scholar?q=Climate change exposure and cost of equity>). [Replication](https://ars.els-cdn.com/content/image/1-s2.0-S0140988323007867-mmc1.zip)。
  - 该文的复现文档包含多个文件夹，分类放置了 .do 文件，数据文件和输出结果。数据处理过程涉及多个数据文件的合并。


# T3. Bao-2025-MS

- Bao, L., Huang, D., & Lin, C. (**2025**). Can Artificial Intelligence Improve Gender Equality Evidence from a Natural Experiment. **Management Science**. [Link](https://doi.org/10.1287/mnsc.2022.02787), [PDF](https://file-lianxh.oss-cn-shenzhen.aliyuncs.com/Refs/2026-Spring/Bao-2024-MS.pdf), [PDF-wp](https://file-lianxh.oss-cn-shenzhen.aliyuncs.com/Refs/2026-Spring/Bao-2024-MS-wp.pdf), [Appendix](https://pubsonline.informs.org/doi/suppl/10.1287/mnsc.2022.02787/suppl_file/mnsc.2022.02787.sm1.pdf), [Google](<https://scholar.google.com/scholar?q=Can Artificial Intelligence Improve Gender Equality Evidence from a Natural Experiment>), [Replication](https://services.informs.org/dataset/download.php?doi=mnsc.2022.02787).
  - **简介**：该文研究的问题是：当教师队伍的性别结构与观念短期难改时，能否借助被设计为“性别中性”的 AI 教学，改善学习效果并缩小既有性别差距？作者利用一次疫情隔离触发的自然实验：2021年1月当地疫情反弹导致16/36名教师被隔离，机构以 AI 复盘替代部分人类教师，形成处理组与对照组，并追回冲击前后两个学期的训练数据(2月春节无训练)。结果显示，AI 训练显著提高胜率与落子质量，并减少错误、重大错误及错误幅度；同时，女生的进步更快，干预后约 5 个月性别差距明显收敛乃至被消除。
  - 方法：
    - 双重差分 (DID)、三重差分 (DDD)
    - 内生性应对：样本选择偏误、遗漏变量敏感性分析、纠偏多变量联合检验
    - 稳健性检验、异质性分析部分都做的非常细致
    - 因果识别论证思路严谨、复现文档结构清晰


# T4. Huang-2020-JF

- Huang, Y., Pagano, M., & Panizza, U. (2020). Local Crowding‐Out in China. The Journal of Finance, 75(6), 2855–2898. Portico. [Link](https://doi.org/10.1111/jofi.12966) (rep), [PDF](http://www.pushan.org.cn/Private/Files/6382770613883614602008936831.pdf), [Google](<https://scholar.google.com/scholar?q=Local Crowding‐Out in China. The Journal of Finance, 75(6), 2855–2898>). [-Appendix-](https://onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1111%2Fjofi.12966&file=jofi12966-sup-0001-OnlineAppendix.pdf), [Replication](https://onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1111%2Fjofi.12966&file=jofi12966-sup-0002-ReplicationCode.zip) 


# T5. Crosignani-2026-JFE-Export-Control
- Crosignani, M., Han, L., Macchiavelli, M., & Silva, A. F. (2026). Securing technological leadership? The cost of export controls on firms. Journal of Financial Economics, 175, 104192. [Link](https://doi.org/10.1016/j.jfineco.2025.104192) (rep), [PDF](http://matteocrosignani.com/site/wp-content/uploads/2025/04/CHMS_Tech_Leadership.pdf), [Google](<https://scholar.google.com/scholar?q=Securing technological leadership? The cost of export controls on firms>). [Replication](https://data.mendeley.com/datasets/sw4y26xcd4/2) 
  - R codes 为主；有一张表格是用 Stata 做的
  - 技术难度不大，关键在于学习作者的论证思路和研究设计
  - **摘要**：为了维护其技术领先地位，美国限制国内供应商向特定中国企业出口尖端技术。受这些出口管制影响的美国企业如预期般停止向中国客户销售产品，但却难以在国内或政治立场相近的地区建立新的客户关系。因此，美国供应商的市值大幅缩水，盈利能力、就业和银行贷款也随之减少。中国企业则更积极主动地重组供应链，尽管这并非没有代价。总而言之，出口管制反而给那些开发这些政策旨在保护的技术的美国企业带来了更大的成本。


# T6. Kilic-2026-JFE

- Kilic, M., & Tüzel, Ş. (2026). Investing in misallocation. Journal of Financial Economics, 176, 104208. [Link](https://doi.org/10.1016/j.jfineco.2025.104208) (rep), [PDF](https://doi.org/10.1016/j.jfineco.2025.104208), [Google](<https://scholar.google.com/scholar?q=Investing in misallocation>). [-Appendix-](https://ars.els-cdn.com/content/image/1-s2.0-S0304405X25002168-mmc1.pdf), [Replication](https://data.mendeley.com/datasets/vmhdthtzxg/1).
  - We document that 20% of Compustat firms exhibit above-median investment rates despite having below-median marginal product of capital (MPK), seemingly “misallocating” resources. These firms are typically younger and more likely to experience substantial upwards jumps in sales and MPK in subsequent years. They contribute significantly to innovation, and their investments predict future aggregate productivity, creating value beyond their current MPK. We propose and estimate a simple endogenous firm growth model that captures key cross-sectional features and enables counterfactual analysis. Ignoring the potential for future jumps in hypothetical investment policies reduces MPK and investment dispersion but also lowers aggregate productivity.
  - 作者提供了一份「伪数据」，用于演示论文中实证结果的实现过程
  - 也提供了 dofiles 来复现论文中的主要表格和图形
  
# T7. Baker-2026-JFE

- Baker, S. R., Bloom, N., Davis, S. J., & Kost, K. (2026). Policy news and stock market volatility. Journal of Financial Economics, 175, 104187. [Link](https://doi.org/10.1016/j.jfineco.2025.104187) (rep), [PDF-wp](https://static1.squarespace.com/static/5e2ea3a8097ed30c779bd707/t/673f8453a8f94f09d66b14d5/1732215892470/Policy+News+and+Stock+Market+Volatility%2C+19+November+2024.pdf), [Google](<https://scholar.google.com/scholar?q=Policy news and stock market volatility>). [Replication](https://data.mendeley.com/datasets/rmhtcwnvrk/1)
  - Stata codes
  - We use newspapers to create Equity Market Volatility (EMV) trackers at daily and monthly frequencies. Our headline EMV tracker moves closely with the VIX and the S&P500 returns volatility in and out of sample. We exploit the volume of newspaper text to construct forty category-specific EMV trackers. News about commodity markets, interest rates, real estate markets, aggregate activity, and inflation figure prominently in EMV articles. Policy news is another major source of market volatility: 30 % of EMV articles discuss tax policy, 30 % discuss monetary policy, and 25 % refer to some form of regulation. Combining our newspaper-based trackers with textual analysis of 10-K filings, we obtain monthly firm-level risk exposure measures. These measures help explain the cross-sectional structure of realized volatilities and its evolution over time, even after conditioning on firm and time fixed effects.

# T8. Carpenter-2026-JFE-中美债券收益风险
- Carpenter, J. N., Lu, F., & Whitelaw, R. F. (**2026**). Government bond risk and return in the US and China. **Journal of Financial Economics**, 176, 104224. [Link](https://doi.org/10.1016/j.jfineco.2025.104224) (rep), [PDF-wp](https://pages.stern.nyu.edu/~rwhitela/papers/Government%20Bond%20Risk%20and%20Return%20in%20the%20US%20and%20China.pdf), [Google](<https://scholar.google.com/scholar?q=Government bond risk and return in the US and China>). [Replication](https://data.mendeley.com/datasets/h4t3bpbrvn/2), 
  - Table 1 and Table 2: Python codes
  - Table 3-6, Stata 16

- We propose a new approach to modeling bond risk and risk premia, inspired by the equity risk-return literature, which does not impose the tight restrictions found in models that generate closed-form bond prices. We estimate the joint dynamics of the volatility and Sharpe ratio of principal-component bond-factor portfolios for the US and China. Predictors include yield curve variables and, for the US, VIX. We document complex time-varying relations between the price and quantity of interest rate risk inconsistent with the frameworks in existing studies. Interesting differences between the US and China further highlight the need for our more flexible approach.


![](https://ars.els-cdn.com/content/image/1-s2.0-S0304405X25002326-gr1_lrg.jpg)



# T9. Hau-2024-JF

Hau, H., Huang, Y., Lin, C., Shan, H., Sheng, Z., & Wei, L. (2024). FinTech Credit and Entrepreneurial Growth. **The Journal of Finance**, 79(5), 3309–3359. Portico. [Link](https://doi.org/10.1111/jofi.13384) (rep), [PDF](http://sci-hub.ren/10.1111/jofi.13384), [-Appendix-](https://onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1111%2Fjofi.13384&file=jofi13384-sup-0001-InternetAppendix.pdf), [Google](<https://scholar.google.com/scholar?q=FinTech Credit and Entrepreneurial Growth. The Journal of Finance, 79(5), 3309–3359>). [Replication](https://onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1111%2Fjofi.13384&file=jofi13384-sup-0002-ReplicationCode.zip)

- 文中提供了简单的例子，可以采用模拟来演示

![Hau-2024-JF-Figure01-histogram-RDD](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/Hau-2024-JF-Figure01-histogram-RDD.png)

![Hau-2024-JF-Figure02-RDD](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/Hau-2024-JF-Figure02-RDD.png)









# T10. 计数模型-多期DID应用

Yang, Z., & Ding, H. (2024). Turning a blind eye: How local government fiscal distress affects the entry of energy-intensive enterprises. **Energy Economics**, 138, 107828. [Link](https://doi.org/10.1016/j.eneco.2024.107828) (rep), [PDF](https://doi.org/10.1016/j.eneco.2024.107828), [Google](<https://scholar.google.com/scholar?q=Turning a blind eye: How local government fiscal distress affects the entry of energy-intensive enterprises>).
[Replication](https://ars.els-cdn.com/content/image/1-s2.0-S014098832400536X-mmc1.zip)

- This study explores the impact of local fiscal distress on energy-intensive entrepreneurial ventures. We theoretically establish a conceptual framework between government fiscal distress and energy-intensive entrepreneurial activity through the lens of environmental regulation. Using the newly available firm registration data, we employ the **Poisson regression** model and find that the falling fiscal condition of county governments triggered by an exogenous tax reform significantly leads to more entry of energy-intensive enterprises. We uncover that the increased entry of energy-intensive enterprises is primarily driven by relaxing environmental regulation rather than other policy changes. Delving into firm nature, we find that these energy-intensive entrants are usually large firms and privately owned firms. Further evidence suggests that industrial agglomeration, regional marketization levels, and legal environments negatively moderate the impact of fiscal distress on the entry of energy-intensive enterprises. This paper sheds light on the potential environmental consequences of governments' fiscal distress.

$$
\text { EnergyFirm }_{i t}=\exp \left(\sum_{t=2001, t \neq 2004}^{2007} \beta_t \cdot \text { Shock }_i \cdot \text { YrD }_t+\gamma^{\prime} \mathbf{X}_{i, t-1}+\lambda_{c t}+\mu_i\right) \varepsilon_{i t}
$$

- 方法：
  - `reghdfe`
  - `ppmlhdfe`
    - 左志勇, 2022, [Stata：三维引力模型介绍与估计-ppmlhdfe-nbreg-reghdfe](https://www.lianxh.cn/details/848.html).
  - `permute` 
  - `dpplot`
  - Placebo test


# T11. Mijit-2025-EE

>论文推介和复现：异质性多期DID-eventstudyinteract应用

Mijit, R., Hu, Q., Xu, J., & Ma, G. (2025). Greening through AI? The impact of Artificial Intelligence Innovation and Development Pilot Zones on green innovation in China. Energy Economics, 146, 108507. [Link](https://doi.org/10.1016/j.eneco.2025.108507) (rep), [PDF](http://sci-hub.ren/10.1016/j.eneco.2025.108507), [Google](<https://scholar.google.com/scholar?q=Greening through AI? The impact of Artificial Intelligence Innovation and Development Pilot Zones on green innovation in China>), [Replication](https://www.sciencedirect.com/science/article/pii/S0140988325003317#appSB) 
- 方法：

### 方法

`eventstudyinteract`，[Sun](https://doi.org/10.1016/j.jeconom.2020.09.006) and Abraham ([2021](http://sci-hub.ren/10.1016/j.jeconom.2020.09.006))
  - Sun, L., & Abraham, S. (2021). Estimating dynamic treatment effects in event studies with heterogeneous treatment effects. Journal of Econometrics, 225(2), 175–199. [Link](https://doi.org/10.1016/j.jeconom.2020.09.006), [PDF](http://sci-hub.ren/10.1016/j.jeconom.2020.09.006), [PDF2](https://arxiv.org/pdf/1804.05785), [Google](<https://scholar.google.com/scholar?q=Estimating dynamic treatment effects in event studies with heterogeneous treatment effects>), [Slides](https://lsun20.github.io/event_studies_slides.pdf)
  - Stata 命令：
    - `eventstudyinteract`
    - `lincomest`


# T13. Leblebicioğlu-2025-AEJ-EP

- Leblebicioğlu, A., & Savaşer, T. (2025). The Not-So-Uniform Effects of Trade Secret Protection on Business Entry. **American Economic Journal**: Economic Policy, 17(4), 192–227. [Link](https://doi.org/10.1257/pol.20220814) (rep), [PDF](http://sci-hub.ren/10.1257/pol.20220814), [Appendix](https://www.aeaweb.org/doi/10.1257/pol.20220814.appx), [Google](<https://scholar.google.com/scholar?q=The Not-So-Uniform Effects of Trade Secret Protection on Business Entry>). [-Replication-](https://www.openicpsr.org/openicpsr/project/201465/version/V1/view) 
  - 加强商业秘密保护 (UTSA 实施) 会抑制小企业的创立和进入；但会促进大企业的进入。
  - We explore the consequences of trade secret protection for new business formation in the United States. We find the states that adopt the Uniform Trade Secrets Act (UTSA), which enhances intellectual property rights, experience an overall decline in firm and establishment entry rates. This result is driven by the reduction in the establishment entry rates of start-ups and small firms. By contrast, the law increases the establishment entry rates of incumbents and larger firms. The negative impact of the UTSA is larger in industries that rely more on intellectual assets and trade secrets, as well as external-finance-dependent industries.






# T14. Stata 程序编写：Oster (2019) 系数稳定性检验的 Stata 实现

根据如下理论分析和 [github-`coefstability`](https://github.com/gratzt/Coef-Stability-Oster) 中的初始代码编写一个正式的 Stata 程序 `coefstability.ado`，用于实现 Oster (2019) 提出的系数稳定性检验方法。

- 连老师会提供全程指导
- 完成后的论文可以合作投稿到 Stata Journal

> Oster, E. (**2019**). Unobservable Selection and Coefficient Stability: Theory and Evidence. **Journal of Business & Economic Statistics**, 37(2), 187–204. [Link](https://doi.org/10.1080/07350015.2016.1227711), [PDF](http://sci-hub.ren/10.1080/07350015.2016.1227711), [Google](<https://scholar.google.com/scholar?q=Unobservable Selection and Coefficient Stability: Theory and Evidence>). [-cited-5000次](https://scholar.google.com/scholar?cites=11936978270607540916&as_sdt=2005&sciodt=0,5&hl=zh-CN), [github-`coefstability`](https://github.com/gratzt/Coef-Stability-Oster)

相关应用：
- Acheampong, A. O., & Said, R. (2024). Financial inclusion and the global net-zero emissions agenda: Does governance quality matter? Energy Economics, 137, 107785. [Link](https://doi.org/10.1016/j.eneco.2024.107785) (rep), [PDF](http://sci-hub.ren/10.1016/j.eneco.2024.107785), [Google](<https://scholar.google.com/scholar?q=Financial inclusion and the global net-zero emissions agenda: Does governance quality matter>). [Replication](https://ars.els-cdn.com/content/image/1-s2.0-S0140988324004936-mmc1.zip) 
  - 存放于 `PX_papers4/Acheampong-2024-EE-Oster-2019-omit-variable-test` 目录下
  
```stata
//Table 10: Oster (2019) test for omitted variable bias
//OLS results and Oster stability test
eststo clear
eststo: regress lnco2kt  lnrgdpc lnrgdpc2 lnrenew lnfdi  lntrad lnurb FI i.year,  robust
psacalc delta FI, rmax (1)
```

- Cepni, O., Şensoy, A., & Yılmaz, M. H. (2024). Climate change exposure and cost of equity. Energy Economics, 130, 107288. [Link](https://doi.org/10.1016/j.eneco.2023.107288) (rep), [PDF](https://file-lianxh.oss-cn-shenzhen.aliyuncs.com/Refs/2026-Spring/Cepni_2024_Climate_change_exposure_and_cost_of_equity.pdf), [Google](<https://scholar.google.com/scholar?q=Climate change exposure and cost of equity>). [Replication](https://ars.els-cdn.com/content/image/1-s2.0-S0140988323007867-mmc1.zip)
  - 存放于 `PX_papers4/Cepni-2024-EE-xtabond2-DID-robust` 目录下
- Bao, L., Huang, D., & Lin, C. (2024). Can Artificial Intelligence Improve Gender Equality? Evidence from a Natural Experiment. Management Science. [Link](https://doi.org/10.1287/mnsc.2022.02787), [PDF](https://papers.ssrn.com/sol3/Delivery.cfm/4202239.pdf?abstractid=4202239&mirid=1), [Google](<https://scholar.google.com/scholar?q=Can Artificial Intelligence Improve Gender Equality? Evidence from a Natural Experiment>).

```stata
*- table_b1.do

// =======
// Table B1: Oster (2019)
// =======

** set path **
local path_data "$root/Data/"
local path_results "$root/Results/"

use "`path_data'/data_main.dta", clear

* install psacalc
ssc install psacalc

* pca
pca visual_positive visual_negative vocal_positive vocal_negative verbal
predict pc1 pc2 pc3, score

areg quality pc2 teacher_gender teacher_age teacher_experience age study gender, absorb(month)


** Part 1: min(2R^2,1)

bs r(beta), rep(100): psacalc beta pc2, rmax(0.40) delta(1) model(areg quality pc2 teacher_gender teacher_age teacher_experience age study gender, absorb(month))

bs r(beta), rep(100): psacalc beta pc2, rmax(0.40) delta(1.5) model(areg quality pc2 teacher_gender teacher_age teacher_experience age study gender, absorb(month))

psacalc delta pc2, rmax(0.40) beta(0) model(areg quality pc2 teacher_gender teacher_age teacher_experience age study gender, absorb(month))
```