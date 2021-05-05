#爬取唐人街探案影评 生成词云
import requests
from fake_useragent import UserAgent
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from time import sleep
import random
import parsel
def get_one_page(url):
    """
    获取网页html内容并返回
    :param url: 目标网址
    :return html
    """
    headers = {"User-Agent": UserAgent(verify_ssl=False).random,
               "Accept":'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
               'Host': 'movie.douban.com',
               'Referer': 'https: // movie.douban.com / subject / 26754233 / reviews?start = 140',
               }
    try:
        # 获取网页内容，返回html格式数据
        response = requests.get(url, headers=headers,timeout=100)
        # 通过状态码判断是否获取成功
        if response.status_code == 200:
            # 指定编码，否则中文出现乱码
            response.encoding = 'utf-8'
            return response.text
        return None
    except RequestException as e:
        return None

base_url = 'https://movie.douban.com/subject/27619748/reviews?start='


def parse_result(content):
    selector = parsel.Selector(content)
    data = selector.css('#content  .article .review-list .short-content::text').getall()
    for i in data:
        a = i.strip().replace('\n', '').replace(')', '').replace('(', '')
        with open('唐探3' + '.txt', mode='a', encoding='utf-8') as f:
            f.write(a)
            f.write('\n')
def main():
    for i in range(0,100):
        url = base_url + str(i*20)
        content = get_one_page(url)
        parse_result(content)
        sleep(random.uniform(1, 10))
        print(f'第{i+1}页爬取完成。。。')
#if __name__ == "__main__":
    #main()
print('=====根据爬取结果生成词云=====')
# 结巴分词使用停用词
import jieba,numpy
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import collections
with open('唐探3切词.txt','r',encoding='utf-8') as f:
    words = f.read()
new_words = ' '.join(jieba.cut(words))
word_counts  = collections.Counter(new_words) # 统计切词后，每个词出现的次数
print('前10词:',word_counts.most_common(15))
# 设置停用词，屏蔽不想展示的词
STOPWORDS.add('的')
STOPWORDS.add('我')
STOPWORDS.add('在')
STOPWORDS.add('了')
STOPWORDS.add('和')
STOPWORDS.add('就')
STOPWORDS.add('是')
alice_mask = numpy.array(Image.open('tangtan3.jpg'))
wordcloud = WordCloud(width=1000,
                      height=860,
                      margin=2,
                      mask=alice_mask,
                      background_color='#d4ff80',# 设置背景颜色
                      font_path=r'C:\Windows\Fonts\STSONG.TTF',
                      stopwords=STOPWORDS)
wordcloud.generate(new_words)
wordcloud.to_file('tangtan3_wordcloud.jpg')