# 使用BS4解析数据
import requests
import json
from time import sleep
from fake_useragent import UserAgent
import random
from bs4 import BeautifulSoup


def request_dangdang(url):
    headers = {"User-Agent": UserAgent(verify_ssl=False).random}
    try:
        response = requests.get(url, headers=headers, timeout=1000)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


# url = 'http://bang.dangdang.com/books/fivestars/1-1'
# content = request_dangdang(url)
# 分析页面
def parse_result(content):
    soup = BeautifulSoup(content, 'lxml')
    book_list = soup.find(class_='bang_list clearfix bang_list_mode').find_all('li')
    book_info = []
    for item in book_list:
        now_book_dict = {}
        now_book_dict['rank'] = item.find(class_='list_num').string
        now_book_dict['imag'] = item.find(class_='pic').find('a').find('img').get('src')
        now_book_dict['title'] = item.find(class_='name').find('a').get('title')
        now_book_dict['recommend'] = item.find(class_='star').find(class_='tuijian').string
        if item.find(class_='publisher_info').find('a') != None:
            now_book_dict['author'] = item.find(class_='publisher_info').find('a').get('title')
        else:
            now_book_dict['author'] = item.find(class_='publisher_info').string
        now_book_dict['times'] = item.find(class_='biaosheng').find('span').string
        now_book_dict['price'] = item.find(class_='price').find('p').find('span').string
        book_info.append(now_book_dict)
    return book_info


def write_item_to_file(item):
    print('开始写入数据 ====> ' + str(item))
    with open('book.txt', 'a', encoding='UTF-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')


def main(page):
    url = 'http://bang.dangdang.com/books/fivestars/1-' + str(page)
    content = request_dangdang(url)
    book_info = parse_result(content)  # 解析过滤我们想要的信息
    for item in book_info:
        write_item_to_file(item)


if __name__ == "__main__":
    for i in range(1, 26):
        main(i)
        sleep(random.uniform(1, 5))
