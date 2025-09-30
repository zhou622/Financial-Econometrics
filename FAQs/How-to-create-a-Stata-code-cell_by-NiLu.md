# Stata代码单元格如何建立
> 作者：倪璐  

> 补充连老师给的教程，给出一些容易坑人的小细节的提醒
# 前情提要：
请安装Anaconda和VScode，详细安装流程请参考：
## 1. 安装Anaconda：
https://lianxhcn.github.io/research_with_AI/body/01_install_Python_Anaconda.html#%E5%AE%89%E8%A3%85-anaconda
## 2. 安装VScode：
https://lianxhcn.github.io/research_with_AI/body/01_install_Python_Anaconda.html#%E5%AE%89%E8%A3%85-vscode-%E5%8F%8A%E6%8F%92%E4%BB%B6  

# 第一步：安装Stata17
1. 请务必安装老师给出的正版软件！！！
2. 请务必记住，请尽量安装在D盘，路径建议和我的一摸一样：D:\Stata17

# 第二步：安装nbstata
## 1. 在插件市场安装 Python 和 Jupyter 插件
以下是我安装的相关插件：
> 不是每个都有必要，自己判断，我只能保证像我这样安装后续一定不会有麻烦  
>
![插件1](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250930082311.png)
![插件2](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250930082455.png)
![插件3](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250930082530.png)
![插件4](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250930082553.png)
## 2. 确保可以在 VS Code 中新建 .ipynb 文件并执行代码块中的 Python 代码
- 如果运行python代码总是报错，又找不到原因，建议淘宝搜索“Anoconda和VScode技术指导python环境配置”，几块钱搞定，建议不要死磕。
- 最简单的测试方式：
  ` print("hello world") `
![python检测](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250930083709.png)
## 打开VScode的终端
- 点击下面红框里面的三个点
![1.1](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250930085847.png)
- 点击“终端”——“新建终端”
![1.2](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250930091346.png)
- 然后成功打开终端
## 4. 依次执行以下命令
- 在下面红框那里，冒号的下面，先输入：
` pip install nbstata `
![2.1](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250930090121.png)
- 请务必等他运行完了，出现下图显示的情况，再输入下一行命令
![2.2](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250930091429.png) 
- 上一行命令执行完了，再输入下一行命令，如下：
` python -m nbstata.install --conf-file `
![2.3](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250930091451.png)
- 最后会出现类似于以下的显示：  
` C:\Users\EZ-Control\.config\nbstata\nbstata.conf `
## 5. 处理路径给出的文件nbstata.conf
- 顺着给出的路径找到文件nbstata.conf
  以我的路径为例：
> C盘  

![3.1](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250930090458.png)  

> 文件夹 Users  

![3.2](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250930090534.png)  

> 文件夹 EZ-Control  

![3.3](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250930090710.png)  

> 文件夹 .config

![3.4](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250930090851.png)

> 文件夹 nbstata

![3.5](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250930091014.png)  

> 文件 nbstata.conf

![3.6](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250930091104.png)  

- 使用VScode打开nbstata.conf
  右击nbstata.conf——选择使用app打开——选择VScode打开
![4.1](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250930091532.png)  
- 使用VScode打开nbstata.conf后出现以下页面
  每个人情况不一样
![5.1](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250930091626.png)  
- 打开刚刚安装的stata17，输入命令：sysdir
  然后复制STATA后面的路径，把它粘贴到VScode里面的stata_dir后面
![6.1](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250930091747.png)  
![6.2](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250930091818.png)  
- 打开刚刚安装的stata17的文件夹，查看下图位置，显示的是StataMP-64.exe，然后把VScode里面的edition改成mp，如下所示：
![7.1](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250930091913.png)  
![7.2](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250930091948.png)  
- 剩下的所有参数和我写成一样的。
  注意注意，是需要修改的，请修改成和我一样的。  
- 保存文档，点击以下图片红圈部分：
![8.1](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250930092130.png)  
## 6. 开始测试上面的操作是否成功  
- 打开或新建一个 .ipynb 文件（文件后缀设置成 .npynb）
![9.1](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250930092410.png)  
- 点击 + 代码 按钮，创建一个新的代码单元格  
![9.2](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250930092617.png)
- 按照下图操作，指定 内核 为 Stata (nbstata)
  【第一次操作的界面显示和我的不一样，总之按照我说的来做就行】
    - 首先，点击下面红框位置
![9.3](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250930092717.png)  
    - 然后，点击“选择其他内核”  
![9.4](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250930092841.png)  
    - 接着，点击“Jupyter Kenel”  
![9.5](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250930092933.png)  
    - 最后，点击“Stata（nbstata）”  
![9.6](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250930093017.png)  
- 按照下图操作，建立stata代码单元块  
  【一开始框的右下角不会显示Stata的，要按照我的来设置，我会显示是因为我已经设置了】
    - 首先，点击下面红框位置
![10.1](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250930093156.png)
    - 选择“stata”，然后框的右下角就会显示“Stata”  
![10.1](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250930093156.png)  
    - 在框里面输入：
    ` help reg `
    - 如果没有报错，再输入：
    ` display 2 + 2 `
    - 如果显示结果是4，那么——
# 恭喜你！完成Stata代码单元块的设置！！！






