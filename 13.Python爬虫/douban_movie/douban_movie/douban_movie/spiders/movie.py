import scrapy
from ..items import MovieItem,CommentItem
import re

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['movie.douban.com']
    base_url = "https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start={}"

    def start_requests(self):
        for x in range(0,10000,20):
            url = self.base_url.format(x)
            yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):
        result = response.json()
        try:
            movies = result['data']
            for movie in movies:
                url = movie['url']
                yield scrapy.Request(url, callback=self.parse_detail)
        except KeyError as e:
            pass

    def parse_detail(self,response):
        movie_id = re.search(r"/subject/(\d+)/",response.url).group(1)
        title = response.xpath("//div[@id='content']/h1/span/text()").get().split(" ")[0]
        cover = response.xpath("//a[@class='nbgnbg']/img/@src").get()
        infos = response.xpath("//div[@id='info']//text()").getall()
        handle_infos = []
        for info in infos:
            if info.replace("\n","").replace(" ","") == "":
                continue
            elif info.strip() == ":":
                handle_infos[-1] = handle_infos[-1] + ":"
            else:
                handle_infos.append(info)

        maps = ["导演:","编剧:","主演:","类型:","制片国家/地区:","语言:","上映日期:","片长:","又名:","IMDb链接:"]
        director = ""
        scriptwriter = ""
        actor = ""
        category = ""
        country = ""
        language = ""
        release_date = ""
        duration = ""
        index = 0
        handle_infos_len = len(handle_infos)
        while index < handle_infos_len:
            info = handle_infos[index]
            if info.strip() == "导演:":
                for x in range(index+1,handle_infos_len):
                    temp_info = handle_infos[x]
                    if temp_info in maps:
                        index = x
                        break
                    director += temp_info
            elif info.strip() == "编剧:":
                for x in range(index+1,handle_infos_len):
                    temp_info = handle_infos[x]
                    if temp_info in maps:
                        index = x
                        break
                    scriptwriter += temp_info
            elif info.strip() == "主演:":
                for x in range(index+1,handle_infos_len):
                    temp_info = handle_infos[x]
                    if temp_info in maps:
                        index = x
                        break
                    actor += temp_info
            elif info.strip() == "类型:":
                for x in range(index+1,handle_infos_len):
                    temp_info = handle_infos[x]
                    if temp_info in maps:
                        index = x
                        break
                    category += temp_info
            elif info.strip() == "制片国家/地区:":
                for x in range(index+1,handle_infos_len):
                    temp_info = handle_infos[x]
                    if temp_info in maps:
                        index = x
                        break
                    country += temp_info
            elif info.strip() == "语言:":
                for x in range(index+1,handle_infos_len):
                    temp_info = handle_infos[x]
                    if temp_info in maps:
                        index = x
                        break
                    language += temp_info
            elif info.strip() == "上映日期:":
                for x in range(index+1,handle_infos_len):
                    temp_info = handle_infos[x]
                    if temp_info in maps:
                        index = x
                        break
                    release_date += temp_info
            elif info.strip() == "片长:":
                for x in range(index+1,handle_infos_len):
                    temp_info = handle_infos[x]
                    if temp_info in maps:
                        index = x
                        break
                    duration += temp_info
            else:
                index += 1

        profiles = response.xpath("//div[@id='link-report']//text()").getall()
        profile = "".join(profiles)
        profile = re.sub(r"\s","",profile)

        rating_tag = response.xpath("//div[contains(@class,'rating_wrap')]")
        rating = rating_tag.xpath(".//strong/text()").get()
        rating_people = rating_tag.xpath(".//a[@class='rating_people']/span/text()").get()
        star_levels = rating_tag.xpath(".//span[@class='rating_per']/text()").getall()
        star5,star4,star3,star2,star1 = 0,0,0,0,0
        if len(star_levels) == 5:
            star5 = star_levels[0]
            star4 = star_levels[1]
            star3 = star_levels[2]
            star2 = star_levels[3]
            star1 = star_levels[4]

        item = MovieItem(
            movie_id=movie_id,
            title = title,
            cover = cover,
            director = director,
            scriptwriter = scriptwriter,
            actor = actor,
            category = category,
            country = country,
            language = language,
            release_date = release_date,
            duration = duration,
            profile = profile,
            rating=rating,
            rating_people=rating_people,
            star5=star5,
            star4=star4,
            star3=star3,
            star2=star2,
            star1=star1,
            origin_url = response.url
        )
        yield item

        comment_url = response.url + "comments?start=0&limit=20&status=P&sort=new_score"
        yield scrapy.Request(comment_url,callback=self.parse_comment,meta={"movie_id":movie_id})

    def parse_comment(self,response):
        movie_id = response.meta.get("movie_id")
        comment_list = response.xpath("//div[contains(@class,'comment-item')]")
        for comment_item in comment_list:
            username = comment_item.xpath(".//span[@class='comment-info']/a/text()").get()
            avatar = comment_item.xpath(".//div[@class='avatar']//img/@src").get()
            rating_str = comment_item.xpath(".//span[contains(@class,'rating')]/@title").get()
            rating = 0
            if rating_str == "力荐":
                rating = 5
            elif rating_str == "推荐":
                rating = 4
            elif rating_str == "还行":
                rating = 3
            elif rating_str == "较差":
                rating = 2
            elif rating_str == "很差":
                rating = 1
            pub_date = comment_item.xpath(".//span[contains(@class,'comment-time')]/@title").get()
            content = comment_item.xpath(".//p[contains(@class,'comment-content')]//text()").getall()
            content = "".join(content).strip()

            item = CommentItem(
                movie_id=movie_id,
                username=username,
                rating=rating,
                pub_date=pub_date,
                content=content,
                avatar=avatar
            )
            yield item

            start = response.meta.get("start") or 0
            url = re.sub(r"start=\d+","start=%d"%(start+20),response.url)
            yield scrapy.Request(url,callback=self.parse_comment,meta={"start":start,"movie_id":movie_id})
