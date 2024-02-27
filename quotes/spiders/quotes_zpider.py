import scrapy
import json
from quotes.items import QuotesItem

class QuotesZpiderSpider(scrapy.Spider):
    name = "quotes_zpider"
    allowed_domains = ["quotes.toscrape.com"]
    api_url = "http://quotes.toscrape.com/api/quotes?page={}"
    start_urls = [api_url.format(1)]

    def parse(self, response):
        quotes_item = QuotesItem()
        data = json.loads(response.text)

        for quote in data["quotes"]:
            quotes_item["author"] = quote["author"]["name"]
            quotes_item["tags"] = quote["tags"]
            quotes_item["quote"] = quote["text"]
            quotes_item["goodreads_link"] = quote["author"]["goodreads_link"]
        
        if data["has_next"]:
            next_page_number = data["page"] + 1
            yield response.follow(self.api_url.format(next_page_number), callback= self.parse)
        
        yield quotes_item
