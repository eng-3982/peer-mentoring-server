from flask import jsonify
from pymongo import MongoClient

client = MongoClient()
db = client.db_00
coll = db.users


# define the function to print out all data 
# in database db, coll
#
def data(collection_name):
    # Create the collection object
    #
    collexion = db[collection_name]

    # Import database minus the '_id' field
    #
    cursor = collexion.find({},{ '_id':0 })
    result = {}
    
    # Iterate over collection to create dictionary
    #
    for c in cursor:
        result[c['name']]=c
    return result

# Function to add values to the database
#
def post(name,passwd):

    print "POSTING TO DATABASE"
    x = coll.insert({'name':name, 'password':passwd})
    return 'Entry was added successfully\n'

if __name__ == '__main__':
    pass    # pass does nothing
