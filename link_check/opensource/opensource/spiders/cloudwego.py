import scrapy
from scrapy.spiders import logging
from opensource.common.utils import should_ignore
from opensource.common.base import BaseSpider


class CloudwegoSpider(BaseSpider, scrapy.Spider):
    name = "cloudwego"
    allowed_domains = ["www.cloudwego.io"]
    start_urls = ["https://www.cloudwego.io"]
