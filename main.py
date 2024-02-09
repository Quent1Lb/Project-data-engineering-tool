from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrap import FranceFleursSpider
from flask import Flask, jsonify
from pymongo import MongoClient
import json
from bson import json_util

def main():
    


# Nom du fichier contenant votre spider, par exemple 'francefleurs_spider.py'
# from francefleurs_spider import FranceFleursSpider

    process = CrawlerProcess(get_project_settings())

    process.crawl(FranceFleursSpider)
    process.start()

app = Flask(__name__)

# Connexion à MongoDB
client = MongoClient("mongodb://mongo:27017")
db = client['MONGO_DATABASE']  

@app.route('/')
def index():
    # Récupération des données de MongoDB
    produits = list(db.produits.find())  # Remplacez par le nom de votre collection
    
    # Convertir les documents MongoDB en JSON
    return json.dumps(produits, default=json_util.default)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')