import scrapy
import json

class ProductSpider(scrapy.Spider):
    name = 'productSpider'

    def start_requests(self):
        # with open('product.json', 'r') as file:
        #     data = []
        #     for line in file.readlines():
        #         data.append(line[:-1])
        #         print(line[:-1])
        with open('/Users/adam.stepanek/Desktop/Projects/knittingScraper/knitting/product.json', 'r') as file:
            data = json.loads(file.read())
        for item in data[1:-1]: # one '[' and one ']' 
            yield scrapy.Request(url=item['url'], callback=self.parse)

    def parse(self, response):
        yield {
            'name': response.css('h1::text').get(),
            'url': response.url,
            'category': response.url.split('.cz')[1], 
            'prize': response.css('div.c1305 span.c2009::text').get().split()[0],
            'stock': response.css('div.c1305 div.c757::text').get().split()[1],
            'description': ''.join(response.css('div.main-grid div.detail div.c85 div.c89 span::text').getall() + response.css('div.main-grid div.detail div.c85 div.c89 p::text').getall())
        }
