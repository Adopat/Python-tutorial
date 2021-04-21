# 局部变量
print("======局部变量======")
def sum(x,y):
    sum = x + y
    return sum
print(sum(4,6))
#print(x)# name 'x' is not defined
# 全局变量
print("======全局变量======")
z = 10
y = 11
def afunction():
    global z # 要在函数内部修改全局变量使用关键字global
    z =9
    y =9
afunction()
print(z)
print(y)
# 练习
print("======练习=====")
z = 10
def func1():
    global z
    z =3
def func2(x,y):
    global z
    return x+y+z
func1()
total = func2(4,5)
print(total)#12