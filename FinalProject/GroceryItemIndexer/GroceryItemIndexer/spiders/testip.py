import scrapy
from ..items import IpTimestamp,timestampReceival

class AmazonWholeFood(scrapy.Spider):
    # variable name required to run scrtapy crawl
    name = 'testip'
    
    def start_requests(self):
        urls = ['https://httpbin.org/ip']
        for url in urls:
            request = scrapy.Request(url=url, callback=self.parse)
            yield request

    def parse(self,response):
        ipInfo = IpTimestamp()
        ipInfo['ip'] = response.css('p::text').getall()
        ipInfo['time'] = timestampReceival()
        yield ipInfo
