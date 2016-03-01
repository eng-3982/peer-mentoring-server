# File: models.py
# Author: Daniel Douglas, Claire Durand

import sys, os

# Move to the directory that contains the interfacing script to import it
# (I'm actually pretty proud of this line because it means I can call database from anywhere)
#sys.path.append(os.path.join(os.path.dirname(__file__),'..','app_interface'))
from pm_app.interface import database

from flask_login import UserMixin

# Define User class. User inherits from UserMixin class
# which we will "overload" (C++ term)
#
class User(UserMixin):
    # Import user data
    #
    user_database = database.data('users')

    # Initialize class parameters
    #
    def __init__(self, username, password):
        self.id = username
        self.password = password

    # Define a classmethod for easy repeatability
    #
    @classmethod
    def get(cls, id):
        return cls.user_database.get(id)
