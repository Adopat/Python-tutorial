# 1.包和模块的定义 包是一个文件夹，它里面会有一个__init__.py 还有我们自己定义的.py文件
# 我们自己定义的.py文件称为模块
# 2. __init__.py的作用 __init__.py 会使得普通的文件夹变为package. 实际上， __init__.py 也是一个模
# 块，其名称正是package的名字。同时还可以为它增加其他功能。
# 因为在导入一个包时实际上导入它的__init__.py 文件，利用此特性，可以在__init__.py 文
# 件中批量导入多个模块都在公用的模块，而不再需要一个一个的导入。可以用来初始化
# 4.解决找不到模块的问题 sys.path 包查找路径
# 调整为根目录(调用dirname一次获得其所在文件夹)
# 就当前文件目录，我们两次便定位到根目录 classdemo
import os
import sys

'''
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# __file__获取执行文件相对路径，整行为取上一级的上一级目录
sys.path.append(BASE_DIR)
import animals
'''
