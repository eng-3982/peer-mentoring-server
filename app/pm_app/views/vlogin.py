# File: vlogin.py
# Author: Daniel Douglas, Claire Durand

from pm_app import app
from flask import request, Response, session, jsonify
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from flask.ext.bcrypt import Bcrypt
from pm_app.models import User
from pm_app.interface import database

# Create the bcrypt object
#
bcrypt = Bcrypt(app)

# Initialize login manager instance
#
login_manager = LoginManager()
login_manager.init_app(app)

@app.after_request
def remove_if_invalid(response):
    if "__invalidate__" in session:
        response.delete_cookie(app.session_cookie_name)
    return response

# Provide method for login manager to load a user
@login_manager.request_loader
def load_user_by_request(request):
    # Look for token in Authorization headers or request
    # arguments
    #
    print 'HEADERS::', request.headers
    token = request.headers.get('Username'),request.headers.get('Password')
    if token[0] is None or token[1] is None:
        token = None
        print 'NO CREDENTIALS PROVIDED'

    # Once we have the token, check for a match
    #
    if token is not None:
        
        username, request_password = token[0],token[1] # ASSUMING A NAIVE TOKEN
        
        # get the user information from class parameters
        #
        user_entry = User.get(username)

        # Create User() object from information
        #        
        if (user_entry is not None):           
            
            user = User(user_entry['name'], user_entry['password'])
            
            # If authentication info is correct, return user instance
            # We also decrypt the database password here
            #
            if bcrypt.check_password_hash(user.password, request_password):
                login_user(user)
                session.permanent = True
                return user

        # If authenticaton fails, return None
        #
        return None

# Method for login manager to authenticate a returning user
@login_manager.user_loader
def load_user(user_id):
    return_user = User.get(user_id)
    user = User(return_user['name'], return_user['password'])
    return user

# Method called when a user is unauthorized
@login_manager.unauthorized_handler
def unauthorized():
    return Response(response='Authentication Failed :(\n')

# Authenticate user operation
@app.route('/login/', methods=['GET', 'POST'])
@login_required    # this line makes the route requre authentication
def login():
    usr = database.user_info(current_user.id)
    usr_json = jsonify(**usr)
    return usr_json

# Logout user
@app.route('/logout/', methods=['POST'])
def logout():
    logout_user()
    session.clear()
    session['__invalidate__'] = True
    return Response(response='Signed Out\n', status=200)
