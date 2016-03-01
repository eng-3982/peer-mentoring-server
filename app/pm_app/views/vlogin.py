
# File: vlogin.py
# Author: Daniel Douglas, Claire Durand

from pm_app import app
from flask import request, Response
from flask_login import LoginManager, login_user, logout_user, current_user
from flask.ext.bcrypt import Bcrypt
from pm_app.models import User

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
