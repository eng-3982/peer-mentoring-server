from pymongo import MongoClient
client = MongoClient()

coll = client.primer.dataset

cursor = coll.find()

for c in cursor:
    print c
