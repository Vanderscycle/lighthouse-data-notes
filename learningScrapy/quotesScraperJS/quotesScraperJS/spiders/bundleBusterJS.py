import scrapy
from scrapy_splash import SplashRequest


class g1(scrapy.Spider):

    name = 'bundleBuster'
    start_urls = 'https://www.realcanadiansuperstore.ca/Food/c/RCSS001000000000?navid=flyout-L2-Food'
    
    # splash
    # def start_requests(self):
    #     yield SplashRequest( # check the documentation as it finally makes sense
    #         url = self.start_urls,
    #         callback=self.parse,
    #         endpoint='render.html', 
    #         args={'wait': 4,'lua_source': 'script','html':1,'engine':'chromium'}
    #     )
    
    def start_requests(self):
        yield PuppeteerRequest(g1.start_urls, callback=self.parse)

    
    def parse(self,response):
        open('bundleBuster.html', 'wb').write(response.body)
        # manual check that the 200 reponse returned  
        self.logger.info(f'response for: {response.url} is ready')
        
        # saving the html page (ultimately mygoal)
        filename = response.url.split("/")[-1] + '.html' #-1 for the last /
        with open(filename, 'wb') as f:
            f.write(response.body)