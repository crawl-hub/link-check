import scrapy
from scrapy.spiders import logging
from opensource.common.utils import should_ignore


class CloudwegoSpider(scrapy.Spider):
    name = "cloudwego"
    allowed_domains = ["www.cloudwego.io"]
    start_urls = ["https://www.cloudwego.io"]

    def parse(self, response):
        if response.status >= 400:
            logging.error("page error: {}".format(response.url))
            return

        for link in response.css("a::attr(href)").extract():
            if should_ignore(response.url, link):
                continue
            yield response.follow(link, self.parse)
