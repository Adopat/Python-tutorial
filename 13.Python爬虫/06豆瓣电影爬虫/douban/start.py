from scrapy import cmdline

# "scrapy crawl douban_spider".split(" ")
# ["scrapy","crawl","douban_spider"]
cmdline.execute("scrapy crawl douban_spider".split(" "))