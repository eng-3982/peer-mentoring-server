from flask import jsonify
from pymongo import MongoClient

client = MongoClient()
db = client.db_00
coll = db.dataset

# define the function to print out all data 
# in database primer, collection dataset
def data():
    print "Innerds of data"
    cursor = coll.find({},{ '_id':0 })
    result = {}
    i = 0
    for c in cursor:
        result[str(i)]=c
        i+=1
    print result
    return jsonify(**result)

# Function to add values to the database
#
def post(name,passwd):
    
    print "POSTING TO DATABASE"
    x = coll.insert({"name":name, 'pass':passwd})
    return 'Entry was added successfully\n'

if __name__ == '__main__':
    pass    # pass does nothing
