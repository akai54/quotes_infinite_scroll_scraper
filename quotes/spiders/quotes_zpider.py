import scrapy


class QuotesZpiderSpider(scrapy.Spider):
    name = "quotes_zpider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        pass
