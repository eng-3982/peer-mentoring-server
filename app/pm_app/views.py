#!/usr/bin/env python

# File: views.py
# Author: Daniel Douglas, Claire Durand

from pm_app import app
import sys, os
from flask import Flask, request, Response, jsonify
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from flask.ext.bcrypt import Bcrypt
from models import User

# Move to the directory that contains the interfacing script to import it
# (I'm actually pretty proud of this line because it means I can call server.py from anywhere)
sys.path.append(os.path.join(os.path.dirname(__file__),'..','app_interface'))
import database

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

    
