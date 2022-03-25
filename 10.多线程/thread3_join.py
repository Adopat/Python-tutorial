import threading
import time


def thread_job():
    print('T1 start')
    for i in range(10):
        time.sleep(1)
    print('T1 finish')


def T2_job():
    print('T2 start')
    print('T2 finish')


def main():
    t1thread = threading.Thread(target=thread_job, name='T1')
    t2thread = threading.Thread(target=T2_job, name='T2')
    t1thread.start()
    t2thread.start()
    # 将t1thread 加入到主线程
    t1thread.join()
    # 将 t2thread 加入到主线程
    t2thread.join()
    print('主线程完成')


if __name__ == '__main__':
    main()
