# -*- coding:utf-8 -*-

import requests

# 创建session对象
session = requests.session()

# data
data = {
    'username': '969253189@qq.com',
    'password': '123456a',
    'rememberLogin': 'true',
    'time': 1528394945590,
}

session.post('http://www.matchvs.com/zhangwan/login.json', data=data)

response = session.get('http://www.matchvs.com/data/get-news-trends-list.json', params={'title': ''})

print(response.text)
