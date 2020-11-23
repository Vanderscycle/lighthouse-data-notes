import scrapy
import time
import re
from datetime import datetime
from ..items import FlyerItem
import random


class flyerSpider(scrapy.Spider):
    name = 'fSpider'
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
        self.logger.info(f'--------short Break 3-10 seconds')
        time.sleep(random.randint(3, 10))
        flyerSpider.currentStore = nextStore[0]
        # CLI feedback
        self.logger.info(f'The following store was selected: {nextStore[0]} ; url: {nextStore[1]}')
        
        yield scrapy.Request(url=nextStore[1], callback=self.storeParser)


    def storeParser(self,response):
        # eventually I will need a way to check the flyers otherwise I'm being a dick

        # this is the first time we are in the store so we want to map out the flyers
        if storeFlyerCrawled%50==0:
            self.logger.info(f'--------long break 5-8 minutes')
            time.sleep(random.randint(5, 8)*60)


        storeFlyerDict = self.urlDictPackager(response.css('.view-flyer a::attr(href)').getall())
        randomOrderDict = dict()
        for i in range(len(storeFlyerDict)):
            randomOrderDict[i] = self.randomUrl(storeFlyerDict)
        flyerSpider.storeFlyerDictRandom = randomOrderDict

        # range(len(nextFlyer))
        nextFlyer = self.randomUrl(flyerSpider.storeFlyerDictRandom)
        self.logger.info(f'store: {flyerSpider.currentStore} flyer name: {nextFlyer[0]}; url: {nextFlyer[1]}')
        
        yield scrapy.Request(url=nextFlyer[1], callback=self.flyerParser)
        

    def flyerParser(self,response): 

        if len(flyerSpider.storeFlyerDictRandom)>0:
            ## --we parse the content and yield the data
            # create a specific pipeline and item class
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
            flyerSpider.storeFlyerCrawled = 0
            flyerSpider.storeCrawled += 1
            self.logger.info(f'--------we finished going through all the flyers in {flyerSpider.currentStore}')
            nextStore = self.randomUrl(flyerSpider.stores)
            self.logger.info(f'--------short Break 3-10 seconds')
            time.sleep(random.randint(3, 10))
            flyerSpider.currentStore = nextStore[0]
            # CLI feedback
            self.logger.info(f'The following store was selected: {nextStore[0]} ; url: {nextStore[1]}')
            self.logger.info(f' we have crawled:{flyerSpider.storeCrawled} stores our of {len(flyerSpider.stores)}')
            yield scrapy.Request(url=nextStore[1], callback=self.storeParser)
   
    # helper methods
    def randomUrl(self,dictionary):
        # we want to obtain a random index. Since we are passing a Dict Python wants a list
        randIdx = random.sample(list(dictionary),1)
        # since we do not want to visit the address again we remove it from the list
        # 
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
    