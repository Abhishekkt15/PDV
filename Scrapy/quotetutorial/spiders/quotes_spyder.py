# -*- coding: utf-8 -*-

import scrapy

from ..items import QuotetutorialItem 



class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com'
        ]
    
    def parse(self, response):
        
        items = QuotetutorialItem()
        
        all_div_quotes = response.css('div.quote')
        
        for quotes in all_div_quotes:
            
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()
            
            items['title'] = title
            items['author'] = author
            items['tag'] = tag
        
        
            yield items

 #   def parse(self, response):
  #      all_div_quotes = response.css('div.quote')[0]
  #      title = all_div_quotes.css('span.text::text').extract()
   #     author = all_div_quotes.css('.author::text').extract()
    #    tag = all_div_quotes.css('.tag::text').extract()
     #   yield{
      #     'author':author,
        #    'tag':tag
         #   }
         
 #   def parse(self, response):
  #      all_div_quotes = response.css('div.quote')[0]
   #     for quotes in all_div_quotes:
    #        title = quotes.css('span.text::text').extract()
     #       author = quotes.css('.author::text').extract()
      #      tag = quotes.css('.tag::text').extract()
       #     yield{
        #            'title' : title,
         #         'tag':tag
           #         }