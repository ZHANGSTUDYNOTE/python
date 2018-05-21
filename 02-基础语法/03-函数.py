def test(a, b=1, c=2):
    print(a + b + c)


# 命名参数
test(1, c=22)


# 不定参数
def test1(a, b=1, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


test1(11, 22, 33, aa=11, bb=22)

# 匿名函数
func = lambda a, b: a + b

result = func(11, 22)

# 变量的交换方式
a = 4
b = 5

a = a + b
b = a - b
a = a - b
print(a, b)
