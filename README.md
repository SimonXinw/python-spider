# 前提

免责声明: 这里是用 python 编写的只能用于个人学习的代码，不可用于违法犯罪，由于自己使用造成的一切后果，自己承担，本作者不承担一切连带责任！

# 介绍

这里是 python 编写的爬虫脚本，可以进行数据爬取、数据清洗、数据分析等，欢迎 Star、欢迎 fork、欢迎提问、欢迎沟通

有任何问题都可以加群互相学习

![Alt text](qrcode.png)

# 每个项目的同级都有对应的 README.md 文件，请到对应项目文件下查看，这里列出目录

## [1.git 上传下载太慢解决配置 hosts 文件](./IP-获取域名对应的IP/README.md)

## [2.boss 直聘抓取分析前端、测试、各编程语言岗位薪资](./Boss-爬取分析各编程语言岗位薪资/README.md)

## [3.excel 文件数据处理分析](./Excel-处理转化/README.md)

## [4.B 站自动识别验证码登陆](./BliBli-自动识别验证码登陆/README.md)

## [5.JD 爬取搜索结果页面的商品图片](./JD-搜索结果页图片/README.md)

# git 免输入用户名密码设置

如果 git push 提示输入用户名密码，先去 github 申请 token
PS:token 不可以放在仓库里面，github 会自动删除

然后设置 git 缓存

```bash
#默认缓存15分钟
git config --global credential.helper cache
#可以更改默认的密码缓存时限 3600 秒
git config --global credential.helper 'cache --timeout=3600'
```

再输入一次 用户名，下次就不用了
