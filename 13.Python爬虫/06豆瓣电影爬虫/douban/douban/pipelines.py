# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class DoubanPipeline:
    def __init__(self):
        self.fp = open("movies.csv","w",encoding='utf-8',newline="")
        filenames = ["title","cover","rating","director","actor","category","country","language","pub_date","duration"]
        writer = csv.DictWriter(self.fp,filenames)
        writer.writeheader()
        self.writer = writer

    def process_item(self, item, spider):
        self.writer.writerow(dict(item))
        return item

    def close_spider(self,spider):
        self.fp.close()
