import threading
from queue import Queue
import copy
import time


# python 多线程只适合两个完全不相关的事务，如果对于同一批数据的处理建议使用多进程
def job(l, q):
    res = sum(l)
    q.put(res)


def multithreading(l):
    q = Queue()
    threads = []
    for i in range(4):
        t = threading.Thread(target=job, args=(copy.copy(l), q), name='T%i' % i)
        t.start()
        threads.append(t)
    [t.join() for t in threads]
    total = 0
    for _ in range(4):
        total += q.get()
    print(total)


def normal(l):
    total = sum(l)
    print(total)


if __name__ == '__main__':
    l = list(range(10000000))
    s_t = time.time()
    normal(l * 4)
    print('normal: ', time.time() - s_t)
    s_t = time.time()
    multithreading(l)
    print('multithreading: ', time.time() - s_t)
