# 对外引出
__all__ = ["Test1"]


class Test1(object):
    pass


# 包/__init__.py 【py2/py3通用】
# __init__ = ["文件名"]
# import . from "test"


# 系统模块 【接收系统参数】
import sys

print(sys.argv)
