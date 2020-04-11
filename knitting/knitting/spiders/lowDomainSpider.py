import scrapy
import json

class KnittingSpider(scrapy.Spider):
    name = "knittingLowDomain"

    def start_requests(self):
        with open('url.json', 'r') as file:
            file.readline()
            data = []
            for line in file.readlines():
                data.append(line.split(',')[0])
        for url in data[:-4]: # one ']' and 3 not wanted links
            if url is not None: 
                yield scrapy.Request(url=json.loads(url)['url'], callback=self.parse)

    def parse(self, response):
        print('im in parse---')
        for product in response.css('div.product'):
            yield {
                'url': response.urljoin(product.css('a').attrib['href']),
                'category': response.url.split('.cz')[1]
                }
