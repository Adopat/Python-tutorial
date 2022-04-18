import requests
from lxml import etree
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Host': 'www.ygdy8.net',
    'Cookie': 'XLA_CI=fd5224e14dece9ad9632d02323aab291',
}

BASE_DOMAIN = "https://www.ygdy8.net"

def crawl_list(url):
    resp = requests.get(url,headers=headers,verify=False)
    try:
        html = resp.content.decode("gbk")
    except:
        html = resp.text
    parser = etree.HTML(html)
    detail_urls = parser.xpath("//div[@class='co_content8']//a[@class='ulink']/@href")
    for detail_url in detail_urls:
        detail_url = BASE_DOMAIN + detail_url
        crawl_detail(detail_url)
        time.sleep(2)


def crawl_detail(url):
    resp = requests.get(url,headers=headers,verify=False)
    try:
        html = resp.content.decode("gbk")
    except:
        html = resp.text

    with open("dytt.html","w",encoding='utf-8') as fp:
        fp.write(html)

    parser = etree.HTML(html)
    movie_name = parser.xpath("//div[@class='title_all']//font/text()")[0]
    zoom = parser.xpath("//div[@id='Zoom']")[0]
    cover = zoom.xpath(".//img/@src")[0]
    infos = zoom.xpath(".//text()")
    yiming = ""
    year = ""
    pub_date = ""
    for info in infos:
        if info.startswith("◎译　　名"):
            yiming = info.replace("◎译　　名","").strip()
        elif info.startswith("◎年　　代"):
            year = info.replace("◎年　　代","").strip()
        elif info.startswith("◎上映日期"):
            pub_date = info.replace("◎上映日期","").strip()
    movie = {
        "电影名": movie_name,
        "封面图": cover,
        "译名": yiming,
        "年代": year,
        "上映日期": pub_date
    }
    print(movie)


if __name__ == '__main__':
    for page in range(2,101):
        url = f"https://www.ygdy8.net/html/gndy/dyzz/list_23_{page}.html"
        crawl_list(url)
        time.sleep(3)