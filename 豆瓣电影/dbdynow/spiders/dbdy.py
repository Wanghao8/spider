# -*- coding: utf-8 -*-
import scrapy
from dbdynow.items import DbdynowItem
import re

class DbdySpider(scrapy.Spider):
    name = 'dbdy'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/cinema/nowplaying/zhengzhou/']

    def parse(self, response):
        urls = response.xpath('//li/ul/li[2]/a/@href').extract()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_content)

    def parse_content(self, response):
        item = DbdynowItem()

        item['filmname'] = response.xpath('//*[@id="content"]/h1/span[1]/text()').extract()
        item['director'] = response.xpath('//*[@id="info"]/span[1]/span[2]/a/text()').extract()
        item['screenwriter'] = response.xpath('//*[@id="info"]/span[2]/span[2]/a/text()').extract()
        actor = response.xpath('//*[@id="info"]/span[3]/span[2]').extract()
        actor = re.findall(r'.*?>(\w*)<.*?', str(actor))
        item['actor'] = actor
        item['type'] = response.xpath('//*[@id="info"]/span[@property="v:genre"]/text()').extract()
        item['country'] = response.xpath('string(//*[@id="info"]/text()[9])').extract()
        item['language'] = response.xpath('string(//*[@id="info"]/text()[11])').extract()
        item['playtime'] = response.xpath('//*[@id="info"]/span[11]/text()').extract()
        item['duration'] = response.xpath('//span[@property="v:runtime"]/text()').extract()
        item['anothername'] = response.xpath('//*[@id="info"]/text()[17]').extract()
        item['score'] = response.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()').extract()
        introduction = response.xpath('string(//*[@id="link-report"]/span[1]/text())').extract()
        introduction = re.sub(r'\s*', '', str(introduction))
        item['introduction'] = introduction


        yield item
