import scrapy
from ..items import QuotetutorialItem
class QuoteSpider(scrapy.Spider):
    page_number=2
    name='quotes'
    start_urls={
        'https://quotes.toscrape.com/'
    }


    def parse(self,response):
        # print("CRAWLING ON URL https://quotes.toscrape.com/page/ " +QuoteSpider.page_number)
        items=QuotetutorialItem()
        all_div_quotes=response.css('div.quote')


        for quotes in all_div_quotes:
                title=quotes.css('span.text::text').extract()
                author=quotes.css('.author::text').extract()
                tag=quotes.css('.tag::text').extract()


                items['title']=title
                items['author']=author
                items['tag']=tag


                yield items

        next_page=response.css('li.next a::attr(href)').get()
        print(next_page)
        if next_page is not None:
             yield response.follow(next_page,callback=self.parse) 
        # next_page='https://quotes.toscrape.com/page/'+str(QuoteSpider.page_number)+'/'
  
        # if QuoteSpider.page_number<11:
        #      QuoteSpider.page_number+=1
        #      yield response.follow(next_page,callback=self.parse)   

        
