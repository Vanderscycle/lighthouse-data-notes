import scrapy
import time
import re
from datetime import datetime
from ..items import FlyerItem, ImgData, timestampReceival
import random


class flyerSpider(scrapy.Spider):
    # class variable for crawl command
    name = 'fSpider'
    
    # If you have multiple spiders that have different pipelines it is easier to have it part of the main spider.
    custom_settings = {
        'ITEM_PIPELINES' : {
    'scrapy.pipelines.images.FilesPipeline': 1,
    'GroceryItemIndexer.pipelines.FlyerPipeline': 500,
        },
        'FILES_STORE' :"/home/henri/Documents/Lighthouse-lab/Databases/final project db/flyerScrapedData",
        # Scrapy filters duplicate requests by default, otherwise it 
        'DUPEFILTER_CLASS' : 'scrapy.dupefilters.BaseDupeFilter'
    }
    # exception handling? otherwise the data crashes
    # def process_exception(self, request, exception, spider):
    #     request.dont_filter = True
    #     return request

    # other relevan class variable
    stores = '' # dictionary of all stores names with urls
    currentStore = '' # the current store we are on
    storeFlyerDictRandom = '' # the store's associated flyers name/url in a random order
    storeCrawled = 0
    storeFlyerCrawled = 0


    def start_requests(self): 
        start_url = 'https://flyers.smartcanucks.ca/'
        yield scrapy.Request(url=start_url, callback=self.websiteSizingParser)

    def websiteSizingParser(self,response):
        self.logger.info(f'------- At home page of {response}')

        # we are at the homepage of smartcanucks
        regex = r'https:\/\/flyers\.smartcanucks\.ca\/[a-zA-Z0-9].+'
        # len >4 to filter out garbage single numbers
        href = [f for f in response.css('li a::Attr(href)').getall() if (re.search(regex,f)) and len(f) >4]
        name = [head.split('/')[-1] for head in href]

        # package them into a dictionary comprehension
        flyerSpider.stores = {i:[name [i], href[i]] for i in range(len(name))}
        # choosing the first destination randomly
        nextStore = self.randomUrl(flyerSpider.stores)
        
        flyerSpider.currentStore = nextStore[0]
        # CLI feedback
        self.logger.info(f'The following store was selected: {nextStore[0]} ; url: {nextStore[1]}')
        self.logger.info(f'--------short Break 6-18 seconds')
        time.sleep(random.randint(6, 18))
        yield scrapy.Request(url=nextStore[1], callback=self.storeParser)


    def storeParser(self,response):
        # eventually I will need a way to check the flyers otherwise I'm being a dick
        # in that case that would only be the first flyer in the list

        # every 50 stores crawled we want to stop
        if flyerSpider.storeFlyerCrawled%50==0 and flyerSpider.storeFlyerCrawled !=0:
            self.logger.info(f'--------long break 5-8 minutes')
            time.sleep(random.randint(5, 8)*60)

        # this is the first time we are in the store so we want to map out the flyers
        storeFlyerDict = self.urlDictPackager(response.css('.view-flyer a::attr(href)').getall())
        randomOrderDict = dict()
        for i in range(len(storeFlyerDict)):
            randomOrderDict[i] = self.randomUrl(storeFlyerDict)
        flyerSpider.storeFlyerDictRandom = randomOrderDict

        # range(len(nextFlyer))
        nextFlyer = self.randomUrl(flyerSpider.storeFlyerDictRandom)
        # add /all because that makes the website display all of the images.
        nextFlyer[1] += '/all'
        self.logger.info(f'store: {flyerSpider.currentStore} flyer name: {nextFlyer[0]}; url: {nextFlyer[1]}')
        
        yield scrapy.Request(url=nextFlyer[1], callback=self.flyerParser)
        

    def flyerParser(self,response): 

        if len(flyerSpider.storeFlyerDictRandom)>0:
            ## --we parse the content and yield the data

            flyerItemDjango = FlyerItem()           
            flyerItemDjango['store'] = flyerSpider.currentStore
            flyerItemDjango['flyersDate'] = response.css('#flyer-title::text').get()
            flyerItemDjango['spider'] = flyerSpider.name
            flyerItemDjango['timeScraped'] = timestampReceival()
            images = list()
            for idx, imgUrl in enumerate(response.css('img::attr(src)')[2:-1].getall()):
                flyerItemDjango['page'] = idx+1
                flyerItemDjango['file_urls']=[imgUrl]
                yield flyerItemDjango
            #     cleanImageUrls.append(response.urljoin(imgUrl))

            
            #  # returns all of the images url
            # yield {
            #     'image_urls' : cleanImageUrls
            # }
            # move to the next flyer
            flyerSpider.storeFlyerCrawled += 1
            nextFlyer = self.randomUrl(flyerSpider.storeFlyerDictRandom)
            self.logger.info(f'--------short Break 3-10 seconds')
            self.logger.info(f'crawled {flyerSpider.storeFlyerCrawled} flyers from {flyerSpider.currentStore} flyers left : {len(flyerSpider.storeFlyerDictRandom)}')
            self.logger.info(f'--------store: {flyerSpider.currentStore} flyer name:  {nextFlyer[0]} ; url: {nextFlyer[1]}')
            time.sleep(random.randint(3, 10))
            yield scrapy.Request(url=nextFlyer[1], callback=self.flyerParser)
        # there are nomore flyers to go through
        else:
            #CLI stats
            
            flyerSpider.storeCrawled += 1
            self.logger.info(f'--------we finished going through all {flyerSpider.storeFlyerCrawled} flyers in {flyerSpider.currentStore}')
            flyerSpider.storeFlyerCrawled = 0
            nextStore = self.randomUrl(flyerSpider.stores)
            # CLI feedback
            self.logger.info(f'The following store was selected: {nextStore[0]} ; url: {nextStore[1]}')
            self.logger.info(f' we have crawled:{flyerSpider.storeCrawled} stores our of {len(flyerSpider.stores)} stores')
            self.logger.info(f'--------short Break 3-10 seconds')
            time.sleep(random.randint(3, 10))
            flyerSpider.currentStore = nextStore[0]
            
            yield scrapy.Request(url=nextStore[1], callback=self.storeParser)
   
    # helper methods
    def randomUrl(self,dictionary):
        # we want to obtain a random index. Since we are passing a Dict Python wants a list
        randIdx = random.sample(list(dictionary),1)
        # since we do not want to visit the address again we remove it from the list
        selectedURL = dictionary.pop(randIdx[0])
        return selectedURL

    def urlDictPackager(self,responseList,regex=''):
        """
        Used when all the info is in the url of the href. Regex is optional
        Returns a dict
        """
        # url
        if regex:
            pass
        else:
            #>4 to clean number garbage
            href = [f for f in responseList if len(f) >4]
            # info from the url
            name = [head.split('/')[-1] for head in href]
            # dictionary comprehension
        return {i:[name [i], href[i]] for i in range(len(name))}
    