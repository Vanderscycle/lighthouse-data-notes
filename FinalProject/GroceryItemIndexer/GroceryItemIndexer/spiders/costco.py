import scrapy
import time
from datetime import datetime
# from the spider other file
from ..items import GroceryitemindexerItem



class AmazonWholeFood(scrapy.Spider):
    name = 'costco'   
    foodSection = 'frozen'
    pageNumber = 1

    def start_requests(self): 
        start_url = 'https://www.costco.ca/grocery-household.html'
        yield scrapy.Request(url=start_url, callback=self.parse)
            
    def parse(self,response):  

        groceryItem = GroceryitemindexerItem()
        self.logger.info(f'----------------------------start of page: {AmazonWholeFood.pageNumber}--')
        yield response.body('title')
        self.logger.info(f'----------------------------end of page: {AmazonWholeFood.pageNumber}--')

        #* part 1 extract href and titles
        regexHref = r'(https:\/\/flyers\.smartcanucks\.ca\/.+)'
        # for i in range(len(response.css('li a::Attr(href)').getall())):
        #     text = response.css('li a::Attr(href)')[i].getall().pop()
        #     x = re.search(regex,text)
        #     if x:
        #         print(x.groups())
        regexTitle = r'^(?!.*View Flyer)(?!.*\d).*$'