# 写入文件
import os

f = open('fileTest.txt', 'w+')
f.write('text')
f.close()


# 读取文件
f1 = open('fileTest.txt', 'r+')
str = f1.read()
print(str)
f1.close()


# 定位文件位置（类似指针）
f2 = open('fileTest.txt', 'r+')
f2.seek(0, 2)
f2.close()


# 文件模块
os.rename('fileTest.txt', 'fileTest_re.txt')
os.remove('fileTest_re.txt')
os.mkdir('dirTest')
os.getcwd()

# 修改默认路径
os.chdir('../')

# 获取目录列表
os.listdir('./')





