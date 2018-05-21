import sys


class Test:
    # 类属性
    num = 0

    # 类方法
    @classmethod
    def add_num(cls):
        cls.num += 1

    # 初始化对象
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "name=%s,age=%d" % (self.name, self.age)

    def __del__(self):
        print("对象销毁之前。。。")

    # 私有方法
    @staticmethod
    def __testSend():
        print("执行私有方法。。。")

    # 方法
    def showName(self):
        print("name=%s" % self.name)
        self.__testSend()

    def showAge(self):
        print("age%d" % self.age)


tom = Test("TOM", 20)
tom.showName()
tom.showAge()
print(tom)

# 测量对象引用个数（比实际个数多1）
fcount = sys.getrefcount(tom)
print(fcount)


# 继承
class Test1(Test):
    def showFn(self):
        print("子类特有方法。。。")

    def showAge(self):
        print("重写父类方法。。。")

        # 调用父类被重写的方法
        super().showAge()


tom1 = Test1("tom1", 18)
tom1.showFn()
tom1.showAge()


# 多继承
class Test2(object):
    def show1(self):
        print('--------------test2')


class Test3(object):
    def show2(self):
        print('--------------test3')


class Test4(Test2, Test3):
    def show3(self):
        print('--------------test4')
