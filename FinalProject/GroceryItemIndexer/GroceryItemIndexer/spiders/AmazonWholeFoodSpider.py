import scrapy
import readline

import time
import re
import random 
from datetime import datetime
# from the spider other file
from ..items import GroceryitemindexerItem
# init 
class AmazonWholeFood(scrapy.Spider):
    # variable name required to run scrtapy crawl
    name = 'AWFSpider'
    started = False
    pageNumber = 7
    foodSection = 'Gourmet Gifts'
    start_urls = [f'https://www.amazon.ca/s?rh=n%3A6967215011&page={pageNumber}&qid=1605815840&ref=lp_6967215011_pg_{pageNumber}']
    
    # def start_requests(self,response=''): <- where the issue is rn
    #     # we want to scrape the first page
    #     if not AmazonWholeFood.started:
    #         AmazonWholeFood.started = True
    #     yield {
    #         scrapy.Request(url=AmazonWholeFood.start_urls[0] ,callback=self.parse)
    #     }
    #
        # else:
        #     catIndex = categorieUrls(response)
        #     for k,v in catIndex.items:
        #         print(f'key/value: {k} : {v}')
            
    def timestampReceival(self):
        now = datetime.now()
        return  now.strftime("%m/%d/%Y, %H")

    # eventually I'd to create a list with url + type
    

    def parse(self,response):# could add the category and the url 
        
        catIndex = self.categorieUrls(response)
        for k,v in catIndex.items():
            print(f'key/value: {k} : {v}')


        groceryItem = GroceryitemindexerItem()

        # manual check that the 200 reponse returned  
        self.logger.info(f'\n----------------------------------------start page: {AmazonWholeFood.pageNumber} -- for: {response.url} is ready---------- \n')
        
        for i in range(0,len(response.css('.a-color-base.a-text-normal::text').getall())):
            try:
                self.logger.info(f'item number:{i} of page:{AmazonWholeFood.pageNumber} \n')
                groceryItem['name'] = response.css('.a-color-base.a-text-normal::text')[i].getall().pop()
                #getall() returns a list containing strings. so we pop the element
                groceryItem['price'] = float((response.css('.a-price span .a-price-whole::text')[i].getall().pop()) + 
                    '.' + response.css('.a-price span .a-price-fraction::text')[i].getall().pop())
                groceryItem['currency'] = response.css('.a-price-symbol::text')[i].getall().pop()
                groceryItem['rating'] = response.css('.aok-align-bottom .a-icon-alt::text')[i].getall().pop()
                groceryItem['numberOfRating'] = response.css('.a-size-small .a-size-base::text')[i].getall().pop()
                groceryItem['link'] = response.css('.s-line-clamp-4 .a-link-normal::attr(href)')[i].getall().pop()
                groceryItem['spider'] = AmazonWholeFood.name
                groceryItem['section'] = AmazonWholeFood.foodSection
                groceryItem['time'] = self.timestampReceival()
                yield groceryItem
            # some issue as some items falls outside detectable range
            except Exception as e:
                # most common error: IndexError: list index out of range
                self.logger.info(f'error: {e}')

        self.logger.info(f'-------------------------------------------end page: {AmazonWholeFood.pageNumber}--')
        
        

        #delay for each robots since scrapy is asynchronous and can process up to 32 parse/spiders
        time.sleep(random.randint(1, 5))
        
        # loop from page 2 to the end
        #if AmazonWholeFood.next_page is not None:
        
        # test if
        if AmazonWholeFood.pageNumber < 3:
            AmazonWholeFood.pageNumber += 1
            next_page = 'https://www.Amazon.ca' + response.css('.a-last a::attr(href)').get()
            self.logger.info(f"{response.css('.a-last a::attr(href)').get()}")
            self.logger.info(f'-------Moving to page: {AmazonWholeFood.pageNumber} of {next_page}')
            # error above
            yield scrapy.Request(next_page,callback=self.parse)
        # we scraped the entire section
        else:
            # some program that move to another list category
            # return start_requests(response)
            pass





    def regexFunc(self,regexText,regex):

        cleanList = list()
        for line in regexText:

            z = re.search(regex, line)
            cleanList.append(z.groups(0))

        return cleanList

    def categorieUrls(self,response):
        regex = r'(?<=\/)(.+)(?=\/)'
        
        # This is where the error is as it returns the href
        # doesn't return me the same regex that I 
        #regexText = response.css('#departments li a::attr(href)').getall()
        #print(regexText)
        #catList = self.regexFunc(regexText,regex)

        # manual way
        catList = ['Baby-Food',
            'Beverages',
            'Breads-Bakery',
            'Breakfast-Food',
            'Candy-Chocolate',
            'Canned-Jarred-Foods',
            'Condiments-Pickles-Relishes',
            'Cooking-Baking-Supplies',
            'Dried-Beans-Grains-Rice',
            'Dried-Fruits-Raisins',
            'Gourmet-Gifts',
            'Herbs-Spices-Seasonings',
            'Home-Brewing-Winemaking',
            'Jams-Jellies-Sweet-Spreads',
            'Oils-Vinegars-Salad-Dressings',
            'Packaged-Meals-Side-Dishes',
            'Pasta-Noodles',
            'Sauces-Gravies-Marinades',
            'Snack-Food']
        urlReady = [ 'https://www.Amazon.ca'+ response.css('#departments li a::attr(href)')[i].getall().pop() for i in range(len(response.css('#departments li a::attr(href)').getall()))]
        
        urlCategory = dict()
        for i in range(len(urlReady)):

            urlCategory[catList[i]] = urlReady[i]
        return urlCategory

# # finding a way to loop through website
# using fetch('https://www.amazon.ca/s?rh=n%3A6967215011&page=2&qid=1605815840&ref=lp_6967215011_pg_2')
# # it is much easier to scrape on the second page 
# 
# # From any of the second page returns all the amazon list links that are required  
# response.css('#departments li a::attr(href)').getall() 

# # you add https://www.Amazon.ca + hreflink
# # we are now on the first page of the link
# fetch('https://www.amazon.ca/Herbs-Spices-Seasonings/b?ie=UTF8&node=7352114011')
# response.css('#pagnNextLink::Attr(href)').getall()
# you add https://www.Amazon.ca + hreflink
# You are now on the 2nd page of the {}
# # Scrape


#  {type of grocery{} in {list of type of grocery link}
#       Go to the second page
#       Scrape everything

#       Randdelay per robot request

#       if {nextpagelink} is not None:
#           Go to the next page until (finished)
#       else:
#           Go back to the start of the loop