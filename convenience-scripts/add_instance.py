import sys
from flask import jsonify
from pymongo import MongoClient

# Setup the MongoDB client (to communicate with the DB) and give variable names
# to the database and document collection for convenience's sake
client = MongoClient()
db = client.primer
coll = db.dataset


# If the argument list argv (excluding the script name) is even, 
# increment through every two arguments and assign the first one to key
# and the second to value, adding each pair into the MongoDB dataset as key:value pairs
# Otherwise, if the user entered an odd number of arguments, the key value pairs match up.
# Print out an error message to the user, inviting him or her to try again.
if(len(sys.argv)%2 == 1):
    # Save the first key:value pair for reference
    key1 = sys.argv[1]
    value1 = sys.argv[2]
    coll.insert_one({key1:value1})

    # Update the instance with any remaining key value pairs
    # (Only occurs if user is trying to insert more than one key:value pair per document)
    if(len(sys.argv)>3):
        for i in range(3,len(sys.argv),2):
            key = sys.argv[i]
            value = sys.argv[i+1]
            
            coll.update(
                { key1 : value1 },
                { "$set": { key : value } }
            )
else:
    print "ERROR >>> You've entered an odd number of arguments. Please enter key:value pairs"
"""
coll.update(
    {"name": "Claire" },
    {"$set": {"major": "Electrical Engineering"} }
)
"""
   



