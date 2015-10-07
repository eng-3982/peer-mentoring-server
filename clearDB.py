from flask import jsonify
from pymongo import MongoClient

client = MongoClient()
db = client.primer
coll = db.dataset

deleted = coll.delete_many({})
