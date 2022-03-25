import threading


def thread_job():
    print("This is a thread of %s" % threading.current_thread())


def main():
    # 创建一个线程
    thread = threading.Thread(target=thread_job, )
    # 启动线程
    thread.start()
    



if __name__ == '__main__':
    main()
