#!/usr/bin/env python

# File: __init__.py
# Author: Daniel Douglas, Claire Durand

from flask import Flask

# Create the application
#
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
    

# Load the dependent modules
#
import pm_app.modules
import pm_app.views.vlogin
import pm_app.views.vdata
