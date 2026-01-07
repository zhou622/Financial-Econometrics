
## FE-课程报告写作指南

&emsp;

> 连玉君 (arlionn@163.com)  , &emsp; [课程主页](https://gitee.com/arlionn/EF)


- V1: `2026/1/7 19:39`


&emsp;

## 0. 课程报告提交 

![](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/Lianxh_装饰黄线.png)

**提交报告：** 

- **坚果云**：[-点击提交 &#x1F34E; -](https://workspace.jianguoyun.com/inbox/collect/8b71e5254a0f4f36ac95b582ffd7f2db/submit) (1 分钟即可完成)
  - 姓名写法：**FE-姓名** (在姓名前加上 `FE` 字样) 
- **deadline**：2026 年 1 月 26 日 23:59 
  - 提前提交的同学，我可以提供 2-3 次指导和反馈，帮助你完善报告内容和格式。课程报告的成绩以最后一版为准。

![](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/Lianxh_装饰黄线.png)


**注意事项**：

1. **更新课程报告**。 你可以更新你提交的资料。提交新版本时，只需添加 `V1, V2, ……` 这样的版本号标记即可，如「`FE-张帅帅-V2-论文作者-年份.zip`」。
2. **复现论文的引文信息**。 请务必在报告开头部分写明你复现的论文的引文信息，可以 Fork 本仓库后，打开 [topic.md](topic.md) 文档，进入编辑模式，然后复制 md 格式的完整的参考文献信息。例如：**T1. Wang-2024-EE** 的引文信息是：
  - Wang, Z., Zhang, T., Ren, X., & Shi, Y. (**2024**). AI adoption rate and corporate green innovation efficiency: Evidence from Chinese energy companies. **Energy Economics**, 132, 107499. [Link](https://doi.org/10.1016/j.eneco.2024.107499), [PDF](https://file-lianxh.oss-cn-shenzhen.aliyuncs.com/Refs/2026-Spring/Wang_2024_AI_adoption_rate_and_corporate_green_innovation.pdf), [Google](<https://scholar.google.com/scholar?q=AI adoption rate and corporate green innovation efficiency: Evidence from Chinese energy companies>), [cited](https://scholar.google.com/scholar?cites=3084301341760475150&as_sdt=2005&sciodt=0,5&hl=zh-CN), [Replication](https://ars.els-cdn.com/content/image/1-s2.0-S014098832400207X-mmc1.zip)。 
3. **图片名称和图片上传**。
   - 课程报告中出现的所有图片都按此规则命名：【`Author-Year-Fig#-图片简称-作者姓名.png`】 (或 jpg)。例如，【`Tian-2024-Fig01-ttest-连小白.png`】
   - 所有图片必须使用 **2.3 设定 PicGo 图床** 中介绍的方法上传到 lianxh.cn 图床，并使用该图床的链接插入到报告中。&#x1F34F;：未按要求上传图片的报告将被退回修改，我也会酌情扣分 (5-10 分)。



![](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/Lianxh_装饰黄线.png)


大家好！写这份文档是为了各位更好地完成课程报告。主要介绍了论文复现报告的写作要求和注意事项。我也分享了一些我平时使用的工具和软件

## 1. 需要提交的资料
- A. **中文精要**。用 Markdown 撰写
    - 建议使用编辑器：VScode ([插件安装和使用](https://www.lianxh.cn/details/1490.html); [实用插件推荐](https://www.lianxh.cn/details/1390.html))
    - 导出 PDF 格式的报告。
      - **方法 1**：将你的最终稿贴入 <https://md.doocs.org/>，然后点击 `文件` &rarr; `导出` &rarr; `导出为 PDF` 获得 PDF 格式。
      - **方法 2**：在 VScode 编辑器中安装 **Markdown PDF** 或 **Markdown All in one** 等插件，将你的 Markdown 文档转换为 HTML 或 PDF 格式；
    - (选做) 你也可以使用 marp 制作一份与课程报告对应的幻灯片，参见 [Marp：用Markdown快速写幻灯片](https://www.lianxh.cn/news/148555c4f20ce.html)。Note：借助 ChatGPT 等 AI 工具，也可以加快制作 Slides 的进度。你可以把你的课程报告 (`.md` 格式) 传给 AI，然后写提示词：`帮我制作一份 Marp 格式的 Slides，正文字号 24；30 页左右；你可以从我的 .md 文档中选取合适的内容制作幻灯片`。
- B. **重现数据和代码**。建议参考 [T6_Chen_2019](https://www.jianguoyun.com/p/DZc_UaEQtKiFCBjr7OUEIAA) 的模式放置相关文档 (具体设定可以酌情增减)。
  - 文档名称：请使用我指定的文件夹名称，不要擅自修改。
  - 代码格式：原文作者提供的代码有时候排版很奇怪，请参考 [一些论文重现范本](https://www.jianguoyun.com/p/DVlZ9DYQtKiFCBil9O4EIAA) 中的代码格式进行调整。确保代码结构清晰，版面整洁、风格一致。
  ![20221117164308](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20221117164308.png)


### 1.1 中文精要写作要点
中文精要的目的是为了通过重现期刊论文中的关键结果，更好地掌握课程中介绍的计量方法，了解一篇实证分析论文的研究过程。要求如下：
- 全文 10000-15000 字。格式参见【**1.3 范本：一些论文重现范本**】。
- 文章背景介绍：
  - 1-2 页 (800-1500 字)
  - 重点介绍：研究了什么问题、基本方法、数据来源、主要结论
- 实证分析部分
  - 模型设定 (重点介绍对应专题中涉及的方法)
  - 关键变量的定义和含义
  - 作者的估计过程
  - 核心结果的讨论
  - 在介绍论文核心实证结果时，可以插入原文中的表格，并对作者提供的代码进行适当精简 (只选取有代表性的代码) 来说明表格中的结果对应的 Stata 代码。主要目的是使读者能够将论文中的结果和如何实操结合起来。 
  - 图片必须通过
- 其他相关文献扩展  (针对 **B 类**文献)
  - 介绍 2-3 篇引用该文的后续文献，重点介绍它们进行了拓展，或者从哪些新的角度 (样本、方法、变量等) 进行了分析。
  - 每篇半页篇幅即可

### 1.2 复现代码风格

参见如下推文，酌情调整。

  - [论文重现：外部命令的版本控制](https://www.lianxh.cn/news/e26dd9c9dd67a.html)
  - [Stata：论文重现代码模板](https://www.lianxh.cn/news/ca673ff4a27cc.html)
  - [可重复性研究：如何保证你的研究结果可重现？](https://www.lianxh.cn/news/6d3f9bbbdef36.html)


### 1.3 范本：一些论文重现范本

- **下载：** Top 论文复现及中文精要范例
  - 坚果云：[Top论文复现及中文精要](https://www.jianguoyun.com/p/DVlZ9DYQtKiFCBil9O4EIAA)

- 这些都是连享会往期课程中使用的讲义，每篇文章都对应了**中文精要**、**Data\Codes**
- 部分论文还提供了使用 Marp 制作的幻灯片。 

![20221117122439](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20221117122439.png)

&emsp; 

### 1.4 补充说明和资料

我主要从 AER，QJE，JFE，MS 等期刊选择论文，这些论文都提供了相对完整的复现数据和代码，使用的方法也与我们本次课程中讲解的主题密切相关。主要借助如下网站进行搜索：

> [连享会：论文重现网站大全](https://www.lianxh.cn/news/e87e5976686d5.html)

- Mendeley 平台: [Discover Mendeley Data](https://data.mendeley.com/)
- 密歇根大学的 ICPSR: [ICPSR Data](https://www.icpsr.umich.edu/icpsrweb/)
- 哈佛大学的 IQSS: [Harvard Dataverse](https://dataverse.harvard.edu/)
- Sebastian Kranz（Ulm University）: [Find Economic Articles with Data](https://ejd.econ.mathematik.uni-ulm.de/)
  - 可以指定期刊名称、代码类型等。这是我的主要搜索工具。
- Replication WIKI: [Replication in the social sciences, particularly economics!](http://replication.uni-goettingen.de/wiki/index.php/Main_Page)


&emsp; 

## 2. 写作流程和工具

> **常用软件下载链接**
- 链接：https://pan.baidu.com/s/1tfXziwFDeSdyboLdpBLq8g 
- 提取码：qsvf
- Note: 除了 PicGo 软件外，其它软件大家可以下载最新版。

### 2.1 课程报告写作流程 - 速览
- **S1：** 在 VScode 或 Typora 中写推文初稿 (建议两个同时用)。
  - 推文中的图片 **务必** 上传到连享会主页图床，参见第 **「2.3 设定 PicGo 图床」** 小节。
  - 推文格式要求请务必严格遵守，参见 「**4. 推文格式要求**」，以及 「[推文极简模板](https://gitee.com/arlionn/EF/wikis/%E8%AF%BE%E7%A8%8B%E6%8A%A5%E5%91%8A%E6%A8%A1%E6%9D%BF-001-%E7%B2%BE%E7%AE%80%E7%89%88.md?sort_id=3232133)」(单击页面中的【编辑】按钮查看原始 Markdown 文档)，或原始 Markdown 文档：[推文范例s](https://www.jianguoyun.com/p/DcTq2fwQ34HYCBjd4-oEIAA)。
- **S2：** 完成推文后务必贴入 [mdnice.com](https://mdnice.com/) 测试一下文中的数学公式和图片是否能正常显示
- **S3：** 将测试完的推文 Markdown 文档转换成 HTML 或 PDF 格式，确认：(1) 数学公式是否正常显示；(2) 图片是否能正常显示; (3) 有没有遗漏或显示不全的内容，有没有错别字和病句。
- **S4：** 提交：
  - &#x2B55; 提交 2 - **坚果云**：请同时传一份到坚果云中：[-点击提交推文-](https://workspace.jianguoyun.com/inbox/collect/9375d5be4dc24ac9a3f23bee9bff89a2/submit) (1 分钟即可完成)
> Note: 写作过程中，有任何问题，都可以在微信群里讨论，亦可私信我。

### 2.2 Markdown 编辑器

课程报告需要用 Markdown 来写。为了保证推文中的图片都能永久保存，请务必使用第 **「2.3 设定 PicGo 图床」** 小节介绍的图床。

- **推文写作工具**。建议统一使用 [「VS Code」](https://code.visualstudio.com/) ([教程1](https://www.cnblogs.com/clwydjgs/p/10078065.html)；[教程2](https://www.cnblogs.com/qianguyihao/archive/2019/04/18/10732375.html)) 或 撰写 Markdown 文稿。
  - 也可以用 Typora 编辑器。请预先安装 [Pandoc](https://pandoc.org/installing.html)，以便把 .md 转换为 PDF，HTML，幻灯片，Word 文档。     
- **VScode 的插件**：点击 VScode 编辑器最左侧的第四个按钮 **安装常用插件**：
  - 搜「Chinese」&rarr; 安装 `Chinese (Simplified) Language` 插件 
  - 搜「Stata」&rarr; 安装 `Stata Enhanced`, `Stata Language`, `statarun` 等插件
  - 搜「Markdown」&rarr; 安装 `Markdown Extended`, `Markdown All in One`, `Markdown PDF`, `Markdown Preview`, `Markdown TOC`, `Marp for VS Code` (制作 Markdown 幻灯片) 等插件
  - 搜「LaTeX」&rarr; 安装 `LaTeX language support`     
  - 中英文混排添加空格的插件：`assist` 
- **测试和上传**。写好推文后，请将 Markdown 文稿贴入 [mdnice.com]([www.mdnice.com](https://mdnice.com/)) 网站编辑器，确保能正常显示。重点查看数学公式和图片是否能正常显示。



### 2.3 设定 PicGo 图床 

> - [图床工具的使用：PicGo 介绍](https://www.jianshu.com/p/9d91355e8418)
> - [Markdown图片神器：PicGo-让你爱上笔记与分享](https://www.lianxh.cn/news/3b9caefb73bc5.html)

#### 2.3.1 下载-安装 PicGo

百度云盘：<https://pan.baidu.com/s/10N736oJVCPrTuVNaGrNOwQ>

解压后按提示安装即可。

最新版下载地址：<https://github.com/Molunerfinn/PicGo/releases>

- **推文格式**：[template](https://github.com/arlionn/lianxhta/blob/main/template/readme.md) 文件夹中放置了一些已经发布的推文，可以参考其行文风格和格式。
- **数学公式**：
  - LaTeX 公式录入方法参见：[Markdown中书写LaTeX数学公式简介](https://www.lianxh.cn/details/250.html)
  - **公式识别**：可以使用 [Mathpix](https://www.lianxh.cn/details/284.html) (收费) 或者 [simpletex](https://simpletex.cn/) (推荐，免费) 来识别数学公式。
- **图片**：
  - **本地图片的命名规则**：请严格按照 `作者汉语拼音_推文编号_Figxx.png` 格式命名图片，例如：`lianyujun_B782_Fig02.png`。由于我们所有人的图片都放置在同一个图床，同名文件会自动「旧的覆盖新的」。如果图片名称过于简单，不但会导致你的图片无法正常显示，也会导致此前的推文图片引用错误。(Update: `2025.8.14`) 
  - 如果截图后使用 [PicGo 软件](https://github.com/arlionn/lianxhta/wiki/lianxh_PicGo) 上传图片，并在 **PicGo 设置** 中选择了「时间戳重命名 (`开`)」，它会自动利用时间戳作为图片名称，通常不会产生冲突。
  - 可以使用 [Snipaste](https://www.lianxh.cn/details/1111.html) 截图工具，直接截图到剪贴板中，然后使用 PicGo 软件上传到连享会图床，将产生的链接 (已自动存入剪切板) 粘贴到 Markdown 文档中。Snipaste 也可以将截图保存为图片文件，方便后续使用。

- **借助 AI 写推文**：参见连玉君, 2025, **Empirical Research with AI**，[Chapter 7-9](https://lianxhcn.github.io/research_with_AI/body/05_00_read_paper_with_AI.html) 介绍的方法和提示词。 

#### 2.3.2 配置图床 (依次填入)

打开 PicGo，点击左侧「**图床设置**」下来菜单，选择「**阿里云OSS**」，填入如下信息：

  - **设定 KeyID：** LTAI4Fv321ae7Sm9okgZLfMz
  - **设定 KeySecret：** <*请向连老师索取*> 
  - **设定存储空间名：** fig-lianxh  
  - **确认存储区域：** oss-cn-shenzhen   
  - **指定存储路径：** 不填
  - **设定自定义域名：** 不填

![PicGo-阿里云图床配](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/PicGo-阿里云图床配置.png)


#### 2.3.3 上传图片
- **本地图片**：采用点击或拖拽方式上传完图片后，PicGo 会自动生成 Markdown 格式的图片链接：一份自动存于剪切板，另一份显示在屏幕右下角。我们只需到 Markdown 编辑窗口中，按下快捷键「**Ctrl+V**」即可贴入图片链接地址。
- **剪切板图片**：通过截图等方式得到的图片 (已经自动保存在了剪切板上)，可以直接点击图中右底角【剪切板图片上传】按钮上传图片 (有时候需要点击两次才能正确上传，可以点击左边栏的【相册】按钮查看是否成功上传)。

补充说明：

- 点击【PicGo设置】可设定快捷键和各种参数。比如，可以设置「时间戳重命名 (`开`)」，它会自动利用时间戳作为图片名称，通常不会产生冲突。也可以点击「自定义链接格式」，填入 `<img src="$url" width="650" alt="$fileName">`，以便自动产生如下格式的图片链接：

```HTML
<img src="https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/image_name.png" width="650" alt="image_name.png">
``` 

![](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/PicGo-上传图片.png)

- 点击左边栏【相册】按钮，可以查看已经上传的图片，并从图片下方的第一个菜单复制图片链接； 


### 2.4 其它工具

- **mathpix**
  - 快速图片转公式软件，亦可以整页识别 PDF 文档。[Mathpix介绍](https://blog.csdn.net/qq_34243930/article/details/89158366)
- **Snipaste**
  - 截图-贴图软件，配合 PicGo 使用。[官网介绍](https://zh.snipaste.com/)；[Snipaste简介](https://baijiahao.baidu.com/s?id=1654041827952660862&wfr=spider&for=pc)
  - 可以使用 [Snipaste](https://www.lianxh.cn/details/1111.html) 截图工具，直接截图到剪贴板中，然后使用 PicGo 软件上传到连享会图床，将产生的链接 (已自动存入剪切板) 粘贴到 Markdown 文档中。Snipaste 也可以将截图保存为图片文件，方便后续使用。


&emsp;

## 3. 课程报告格式要求

> **特别注意：** 除非万不得已，尽量 **不要** 用图片形式展示 Stata 结果。推文中的 Stata 结果尽量采用结果窗口中呈现的文本信息来呈现，也就是采用代码块来呈现估计结果。这样就不会过度依赖图床，图床一旦出问题，就会导致推文中的所有图片都无法正常显示。另外，使用文本块显示结果可以获得更好的跨平台展示效果。
> &emsp;        
> **范本：** 参见「1.3 范本：一些论文重现范本」小节。

### 3.1 署名
请在推文首行填入你的真实姓名 (单位信息)，格式为 
```Markdown 
&emsp;

> **作者**：xxx (xxx大学)    
> **邮箱**：<xxx#163.com>  
```
- **Notes:** (1) `**作者**：xxx (xxx大学)  `，行尾添加两个空格，以保证能正常换行；(2) `**E-Mail:** <xxx#163.com>` 邮箱地址外侧加上 `<>` 符号，以便显示为超链接形式。(3) `&emsp;` 是一个网页标记符，用于产生一个空白行。 


### 3.2 标题层级和目录

- 推文的各个小节需要顺序编号
- 一级标题用 **「`## 1. 一级标题`」** (说明：`##` 后要添加一个空格)
- 二级标题用 **「`### 1.1 二级标题`」**，最多用到三级标题，即「`#### 1.1.1 三级标题`」。
- 如果后续还需细分，可以用 **条目(item)** 或独占一行的粗体文字代替。这主要是因为，多数 Markdown 编辑器的一级标题字号都太大了。
- **文档目录** 不必手动添加，只需在正文之前独占一行加上 `[toc]`，或 `[TOC]`，或 `[[TOC]]`，具体采用何种方式取决于你的 Markdown 编辑器。 


### 3.3 段落

- 段落之间要空一行，这样网页上的显示效果比较好；
- 每个段落不要太长 (最好不好超过 200 字，4 行以内比较好)，否则网页或手机阅读时会比较累；


### 3.4 中英文混排

- **记得加空格！！** 英文字符和数字两侧要空一格，否则中英文混排时字符间距过小；例如：`我用Stata已经15年了(Cox,2019)，但Arlion(2018)说他刚用了14年。` 要修改为：`我用 Stata 已经 15 年了 (Cox, 2019)，但 Arlion (2018) 说他刚用了 14 年。`。
  - 若需批量添加中英文混排的空格，可以将 Markdown 文本贴入 [mdnice.com](https://www.mdnice.com/)，依次点击 **格式** &rarr; **格式化文档 (Ctrl+Alt+F)** 即可。部分尚未达到要求的可以手动修改。
  - 另一个办法是在 VScode 中查找插件 **assist**，可以自动添加空格并调整中英文混排的标点符号。快捷键：选中文字，两次按下 `Ctrl+K`。
- **括号的使用** 文中所有圆括号都要在半角模式下输入，`(` 左侧和 `)` 右侧各添加一个空格。中英文混排格式参见上一行里的例子。


### 3.5 Stata 相关

  - Stata 要写为 「Stata」(首字母大写，无需加粗)，不要写成 「stata」或「STATA」。
  - 变量名用粗体 (如 \*\*varname\*\* &rarr; **varname**)；
  - Stata 命令用高亮显示 (如 \`regress\` &rarr; `regress`)；
  - 多行 Stata 命令和结果展示使用 **代码块样式**，即使用首尾 **\`\`\`** 包围，首行为 「\`\`\`stata」，最后一行为「\`\`\`」。
  - **特别注意：** 除非万不得已，尽量不要用图片形式展示 Stata 结果。推文中的 Stata 结果尽量采用结果窗口中呈现的文本信息来呈现，也就是采用代码块来呈现估计结果。这样就不会过度依赖图床，图床一旦出问题，就会导致推文中的所有图片都无法正常显示。另外，使用文本块显示结果可以获得更好的跨平台展示效果。
  - 把如下语句加入你的 **profile.do** 文档中，以便保证结果显示格式比较规整：
  
  ```stata
  set cformat  %4.3f  //回归结果中系数的显示格式
  set pformat  %4.3f  //回归结果中 p 值的显示格式      
  set sformat  %4.2f  //回归结果中 se值的显示格式  
  ```


### 3.6 数学公式
- **参考资料：** [Markdown-LaTeX 数学公式简介](lianxh.cn/news/845d7f5a2d977.html)；[常用公式](https://www.lianxh.cn/news/554f3e9c9f08d.html)
- **(1) 单行公式：** 用 **\$\$**math**\$\$** 包围的单行数学公式上下各空一行，以保证公式和正文之间的段落间距合理。
- **(2) 行内公式：** 可以使用 **\$**math**\$** 包围。为了保证在知乎和连享会主页中都能正常显示公式，请把 $y=x\beta$ 写成 `$y=x\beta$`，而不要写成 `$ y=x\beta $` (内侧多加了两个空格)。
- **(3) 公式编号：** 不要使用 `\tag{#}` 方式，换以手动方式，即在公式行尾添加 `\quad (#)`，其中，`#` 为公式编号。 
- **(4) mathpix 神器 - 惊喜：** 无论是网页还是 PDF 中的数学公式，都可以使用 mathpix (https://mathpix.com/) 软件扫描后识别成 LaTeX 数学公式，非常快捷。参见 [神器-数学公式识别工具 mathpix](https://www.jianshu.com/p/1f0506163694)。本页面顶端的「连享会成员工具包」中提供该软件的下载。




### 3.7 图片

- **图片存放**。再次强调，请务必使用 lianxh.cn 的图床，参见第 **「2.3 设定 PicGo 图床」** 小节。
- **图片清晰度**。图片要保证清晰，分辨率在 600px 以上。全文顺序编号。
- <font color=red>图片名称</font>：【`Author-Year-Fig#-图片简称-作者姓名.png`】 (或 jpg)。例如，【`Tian-2024-Fig01-ttest-连小白.png`】。**注意：** 图片名称中不要包含空格和特殊字符。
  - **特别提示：** 由于我们的团队统一使用一个图床，每幅图片的名称就是这幅图片的唯一识别码，因此图片名称尽可能有区分度，==**千万不要** 定义 **fig1** 或 **图1** 这样的过于简略的名称==，要尽量按上述建议格式命名图片。 
- **图片缩放**。在 Markdown 中插入图片的代码是 `![](url)`，如果需要调整图片的显示尺寸，以保证全文图片中的字号保持一致，可以使用如下命令 (`650px` 是图片宽度，可以根据需要更改)：
    ```md
    <img style="width: 650px" src="url">
    ```

### 3.8 版权、引用和参考资料

- 要按照学术规范进行引用和标注。
- **文末参考资料/参考文献**：
  - 文中提到的，以及写作过程中重点参考的教科书、论文、网文等都要在文末列出，以免引起版权纠纷；尽量提供原文或 PDF 下载链接；若包含连享会过往推文，请使用 `lianxh 关键词, m` 命令获取引文信息。 
  - 学术论文的引文信息可以使用 [getiref](https://www.lianxh.cn/details/1382.html) 命令自动生成。


---

**温馨提示**：

该文档经过多次修订，但仍可能存在表述不准确甚至前后矛盾的地方。 如果你在写作过程中遇到任何问题，欢迎随时联系我 (在课程群里发消息或私信我都行)。

