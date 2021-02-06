from pymongo import MongoClient
client = MongoClient('127.0.0.1', 28000)

db = client.factory

brands = db.brands
brands.insert_one({"name": "seat"})
brands.insert_one({"name": "Ford"})

brands.find_one({"name": "seat"})
brands.find_one({"name": "Ford"})