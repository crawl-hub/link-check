import scrapy
import logging
from opensource.common.utils import should_ignore


class DaprSpider(scrapy.Spider):
    name = "dapr"
    allowed_domains = ["docs.dapr.io"]
    start_urls = ["https://docs.dapr.io"]

    def parse(self, response):
        if response.status >= 400:
            logging.error("page error: {}".format(response.url))
            return

        for link in response.css("a::attr(href)").extract():
            if should_ignore(response.url, link):
                continue
            yield response.follow(link, self.parse)
