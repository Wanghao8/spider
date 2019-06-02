# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

class PagongjiaoPipeline(object):
    def __init__(self):
        self.f = codecs.open('E:\\pashujv\\北京公交车.json', 'w', encoding='utf8')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.f.write(content)
        return item

    def close_item(self):
        self.f.close()
