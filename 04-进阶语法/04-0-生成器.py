# 1-列表生成器
b = (x * 2 for x in range(10))

print(next(b))
print(next(b))
print(next(b))
print(next(b))


# 2-yield生成器
def createNum():
    print('start')
    a, b = 0, 1
    for i in range(5):
        yield b
        a, b = b, a + b
    print('end')


a = createNum()
next(a)


# 3-send传入参数
def test1():
    i = 0
    while i < 5:
        temp = yield i
        print(temp, i)
        i += 1


t = test1()
t.__next__()
t.send('aaa')
