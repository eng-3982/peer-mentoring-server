#!/usr/bin/env python

# File: views.py
# Author: Daniel Douglas, Claire Durand

from pm_app import app
import sys, os
from flask import Flask, request, Response, jsonify
from flask_login import LoginManager, login_required
from flask.ext.bcrypt import Bcrypt
from models import User

# Move to the directory that contains the interfacing script to import it
# (I'm actually pretty proud of this line because it means I can call server.py from anywhere)
#sys.path.append(os.path.join(os.path.dirname(__file__),'..','app_interface'))
#import database

# Default URL operations
@app.route('/')
def home_page():
    
    # Print simple welcome message
    #
    return 'Welcome to Peer-Mentoring App\n'


# Authenticated user operation
@app.route('/private/', methods=['GET', 'POST'])
@login_required    # this line makes the route requre authentication
def private():
    return Response(response='success', status=200)

    
