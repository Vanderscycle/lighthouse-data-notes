import scrapy
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

    pageNumber = 1
    foodSection = 'Baby-Food'
    idxKey = 0
    catIndex = {
 0: ('https://www.Amazon.ca/s?i=grocery&bbn=6967216011&rh=n%3A6967215011%2Cn%3A7351088011&dc&qid=1605898257&rnid=6967216011&ref=sr_nr_n_1',
  'Baby-Food'),
 1: ('https://www.Amazon.ca/s?i=grocery&bbn=6967216011&rh=n%3A6967215011%2Cn%3A7351094011&dc&qid=1605898257&rnid=6967216011&ref=sr_nr_n_2',
  'Beverages'),
 2: ('https://www.Amazon.ca/s?i=grocery&bbn=6967216011&rh=n%3A6967215011%2Cn%3A7351153011&dc&qid=1605898257&rnid=6967216011&ref=sr_nr_n_3',
  'Breads-Bakery'),
 3: ('https://www.Amazon.ca/s?i=grocery&bbn=6967216011&rh=n%3A6967215011%2Cn%3A7351255011&dc&qid=1605898257&rnid=6967216011&ref=sr_nr_n_4',
  'Breakfast-Food'),
 4: ('https://www.Amazon.ca/s?i=grocery&bbn=6967216011&rh=n%3A6967215011%2Cn%3A7351266011&dc&qid=1605898257&rnid=6967216011&ref=sr_nr_n_5',
  'Candy-Chocolate'),
 5: ('https://www.Amazon.ca/s?i=grocery&bbn=6967216011&rh=n%3A6967215011%2Cn%3A7351796011&dc&qid=1605898257&rnid=6967216011&ref=sr_nr_n_6',
  'Canned-Jarred-Foods'),
 6: ('https://www.Amazon.ca/s?i=grocery&bbn=6967216011&rh=n%3A6967215011%2Cn%3A7351893011&dc&qid=1605898257&rnid=6967216011&ref=sr_nr_n_7',
  'Condiments-Pickles-Relishes'),
 7: ('https://www.Amazon.ca/s?i=grocery&bbn=6967216011&rh=n%3A6967215011%2Cn%3A7351934011&dc&qid=1605898257&rnid=6967216011&ref=sr_nr_n_8',
  'Cooking-Baking-Supplies'),
 8: ('https://www.Amazon.ca/s?i=grocery&bbn=6967216011&rh=n%3A6967215011%2Cn%3A7352088011&dc&qid=1605898257&rnid=6967216011&ref=sr_nr_n_9',
  'Dried-Beans-Grains-Rice'),
 9: ('https://www.Amazon.ca/s?i=grocery&bbn=6967216011&rh=n%3A6967215011%2Cn%3A7352684011&dc&qid=1605898257&rnid=6967216011&ref=sr_nr_n_10',
  'Dried-Fruits-Raisins'),
 10: ('https://www.Amazon.ca/s?i=grocery&bbn=6967216011&rh=n%3A6967215011%2Cn%3A7351586011&dc&qid=1605898257&rnid=6967216011&ref=sr_nr_n_11',
  'Gourmet-Gifts'),
 11: ('https://www.Amazon.ca/s?i=grocery&bbn=6967216011&rh=n%3A6967215011%2Cn%3A7352114011&dc&qid=1605898257&rnid=6967216011&ref=sr_nr_n_12',
  'Herbs-Spices-Seasonings'),
 12: ('https://www.Amazon.ca/s?i=grocery&bbn=6967216011&rh=n%3A6967215011%2Cn%3A7351600011&dc&qid=1605898257&rnid=6967216011&ref=sr_nr_n_13',
  'Home-Brewing-Winemaking'),
 13: ('https://www.Amazon.ca/s?i=grocery&bbn=6967216011&rh=n%3A6967215011%2Cn%3A7352198011&dc&qid=1605898257&rnid=6967216011&ref=sr_nr_n_14',
  'Jams-Jellies-Sweet-Spreads'),
 14: ('https://www.Amazon.ca/s?i=grocery&bbn=6967216011&rh=n%3A6967215011%2Cn%3A7352211011&dc&qid=1605898257&rnid=6967216011&ref=sr_nr_n_15',
  'Oils-Vinegars-Salad-Dressings'),
 15: ('https://www.Amazon.ca/s?i=grocery&bbn=6967216011&rh=n%3A6967215011%2Cn%3A7352227011&dc&qid=1605898257&rnid=6967216011&ref=sr_nr_n_16',
  'Packaged-Meals-Side-Dishes'),
 16: ('https://www.Amazon.ca/s?i=grocery&bbn=6967216011&rh=n%3A6967215011%2Cn%3A7352268011&dc&qid=1605898257&rnid=6967216011&ref=sr_nr_n_17',
  'Pasta-Noodles'),
 17: ('https://www.Amazon.ca/s?i=grocery&bbn=6967216011&rh=n%3A6967215011%2Cn%3A7352295011&dc&qid=1605898257&rnid=6967216011&ref=sr_nr_n_18',
  'Sauces-Gravies-Marinades'),
 18: ('https://www.Amazon.ca/s?i=grocery&bbn=6967216011&rh=n%3A6967215011%2Cn%3A7352635011&dc&qid=1605898257&rnid=6967216011&ref=sr_nr_n_19',
  'Snack-Food')}
    def start_requests(self):            
        #start_urls = ['https://www.Amazon.ca/s?i=grocery&bbn=6967216011&rh=n%3A6967215011%2Cn%3A7351088011&dc&qid=1605856107&rnid=6967216011&ref=sr_nr_n_1']
        
        
        yield scrapy.Request(url=AmazonWholeFood.catIndex[0][0], callback=self.parse)
            
    def parse(self,response):# could add the category and the url 
        
        groceryItem = GroceryitemindexerItem()

        # manual check that the 200 reponse returned  
        self.logger.info(f'---------------------------start page: {AmazonWholeFood.pageNumber} -- for: {response.url} is ready---------- \n')
        
        if AmazonWholeFood.pageNumber ==1:
            pass
        
        else:
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
                    self.logger.info(f'-----------------error: {e}')

        self.logger.info(f'----------------------------end page: {AmazonWholeFood.pageNumber}--')
        
        

        #delay for each robots since scrapy is asynchronous and can process up to 32 parse/spiders
        #time.sleep(random.randint(1, 5))
        

        
        # skipping page 1
        if AmazonWholeFood.pageNumber == 1:

            AmazonWholeFood.pageNumber += 1
            try:
                # try the next url that leads on page 2

                next_page = 'https://www.Amazon.ca' + response.css('#pagn :nth-child(3) a::attr(href)').get()

            except Exception as e:
                # the second page exist
                self.logger.info(f'----could not move the second page-----------error: {e}')
                self.logger.info(f'next link: {response.css("#pagn :nth-child(3) a::attr(href)").get()}--')
                #catIndex = self.categorieUrls(response)
                self.changeCat(AmazonWholeFood.catIndex)
                next_page = AmazonWholeFood.start_urls
                 
            yield scrapy.Request(next_page,callback=self.parse)



        # loop from page 2 to the end
        #elif ((response.css('.a-last a::attr(href)').get() is not None) and (1<AmazonWholeFood.pageNumber)):
        # current test
        elif 1 < AmazonWholeFood.pageNumber <3:
            AmazonWholeFood.pageNumber += 1
            next_page = 'https://www.Amazon.ca' + response.css('.a-last a::attr(href)').get()
            self.logger.info(f'-------Moving to page: {AmazonWholeFood.pageNumber} of {next_page}')
            # error above
            requestProxy = scrapy.Request(next_page,callback=self.parse)

            yield requestProxy
        # category change since we have explored every single page
        else:

            #catIndex = self.categorieUrls(response)
            self.changeCat(AmazonWholeFood.catIndex)

            yield scrapy.Request(AmazonWholeFood.start_urls,callback=self.parse)
            # some program that move to another list category
            # return start_requests(response)
            # pass

    def timestampReceival(self):
        now = datetime.now()
        return  now.strftime("%m/%d/%Y, %H")


    def regexFunc(self,regexText,regex):

        cleanList = list()
        for line in regexText:

            z = re.search(regex, line)
            cleanList.append(z.groups(0))


        return cleanList


    def changeCat(self,catIndexDict):
        """ method that changes the category"""
        AmazonWholeFood.pageNumber = 1
        AmazonWholeFood.idxKey += 1
        AmazonWholeFood.start_urls = catIndexDict[AmazonWholeFood.idxKey][0] 
        AmazonWholeFood.foodSection = catIndexDict[AmazonWholeFood.idxKey][1]
        # print the CLI an update
        self.logger.info(f'\n \n-*-*-*------------------ Index -- {AmazonWholeFood.idxKey} -- \
        New Category:{AmazonWholeFood.foodSection} -- \
        New url: {AmazonWholeFood.start_urls} -------------------*-*-*-\n \n') 


    def categorieUrls(self,response): #* this is not working
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

            urlCategory[i] = (urlReady[i],catList[i])
        #self.logger.info(f'{urlCategory}')
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


# weird errors
# I was getting weird feed errors 
# https://stackoverflow.com/questions/37223700/why-does-scrapyd-throw-feedexporter-object-has-no-attribute-slot-exceptio
# they are non critical since when I remove -o awf.json they disappear

# key error 3 
# because categorieUrl was using the reponse everytime on 

#  0: ('https://www.Amazon.ca/s?i=grocery&bbn=6967216011&rh=n%3A6967215011%2Cn%3A7351088011&dc&qid=1605898257&rnid=6967216011&ref=sr_nr_n_1',  'Baby-Food'),