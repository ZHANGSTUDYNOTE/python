import urllib.request

# 错误处理

# URLError
# URLError 产生的原因主要有：
#
# 没有网络连接
# 服务器连接失败
# 找不到指定的服务器


# HTTPError
# 注意，urllib2可以为我们处理重定向的页面（也就是3开头的响应码），100-299范围的号码表示成功，所以我们只能看到400-599的错误号码。

requset = urllib.request.Request('http://www.ffggyy.com')

try:
    response = urllib.request.urlopen(requset)
except urllib.request.HTTPError as err:
    print(err.code)
except urllib.request.URLError as err:
    print(err)
else:
    print('Good Job')
