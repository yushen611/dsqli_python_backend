from sqliDetector import *
from bottle import request, response ,Bottle
# import subprocess
import json

# # 要安装的依赖包名称，可以以列表形式传递多个包
# required_packages = ['libinjection-python']

# def install():
#     # 执行 pip install 命令来安装依赖
#     for package in required_packages:
#         subprocess.check_call(['pip', 'install', package])

app = Bottle()

@app.route('/ping')
def ping():
    return 'Hello, this is python server'

@app.post('/SQLiTest/lib')
def sqli_test():
    try:
        # 获取 POST 请求的 JSON 参数
        data = request.json
        query = data.get('query',"Error:you have a wrong query json!")
        # 处理数据
        result = isSQLiAnalyzer(query)
        # 返回 JSON 格式的数据
        response.content_type = 'application/json'
        result['code'] = 200
        return json.dumps(result)
    except Exception as e:
        result = isSQLiAnalyzer("Server Error")
        result['code'] = 500
        return json.dumps(result)
        


if __name__=="__main__":
    # install()
    app.run(host='0.0.0.0', port=8001)



