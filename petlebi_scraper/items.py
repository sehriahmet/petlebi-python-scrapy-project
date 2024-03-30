# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PetlebiScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

def serialize_price(value):
    return f'{str(value)} TL'

class petlebiItem(scrapy.Item):
   url = scrapy.Field()
   name = scrapy.Field()
   barcode = scrapy.Field()
   price = scrapy.Field()
   stock = scrapy.Field()
   images = scrapy.Field()
   description = scrapy.Field()
   category = scrapy.Field()
   brand = scrapy.Field()