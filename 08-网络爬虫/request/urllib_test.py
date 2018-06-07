import urllib.request

url = 'http://www.baidu.com'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
}

# 基本使用方式
request1 = urllib.request.urlopen(url)
response1 = request1.read()

# 带data参数为post请求
request2 = urllib.request.Request(url, headers=header)
response2 = urllib.request.urlopen(request2).read()

# 普通代理
http_proxy_handler = urllib.request.ProxyHandler({'http': '114.215.95.188:3128'})
opener1 = urllib.request.build_opener(http_proxy_handler)
response3 = opener1.open(url)

print(response1)
print(response2)
print(response3.read())
print(response3.headers['content-type'])
# file = open('./bai.html', 'wb')
# file.write(response3)
# file.close()
