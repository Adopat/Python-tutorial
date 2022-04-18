import json

books = [{
    'title': '钢铁是怎样练成的',
    'price': 9.8
  },{
    'title': '红楼梦',
    'price': 9.9
}]

# 1. json.dumps：python对象（列表、字典）转换成json格式的字符串
# 2. json.loads：json格式的字符串转换成python对象（列表、字典）
# 3. json.load：是从文件中读取json格式字符串，然后转换成python对象（列表、字典）
# 4. json.dump：直接将python对象转换成json格式，并存储到文件中

# print(type(books))
# json_str = json.dumps(books,ensure_ascii=False)
# print(json_str)
# print(type(json_str))

# obj = json.loads(json_str)
# print(obj)
# print(type(obj))

# with open("book.json","r",encoding='utf-8') as fp:
#     result = json.load(fp)
#     print(result)
#     print(type(result))

with open("book1.json","w",encoding='utf-8') as fp:
    json.dump(books,fp,ensure_ascii=False)