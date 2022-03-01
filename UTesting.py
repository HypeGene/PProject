import unittest
import scrapy
class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://www.github.com'

    ]
    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

    def start_requests(self):
        urls = [
            'https://www.github.com'
        ]
        for url in urls:
            yield scrapy.requests(url=url, callback=self.parse)
    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

if __name__ == '__main__':
    unittest.main()