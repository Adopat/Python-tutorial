## 利用Python 制造测试数据
import os
from datetime import datetime


def build_data(file_path, data_count):
    if os.path.exists(file_path):
        os.remove(file_path)

    file = open(file_path, 'w')
    start = datetime.now()
    print('数据生成中')
    for var in range(data_count):
        file.writelines(
            str(var) + " 用户" + str(var) + " email" + str(var) + "@email.com" + " " + "1592837482" + str(var))
        file.write('\n')
    end = datetime.now()
    print('耗时:' + str((end - start).seconds) + "s")

##build_data('user.txt', 5000000)

# 利用多线程 生成数据 https://blog.csdn.net/mathcoder23/article/details/103544929?spm=1001.2014.3001.5501


# 利用fake 快速生成数据 https://blog.csdn.net/Makasa/article/details/112319149?spm=1001.2014.3001.5501
