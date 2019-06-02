# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from pagongjiao.items import PagongjiaoItem

class ZzgjSpider(CrawlSpider):
    name = 'zzgj'
    allowed_domains = ['beijing.8684.cn']
    start_urls = ['http://beijing.8684.cn/']

    rules = (
        Rule(LinkExtractor(allow=r'line'), process_links='parse_first', follow = True),
        Rule(LinkExtractor(allow=r'/\w_'), callback='parse_item',),

    )

    def parse_first(self, links):
        for link in links:
            scrapy.Request(link.url)
        return links

    def parse_item(self, response):
        item = PagongjiaoItem()

        item['busname'] = response.xpath('string(//div[@class="bus_i_t1"]/h1/text())').extract()[0]
        item['runtime'] = response.xpath('string(//div[@class="bus_i_content"]/p[1]/text())').extract()[0]
        item['money'] = response.xpath('string(//div[@class="bus_i_content"]/p[2]/text())').extract()[0]
        item['lastupdate'] = response.xpath('string(//div[@class="bus_i_content"]/p[4]/text())').extract()[0]
        item['topline'] = response.xpath('string(//div[@class="bus_line_top "][1]/div/strong/text())').extract()[0]
        item['downline'] = response.xpath('string(//div[@class="bus_line_top "][2]/div/strong/text())').extract()[0]
        item['line'] = response.xpath('string(//div[@class="bus_line_site "])').extract()[0]

        yield item
