import copy

a = [11, 22, 'aa']
b = a  # 浅拷贝

c = copy.deepcopy(a)  # 深拷贝
print(id(a))
print(id(b))
print(id(c))

# copy.copy()         # 自动判断是否是可变类型，如：元组 是浅拷贝|可变类型是深拷贝

print(locals())
globals()
