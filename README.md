# 每个项目的同级都有对应的 README.md 文件，请到对应项目文件下查看

github.com 的代理的 hosts 文件配置

这个直接使用 ip 获取域名对应的 ip 去配置 hosts 文件

#  git 的 配置
先去 github 申请 token 注意， token 不可以放在仓库里面，github 会自动删除

然后设置 git 缓存

```bash
#默认缓存15分钟
git config --global credential.helper cache
#可以更改默认的密码缓存时限 3600 秒
git config --global credential.helper 'cache --timeout=3600'
```
再输入一次 用户名，下次就不用了