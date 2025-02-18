import scrapy

class SeoSpider(scrapy.Spider):
    name = "seo_spider"  #
    start_urls = ['https://www.ritrjpm.ac.in/']  

    def parse(self, response):
        title = response.css('title::text').get()
        meta_description = response.css('meta[name="description"]::attr(content)').get()
        yield {
            'url': response.url,
            'title': title,
            'meta_description': meta_description,
        }
