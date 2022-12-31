import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['duckduckgo.com']
    start_urls = ['http://duckduckgo.com/']

    def parse(self, response):
        pass
