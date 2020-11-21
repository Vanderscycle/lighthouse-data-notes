
import scrapy
import time
import re
import random

from datetime import datetime
# from the spider other file
from ..items import GroceryitemindexerItem



class AmazonWholeFood(scrapy.Spider):
    name = 'tandt'    
    foodSection = 'frozen'
    pageNumber = 1
    
    def start_requests(self): 
        start_url = 'https://www.tntsupermarket.com/fresh-frozen.html'
        yield scrapy.Request(url=start_url, callback=self.parse)
            
    def parse(self,response):  

        groceryItem = GroceryitemindexerItem()
        self.logger.info(f'----------------------------start of page: {AmazonWholeFood.pageNumber}--')
        for i in range(len(response.css('.product-item-link::text').getall())):
            self.logger.info(f'item number:{i} of page:{AmazonWholeFood.pageNumber} \n')
            groceryItem['name'] = response.css('.product-item-link::text')[i].getall()
            groceryItem['price'] = response.css('.price::text')[i].getall()
            groceryItem['link'] = response.css('.product-item-link::attr(href)')[i].getall()
            groceryItem['currency'] = 'CAD'
            #groceryItem['rating'] = 0 # can't access it but mongo can accept it

            groceryItem['numberOfRating'] = response.css('.view::text')[i].getall().pop()
            groceryItem['spider'] = AmazonWholeFood.name
            groceryItem['section'] = AmazonWholeFood.foodSection
            
            groceryItem['time'] = self.timestampReceival()
            yield groceryItem
        self.logger.info(f'----------------------------end of page: {AmazonWholeFood.pageNumber}--')
        # next we loop
        next_page = response.css('.action.next::attr(href)').get() 
        if next_page is not None:
            AmazonWholeFood.pageNumber +=1
            yield scrapy.Request(url=next_page,callback=self.parse)
        

    def timestampReceival(self):
        now = datetime.now()
        return  now.strftime("%m/%d/%Y, %H")
    
