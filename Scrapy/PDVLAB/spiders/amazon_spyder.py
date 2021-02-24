# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 09:46:20 2021

@author: Abhis
"""

import scrapy
from ..items import PdvlabItem

class Amazon(scrapy.Spider):
    page_number = 2
    name = 'amazon'
    start_urls = [
        
    'https://www.amazon.in/s?i=electronics&bbn=1389401031&rh=n%3A1389401031%2Cp_89%3ARedmi%7CSamsung&dc&qid=1611371966&rnid=3837712031&ref=sr_nr_p_89_1'
    
    ]
    
    def parse(self, response):
        
        items = PdvlabItem()
        
        model_name = response.css(".a-color-base.a-text-normal::text").extract()
        price = response.css(".a-price-whole::text").extract()
        ratings = response.css(".aok-align-bottom span.a-icon-alt::text").extract()
        Delivery_type=response.css(".sg-col-12-of-16:nth-child(16) .s-align-children-center span , .sg-col-12-of-16:nth-child(15) .s-align-children-center span , .sg-col-12-of-16:nth-child(4) .s-align-children-center span , .AdHolder+ .sg-col-12-of-16 .s-align-children-center span , .s-align-children-center .s-align-children-center+ .a-row span").xpath('@aria-label').getall()
            
        for (model_name,price,ratings,Delivery_type) in zip(model_name,price,ratings,Delivery_type):
            items['model_name'] = model_name
            items['price'] = price
            items['ratings'] = ratings
            items['Delivery_type'] = Delivery_type
            
            yield items
        
        next_page = "https://www.amazon.in/s?i=electronics&bbn=1389401031&rh=n%3A1389401031%2Cp_89%3ARedmi%7CSamsung&dc&page=2&qid=1611371970&rnid=3837712031&ref=sr_pg_"+str(Amazon.page_number)
        if Amazon.page_number < 5:
           yield response.follow(next_page,callback=self.parse)
           Amazon.page_number += 1