# 1.求绝对值
print(abs(-10))
# 2.进制转化 bin() 10进制转二进制 oct() 10进制转8进制 hex() 10进制转16进制
print(bin(10))#0b1010
print(oct(10))#0o12
print(hex(15))#0xf
# # 3.整数和ASCII互转
print(chr(65)) # A
print(ord('A')) # 65
print(ord('a')) # 97
print(ord('Z')) # 90
print(ord('z')) #122
print(ord('0')) #48
print(ord('9')) #57
# # 4.元素都为真检查 all()元素都为真检查
print(all([1,0,1,2,3])) # False 0为假
print(all(['',1,2,3,4,5])) # False '' 为假
print(all([None,1,2,3,4,5])) #False
# # 5.元素至少一个为真检查 any() 至少一个为真检查
print(any([1,2,3,40,0,0])) #True
# # 6.判断真假 bool()
print(bool(True)) # True
print(bool(0)) # False
print(bool(1)) # True
print(bool(None)) # False
print(bool("")) # False
# # 7.创建复数 complex()
print(complex(1,2)) #(1+2j)
# # 8.取商和余数 divmod()
print(divmod(10,3)) # (3,1)
# # 9.转为浮点数类型 float()
print(float(3.2)) #3.2
# # 10.转为整型 int(x,base=10) base=10 代表的是x为10进制 base=10为默认
print(int('12',16)) #16进制的12 转为10进制为 18
print(int('101010',2)) # 2进制101010转为10进制为 42
print("=====int发生截断=====")
print(int(3.1))
print(int(0.5))
print(int(3.5))
print(int(3.6))
# # 11.次幂 pow(x,y[,z]) 等效于 pow(x,y)%z
print(pow(3,2,4)) #1
# # 12.四舍五入
from decimal import Decimal
print(round(3.15,1)) #3.1 不是标准3.2
print(Decimal(3.15)) # 3.149999999999999911182158029987476766109466552734375 可以看到3.15 在计算机中存储精度丢失所以导致 四舍五入结果不对
print(Decimal('3.15'))
# 如何才能实现四舍五入的效果，四舍五入是针对十进制的
import decimal
# 修改舍入方式为四舍五入
decimal.getcontext().rounding="ROUND_HALF_UP"
# 使用字符串来存储小数不会有精度误差
print(decimal.Decimal('1.535').quantize(decimal.Decimal('0.00'))) # 保留两位小数
# https://blog.csdn.net/xun527/article/details/103032589?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_title~default-0.pc_relevant_baidujshouduan&spm=1001.2101.3001.4242
# 13.链式比较 python 可以进行链式比较，这是Python和其他语言的一个小区别
print(1<2<3)# True
# 14.Python 中的除法
print(3/2)# 正常除法
print(3//2) # 整除 1
print(3%2) # 求模 1
print(3/2.0) # 1.5 在其他语言比如Java中要得到浮点数 一般采用这种写法