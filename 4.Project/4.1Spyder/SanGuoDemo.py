# # 爬取三国演义，并用词云图展示关键信息
# import requests
# from fake_useragent import UserAgent
# from requests.exceptions import RequestException
# from bs4 import BeautifulSoup
# from time import sleep
# import random
# def get_one_page(url):
#     """
#     获取网页html内容并返回
#     :param url: 目标网址
#     :return html
#     """
#     headers = {"User-Agent": UserAgent(verify_ssl=False).random
#                }
#     try:
#         # 获取网页内容，返回html格式数据
#         response = requests.get(url, headers=headers,timeout=100)
#         # 通过状态码判断是否获取成功
#         if response.status_code == 200:
#             # 指定编码，否则中文出现乱码
#             response.encoding = 'utf-8'
#             return response.text
#         return None
#     except RequestException as e:
#         return None
# base_url = 'http://www.shicimingju.com/book/sanguoyanyi.html'
# # 获取所有目录链接
# def parse_result(content):
#     soup = BeautifulSoup(content,'lxml')
#     menu_list = soup.find('div',class_='book-mulu').find('ul').find_all('li')
#     new_menu_list = []
#     for menu_l in menu_list:
#         menu_dic = {}
#         menu_dic['title'] = menu_l.find('a').string
#         menu_dic['url'] = 'http://www.shicimingju.com'+menu_l.find('a').get('href')
#         new_menu_list.append(menu_dic)
#     return new_menu_list
# content = get_one_page(base_url)
# # print(content)
# # new_memu_list = parse_result(content)
# # print(new_memu_list)
# # for i in new_memu_list:
# #     content = get_one_page(i['url'])
# #     soup = BeautifulSoup(content,'lxml')
# #     content_list = soup.find('div',class_='card bookmark-list')
# #     print(content_list)
#
# response = requests.get(base_url)
# print(response.status_code)


import requests
from bs4 import BeautifulSoup

'''
    解析流程:
        1.pip install bs4
        2.导包:from bs4 import BeautifulSoup
        3.实例化一个BeautifulSoup对象(将页面源码数据加载到该对象中)
        4.调用BeautifulSoup对象中的相关属性和方法进行标签的定位
'''

url='http://www.shicimingju.com/book/sanguoyanyi.html'

headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.20 Safari/537.36'
}

page_data=requests.get(url=url,headers=headers).text

#实例化一个BeautifulSoup对象
soup=BeautifulSoup(page_data,'lxml')
li_list=soup.select('."book-mulu" > ul > li')

fp=open('三国演义.txt','w',encoding='utf8')

for li in li_list:
    url='http://www.shicimingju.com'+li.a['href']
    section_page_data=requests.get(url=url,headers=headers).text

    soup=BeautifulSoup(section_page_data,'lxml')
    section_title=soup.select('.www-main-container > h1')[0].string
    section_content=soup.find('div',class_="chapter_content").text
    fp.write(section_title+'\n'+section_content+'\n\n')
    print(section_title+'\t'+'下载完成')
fp.close()