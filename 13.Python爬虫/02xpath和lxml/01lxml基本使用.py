from lxml import etree

fp = open("test.html","r",encoding='utf-8')
html = fp.read()

parser = etree.HTML(html)

# 1. 获取网页中所有的li标签
# li_list = parser.xpath("//li")
# for li_tag in li_list:
#     print(etree.tostring(li_tag))


# 2. 获取网页中所有的li标签的class属性
# class_list = parser.xpath("//li/@class")
# print(class_list)

# 3. 获取元素下的文本内容
# xpath：不管获取到的内容有多少个，返回的都是一个列表

# a_tag = parser.xpath("//li[last()-1]/a")[0]
# print(a_tag.text)

text = parser.xpath("//li[last()-1]/a/text()")[0]
print(text)


fp.close()