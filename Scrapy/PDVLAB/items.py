# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PdvlabItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    model_name = scrapy.Field()
    price = scrapy.Field()
    ratings = scrapy.Field()
    Delivery_type = scrapy.Field()
