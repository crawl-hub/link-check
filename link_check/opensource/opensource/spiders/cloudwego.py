import scrapy
from scrapy.spiders import logging


class CloudwegoSpider(scrapy.Spider):
    name = "cloudwego"
    allowed_domains = ["www.cloudwego.io"]
    start_urls = ["https://www.cloudwego.io"]

    def parse(self, response):
        if response.status >= 400:
            logging.error("page error: {}".format(response.url))
            return

        for link in response.css("a::attr(href)").extract():
            if link.startswith("mailto"):
                logging.warn("page: {}, mail link: {}".format(response.url, link))
                continue
            yield response.follow(link, self.parse)
