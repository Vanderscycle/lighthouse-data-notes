# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from datetime import datetime

def timestampReceival():
    now = datetime.now()
    return  now.strftime("%m/%d/%Y, %H")

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

class IpTimestamp(scrapy.Item):
    ip = scrapy.Field()
    time = scrapy.Field() # doesn't work

class FlyerItem(scrapy.Item):
    store = scrapy.Field()
    flyersDate = scrapy.Field() # the week the flyer is valid for
    file_urls = scrapy.Field()
    files = scrapy.Field()
    spider = scrapy.Field()
    page = scrapy.Field()
    timeScraped = scrapy.Field()

class ImgData(scrapy.Item):
    image_urls=scrapy.Field()
    images=scrapy.Field()

