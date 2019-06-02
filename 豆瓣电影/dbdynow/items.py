# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class DbdynowItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    filmname = Field()
    director = Field()
    screenwriter = Field()
    actor = Field()
    type = Field()
    country = Field()
    language = Field()
    playtime = Field()
    duration = Field()
    anothername = Field()
    score = Field()
    introduction = Field()
