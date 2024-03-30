import scrapy
from petlebi_scraper.items import petlebiItem  


class PetlebiScrapySpider(scrapy.Spider):
    name = "petlebi_scrapy"
    allowed_domains = ["www.petlebi.com"]
    start_urls = ["https://www.petlebi.com"]
    
    custom_settings = {
        'FEEDS': {
            'petlebi_products.json':{'format': 'json', 'overwrite': True},
        }
    }

    def parse(self, response):
        
        #yield response.follow("https://www.petlebi.com/kemirgen-petshop-urunleri", callback=self.parse_products_page)

        list = [
            "https://www.petlebi.com/kedi-petshop-urunleri",
            "https://www.petlebi.com/kopek-petshop-urunleri",
            "https://www.petlebi.com/kus-petshop-urunleri",
            "https://www.petlebi.com/kemirgen-petshop-urunleri"
        ]

        for i in list:
            yield response.follow(i, callback=self.parse_products_page)


    def parse_products_page(self,response):
        products = response.css('div.search-product-box')


        next_page = response.css('ul.pagination li:last-child  a ::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse_products_page)

        for product in products:
            url_product = product.css('a.p-link').attrib['href']
            yield response.follow(url_product, callback=self.parse_product_information)

    def parse_product_information(self,response):

        petlebi_item= petlebiItem()

        petlebi_item['url'] = response.url
        petlebi_item['name'] = response.css('h1.product-h1 ::text').get()
        petlebi_item['barcode'] = response.css('div.product-text-area div.mb-2 div.col-10::text').get()
        petlebi_item['price'] = response.css('span.new-price ::text').get()
        petlebi_item['stock'] = response.css('option:last-child ::text').get()
        petlebi_item['images'] = response.css('div.product-detail-main a::attr(href)').extract()
        petlebi_item['description'] = response.css('#productDescription').get()
        #'sku' : 
        petlebi_item['category'] = response.css('li.breadcrumb-item:last-child span[itemprop="name"]::text').get()
        #'product_id' : 
        petlebi_item['brand'] = response.css('div.brand-line a::text').get()


        yield petlebi_item


