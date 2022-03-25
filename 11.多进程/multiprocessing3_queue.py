import multiprocessing as mp
import time


def job(q):
    res = 0
    for i in range(1000000):
        res += i + i ** 2 + i ** 3
    q.put(res)


def multiprocess():
    q = mp.Queue()
    process = []
    for i in range(2):
        p = mp.Process(target=job, args=(q,), name='P%i' % i)
        p.start()
        process.append(p)
    [pro.join() for pro in process]
    total = 0
    for _ in range(2):
        total += q.get()
    return total


def normal():
    res = 0
    for _ in range(2):
        for i in range(1000000):
            res += i + i ** 2 + i ** 3
    return res


if __name__ == '__main__':
    start_time = time.time()
    result = multiprocess()
    print('多进程结果为', result)
    print('多进程耗时为:', time.time() - start_time)
    normal_starttime = time.time()
    normal_result = normal()
    print('单进程结果为', normal_result)
    print('单进程耗时为:', time.time() - normal_starttime)
