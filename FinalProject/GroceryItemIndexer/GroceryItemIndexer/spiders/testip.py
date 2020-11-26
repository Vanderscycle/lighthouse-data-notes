import scrapy
from datetime import datetime
from ..items import IpTimestamp,

def timestampReceival():
    now = datetime.now()
    return  now.strftime("%m/%d/%Y, %H")

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
