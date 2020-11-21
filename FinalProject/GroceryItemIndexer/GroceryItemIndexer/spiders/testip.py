import scrapy

class AmazonWholeFood(scrapy.Spider):
    # variable name required to run scrtapy crawl
    name = 'testip'
    
    def start_requests(self):
        urls = ['https://httpbin.org/ip']
        for url in urls:
            request = scrapy.Request(url=url, callback=self.parse)
            yield request

    def parse(self,response):
        yield {
            'myip' : response.css('p::text').getall()
            #'myip' : response.css('.a-color-base.a-text-normal').getall()
        }
        