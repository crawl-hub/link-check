import scrapy
import logging
from opensource.common.utils import should_ignore
from opensource.common.base import BaseSpider


class OpentelemetrySpider(BaseSpider, scrapy.Spider):
    name = "opentelemetry"
    allowed_domains = ["opentelemetry.io"]
    start_urls = ["https://opentelemetry.io/"]
