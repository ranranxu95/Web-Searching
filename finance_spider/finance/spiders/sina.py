# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from finance.items import FinanceItem

class BangbingSpider(CrawlSpider):
    name = 'sina'
    allowed_domains = ['finance.sina.com.cn']

    start_urls = []
    with open('/root/Web-Searching/finance_spider/finance/urls/sina.txt') as fp:
        data = fp.readline().strip()
        while data !='':
            start_urls.append(data)
            data = fp.readline().strip()

    rules = (
        Rule(LinkExtractor(allow='.*?/doc-[a-z]*[0-9]*\.shtml'), callback='parse_item', follow=True),
    )

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, dont_filter=False)

    def parse_item(self, response):
        item = FinanceItem()
        text = response.xpath('//div[@class="article article_16"]/p/text()').extract()
        content = []
        for t in text:
            content.append(["p", t])
        item['content'] = content
        item['source']  = 'sina'
        item['datetime']    = response.xpath('//div[@class="page-info"]/span[@class="time-source"]/text()').extract()#[0]
        item['title']   = response.xpath("/html/head/title/text()").extract()[0]
        item['href']    = response.url
        item['type']    = 'sina'
      
        yield item
