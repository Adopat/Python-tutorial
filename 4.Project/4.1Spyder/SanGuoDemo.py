#爬取三国演义，并用词云图展示关键信息
import requests
from fake_useragent import UserAgent
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from time import sleep
import random
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
# 获取所有目录链接
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
# new_memu_list = parse_result(content)

# for i in new_memu_list:
#     content = get_one_page(i['url'])
#     soup = BeautifulSoup(content,'lxml')
#     content_list = soup.find('div',class_='card bookmark-list')
#     with open('三国演义.txt','a',encoding='utf-8') as f:
#         f.write(i['title']+'\n'+content_list.text+'\n')
#     print(i['title']+'爬取完毕')
#     sleep(random.uniform(5, 10))
#将三国演义文件生成 词云看看主要内容是什么
# import jieba
# import collections
# # 加载停用词
# def stopwordslist(filepath):
#     stopwords = [line.strip() for line in open(filepath,'r',encoding='utf-8').readlines()]
#     return stopwords
# # 对句子进行分词
# def seg_sentence(sentence):
#     jieba.load_userdict("cidian1.txt") # 加载自定义字典
#     sentence_seged = jieba.cut(sentence.strip())
#     stopwords = stopwordslist(r'hit_stopwords.txt')
#     outstr = ""
#     for word in sentence_seged:
#         if word not in stopwords:
#             if word!='\t':
#                 outstr +=word
#                 outstr +=" "
#     return outstr
# with open(r'三国演义.txt','r',encoding='utf-8') as f:
#     for line in f:
#         lien_seg = seg_sentence(line.replace(' ','').replace('\u3000',''))
#         with open(r'三国演义切词.txt','a',encoding='utf-8') as fq:
#             fq.write(lien_seg)
# # 统计切词后的词频
# with open(r'三国演义切词.txt','r',encoding='utf-8') as f:
#     # data = jieba.cut(f.read().replace('...','').replace('\n','').replace(" ",'').replace('，','').replace('。','').replace('\xa0',''))
#     data = jieba.cut(f.read())
# data = dict(collections.Counter(data).most_common(10))
# print(data)
print('========将切词后的结果生成词云========')
import jieba,numpy
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import collections
with open('三国演义切词.txt','r',encoding='utf-8') as f:
    words = f.read()
new_words = ' '.join(jieba.cut(words))
word_counts  = collections.Counter(new_words) # 统计切词后，每个词出现的次数
print('前10词:',word_counts.most_common(15))
STOPWORDS.add('不')
STOPWORDS.add('人')
STOPWORDS.add('之')
STOPWORDS.add('一')
STOPWORDS.add('道')
STOPWORDS.add('子')
STOPWORDS.add('大')
STOPWORDS.add('王')
STOPWORDS.add('以')
STOPWORDS.add('上')
STOPWORDS.add('中')
STOPWORDS.add('十')
STOPWORDS.add('下')
STOPWORDS.add('来')
wordcloud = WordCloud(width=1000,
                      height=860,
                      margin=2,
                      background_color='#d4ff80',# 设置背景颜色
                      font_path=r'C:\Windows\Fonts\STSONG.TTF',
                      stopwords=STOPWORDS)
wordcloud.generate(new_words)
wordcloud.to_file('三国演义.jpg')
