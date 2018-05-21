# coding=utf-8
# str截取
str = 'abcdefg'

print("截取部分：" + str[2:5])
print("截取到最后字符：" + str[2:])
print("字符倒序：" + str[::-1])

# 数组[列表]
arrs = ['aa', 'bb', 'cc', 11, 22]
print(arrs)

# 添加
arrs.append(33)
arrs.insert(0, 44)
print(arrs)

# 合并
arrs_2 = ['hh', 55]
arrs.extend(arrs_2)
print(arrs)

# 删除
arrs.pop()  # 删除最后一个
arrs.remove("hh");  # 删除指定内容
del arrs[0]  # 删除指定下标
print(arrs)

# 修改
arrs[0] = 'ssdd'

# 判断是否存在
if 'ssdd' in arrs:
    print(arrs)

# 对象[字典]
obj = {'key': 1234, 'num': 123, 'name': 'zhang'};
print(obj.get('key'))
del obj['key']

# 遍历
for a, b in obj.items():
    print(a)
    print(b)
    print('=' * 10)

# valus/keys/items
val = obj.values()
key = obj.keys()
item = obj.items()

# 元组[列常量,定义后不能修改]
c_arrs = (11, 22, 44, 'ss')
