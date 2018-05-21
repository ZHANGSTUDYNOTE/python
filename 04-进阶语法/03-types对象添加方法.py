import types


class P1(object):
    def __init__(self):
        pass


# 实例方法
def eat(*args, **kwargs):
    print('吃吃，，，')


# 静态方法
@staticmethod
def test(*args, **kwargs):
    print('test')


# 类方法
@classmethod
def test1(*args, **kwargs):
    print('test1')


P1.eat = types.MethodType(eat, P1)
P1.test = test
P1.test1 = test1

P1.eat()
P1.test()
P1.test1()
