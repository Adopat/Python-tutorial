# 1./ 返回浮点数
print(8 / 5)  # 1.6
print(4 / 2)  # 2.0
# 2. // 得到整数部分
print(8 // 5)  # 1
# 3. % 得到余数
print(8 % 3)  # 2
# 4.计算乘方
print(5 ** 2)  # 25
print(4 ** 0.5)  # 2.0
# 5. 交互模式下的_ ,上一次打印出来的表达式赋值给变量_
# 6. 十转二
print(bin(1))  # 0b1
# 7.十转八
print(oct(10))  # 0o12
# 8. 十转十六
print(hex(15))  # 0xf
# 9.转为浮点类型 float
print(float(3))  # 3.0
# 10.转为整型,int(x,base) base 代表的是X 的进制,int()返回的都是十进制
print(int('10', base=2))  # 2
print(int('0xf', base=16))  # 15  16进制 oxf,返回十进制的15
# 11.商和余数
print(divmod(10, 3))  # (3, 1)
# 12.幂和余同时做
print(pow(3, 2, 4))  # 1 (3**2)%4
# 13. 四舍五入
print(round(5 / 3))  # 2
# 14. 计算表达式 eval()
print(eval("1+2+3"))  # 6
# 15. 真假 None [] 0 False 都为假值
print(bool(0))  # False
print(bool([]))  # False
print(bool([0]))  # True
print(bool(None))  # False
print(bool(False))  # False
print(bool([False]))  # True
print(bool([0, 0, 0, 0]))  # True
# 16. all 判断元素是否都为真 所有元素都为真返回True
print('=================')
print(all([1, 2, 3, 4, 5, 0]))  # False 存在0
print(all([1, 2, 3, 4, 5]))  # True
# 17. any 至少有一个元素为真则返回真,全部为假则返回假
print(any([1, 2, 3, 4, 5, 0]))  # True
print(any([0, 0, None, [], False]))  # False
# 18. 链式比较
print(3 < 5 < 9)  # True
# 19.元素交换 元组解包
a, b = 1, 3
a, b = b, a
print(f'a = {a},b= {b}')  # a = 3,b= 1
# 20. 链式操作
from operator import (add, sub)


def add_or_sub(a, b, oper):
    return (add if oper == '+' else sub)(a, b)


print(add_or_sub(1, 2, "+"))  # 3
