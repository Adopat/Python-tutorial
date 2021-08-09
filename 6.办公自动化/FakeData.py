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


build_data('user.txt', 5000000)
