import scrapy
import json


class KnittingSpider(scrapy.Spider):
    name = "knittingTopDomain"

    def start_requests(self):
        urls = ['https://www.unezbednychklubicek.cz/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parseTopUrl)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

    def parseTopUrl(self, response):
        for li in response.css('div.container div.main-grid div.content-left div.c1191 ul li.c485'):
            yield {'url': response.urljoin(li.css('a').attrib['href'])}

    
