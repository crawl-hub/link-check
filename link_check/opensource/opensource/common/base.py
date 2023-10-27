import logging
from .utils import should_ignore


class BaseSpider:
    def parse(self, response):
        if response.status >= 400:
            logging.error("page error: {}".format(response.url))
            return

        for link in response.css("a::attr(href)").extract():
            if should_ignore(response.url, link):
                continue
            yield response.follow(link, self.parse)
