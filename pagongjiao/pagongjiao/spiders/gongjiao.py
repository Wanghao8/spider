# -*- coding: utf-8 -*-
import scrapy
from pagongjiao.items import PagongjiaoItem


class GongjiaoSpider(scrapy.Spider):
    name = 'gongjiao'
    allowed_domains = ['https://www.8684.cn/']
    start_urls = ['https://beijing.8684.cn/']

    def parse(self, response):
        item = PagongjiaoItem()

        item['busname'] = tree.xpath('string(//div[@class="bus_i_t1"]/h1/text())').replace('&nbsp', ' ')
        item['runtime'] = tree.xpath('//div[@class="bus_i_content"]/p[1]/text()')[0]
        item['money'] = tree.xpath('//div[@class="bus_i_content"]/p[2]/text()')[0]
        item['lastupdate'] = tree.xpath('//div[@class="bus_i_content"]/p[4]/text()')[0]
        item['topline'] = tree.xpath('string(//div[@class="bus_line_top "][1]/div/strong/text())')
        item['downline'] = tree.xpath('string(//div[@class="bus_line_top "][2]/div/strong/text())')
        item['line'] = tree.xpath('string(//div[@class="bus_line_site "])')

        yield item
