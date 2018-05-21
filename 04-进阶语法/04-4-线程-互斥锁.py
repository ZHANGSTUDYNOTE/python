import threading
import time

# 线程可以共享全局变量
g_num = 100


def test1():
    global g_num
    # mutex.acquire()  # 开启互斥锁,可传入超时时间
    for i in range(1000000):
        mutex.acquire()
        g_num += 1
        mutex.release()  # 释放互斥锁
    print("test1-g_num=%d" % g_num)


def test2():
    global g_num
    # mutex.acquire()
    for i in range(1000000):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("test2-g_num=%d" % g_num)


print("create g_num is %d" % g_num)

# 创建一个互斥锁
mutex = threading.Lock()

t1 = threading.Thread(target=test1)
t1.start()

t2 = threading.Thread(target=test2)
t2.start()
