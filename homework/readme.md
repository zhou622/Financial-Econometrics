# 作业要求和提交说明

## 提交

- &#x1F34E; 提交链接：[点击提交作业](https://workspace.jianguoyun.com/inbox/collect/8b71e5254a0f4f36ac95b582ffd7f2db/submit)  
- &#x1F34F; 所有雷同的作业均将计为 0 分，请勿抄袭！


## News
- 作业发布：[hw-03.md](hw-03.md)
  - 提交截止时间：2025 年 10 月 14 日 23:59
- 作业发布：[hw-01.md](hw-01.md), [hw-02.md](hw-02.md)
  - 提交截止时间：2025 年 10 月 7 日 23:59


![](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/Lianxh_装饰黄线.png)


## 1. 作业要求

> 有些作业要求使用 VScode 编辑器中的 Jupyter Notebook 来完成。如果你还没有安装和配置好 Python 运行环境，请参照讲义 [3  Python：安装和环境配置](https://lianxhcn.github.io/research_with_AI/body/01_install_Python_Anaconda.html) 中的说明，安装必要软件和插件，配置好 Python 运行环境。详细说明参见下方第 3 小节。

### 1.1 格式要求

1. 在呈现公式、代码和图表之前，务必插入一个 Markdown 单元格，写明你要做什么。呈现完后，再插入一个 Markdown 单元格，解释结果。数学公式中的变量和参数在首次出现时，请务必给出定义。
2. 对于数学公式，请使用 LaTeX 语法，并将公式放在美元符号 `$...$` (行内公式) 或 `$$...$$` (独立成行的公式) 之间。独立成行的公式上下方请空一行。
3. 中英文混排时，加空格。例如，`我从 2003 年开始用 Stata 写代码。` 
4. 讲义中的所有圆括号都写为半角模式，即 `Hansen (2025)`，而不是 `Hansen（2025）`。

### 1.2 提交的资料类型

- **单一文档**。如果提交的文档中的不涉及本地数据文件，则只需提交完成作业过程中撰写的程序文件 (可以用 Stata/R/Python 进行分析)，
- **压缩文件**。如果提交的文档中涉及本地数据文件，或包含一个以上的程序文档或分析文档，则需要将所有相关文件打包成一个压缩文件 (zip 格式)，并在压缩包中包含一个 `README.md` 文件，描述数据集的来源和代码的运行方法等。

### 1.3 文档结构

对于较为复杂的数据分析和回归分析任务，请务必按照「Project」来规划文档结构，将数据处理、探索性数据分析 (EDA) 和回归分析等步骤拆分成不同的文档 (Jupyter Notebook 或 Stata Do 文件)，并为不同类型的文档设定不同的子文件夹，以便于阅读和理解。

可以参照讲义 [新建项目文件结构](https://lianxhcn.github.io/research_with_AI/body/01_use_Jupyter_Notebook.html#%E9%A1%B9%E7%9B%AE%E7%BB%93%E6%9E%84%E6%96%87%E6%A1%A3) 中的相关说明，设定项目文件夹和文件。提交的文件夹结构如下：

    ```bash
    # 项目文档结构
    D:/Project/Project_Name (项目根目录，可酌情调整)
    ├── codes
    ├── data_raw
    ├── data_clean
    ├── output
    ├── README.md
    ├── 01_data_clean.ipynb
    ├── 02_EDA_analysis.ipynb
    └── 03_xxx_xxx.ipynb
    ```

---

## 2. AI 工具

**A. 可以用 AI 工具。** 

完成作业过程中，可以借助 AI 工具，但要遵守如下规则：

- 提供 AI 对话的链接 (ChatGPT、豆包等 AI 工具都支持分享链接，DeepSeek 可参考 [这个](https://www.lianxh.cn/details/1566.html) 生成分享链接)；
- 当对话链接不可用时，请采用代码块格式提供原始提示词 (按如下格式插入文本块)，例如 ：

````Markdown
```raw
##Prompt 01
你的第一组提示词 ……

##Prompt 02
你的第二组提示词 ……

……
```
````

**B. 岭院的 AI 助手**

- **URL**: <https://students.ailingnan.top/>。登录方式：详见课程群置顶群公告。
- **特点**：这个 AI 助手是专门针对岭院师生打造的。你可以在下拉菜单中选择「金融计量经济学」课程，以便获取更好的体验。
- **建议**：为了便于后续查找和归类，请勿在一个窗口里一直问不同话题的问题。好的做法是：为每个话题开一个新窗口提问，并及时修改窗口标题 (采用能够反映话题的关键词)。

---

## 3. 软件安装和环境配置

虽然这门课主要使用 Stata 软件，但为了便于大家使用 AI 工具和生成图形等，我们建议大家安装并配置好 Python 运行环境，以便在 VScode 中运行 Stata 命令，并使用 `github copilot` 等 AI 工具辅助完成作业。

> **安装指南：** 

1. **第一步：** 请认真阅读 [3  Python：安装和环境配置](https://lianxhcn.github.io/research_with_AI/body/01_install_Python_Anaconda.html) 中第 3.1 和 3.2 小节的说明，安装必要软件和插件，配置好 Python 运行环境。
2. **第二步：** 参照 [3  Python：安装和环境配置](https://lianxhcn.github.io/research_with_AI/body/01_install_Python_Anaconda.html) 中 [第 3.3 小节 - 配置 Stata 环境：nbstata](https://lianxhcn.github.io/research_with_AI/body/01_install_Python_Anaconda.html#%E9%85%8D%E7%BD%AE-stata-%E7%8E%AF%E5%A2%83nbstata) 中的说明，配置好 Stata 运行环境，以便在 VScode 中运行 Stata 命令。

**注意：**

1. 为了确保能在 VScode 中运行 Stata 命令，建议安装我在课程群置顶群公告中提供的 Stata 17 软件 (这是一个正版软件)。当然，如果你有其他版本的 Stata 软件，也可以尝试使用。**基本原则是**：无论你安装哪个版本的 Stata，最终在 Stata 安装目录下一定要有许可证文件 `STATA.LIC`，否则 `nbstata` 将无法与你的 Stata 软件关联，也就无法在 VScode 中的 `.ipynb` 文件中运行 Stata 命令。
   
2. 安装 Stata 时，建议选择“典型安装”选项，以确保安装所有必要组件。同时，请注意安装路径中不要包含空格或特殊字符，以避免后续配置中的路径问题。我的安装路径是：`D:/stata17`。

