#!/usr/bin/env python

# File: __init__.py
# Author: Daniel Douglas, Claire Durand

from flask import Flask

# Create the application
#
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
    

import pm_app.views
import pm_app.view.vlogin
