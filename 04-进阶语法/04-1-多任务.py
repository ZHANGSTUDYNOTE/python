# 1.进程（主进程结束，程序结束）
# import os
#
# ret = os.fork()
# print(ret)
# if ret > 0:
#     print("---父进程---%d" % os.getpid())
# else:
#     print("---子进程---%d---%d" % (os.getpid(), os.getpid()))

# 2进程-兼容模式
from multiprocessing import Process, Pool


# def test2():
#     print('1-开始执行')
#
#
# def test3():
#     print("2-开始执行")
#
#
# p1 = Process(target=test2)
# p2 = Process(target=test3)
#
# if __name__ == '__main__':
#     p1.start()
#     p2.start()
#
#     p1.join()  # 堵塞，等待所有子线程完成
#     p2.join()  # 堵塞，等待所有子线程完成


# 进程池Pool
def test4(num):
    for i in range(3):
        print("ddd%d" % num)


if __name__ == '__main__':
    print(11)
    po = Pool(3)  # 最大进程数量
    for num in range(3):
        # 向进程池添加任务
        # 注意：如果添加有任务大于 进程中的进程 那么不会导致添加不进去，等到前面的进程结束后 继续执行未执行的任务
        po.apply_async(test4, (num,))  # 非阻塞
        # po.apply(test4, (num,))  # 阻塞
    po.close()
    po.join()

# 子进程结束，父进程调用并把字进程返回值传到父进程调用的函数内
# po.apply_async(func=test,callback=test1)
