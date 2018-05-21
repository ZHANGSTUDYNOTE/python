a = [i for i in range(1, 18)]
print(a)

b = [i for i in range(1, 18) if i % 2 == 0]
print(b)

c = [(i, j) for i in range(5) for j in range(2)]
print(c)



# 列表去重 【set：集合】
d = [11, 22, 11, 55, 66, 11]
e = set(d)
d = list(e)
print(d)