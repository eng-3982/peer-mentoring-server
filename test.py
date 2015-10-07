from flask import jsonify
from pymongo import MongoClient

client = MongoClient()
db = client.primer
coll = db.dataset

coll.insert_one({"major":"Kicking ass"})
   



