# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GroceryitemindexerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    currency = scrapy.Field()
    link = scrapy.Field()
    rating = scrapy.Field()
    numberOfRating = scrapy.Field()
    spider = scrapy.Field()
    section = scrapy.Field()
    time = scrapy.Field()
