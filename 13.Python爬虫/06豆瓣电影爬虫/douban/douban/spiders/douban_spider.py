# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import DoubanItem


def get_info(index,handle_infos):
    info = ""
    handle_infos_len = len(handle_infos)
    for x in range(index + 1, handle_infos_len):
        temp_info = handle_infos[x]
        if temp_info.endswith(":"):
            index = x
            break
        else:
            info += temp_info
    return index, info


class DoubanSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['douban.com']
    # start_urls = ['https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=0']

    def start_requests(self):
        for page in range(0,100,20):
            movie_list_url = f"https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start={page}"
            # yield：会返回scrapy.Request，但是不会让函数停止执行（生成器）
            # return：一旦执行了，整个函数就结束了
            yield scrapy.Request(movie_list_url,callback=self.parse)
            # break

    def parse(self, response):
        text = response.text
        result = json.loads(text)
        movies = result['data']
        for movie in movies:
            detail_url = movie['url']
            yield scrapy.Request(detail_url,self.parse_detail)
            # break

    def parse_detail(self,response):
        # scrapy shell
        # scrapy中，已经在response中内置了xpath功能，不需要先获取源代码，然后用lxml构建一个解析器
        # response.xpath：这个方法会返回一个容器。get方法
        title = response.xpath("//div[@id='content']/h1/span[1]/text()").get()
        cover = response.xpath("//div[@id='mainpic']/a/img/@src").get()
        rating = response.xpath("//strong[@class='ll rating_num']/text()").get()


        """
        ['\n        ', '导演', ': ', '饶晓志', '\n        ', '编剧', ': ', '饶晓志', ' / ', '范翔', ' / ', '李想', '\n        ', '主演', ': ', '刘德 华', ' / ', '肖央', ' / ', '万茜', ' / ', '程怡', ' / ', '黄小蕾', ' / ', '国义骞', ' / ', '狄志杰', ' / ', '郭京飞', ' / ', '刘天佐', ' / ', '路阳', ' / ', '郭帆', ' / ', '刘浩良', ' / ', '饶晓志', ' / ', '雷佳音', ' / ', '史航', ' / ', '魏之皓', ' / ', '王学兵', ' / ', '林海', ' / ', '隋凯', ' / ', '卫莱', '\n        ', '类型:', ' ', '喜剧', ' / ', '犯罪', '\n        \n        ', '制片国家/地区:', ' 中国大陆 / 中国香 港', '\n        ', '语言:', ' 汉语普通话', '\n        ', '上映日期:', ' ', '2021-02-12(中国大陆)', '\n        ', '片长:', ' ', '119分钟', '\n        ', '又名:', ' Endgame', '\n        ', 'IMDb:', ' tt11564214', '\n\n']
        """

        infos = response.xpath("//div[@id='info']//text()").getall()
        handle_infos = []
        for info in infos:
            if info.replace("\n", "").replace(" ", "") == "":
                continue
            elif info.strip() == ":":
                handle_infos[-1] = handle_infos[-1] + ":"
            else:
                handle_infos.append(info)

        """
        ['导演:', '饶晓志', '编剧:', '饶晓志', ' / ', '范翔', ' / ', '李想', '主演:', '刘德华', ' / ', '肖央', ' / ', '万茜', ' / ', '程怡', ' / ', '黄小蕾', ' / ', '国义骞', ' / ', '狄志杰', ' / ', '郭京飞', ' / ', '刘天佐', ' / ', '路阳', ' / ', '郭帆', ' / ', '刘浩良', ' / ', '饶晓志', ' / ', '雷佳音', ' / ', '史航', ' / ', '魏之皓', ' / ', '王学兵', ' / ', '林海', ' / ', '隋凯', ' / ', '卫莱', '类型:', '喜剧', ' / ', '犯罪', '制片国家/地区:', ' 中国大陆 / 中国香港', '语言:', ' 汉语普通话', '上映日期:', '2021-02-12(中国大陆)', '片长:', '119分钟', '又名:', ' Endgame', 'IMDb:', ' tt11564214']
        """
        director = ""
        actor = ""
        category = ""
        country = ""
        language = ""
        pub_date = ""
        duration = ""
        index = 0
        handle_infos_len = len(handle_infos)

        while index < handle_infos_len:
            info = handle_infos[index]
            if info.strip() == "导演:":
                index,director = get_info(index,handle_infos)
            elif info.strip() == "主演:":
                index,actor = get_info(index,handle_infos)
            elif info.strip() == '类型:':
                index,category = get_info(index,handle_infos)
            elif info.strip() == '制片国家/地区:':
                index, country = get_info(index,handle_infos)
            elif info.strip() == '语言:':
                index, language = get_info(index,handle_infos)
            elif info.strip() == "上映日期:":
                index, pub_date = get_info(index,handle_infos)
            elif info.strip() == "片长:":
                index, duration = get_info(index,handle_infos)
            else:
                index += 1

        item = DoubanItem(
            title=title,
            cover=cover,
            rating=rating,
            director=director,
            actor=actor,
            category=category,
            country=country,
            language=language,
            pub_date=pub_date,
            duration=duration,
        )
        # print(item)
        yield item



