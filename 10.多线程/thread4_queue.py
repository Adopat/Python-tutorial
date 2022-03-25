import threading
import time
from queue import Queue


def job(l, q):
    for i in range(len(l)):
        l[i] = l[i] ** 2
    # 将返回值存入队列
    q.put(l)


def multithreading():
    q = Queue()
    threads = []
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    for i in range(4):
        t = threading.Thread(target=job, args=(data[i], q))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    result = []
    for _ in range(4):
        result.append(q.get())
    print(result)
    [].copy()


if __name__ == '__main__':
    multithreading()
