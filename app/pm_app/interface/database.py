# File: database.py
# Author: Daniel Douglas, Claire Durand

from ast import literal_eval
from flask import jsonify
from pymongo import MongoClient
import os.path, subprocess

client = MongoClient()
db = client.db_00
user_coll = db.users

# Define the function to print out all data 
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

# Function to return a single user's information sans password
# Huzzah
#
def user_info(username):
    
    # Lookup the user in database
    #
    parsed_user = db.users.find_one({'name':username})
    
    # We don't want to return the user's password or _id
    #
    del parsed_user['password']
    del parsed_user['_id']
    return parsed_user

# Function to add values to the database
#
def post(name,passwd):

    print "POSTING TO DATABASE"
    try:
        x = user_coll.insert({'name':name, 'password':passwd})
        subprocess.check_call(['touch', 'app/runserver.py']) 
        return 'Entry was added successfully\n'

    except :
        return 'Username is not available\n'

# Function to update user attributes of one field
# If field does not exist, it is created
#
def update_field(username, *kvargs):
    
    # kvargs should contain only dictionaries
    # come at me.
    if all(isinstance(kv, dict) for kv in kvargs):
        
        # Parse the new information to be added
        #
        for kv in kvargs:

            # Update the database with new information
            db.users.update_one(
                {'name':username},
                {'$set':kv})

        return 'User information was updated\n'

    return 'Oops, something went wrong :(\nUser information was not changed\n'
        
# Function to remove a user from the database
# Woooo party
#
def rm_user(username):
    db.users.delete_one(
        {'name':username}
    )

# Function to search database and return the matches. 
# This is a logical AND match operation, only users
# who match all criterion provided are returned
#
def search(criterion):
    
    # Find search result within the database
    # build the results into dict
    # 
    matches = { 'name' : [ match['name'] for match in db.users.find(criterion) ] }
    
    return matches

# Function to match a user to mentors using a
# threshold significance number.
#
def match(profile):

    threshold = 0.6

    # Set fields to exclude from matching
    #
    exclude = ['name','lastname','admin','type']

    # Remove fields we don't to match against
    #
    n_profile = { key : profile[key] for key in profile if key not in exclude } 
   
    #----------------------------#
    ## Naive equal significance scoring This should definitely be improved.
    
    # Initialize our aggregate results
    #
    result = { name : 0 for name in data('users') }            
    total = float(len(n_profile.keys()))

    # Perform the scoring against users in the db
    #
    for name in result.keys():
        for val in n_profile.keys():
            if n_profile[val] == data('users').get(name)[val]:
                result[name] += 1
        if abs( n_profile['age'] - data('users').get(name)['age'] ) <= 3:
            result[name] += 1

    # Remove from results the matches that do
    # do not pass the threshold
    #
    matches = { name : '%s%%' % (result[name]/total*100) for \
                name in result if (result[name] / total) >= threshold }
  
    return matches
    
        
if __name__ == '__main__':
    pass    # pass does nothing
