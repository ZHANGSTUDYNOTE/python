# -*- coding:utf-8 -*-

import requests

response = requests.get('http://www.baidu.com')

cookies = requests.utils.dict_from_cookiejar(response.cookies)

print(cookies)