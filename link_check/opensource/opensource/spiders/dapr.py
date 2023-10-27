import scrapy
import logging
from opensource.common.utils import should_ignore
from opensource.common.base import BaseSpider


class DaprSpider(BaseSpider, scrapy.Spider):
    name = "dapr"
    allowed_domains = ["docs.dapr.io"]
    start_urls = ["https://docs.dapr.io"]
