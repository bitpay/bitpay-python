from pymongo import MongoClient

print("clearing rate limiters")
client = MongoClient()
db = client['bitpay-dev']
collection = db['ratelimiters']
collection.remove()
print("rate limters removed")
