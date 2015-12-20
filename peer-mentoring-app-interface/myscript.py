from flask import jsonify
from pymongo import MongoClient

client = MongoClient()
db = client.primer
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

def post(name):
    print "Innerds of post"
    x = coll.insert_one({"major":name})
    return 'a'   # return bullshit bc flask is angry

if __name__ == '__main__':
    pass    # pass does nothing
