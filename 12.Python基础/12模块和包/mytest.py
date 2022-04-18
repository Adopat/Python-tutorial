
# 模块和包：
# 1. 模块：就是一个单独python文件，里面存储一些相关的类，函数等。可以被外界调用
# 2. 包：是对一些模块的一个整合，里面必须要有一个__init__.py的文件才能称作为包，否则只能叫做文件夹。
# 3. 导入模块：from 模块名 import 对象
# 4. 从包导入模块：from 包名.模块名 import 对象
# 5. 如果某个python文件是作为主运行文件，那么__name__就会等于__main__。如果是作为被导入的方式执行的，那么__name__就会等于当前模块的名字。

from a import add
from mypackage.c import Person

# print(add(1,2))
p1 = Person(name="zhiliao",age=18)
print(p1.name)

print("mytest __name__:",__name__)