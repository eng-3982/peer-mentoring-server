# File: database.py
# Author: Daniel Douglas, Claire Durand

from flask import jsonify
from pymongo import MongoClient

client = MongoClient()
db = client.db_00
user_coll = db.users

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
    # Indexes the dictionary !!by username!! not unicode id
    # This is one of the most important clauses in the entire codebase
    #
    for c in cursor:
        result[c['name']]=c
    return result

# function to return a single user's information sans password
# Huzzah
#
def user_info(username):
    parsed_user = db.users.find_one({'name':username})
    del parsed_user['password']
    del parsed_user['_id']
    return parsed_user

# Function to add values to the database
#
def post(name,passwd):

    print "POSTING TO DATABASE"
    x = user_coll.insert({'name':name, 'password':passwd})
    return 'Entry was added successfully\n'

if __name__ == '__main__':
    pass    # pass does nothing

# Function to update user attributes of one field
# If field does not exist, it is created
#
def update_field(username, new_information):
    db.users.update_one(
        {'name':username},
        {'$set':new_information}) 
        
# Function to remove a user from the database
# Woooo party
#
def rm_user(username):
    db.users.delete_one(
        {'name':username}
    )
