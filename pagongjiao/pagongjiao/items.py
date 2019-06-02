# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PagongjiaoItem(scrapy.Item):
    # define the fields for your item here like:
    busname = scrapy.Field()
    runtime = scrapy.Field()
    money = scrapy.Field()
    lastupdate = scrapy.Field()
    topline = scrapy.Field()
    downline = scrapy.Field()
    line = scrapy.Field()
