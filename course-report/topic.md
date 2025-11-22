
# 
-   [The Risk of Finance Words](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4947710)
    -   with Xinbo Chen, Bowen Du (October 2024)
    -   [Public Data: Volatility Dictionary](https://mlfina.github.io/Volatility_Dictionary/)
    -   [Replication Package: Volatility Dictionary](https://github.com/mlfina/The_Risk_of_Finance_Words)

# 论文推介和复现：Panel Trees

- Cong, L. W., Feng, G., He, J., & He, X. (2025). Growing the efficient frontier on panel trees. Journal of Financial Economics, 167, 104024. [Link](https://doi.org/10.1016/j.jfineco.2025.104024) (rep), [-PDF-](https://doi.org/10.1016/j.jfineco.2025.104024), [PDF2](https://arxiv.org/pdf/2501.16730), [Google](<https://scholar.google.com/scholar?q=Growing the efficient frontier on panel trees>). [-Replication- R 语言](https://data.mendeley.com/datasets/k7d7xmdy4y/2), [作者主页提供的资源](https://www.xinhesean.com/), [Slides](https://jingyuhe.com/files/PTree.pdf)
- Github: <https://github.com/Quantactix/PTree>
- [P-Tree-Public-Data](https://github.com/Quantactix/P-Tree-Public-Data)


# 论文推介和复现

- Leblebicioğlu, A., & Savaşer, T. (2025). The Not-So-Uniform Effects of Trade Secret Protection on Business Entry. **American Economic Journal**: Economic Policy, 17(4), 192–227. [Link](https://doi.org/10.1257/pol.20220814) (rep), [PDF](http://sci-hub.ren/10.1257/pol.20220814), [Appendix](https://www.aeaweb.org/doi/10.1257/pol.20220814.appx), [Google](<https://scholar.google.com/scholar?q=The Not-So-Uniform Effects of Trade Secret Protection on Business Entry>). [-Replication-](https://www.openicpsr.org/openicpsr/project/201465/version/V1/view) 
  - 加强商业秘密保护 (UTSA 实施) 会抑制小企业的创立和进入；但会促进大企业的进入。
  - We explore the consequences of trade secret protection for new business formation in the United States. We find the states that adopt the Uniform Trade Secrets Act (UTSA), which enhances intellectual property rights, experience an overall decline in firm and establishment entry rates. This result is driven by the reduction in the establishment entry rates of start-ups and small firms. By contrast, the law increases the establishment entry rates of incumbents and larger firms. The negative impact of the UTSA is larger in industries that rely more on intellectual assets and trade secrets, as well as external-finance-dependent industries.



# 论文推介：Judge IV

- Chyn, E., Frandsen, B., & Leslie, E. (2025). Examiner and Judge Designs in Economics: A Practitioner’s Guide. Journal of Economic Literature, 63(2), 401–439. [Link](https://doi.org/10.1257/jel.20241719) (rep), [PDF](http://sci-hub.ren/10.1257/jel.20241719), [Appendix](https://www.aeaweb.org/doi/10.1257/jel.20241719.appx), [Google](<https://scholar.google.com/scholar?q=Examiner and Judge Designs in Economics: A Practitioner’s Guide>). [-Replication-](https://doi.org/10.3886/E209883V1) 

  -This article provides empirical researchers with an introduction and guide to research designs based on variation in judge and examiner tendencies to administer treatments or other interventions. We review the basic theory behind this research design, outline the assumptions under which the design identifies causal effects, describe empirical tests of the conditions for identification, and discuss trade-offs associated with choices researchers must make for estimation. We demonstrate concepts and best practices in an empirical case study that uses an examiner tendency research design to study the effects of pretrial detention.


# Stata 新命令：政策学习
Cerulli, G. (2025). Optimal policy learning using Stata. The Stata Journal, 25(2), 309–343. [Link](https://journals.sagepub.com/doi/10.1177/1536867X251341143), [PDF](https://journals.sagepub.com/doi/pdf/10.1177/1536867X251341143), [Google](<https://scholar.google.com/scholar?q=Optimal policy learning using Stata>).

```stata
net describe st0774, from(http://www.stata-journal.com/software/sj25-2)

net describe http://repec.org/bocode/o/opl_ma
```

# darts: 

![20251104003015](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20251104003015.png)

A python library for user-friendly forecasting and anomaly detection on time series.

- Website: <https://unit8co.github.io/darts/>
- Github: <https://github.com/unit8co/darts>
- <https://unit8.com/resources/darts-time-series-made-easy-in-python/>

Herzen, J., Lässig,, F., Piazzetta, S. G., Neuer, T., Tafti, L., Raille, G., Van Pottelbergh, T., Pasieka, M., Skrodzki, A., Huguenin, N., Dumonal, M., Ko?cisz, J., Bader, D., Gusset, F., Benheddi, M., Williamson, C., Kosinski, M., Petrik, M., & Grosch, G. (2022). Darts: User-Friendly Modern Machine Learning for Time Series. Journal of Machine Learning Research 23 (2022) 1-6. [Link](https://doi.org/10.48550/arXiv.2110.03224) (rep), [PDF](https://arxiv.org/pdf/2110.03224.pdf), [Google](<https://scholar.google.com/scholar?q=Darts: User-Friendly Modern Machine Learning for Time Series>).


# darts: Probabilistic Forecasting in Darts

找资料写一排推文，介绍在这个主题

然后使用 `akshare` 包获取沪深 300 指数或上证指数的历史数据，使用 Darts 包中的概率预测模型对该时间序列进行建模和预测，并展示预测结果。

## Introduction

**Darts** is a Python library for user-friendly forecasting and anomaly detection on time series. It contains a variety of models, from classics such as ARIMA to deep neural networks. The forecasting models can all be used in the same way, using `fit()` and `predict()` functions, similar to scikit-learn. The library also makes it easy to backtest models, combine the predictions of several models, and take external data into account. Darts supports both univariate and multivariate time series and models. The ML-based models can be trained on potentially large datasets containing multiple time series, and some of the models offer a rich support for probabilistic forecasting.

Darts also offers extensive anomaly detection capabilities. For instance, it is trivial to apply PyOD models on time series to obtain anomaly scores, or to wrap any of Darts forecasting or filtering models to obtain fully fledged anomaly detection models.

## Documentation

-   [Quickstart](https://unit8co.github.io/darts/quickstart/00-quickstart.html)
-   [User Guide](https://unit8co.github.io/darts/userguide.html)
-   [API Reference](https://unit8co.github.io/darts/generated_api/darts.html)
-   [Examples](https://unit8co.github.io/darts/examples.html)

其它参考资料：
- [Time-Series Forecasting with Darts: A Hands-On Tutorial](https://magnimindacademy.com/blog/time-series-forecasting-with-darts-a-hands-on-tutorial/)

# deeptime 

Hoffmann, M., Scherer, M., Hempel, T., Mardt, A., De Silva, B., Husic, B. E., Klus, S., Wu, H., Kutz, N., Brunton, S. L., & Noé, F. (2021). Deeptime: a Python library for machine learning dynamical models from time series data. ArXiv. [Link](https://doi.org/10.48550/arXiv.2110.15013) (rep), [PDF](https://arxiv.org/pdf/2110.15013.pdf), [Google](<https://scholar.google.com/scholar?q=Deeptime: a Python library for machine learning dynamical models from time series data>). 
- Website: <https://deeptime-ml.github.io/deeptime/>，[-Link2-](https://deeptime-ml.github.io/latest/index.html)
- Github: <https://github.com/deeptime-ml/deeptime>


# 有VaR约束的投资组合优化

Thormann, M.-L., Vuong, P. T., & Zemkoho, A. B. (2024). The Boosted Difference of Convex Functions Algorithm for Value-at-Risk Constrained Portfolio Optimization (Version 2). arXiv. [Link](https://doi.org/10.48550/arXiv.2402.09194) (rep), [PDF](https://arxiv.org/pdf/2402.09194.pdf), [Google](<https://scholar.google.com/scholar?q=The Boosted Difference of Convex Functions Algorithm for Value-at-Risk Constrained Portfolio Optimization (Version 2)>).

- Github: <https://github.com/mlthormann/BDCA-For-Portfolio-Optimization/>

## China Case

使用 `akshare` 包获取中国股票数据，然后用 [Github-BDCA](https://github.com/mlthormann/BDCA-For-Portfolio-Optimization) 中的代码进行优化。

- 张祖冲, 2025, [akshare 与 Python：中国金融数据分析与获取的开源首选工具](https://www.lianxh.cn/details/1642.html).


# 

- Website: <https://pypots.com/>

- [BrewPOTS](https://github.com/WenjieDu/BrewPOTS): The tutorials for PyPOTS, guide you to model partially-observed time series datasets.

![PyPOTS_Ecosystem_Pipeline](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/PyPOTS_Ecosystem_Pipeline.png)


## 子库 - PyGrinder

用于人为产生时间序列数据的缺失值，以便测试各种缺失值处理方法的有效性。

`PyGrinder`: a Python toolkit for grinding data beans into the incomplete for real-world data simulation by introducing missing values with different missingness patterns, including **MCAR** (complete at random), **MAR** (at random), **MNAR** (not at random), sub sequence missing, and block missing

- github: <https://github.com/WenjieDu/PyGrinder>
- website: <https://pypots.com/ecosystem/#PyGrinder>