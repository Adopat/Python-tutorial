import sys
import threading
from queue import Queue


q = Queue()


def sum_number(a,b):
    q.put(a+b)



def mod_number(a,b):
    q.put(a/b)


if __name__ == '__main__':
    result = []
    t1 = threading.Thread(target=sum_number, name='thread1', args=[10,2])
    t2 = threading.Thread(target=mod_number, name='thread2', args=[10,2])
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    while not q.empty():
        result.append(q.get())
    for item in result:
        print(item)


    # print(result)
    # for item in result:
    #     if item[1] == sum_number.__name__:
    #         # print("%s 's return value is : %s" % (item[1], item[0]))
    #         print(item)
    #     elif item[1] == mod_number.__name__:
    #         # print("%s 's return value is : %s" % (item[1], item[0]))
    #         print(item)
