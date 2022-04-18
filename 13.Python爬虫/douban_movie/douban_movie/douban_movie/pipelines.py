# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from .items import MovieItem,CommentItem


class DoubanMoviePipeline:
    def __init__(self):
        self.conn = pymysql.connect(host="127.0.0.1",user="root",password="root",database="douban_movie",port=3306,charset="utf8")
        self.cursor = self.conn.cursor()
        self.movie_sql = "insert into movie(id,db_movie_id,title,cover,director,scriptwriter,actor,category,country,lang,release_date,duration,profile,rating,rating_people,star5,star4,star3,star2,star1,origin_url) values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.comment_sql = "insert into movie_comment(id,db_movie_id,username,avatar,rating,pub_date,content) values(null,%s,%s,%s,%s,%s,%s)"

    def process_item(self, item, spider):
        if isinstance(item,MovieItem):
            self.cursor.execute(self.movie_sql,(
                item['movie_id'],item['title'],item['cover'],item['director'],item['scriptwriter'],item['actor'],item['category'],item['country'],
                item['language'],item['release_date'],item['duration'],item['profile'],item['rating'],item['rating_people'],item['star5'],item['star4'],item['star3'],item['star2'],item['star1'],item['origin_url']
            ))
            self.conn.commit()
        elif isinstance(item,CommentItem):
            self.cursor.execute(self.comment_sql,(
                item['movie_id'],item['username'],item['avatar'],item['rating'],item['pub_date'],item['content']
            ))
            self.conn.commit()
        return item

    def close_spider(self,spider):
        self.conn.close()
