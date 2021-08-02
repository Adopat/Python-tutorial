# 1.字符串转字节 bytes()
s = "apple"
print(bytes(s,encoding='utf-8'))# b'apple'
# 2.任意对象转字符串
print(str(100)) # 100
print(str(3.2)) # 3.2
print(str([])) # []
print(str(dict())) # {}
# 3.执行字符串表示的代码
s = "print('hello world')"
r = compile(s,"<string>","exec")
print(r) # <code object <module> at 0x00000276CDEAADF0, file "<string>", line 1>
exec(r) # hello world
# 4.计算表达式 eval()
print(eval("1+2+3")) # 6
# 5.字符串格式化 .format()
print("{0:30}".format("Python"))
print("{0:+.2f}".format(3.1415926)) # +3.14 {:+.2f} 带符号保留小数点后两位
print("{:.0f}".format(3.1415)) # 3 {:.0f} 不带小数
print("{:0>3d}".format(5)) # 005 {:0>3d} 数字左边补充0宽度为3
print("{:0<3d}".format(5)) # 500 {:0<3d} 数字右边补充0 宽度为3
print("{:a>3d}".format(5)) # aa5  {:x>3d} 数字左边补充x,宽度为3
print("{:,}".format(10000000)) # {:,}以逗号分割的数字格式
print("{:.2%}".format(0.251)) # 25.10% {:.2d%}百分比格式
print("{:2e}".format(100000000000000)) # 1.000000e+14 指数计数法
print("{:>10d}".format(18)) #        18 右对齐默认宽度为10
print("{:<10d}".format(18)) #18        左对齐默认宽度为10
print("{:^10d}".format(18)) #    18    居中对齐默认宽度为10



# 总结，字符串格式化的几种方法
a = "%s张飞、%s关羽、%s刘备、%s赵云" % (1,2,3,4)
print(a)
b = "{}张飞、{}关羽、{}刘备、{}赵云".format(1,2,3,4)
print(b)
c = f"{1}张飞、{2}关羽、{3}刘备、{4}赵云"
print(c)
# https://blog.csdn.net/weixin_41261833/article/details/108080963


