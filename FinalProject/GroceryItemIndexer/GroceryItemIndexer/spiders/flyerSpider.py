import scrapy
import time
from datetime import datetime
# from the spider other file
# create a different item class
from ..items import GroceryitemindexerItem #! change
# all items goes into the pipeline so you have to specify which ones dont


class flyerSpider(scrapy.Spider):
    name = 'fSpider'
        
    def start_requests(self): 
        start_url = 'https://flyers.smartcanucks.ca/'
        yield scrapy.Request(url=start_url, callback=self.parse)
            
    def parse(self,response):
        yield response.body('title')  
   