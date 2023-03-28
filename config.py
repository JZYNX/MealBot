from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client['mealbot']
collection = db['fav']
personal_collection = db['personal']

