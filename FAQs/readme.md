## FAQs 

这里记录了一些课程中经常被问及的问题，包括 Stata 软件的安装，帮助的获取；Python 的安装和使用等。 

### Python 环境配置

#### 1. 如何在 VScode 中运行 Stata 代码？

- 请参照 [3  Python：安装和环境配置](https://lianxhcn.github.io/research_with_AI/body/01_install_Python_Anaconda.html) 中的说明，安装并配置好 Python 运行环境，以便在 VScode 中运行 Stata 命令。
- 安装中的一些常见问题，可以参考倪露同学写的笔记：[How to create a Stata code cell_by NiLu](How-to-create-a-Stata-code-cell_by-NiLu.md)

### Stata 相关

#### 1. 我没有 `profile.do` 文档，怎么办？

初次安装 Stata 时，在 Stata 安装目录下并不存在 `profile.do` 文件。你可以在 Stata 安装目录下手动创建一个 `profile.do` 文件，重启 Stata 时它就会生效。

详情参见：[profile 文档：启动时自动执行的命令](https://book.lianxh.cn/stata101/body/B2b-profile%E6%96%87%E6%A1%A3.html)

#### 2. Stata 安装路径，PERSONAL 文件夹在哪里？

使用 `sysdir` 命令可以查看 Stata 安装路径和系统路径：

```stata
. sysdir

   STATA:  D:\stata17\            // 安装路径
    BASE:  D:\stata17\ado\base\
    SITE:  D:\stata17\ado\site\
    PLUS:  D:/stata/plus\         // 外部命令   
PERSONAL:  D:/stata/personal\     // 个人文件夹
```

注意：除了 **STATA** 和 **BASE** 目录外，其他目录均可以在 [profile.do 文档](https://book.lianxh.cn/stata101/body/B2b-profile%E6%96%87%E6%A1%A3.html) 中，通过 `sysdir set` 命令进行修改。

#### 3. Stata 的帮助文档在哪里？

- 文字版帮助文件：`help command_name`，如 `help regress`
- PDF 版帮助文件：`ihelp xtreg` (需要预先使用 `ssc install ihelp` 命令安装 `ihelp` 命令)
- 模糊检索：`findit keyword`，如 `findit dynamic panel`
- Stata 手册：在 Stata 安装目录下的 **doc** 文件夹下。

#### 4. Stata 的在线资源有哪些？

- 顾小龙, 连玉君, 2020, [Stata帮助和网络资源汇总](https://www.lianxh.cn/details/187.html)
- 游万海, 连玉君, 2019, [Stata: 外部命令的搜索、安装与使用](https://www.lianxh.cn/details/1.html)
- 连享会, 2020, [连享会：论文重现复现网站大全](https://www.lianxh.cn/details/232.html)  