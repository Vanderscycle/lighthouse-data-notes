import scrapy
from scrapy_splash import SplashRequest
import re

testDict = dict()
def placeHolderName(i,response):
    RatingCountRegex = r'[\d]+\,[\d]+'
    ratingResponse = response.css('div .item-container .item-rating-num::text')[i].extract()
    match = re.search(RatingCountRegex,ratingResponse)
    
    yield {

        'price' : response.css('div .item-container .price-was-data::text')[i].extract(),
        'item' : response.css('div .item-container .price-was-data::text')[i].extract(),
        'discount' : response.css('div .item-container .price-save-percent::text')[i].extract(),
        'Shipping cost' : response.css('div .item-container .price-ship::text')[i].extract(),
        'rating' : response.css('div .item-container .item-rating::attr(title)')[i].extract(),
        'rating num' : match[0]
        }
class PostsSpider(scrapy.Spider):
    name ='gSpider'

    def start_requests(self):
        yield SplashRequest(
            url = 'https://www.newegg.ca/Video-Cards-Video-Devices/Category/ID-38',
            callback=self.parse
        )
    

    
    def parse(self, response):
        
        # manual check that the 200 reponse returned  
        self.logger.info('A response from %s just arrived!', response.url)

        # saving the html page
        filename = response.url.split("/")[-1] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

        #RatingCountRegex = r'[\d]+\,[\d]+'

            # extracting the relevant info to a json
        self.logger.info('I am before the loop')

        # the issue is with the loop
        rowNum=0
        for item in response.css('div .item-container'):

            #match = re.search(RatingCountRegex,item.css('.item-rating-num::attr(title)').extract_first())
            self.logger.info('I am in the loop')
            
            testDict[rowNum] = {

                'price' : item.css('.price-was-data::text').extract_first(),
                'item' : item.css('.price-was-data::text').extract_first(),
                'discount' : item.css('.price-save-percent::text').extract_first(),
                'Shipping cost' : item.css('.price-ship::text').extract_first(),
                'rating' : item.css('.item-rating::attr(title)').extract_first()#,
                #'rating num' : match[0]
                }
            rowNum +=1
        self.logger.info('price: %s', 'I am after the loop')
        return testDict
        # the extract here doesn't work
        # extracting the relevant info to a jsonk
        # i = 1
        # RatingCountRegex = r'[\d]+\,[\d]+'
        # ratingResponse = response.css('div .item-container .item-rating-num::text')[i].extract()
        # match = re.search(RatingCountRegex,ratingResponse)
        
        # yield {

        #     'price' : response.css('div .item-container .price-was-data::text')[i].extract(),
        #     'item' : response.css('div .item-container .price-was-data::text')[i].extract(),
        #     'discount' : response.css('div .item-container .price-save-percent::text')[i].extract(),
        #     'Shipping cost' : response.css('div .item-container .price-ship::text')[i].extract(),
        #     'rating' : response.css('div .item-container .item-rating::attr(title)')[i].extract(),
        #     #'rating num' : match[0]
        #     }

        
            
# manual CLI extraction

#extracting the name of container + some garbage we can use regex or a python condition
# Offers
# Repalcement

# import re
# response.css('div .item-container a::text').getall()
# regex = r'^((?![Oo]ffers).(?![Rr]eplacement))*$'
# newlist = list(filter(re.compile(regex).match, searchRes))

#better way?
# response.css('div .item-container .item-title::text')[0:5].getall()

#'make sure to remove [:1] and the gettall()'
# price (normally)
# response.css('div .item-container .price-was-data::text')[:1].getall()

# discount (percent)
#response.css('div .item-container .price-save-percent::text')[:1].getall()

#shipping price
# response.css('div .item-container .price-ship::text')[:1].getall()

#rating
# response.css('div .item-container .item-rating::attr(title)')[:1].getall()

#rating num
# response.css('div .item-container .item-rating-num::text')[:1].getall()

#debugging can be a nightmare
# extract/get are not the same (check the objects)
# how does this parse/start request work? let's explain the process that the crawler goes through
