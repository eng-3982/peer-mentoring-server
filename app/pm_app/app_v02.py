#!/usr/bin/env python

# File: app_v02.py
# Author: Daniel Douglas, Claire Durand

import sys, os
from flask import Flask, request, Response, jsonify
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from flask.ext.bcrypt import Bcrypt
from models import User

# Move to the directory that contains the interfacing script to import it
# (I'm actually pretty proud of this line because it means I can call server.py from anywhere)
sys.path.append(os.path.join(os.path.dirname(__file__),'..','app-interface'))
import database

# Create the application
#
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

# Create the bcrypt object
#
bcrypt = Bcrypt(app)

# Initialize login manager instance
#
login_manager = LoginManager()
login_manager.init_app(app)


# Provide method for login manager to load a user
@login_manager.request_loader
def load_user(request):
    # Look for token in Authorization headers or request
    # arguments
    #
    print 'XXXX', request.authorization
    print 'YYYY', request.headers
    token = request.headers.get('Username'),request.headers.get('Password')
    if token is None:
        token = request.args.get('token')

    # Once we have the token, check for a match
    #
    if token is not None:
        
        print 'token is ', token
        username, request_password = token[0],token[1] # ASSUMING A NAIVE TOKEN
        
        # get the user information from class parameters
        #
        user_entry = User.get(username)
        print 'user entry is ', user_entry

        # Create User() object from information
        #        
        if (user_entry is not None):           
            
            user = User(user_entry['name'], user_entry['password'])
            print 'user is ', user
            # If authentication info is correct, return user instance
            # We also decrypt the database password here
            #
            if bcrypt.check_password_hash(user.password, request_password):
               # login_user(user)
                return user
        # If authenticaton fails, return None
        #
        return None
    

# Logout user
@app.route('/logout/')
def logout():
    logout_user()
    return Response(response='Signed Out\n', status=200)


# Default URL operations
@app.route('/')
def home_page():
    
    # Print simple welcome message
    #
    return 'Welcome to Peer-Mentoring App\n'


# Data fetch and post operations
@app.route('/data/', methods=['POST', 'GET'])
def data():
    
    print 'HEADERS', request.headers

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


# Authenticated user operation
@app.route('/private/', methods=['GET', 'POST'])
@login_required    # this line makes the route requre authentication
def private():
    return Response(response='success', status=200)

if __name__ == '__main__':
    # Run the app on all interfaces in debug mode
    # debug mode will restart server is this file changes.
    app.run(host='0.0.0.0', port=22000, debug=True)
    