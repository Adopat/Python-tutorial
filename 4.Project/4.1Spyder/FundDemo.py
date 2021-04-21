import csv
import time
import random
import requests
import traceback
from time import sleep
from fake_useragent import UserAgent
from lxml import etree
# page = 1
# fundcode = 161725
# sleep(random.uniform(1,5))
# headers = {"User-Agent":UserAgent(verify_ssl=False).random}
# url = f'http://guba.eastmoney.com/list,of{fundcode}_{page}.html'
# response = requests.get(url,headers=headers,timeout=100)
# # print(response.text)
# # 解析网页
# parse = etree.HTML(response.text)
# items = parse.xpath('//*[@id="articlelistnew"]/div')[1:91]
# for item in items:
#     item ={
#         '阅读': ''.join(item.xpath('./span[1]/text()')).strip(),
#         '评论': ''.join(item.xpath('./span[2]/text()')).strip(),
#         '标题': ''.join(item.xpath('./span[3]/a/text()')).strip(),
#         '作者': ''.join(item.xpath('./span[4]/a/font/text()')).strip(),
#         '时间': ''.join(item.xpath('./span[5]/text()')).strip()
#     }
#     print(item)
# with open(f'./{fundcode}.csv', 'a', encoding='utf_8_sig', newline='') as fp:
#     fieldnames = ['阅读', '评论', '标题', '作者', '时间']
#     writer = csv.DictWriter(fp, fieldnames)
#     writer.writerow(item)
def get_fund(url):
    headers = {"User-Agent": UserAgent(verify_ssl=False).random}
    response = requests.get(url,headers=headers,timeout=100)
    html = response.text
    return html
def parse_fund(html,fundcode):
    parse = etree.HTML(html)
    items = parse.xpath('//*[@id="articlelistnew"]/div')[1:91]
    for item in items:
        item ={
            '阅读': ''.join(item.xpath('./span[1]/text()')).strip(),
            '评论': ''.join(item.xpath('./span[2]/text()')).strip(),
            '标题': ''.join(item.xpath('./span[3]/a/text()')).strip(),
            '作者': ''.join(item.xpath('./span[4]/a/font/text()')).strip(),
            '时间': ''.join(item.xpath('./span[5]/text()')).strip()
        }
        # print(item)
    with open(f'./{fundcode}.csv', 'a', encoding='utf_8_sig', newline='') as fp:
        fieldnames = ['阅读', '评论', '标题', '作者', '时间']
        writer = csv.DictWriter(fp, fieldnames)
        writer.writerow(item)
def main(page):
    fundcode = 161725
    url = f'http://guba.eastmoney.com/list,of{fundcode}_{page}.html'
    html = get_fund(url)
    parse_fund(html, fundcode)
if __name__ =="__main__":
    for page in range(1,2):
        main(page)
        sleep(random.uniform(1, 5))
        print(f'第{page}页提取完成')