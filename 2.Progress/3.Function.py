# 1.排序函数 sorted(x,reverse=False) 默认为升序
a =[1,4,2,3,1]
print(sorted(a,reverse=True))
a = [{'name':'xiaoming','age':18,'gender':'male'},
     {'name':'xiaohong','age':28,'gender':'male'},
     {'name':'xiaolan','age':38,'gender':'male'},
     {'name':'xiaohuang','age':8,'gender':'male'},
     ]
print(sorted(a,key=lambda x:x['age'],reverse=False))
'''
[
{'name': 'xiaohuang', 'age': 8, 'gender': 'male'}, 
{'name': 'xiaoming', 'age': 18, 'gender': 'male'}, 
{'name': 'xiaohong', 'age': 28, 'gender': 'male'}, 
{'name': 'xiaolan', 'age': 38, 'gender': 'male'}
]
'''
print(a[0]['name']) # xiaoming
print(a[0]['age']) # 18
print(a[0]['gender']) # male
# 2.sorted 和 sort的区别 sort 是应用再list上的方法，属于列表的成员方法，sorted可以对所有可迭代的对象进行排序操作
# sort() 再原list进行操作，没有返回值,sorted 生成新的list
list1 =[1,2,3,4,5]
print("list1 的内存地址：",id(list1)) # list1 的内存地址： 2694902659776
print("sort：",list1.sort(reverse=True)) # None
print("sorted:",sorted(list1,reverse=True)) # sorted: [5, 4, 3, 2, 1]
print("sorted后的内存地址:",id(sorted(list1,reverse=True))) # sorted后的内存地址: 2215424654272

# 3.求和函数
sum1 = sum([1,2,3,4,5])
print(sum1) #15
print(sum([1,2,3,4,5],15)) # 30
print(sum([1,2,3,4,5],sum([1,2,3,4,5])))# 30

# 4.nonlocal,常用于函数嵌套中，声明变量为非局部变量，局部变量要初始化才可以进行引用，成员变量(属性)会自动有默认值
def outer():
    name ="Python"
    i =0
    def inner():
        # 声明i 不是函数内部变量
        nonlocal i
        i +=1
        #name += "Justin"
        print(i)
        #print(name)
    return inner()

# 5.global 声明全局变量
i = 0
def h():
    global i
    i+=1
    return i
print(h())
## global 和 nonlocal的区别 https://www.cnblogs.com/z360519549/p/5172020.html
# 6.交换两元素
def swap(a,b):
    return b,a
print(swap(1,2))
# 7.操作函数对象
def f1():
    print("hello !!")
def f2():
    print("world!!")
[f1,f2][1]() # world!!
[f1,f2][0]() # hello !!
# 8.生成正序逆序序列
print(list(range(1,10,1)))
print(list(range(1,10,2)))
print(list(range(10,1,-1)))
# 9.Python中函数的参数类型:位置参数，关键字参数，默认参数,可变位置关键字参数的使用
def f(a,*b,c=10,**d):
    print(f'a:{a},b:{b},c:{c},d:{d}')
f(1,2,5,c=10,width=10,height=100) # a:1,b:(2, 5),c:10,d:{'width': 10, 'height': 100} a 为位置参数,b 为可变位置参数,c为默认参数,d 为关键字参数

# 10 slice对象，将切片方法封装












