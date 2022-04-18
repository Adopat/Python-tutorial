# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    title = scrapy.Field()
    cover = scrapy.Field()
    rating = scrapy.Field()
    director = scrapy.Field()
    actor = scrapy.Field()
    category = scrapy.Field()
    country = scrapy.Field()
    language = scrapy.Field()
    pub_date = scrapy.Field()
    duration = scrapy.Field()
