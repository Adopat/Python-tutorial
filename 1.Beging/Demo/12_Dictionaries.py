# 创建字典
words = {}
words["Hello"] = "Bonjour"
words["Yes"] = "Oui"
words["No"] = "Non"
words["Bye"] = "Au Revoir"
print(words["Hello"])
print(words["No"])
# 字典的值可以是不同的
dict = {}
dict["Ford"] = "Car"
dict["Python"] = "The Python Programming Language"
dict[2] = "This sentence is store here"
print(dict['Ford'])
print(dict['Python'])
print(dict[2])
# 使用字典
print("======使用字典======")
print(words)
del words["Yes"]
print(words)
words["Yes"] = "Oui!"
print(words)
