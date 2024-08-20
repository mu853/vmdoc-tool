# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NsxdiffItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    language = scrapy.Field()
    version = scrapy.Field()
    last_modified = scrapy.Field()
    guid = scrapy.Field()
