# 为你读诗 python播放最新音频
> 网页爬取、Python

本程序适用于MAC OS，LUNIX，windows用户可以下载音频文件，但无法播放。

本程序可直接在命令行运行，通过网页爬取获取最新一期的音频文件并自动播放。执行命令如下：

`python weinidushi.py`

若想播放最近第2个音频，执行命令如下：

`python weinidushi.py 2`

### 使用前请设置：
1. weinidushi.py第23行修改为 自己将要保存音频的本地地址。

`local="为你读诗/haha.mp3"`

2. Windows用户无法自动播放功能，可以是实现下载，weinidushi.py需将最后一行（第28行）删掉。

3. Mac,Lunix若实现自动播放，请先在终端安装sox
    
    **Mac**用户：

    `brew install osx`

   **Ubuntu** 的话 可以试试这个命令：

    `sudo apt-get install sox`
    
若依赖包出现问题，用户可自行下载 urllib3 和 lxml

`pip install urllib3`

`pip install lxml`

### 祝你使用愉快。



