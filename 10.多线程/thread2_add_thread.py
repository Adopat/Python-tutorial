import threading


def main():
    print('当前激活线程数量:', threading.activeCount())
    print('当前线程列表:', threading.enumerate())
    print('当前线程', threading.current_thread())


if __name__ == '__main__':
    main()
