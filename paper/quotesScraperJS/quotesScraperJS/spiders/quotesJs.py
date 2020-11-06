import scrapy
from scrapy_splash import SplashRequest

class QuotesJSSpider(scrapy.Spider):
    name = 'quotesJS'

    def start_requests(self):
        yield SplashRequest(
            url = 'https://quotes.toscrape.com/',
            callback=self.parse
        )
    
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {

                'text' : quote.css('span.text::text').extract_first(),
                'author' : quote.css('small.author::text').extract_first()
            }

# The HTML tags are generated from a JSON fiel hence why its not picked up 