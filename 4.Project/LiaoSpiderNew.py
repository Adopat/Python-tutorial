# 使用Python爬取廖雪峰博客
import os
import shutil
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import pdfkit
from PyPDF2 import PdfFileReader, PdfFileWriter
from fake_useragent import UserAgent
from time import sleep
import random
path_wk = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe' #wkhtmltopdf安装位置
config = pdfkit.configuration(wkhtmltopdf = path_wk)
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
{content}
</body>
</html>
"""

base_url = 'https://www.liaoxuefeng.com/wiki/1016959663602400'
book_name = ''
chapter_info = []

# 1. 获取数据连接
def get_one_page(url):
    """
    获取网页html内容并返回
    :param url: 目标网址
    :return html
    """
    headers = {"User-Agent": UserAgent(verify_ssl=False).random}
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
# 2.将目录和链接提取出来
def parse_title_and_url(html):
    soup = BeautifulSoup(html, 'lxml')
    menu = soup.find('div', class_='x-sidebar-left-content').find_all('a', class_='x-wiki-index-item')
    # 将 menu 和连接保存
    book_info = []
    for i in menu:
        now_book_dict = {}
        now_book_dict['menu'] = i.string
        now_book_dict['url'] = 'https://www.liaoxuefeng.com' + i.get('href')
        book_info.append(now_book_dict)
    return book_info
# print(book_info)
# 3. 将html 转为 pdf
def save_pdf(html, filename):
    """
    把所有html文件保存到pdf文件
    :param html:  html内容
    :param file_name: pdf文件名
    :return:
    """
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'enable-local-file-access': "",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ],
        'cookie': [
            ('cookie-name1', 'cookie-value1'),
            ('cookie-name2', 'cookie-value2'),
        ],
        'outline-depth': 100,
    }

    pdfkit.from_string(html, filename, options=options,configuration=config)


def get_content(url):
    """
    解析URL，获取需要的html内容
    :param url: 目标网址
    :return: html
    """
    html = get_one_page(url)
    soup = BeautifulSoup(html, 'lxml')
    content = soup.find('div', class_='x-wiki-content x-main-content')
    html = html_template.format(content=content)
    return html
# 3.保存html 页面
def saveHtml(file_name, file_content):
    # 注意windows文件命名的禁用符，比如 /
    with open('D:\\Python-tutorial\\4.Project\\liaoxuefeng\\Python教程\\'+file_name.replace('/', '_') + ".html", "wb") as f:
        # 写文件用bytes而不是str，所以要转码
        f.write(file_content.encode(encoding='utf-8'))
def main():
    html = get_one_page(base_url)  # 1.获取首页信息
    book_info = parse_title_and_url(html)  # 2.获取目录和链接信息
    for chapter in book_info:
        ctitle = chapter['menu']
        url = chapter['url']
        html = get_content(url)
        # html_to_pdf(html,'D:\\Python-tutorial\\4.Project\\liaoxuefeng\\Python教程\\'+ctitle+".pdf")
        saveHtml(ctitle,html)
        print(f'{ctitle}保存成功')
if __name__ =='__main__':
    main()



