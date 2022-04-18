
# 1. str => bytes：encode
# 除非是一些特殊情况，否则我们编码都用utf-8的形式进行编码，因为utf-8能保存全球所有的国家的字符
# text = "hello world"
# print(text,type(text))
# b_text = text.encode("utf-8")
# print(b_text,type(b_text))


# 2. bytes => str：decode
# 我们怎么定义一个bytes字符串：只要在引号前面加上一个b就可以
text = b"hello world"
print(text,type(text))
s_text = text.decode("utf-8")
print(s_text,type(s_text))