FROM python:3.9

# 设置工作目录为 /app
WORKDIR /app

#复制源码
COPY . /app

#安装依赖
RUN pip install --no-cache-dir -r requirements.txt

#暴露端口
EXPOSE 8001

#启动时执行
CMD ["python","main.py"]