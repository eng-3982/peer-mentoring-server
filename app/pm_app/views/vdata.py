# File: vdata.py
# Author: Daniel Douglas, Claire Durand

from pm_app import app
from flask import request, Response, jsonify
from pm_app.models import User
from flask.ext.bcrypt import Bcrypt
from pm_app.interface import database
from flask_login import login_required, current_user

bcrypt = Bcrypt(app)

# Data fetch and post operations
@app.route('/data/', methods=['POST', 'GET'])
@login_required
def data():
    
    print 'HEADERS::\n', request.headers

    # If the request method is GET..
    #
    if request.method == 'GET':
        
        # Print the key/value data in the database
        #
        return jsonify(database.data('users'))

    # If the request method is POST
    #
    else:
        
        # Add the key/values in request to the database
        #
        name = request.headers.get('Username')
        password = request.headers.get('Password')
        
        # If both fields are present in the request,
        # add the user information to the database
        #
        if (name and password):
            # Encrypt password
            #
            password = bcrypt.generate_password_hash(password)
            return database.post(name,password)
        else:
            # Raise error code 400=BAD REQUEST
            #
            return Response(response="Required Field's Empty", status=200)

# Update user information
@app.route('/data/update/', methods=['POST'])
@login_required
def update_info():
    update_data = request.headers.get('Updates')
    return dict(update_data)

# Delete user instance
@app.route('/data/rm/', methods=['POST'])
@login_required
def rm_instance():
    # Get user name of the user to ELIMINATE
    user_rm = request.headers.get("Username")
    database.rm_user(user_rm)
    return Response(response="User removed", status=200)
