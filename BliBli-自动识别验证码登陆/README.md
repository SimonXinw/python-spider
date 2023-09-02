# 1. 带带大师兄使用问题

module 'PIL.Image' has no attribute 'ANTIALIAS' 问题处理

最近在使用 ddddocr 进行图片识别时，报错了：

AttributeError: module 'PIL.Image' has no attribute 'ANTIALIAS'

查看一下 pillow 的版本：10.0.0

通过在 pillow 官方网站，release notes 中找到了问题：

请点击输入
原来是在 pillow 的 10.0.0 版本中，ANTIALIAS 方法被删除了，改为 10.0 版本许可的参数即可。

解决办法：（推荐方案二）

方案一，修改 ddddocr 的*init*.py 文件，将其中的 ANTIALIAS 替换为新方法：

# image = image.resize((int(image.size[0] \* (64 / image.size[1])), 64), Image.ANTIALIAS).convert('L')

image = image.resize((int(image.size[0] \* (64 / image.size[1])), 64), Image.LANCZOS).convert('L')

方案二，降级 Pillow 的版本，比如使用 9.5.0 版本

先卸载，再重新安装

pip uninstall -y Pillowpip install Pillow==9.5.0
两种方案都亲测可用

# 2. 超级鹰

进入官网查看你想要的验证码类型
https://www.chaojiying.com/api-5.html

进入我的个人中心 - 软件 id - 生成软件 id

就可以开始尝试调用超级鹰的方法去请求验证码了

# 3.模拟 b 站 按顺序点击验证码，这是处理好的验证码的数据结构

code [{'text': '音', 'x': '97', 'y': '229'}, {'text': '清', 'x': '114', 'y': '143'}, {'text': '茶', 'x': '177', 'y': '127'}] order [{'text': '清', 'x': '13', 'y': '27'}, {'text': '音', 'x': '40', 'y': '19'}, {'text': '茶', 'x': '67', 'y': '21'}]
