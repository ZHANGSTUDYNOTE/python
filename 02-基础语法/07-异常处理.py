# 系统异常
try:
    print(num)
except (NameError, FileNotFoundError) as err:
    print("已知异常。。。")
    print(err)
    # raise # 重新抛出异常
except Exception as err:
    print('其它异常。。。')
else:
    print("没有异常。。。")
finally:
    print("---finally---")


# 自定义异常
class TestErr(Exception):
    def __init__(self, len, text):
        self.len = len
        self.text = text


try:
    raise TestErr(5, '自定义异常')
except TestErr as err:
    print(err.text)
    print(err.len)