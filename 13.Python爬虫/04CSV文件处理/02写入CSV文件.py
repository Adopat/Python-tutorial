import csv

# 1. csv.writer的方法写入csv文件
# headers = ['name','age','classroom']
# values = [
#   ["张三",18,"python1"],
#   ["李四",21,"python2"],
#   ["王五",17,"python3"]
# ]
#
# with open("students.csv","w",encoding='utf-8',newline="") as fp:
#   writer = csv.writer(fp)
#   writer.writerow(headers)
#   writer.writerows(values)


# 2. 用csv.DictWriter方法写入csv文件
rows = [
  {"name":'wenn',"age":20,"classroom":'222'},
  {"name":'abc',"age":30,"classroom":'333'}
]
headers = rows[0].keys()
with open("students.csv","w",encoding='utf-8',newline="") as fp:
  writer = csv.DictWriter(fp,headers)
  # 手动写入一些列名
  writer.writeheader()
  writer.writerows(rows)
