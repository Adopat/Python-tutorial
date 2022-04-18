text = " Hello Zhiliao hello world hello python "

# 1. find方法
# result = text.find("hello")
# print(result)

# 2. index方法：
# result = text.index("ellx")
# print(result)

# 3. len函数：
# result = len(text)
# print(result)

# 4. count方法：
# result = text.count("hello")
# print(result)

# 5. replace方法：不会替换原来的字符串，只会把替换后的字符串重新返回一份新的回来
# new_text = text.replace("hello","hahaha")
# print(new_text)
# print(text)

# 6. split方法：
# result = text.split(" ")
# print(result)

# 7. startswith：
# result = text.startswith("hello1")
# print(result)

# 8. endswith方法：
# result = text.endswith("python1")
# print(result)

# 9. lower方法：也不会影响原来字符串
# result = text.lower()
# print(result)
# print(text)

# 10. uppper方法：也不会影响原来的字符串
# result = text.upper()
# print(result)
# print(text)

# 11. strip方法：
# result = text.strip()
# print(result)
# print(text)

# 12. partition方法：
# text = "texthelloxxx"
# result = text.partition("hello")
# print(result)

# 13. isalnum方法：
# text = "hello1"
# result = text.isalnum()
# print(result)

# 14. isalph方法：
# text = "heeee"
# result = text.isalpha()
# print(result)

# 15. isdigit方法：
# text = "1232232q"
# result = text.isdigit()
# print(result)

# 16. isspace方法：\n也是属于空白的字符
text = "        \n"
print(text)
result = text.isspace()
print(result)







