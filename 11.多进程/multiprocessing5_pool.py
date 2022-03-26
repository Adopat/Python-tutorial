# 进程池


import multiprocessing as mp


def job(x):
    return x * x


def multicore():
    # 第一种方式,创建进程池,默认使用CPU的所有核
    pool = mp.Pool(processes=2)
    res = pool.map(job, range(10))
    print(res)
    # 第二种方式,apply_async 默认只能有一个参数
    res = pool.apply_async(job, (2,))
    print(res.get())
    # apply_async 要实现 Pool的效果
    multi_res = [pool.apply_async(job, (i,)) for i in range(10)]
    print([res.get() for res in multi_res])


if __name__ == '__main__':
    multicore()
