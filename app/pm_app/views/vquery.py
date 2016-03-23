# File: vquery.py
# Author: Daniel Douglas, Claire Durand

from pm_app import app
from flask_login import login_required, current_user
from pm_app.interface import database
from flask import request, Response, jsonify

# Data query and search operations.
# Search the database for users whose fields match
# the query. This is a logical AND matching function
# which returns only results that match all criterion
# provided.
@app.route('/query/search/', methods=['GET', 'POST'])
@login_required
def query_search():
    
    print 'QUERY SEARCH'

    # Get the JSON object containing search criterion
    #
    search_criterion = request.get_json() 
    print search_criterion


    # Return the matched mentors 
    # 
    search_result = database.search(search_criterion)
    print search_result
    return jsonify(search_result)


# Data query and match operations
@app.route('/query/match/', methods=['GET', 'POST'])
@login_required
def query_match():
    
    print 'QUERY MATCH'

    # Load the current users profile information
    #
    user_profile = database.user_info(current_user.id)

    # Perform significance matching
    #
    match_result = database.match(user_profile)

    return jsonify(match_result)
    


    
