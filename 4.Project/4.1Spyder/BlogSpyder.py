# # 爬取博客园数据并用词云图展示
import requests
import re
import json
from bs4 import BeautifulSoup
from concurrent import futures
from fake_useragent import UserAgent
from requests.exceptions import RequestException


#
#

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
        response = requests.get(url, headers=headers, timeout=100)
        # 通过状态码判断是否获取成功
        if response.status_code == 200:
            # 指定编码，否则中文出现乱码
            response.encoding = 'utf-8'
            return response.text
        return None
    except RequestException as e:
        return None


# 2.解析博客推荐列表
def getUsers():
    response = get_one_page('https://www.cnblogs.com/aggsite/UserStats')
    soup = BeautifulSoup(response, 'lxml')
    blogger_list = soup.select('#blogger_list>ul>li>a')
    new_BlogList = []
    for blog in blogger_list:
        new_BlogDict = {}
        new_BlogDict['Author'] = blog.string
        new_BlogDict['url'] = 'http:' + blog.get('href')
        new_BlogList.append(new_BlogDict)
    return new_BlogList


new_BlogList = getUsers()
for i in new_BlogList:
    print(i)
# def getUsers():
#     # 获取推荐博客列表
#     r = requests.get('https://www.cnblogs.com/aggsite/UserStats')
#
#     # 使用BeautifulSoup解析
#     soup = BeautifulSoup(r.text, 'lxml')
#     users = [(i.text, i['href']) for i in soup.select('#blogger_list > ul > li > a') if 'AllBloggers.aspx' not in i['href'] and 'expert' not in i['href']]
#
#     # 也可以使用使用正则表达式
#     # user_re=re.compile('<a href="(http://www.cnblogs.com/.+)" target="_blank">(.+)</a>')
#     # users=[(name,url) for url,name in re.findall(blog_re,r.text) if 'AllBloggers.aspx' not in url and 'expert' not in url]
#
#     return users
#
#
# def getPostsDetail(Posts):
#     # 获取文章详细信息：标题，次数，URL
#     post_re = re.compile('\d+\. (.+)\((\d+)\)')
#     soup = BeautifulSoup(Posts, 'lxml')
#     return [list(re.search(post_re, i.text).groups()) + [i['href']] for i in soup.find_all('a')]
#
#
# def getViews(user):
#     # 获取博客阅读排行榜，评论排行榜及推荐排行榜信息
#     url = 'http://www.cnblogs.com/mvc/Blog/GetBlogSideBlocks.aspx'
#     blogApp = user
#     showFlag = 'ShowTopViewPosts,ShowTopFeedbackPosts,ShowTopDiggPosts'
#     payload = dict(blogApp=blogApp, showFlag=showFlag)
#     r = requests.get(url, params=payload)
#
#     TopViewPosts = getPostsDetail(r.json()['TopViewPosts'])
#     TopFeedbackPosts = getPostsDetail(r.json()['TopFeedbackPosts'])
#     TopDiggPosts = getPostsDetail(r.json()['TopDiggPosts'])
#
#     return dict(TopViewPosts=TopViewPosts, TopFeedbackPosts=TopFeedbackPosts, TopDiggPosts=TopDiggPosts)
#
#
# def getCategory(user):
#     # 获取博客随笔分类
#     category_re = re.compile('(.+)\((\d+)\)')
#     url = 'http://www.cnblogs.com/{0}/mvc/blog/sidecolumn.aspx'.format(user)
#     blogApp = user
#     payload = dict(blogApp=blogApp)
#     r = requests.get(url, params=payload)
#     soup = BeautifulSoup(r.text, 'lxml')
#     category = [re.search(category_re, i.text).groups() for i in soup.select('.catListPostCategory > ul > li') if re.search(category_re, i.text)]
#
#     return dict(category=category)
#
#
# def getTotal(url):
#     # 获取博客全部信息，包括分类及排行榜信息
#     # 初始化博客用户名
#     print('Spider blog:\t{0}'.format(url))
#     user = url.split('/')[-2]
#     return dict(getViews(user), **getCategory(user))
#
#
# def mutiSpider(max_workers=4):
#     try:
#         # with futures.ThreadPoolExecutor(max_workers=max_workers) as executor:  # 多线程
#         with futures.ProcessPoolExecutor(max_workers=max_workers) as executor:  # 多进程
#             for blog in executor.map(getTotal, [i[1] for i in users]):
#                 blogs.append(blog)
#     except Exception as e:
#         print(e)
#
# if __name__ == '__main__':
#     blogs = []
#
#     # 获取推荐博客列表
#     users = getUsers()
#     print(json.dumps(users, ensure_ascii=False))
#
#     # 多线程/多进程获取博客信息
#     mutiSpider()
#
#     print(json.dumps(blogs,ensure_ascii=False))
