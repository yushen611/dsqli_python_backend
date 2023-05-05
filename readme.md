# Uage
## 导出项目依赖(不推荐，建议手写依赖)

```bash
pip install pipreqs
pipreqs ./ --encoding=utf8 --force
```

## 构建镜像

```bash
docker build -t sqli-detector-python:latest .
```

## 运行镜像

```bash
docker run --rm -d -p 8001:8001 --name sqli-detector-python sqli-detector-python:latest
```

# 错误解决

## error: socket hang up
连接不上端口
https://stackoverflow.com/questions/64218171/getting-a-socket-hang-up-error-when-trying-to-access-my-flask-app-in-a-docker-co

## 127.0.0.1 与  0.0.0.0 的区别  

https://zhuanlan.zhihu.com/p/72988255  

0.0.0.0 配docker的时候很有用

127.0.0.1 是一个环回地址。并不表示“本机”。0.0.0.0才是真正表示“本网络中的本机”


