# -*- coding:utf-8 -*-

import requests

# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}

# get参数
params = {'test': 'qq'}

# post参数
data = {'test': 'ww'}

# 根据参数的不同选择不同的代理
proxies = {
    "http": "114.215.95.188:3128",
    "https": "http://12.34.56.79:9527",
}

# 如果代理需要使用HTTP Basic Auth，可以使用下面这种格式：
proxy = {"http": "mr_mao_hacker:sffqry9r@61.158.163.130:16816"}

# web客户端验证
auth=('test', '123456')

# 发送请求
response1 = requests.get('http://www.baidu.com', proxies=proxies)

# 返回二进制，用于保存文件
# response.content

# 文本信息
print(response1.text.encode('utf-8'))
file = open('./test.html', 'wb')
file.write(response1.text.encode('ISO-8859-1'))

print(response1.encoding)
