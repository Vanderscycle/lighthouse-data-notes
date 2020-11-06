import scrapy
from scrapy_splash import SplashRequest
import re
# by default, Scrapy runs a single spider per process when you run scrapy crawl
class JavaScriptLearner(scrapy.Spider):
    #class variables are shared between all class instances but there is only one instance
    name = 'JScraper'
    itemNum = 0
    resultDict = dict()
    # This method must return an iterable with the first Requests to crawl for this spider. It is called by Scrapy when the spider is opened for scraping. 
    start_urls = ['https://www.newegg.ca/LCD-LED-Monitors/SubCategory/ID-20?Tid=166066']

    # if you get no answer with splash and no crashes check without splash
    # def start_requests(self):
    #     yield SplashRequest(
    #         url = 'https://www.newegg.ca/LCD-LED-Monitors/SubCategory/ID-20?Tid=166066',
    #         callback=self.parse
    #     )
    # The parse method is in charge of processing the response and returning scraped data and/or more URLs to follow.
    def parse(self,response):
        self.logger.info(f'------ before loop ------')
        for item in response.css('.item-container'):
            self.logger.info(f'------ looping ------')
            yield {

                'price' : item.css('.price-was-data::text').get(),
                'item' : item.css('.item-title::text').get(),
                'discount' : item.css('.price-save-percent::text').get(),
                'Shipping cost' : item.css('.price-ship::text').get(),
                'rating' : item.css('.item-rating::attr(title)').get()#,
                }

        self.logger.info(f'------ after loop ------')

        # manual check that the 200 reponse returned  
        self.logger.info(f'response for: {response.url} is ready')

        # saving the html page (ultimately mygoal)
        filename = response.url.split("/")[-1] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)