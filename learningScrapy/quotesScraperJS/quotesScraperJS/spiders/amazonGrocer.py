import scrapy
import time
import random 

class WholeFood(scrapy.Spider):

    name = 'wholeFood'
    #start_urls = ['https://www.amazon.ca/gp/browse.html?node=6967215011&ref_=nav_em__gro_0_2_16_2']
    pageNumber = 2
    start_urls = [f'https://www.amazon.ca/s?rh=n%3A6967215011%2Cn%3A%216967216011%2Cn%3A7351586011&page={pageNumber}&qid=1605678691&ref=lp_7351586011_pg_{pageNumber}']
    # def parse(self,response):
    #     for item in response.css('#search-results .s-result-item'):
    #         self.logger.info(f'------ looping ------')
    #         yield {
    #             'title': item.css('.a-link-normal::attr(title)').get(),
    #             'url':item.css('.a-link-normal.s-access-detail-page.s-color-twister-title-link::attr(href)').get(),
    #             'non-discounted price' : item.css('.a-color-price::text').get(),#check if we need getall after
    #             'rating' : item.css('.a-popover-trigger .a-icon-alt::text').get()
                
    #             #'num reviews': item.css('.a-size-small.a-link-normal.a-text-normal').get()
    #         }
    #     self.logger.info(f'------ after loop ------')

     

    def parse(self,response):

        # manual check that the 200 reponse returned  
        self.logger.info(f'------response for: {response.url} is ready----------')
        

        for i in range(len(response.css('.a-color-base.a-text-normal::text').getall()) -1):
            self.logger.info(f'------ before looping ------')
            try: #slow I know
                yield {
                    'name' : response.css('.a-color-base.a-text-normal::text')[i].getall(),
                    'link' : response.css('.s-line-clamp-4 .a-link-normal::attr(href)')[i].getall(),
                    'rating' : response.css('.aok-align-bottom .a-icon-alt::text')[i].getall(),
                    'number of rating ' : response.css('.a-size-small .a-size-base::text')[i].getall()
                                        }
            except Exception as e:
                self.logger.info(f'error: {e}')
        self.logger.info(f'------ after loop ------')
            # Wait for random time (it would be best if I can hard)
        time.sleep(random.randint(1, 10))


        if WholeFood.pageNumber < 4:
            WholeFood.pageNumber += 1
            next_page = WholeFood.start_urls[0] # requi
            self.logger.info(f'next: {next_page}')
            yield scrapy.Request(next_page,callback=self.parse) # error is here

        ##to do 
        # create a new file(project)
        # use the items.py
        # figure out why you don't get anything
        # scrapy crawl wholeFood -o test.json