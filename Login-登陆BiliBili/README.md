# 带带大师兄使用问题

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
