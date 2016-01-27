import sys
from flask import jsonify
from pymongo import MongoClient

# Setup the MongoDB client (to communicate with the DB) and give variable names
# to the database and document collection for convenience's sake
client = MongoClient()
db = client.primer
coll = db.dataset


# If there is an item with name = Claire, this adds the key value major = Electrical Engineering to the instance
# Note that the $set option is necessary in order not to overwrite the original key:value
if(len(sys.argv)==5):
    coll.update(
        { sys.argv[1] : sys.argv[2] },
        { "$set" : { sys.argv[3] : sys.argv[4]} }
    )
else:
    print "ERROR>>>Please enter one key:value pair identifying the instance you'd like to update, and one key:value pair to add to the instance"

