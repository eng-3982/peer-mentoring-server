# File: vquery.py
# Author: Daniel Douglas, Claire Durand

from pm_app import app
from flask_login import login_required
from pm_app.interface import database
from flask import request, Response

# Data query and search operations
@app.route('/query/', methods=['GET'])
@login_required
def query():
    
    
