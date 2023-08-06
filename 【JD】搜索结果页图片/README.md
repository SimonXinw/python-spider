这里是使用 python 写的爬虫 1.可以 h 直接进行请求 2.可以进行 ui 测试点击交互

# 配置环境

## 安装 python 环境

安装 python3 https://www.python.org/

如果有 python2 那么执行命令的时候都要加上 3 ，比如 python3， pip3

## 安装包环境

安装依赖包

```bash
pip install -r requirements.txt
```

如果是自己开发的话，开发完毕了之后需要更新一下依赖包

```bash
# 安装
pip install pipreqs
# 在当前目录生成
pipreqs . --encoding=utf8 --force
```

就会自动生成对应的 requirements.txt 文件了

## 安装 selenium 环境

安装好需要的包之后，还需要配置对应的 chromedriver 环境，查找到自己 chrome 浏览器的版本之后，用这个网址下载 https://chromedriver.chromium.org/downloads

# 代码 Debugger ，可以使用 vscode 的左边的三角形爬虫用来调试代码，事半功倍
