import threading
import time

# 线程可以共享全局变量（可能会有数据不同步或数据错误）
g_num = 100

def test1():
    global g_num
    for i in range(30000000):
        g_num += 1

    print("test1-g_num=%d" % g_num)


def test2():
    global g_num
    for i in range(300000000):
        g_num += 1
    print("test2-g_num=%d" % g_num)


print("create g_num is %d" % g_num)

t1 = threading.Thread(target=test1)
t1.start()

# 延时，保证t1已执行完成
# time.sleep(1)

t2 = threading.Thread(target=test2)
t2.start()


