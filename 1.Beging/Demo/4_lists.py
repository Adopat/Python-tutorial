# [] 定义列表
print("=======定义列表======")
l = ["Drake","Derp","Derek","Dominique",1]
print(l)
print(l[0])# 'Drake'
print(l[-1]) # 1
# 列表添加删除
print("========列表添加删除======")
l = ["Drake","Derp","Derek","Dominique",1]
l.append("Victoria")
print(l)#['Drake', 'Derp', 'Derek', 'Dominique', 1, 'Victoria']
l.remove(1)
print(l)#['Drake', 'Derp', 'Derek', 'Dominique', 'Victoria']
l.remove("Victoria")
print(l)#['Drake', 'Derp', 'Derek', 'Dominique']
# 排序列表
print("=================列表排序==================")
l = ['Drake', 'Derp', 'Derek', 'Dominique']
l.sort()
print("排序后的列表是：",l)
# 列表降序 试用 reverse(0
print("======列表降序======")
l = ['a','c','b','d','g','f']
l.sort()
print("默认是升序：",l)
l.reverse()# 没有返回值
print('降序后的排序是',l)#