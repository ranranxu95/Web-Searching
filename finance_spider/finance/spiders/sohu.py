# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from finance.items import FinanceItem


class SohuSpider(CrawlSpider):
    name = 'sohu'
    allowed_domains = ['www.sohu.com']
    start_urls = ['http://www.sohu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*?/a/[0-9]{9}_[0-9]{6}'), callback='parse_item', follow=True),
    )

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, dont_filter=False)

    def parse_item(self, response):
        item = FinanceItem()
        item['content'] = ''.join(response.xpath('//article[@class="article"]/p/text()').extract())
        item['source']  = 'sohu'
        item['time']    = response.xpath('//div[@class="article-info"]/span[@class="time"]/text()').extract()[0]
        item['title']   = response.xpath("/html/head/title/text()").extract()[0]
        item['url']     = response.url

        yield item
