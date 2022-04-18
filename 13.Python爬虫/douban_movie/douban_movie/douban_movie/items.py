# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    movie_id = scrapy.Field()
    title = scrapy.Field()
    cover = scrapy.Field()
    director = scrapy.Field()
    scriptwriter = scrapy.Field()
    actor = scrapy.Field()
    category = scrapy.Field()
    country = scrapy.Field()
    language = scrapy.Field()
    release_date = scrapy.Field()
    duration = scrapy.Field()
    profile = scrapy.Field()
    rating = scrapy.Field()
    rating_people = scrapy.Field()
    star5 = scrapy.Field()
    star4 = scrapy.Field()
    star3 = scrapy.Field()
    star2 = scrapy.Field()
    star1 = scrapy.Field()
    origin_url = scrapy.Field()


class CommentItem(scrapy.Item):
    movie_id = scrapy.Field()
    username = scrapy.Field()
    avatar = scrapy.Field()
    rating = scrapy.Field()
    pub_date = scrapy.Field()
    content = scrapy.Field()
