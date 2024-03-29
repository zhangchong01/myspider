import scrapy
import re
import json
import random
import time
from myspider.items import MyspiderItem

class DoubanSpider(scrapy.Spider):
    name = "douban"
    login_param = {'name': '', 'password': '', 'remember': 'false', 'ck': '', 'ticket': ''}
    login_url = "https://accounts.douban.com/j/mobile/login/basic"
    crawl_url = 'https://movie.douban.com/subject/26794435/comments' # 哪吒之魔童降世
    demo_url = 'https://chung567115.blog.csdn.net/article/details/79772903'

    allowed_domains = ['blog.csdn.net']
    start_urls = []
    
    def __init__(self):
        count = 100
        while count > 0:
            self.start_urls.append('https://chung567115.blog.csdn.net/article/details/79772903')
            count -= 1

    def parse(self, response):
        code = response.status
        self.logger.info(">>>>>>>>>>>>>>>>>>>" + str(code))
    
    # def start_requests(self):
    #     count = 100
    #     while count > 0:
    #         count -= 1
    #         scrapy.Request(url=self.demo_url,callback=self.demo_callback)
    #
    # def demo_callback(self, response):
    #     self.logger.info(">>>>>>>>>>>>>>>>>>>" + response.status)
    
    # def start_requests(self):
    #     return [scrapy.FormRequest(url=self.login_url, formdata=self.login_param, callback=self.after_login)]
    #
    # def after_login(self, response):
    #     if response.status == 200:
    #         if json.loads(response.text)['status'] == 'success':
    #             yield scrapy.Request(url=self.crawl_url, callback=self.parse)
    #         else:
    #             print(response.text)
    #     else:
    #         print("登陆失败！")
    #
    # def parse(self, response):
    #     item = MyspiderItem()
    #     comments = response.xpath('//div[@id="comments"]/div')
    #     for comment in comments:
    #         try:
    #             item['name'] = self.format(comment.xpath('.//div[@class="avatar"]/a/@title').extract()[0])
    #             item['score'] = comment.xpath('.//div[@class="comment"]/h3/span[@class="comment-info"]/span/@title').extract()[0]
    #             item['time'] = comment.xpath('.//div[@class="comment"]/h3/span[@class="comment-info"]/span/@title').extract()[1]
    #             item['comment'] = self.format(comment.xpath('.//div[@class="comment"]/p/span/text()').extract()[0])
    #
    #             yield item
    #         except Exception as e:
    #             print(e)
    #             continue
    #
    #     next_url_param = response.xpath('//div[@id="paginator"]/a[@class="next"]/@href').extract()[0]
    #     if next_url_param:
    #         yield scrapy.Request(url=self.crawl_url + next_url_param, callback=self.parse)
    #
    # def format(self, str):
    #     if not str:
    #         return ''
    #     return re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", str)