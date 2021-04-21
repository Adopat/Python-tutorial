# 介于0和1 之间的随机数
from random import *
print(random())
# 生成一个1-100 之间的随机数,随机整数
print("======1-100之间的随机数======")
from random import *
print(randint(1,100))
# 生成1-10之间的随机数
print("======1-10之间的随机数=====")
# random.uniform()--浮点数 和 random.randarange()--整数 区别
# randoom.randarang()可以产生跳跃的整数，而random.randint()只能产生范围的整数
from random import *
print(uniform(1,10))
print(randint(1,100)//10)
# 打乱列表
print("======打乱列表======")
from random import *
items = [1,2,3,4,5,6,7,8,9,10]
shuffle(items)
print(items)
# 从列表中选择一个随机数
print("======从列表中选择一个随机数======")
from random import *
items = [1,2,3,4,5,6,7,8,9,10]
x = sample(items,1) # 选择一个随机数
print(x[0])
y = sample(items,5) # 随机选择5个随机数
print(y)
# 使用字符串列表做同样的事情
from random import *
items = ['Alissa','Alice','Marco','Melissa','Sandra','Steve']
print("打乱前列表item=",items)
shuffle(items)
print("打乱后列表item=",items)
x = sample(items,1)
print(x[0])
y = sample(items,3)
print(y)