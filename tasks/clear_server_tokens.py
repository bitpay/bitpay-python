from pymongo import MongoClient

print("clearing tokens from server")
client = MongoClient()
db = client['bitpay-dev']
collection = db['tokenaccesses']
collection.remove()
print("tokens removed")

