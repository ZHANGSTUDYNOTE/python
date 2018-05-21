# 队列
# from multiprocessing import Queue
#
# Process创建的进程才能用
# q1 = Queue()
# q1.put("11")
# q1.put("22")
# print(q1.get())
# print(q1.get())
# print(q1.empty())
# print(q1.full())

from multiprocessing import Manager

if __name__ == '__main__':

    # 所有进程间的通讯
    q2 = Manager().Queue()
    q2.put('111')
    print(q2.get())
