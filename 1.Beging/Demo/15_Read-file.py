# 读取文件
import os.path
filename = "14_Random-numbers.py"
if not os.path.isfile(filename):
    print('File does not exist.')
else:
    with open(filename,encoding='utf-8') as f:
        content = f.read().splitlines()# 不读取换行符
        content = f.read() # 读一个字符换行
for line in content:
    print(line)