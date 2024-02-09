import scrapy
from pymongo import MongoClient
from scrapy.utils.project import get_project_settings
import os
from flask import render_template

class FranceFleursSpider(scrapy.Spider):
    name = 'francefleurs'
    start_urls = ['https://www.francefleurs.com/428-roses']

    def __init__(self):
        mongo_uri = os.environ.get('MONGO_URI', 'mongodb://localhost:27017')
        mongo_db = os.environ.get('MONGO_DATABASE', 'default_db')
        self.client = MongoClient(mongo_uri)
        self.db = self.client[mongo_db]
        
    def parse(self, response):
        
        for product in response.css('div.product-container'):
            item = {
                'title': product.css('a.product-name::text').get().strip(),
                'price': product.css('span.price.product-price::text').get().strip()
            }
            self.db['products'].insert_one(item)  # Insert into MongoDB

        next_page = response.css('a.pagination_next_bottom::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def close(self, reason):
        self.client.close()
