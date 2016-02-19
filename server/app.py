import sys
import os
from flask import Flask
from flask import request, make_response

# Move to the directory that contains the interfacing script to import it
# (I'm actually pretty proud of this line because it means I can call server.py from anywhere)
sys.path.append(os.path.join(os.path.dirname(__file__),'..','peer-mentoring-app-interface'))
import database

# Create the application
#
app = Flask(__name__)

# Default URL operations
#
@app.route('/')
def home_page():
    
    # Print simple welcome message
    #
    return 'Welcome to Peer-Mentoring App\n'

@app.route('/data/', methods=['POST', 'GET'])
def data():
    
    # Data directory welcome message
    #
    print "Welcome to data"
    
    # If the request method is GET..
    #
    if request.method == 'GET':
        # Print the key/value data in the database
        #
        return database.data()


    # If the request method is POST
    #
    else:
        # Add the key/values in request to the database
        #
        name = request.form['name']
        passwd = request.form['pass']
        return database.post(name,passwd)

if __name__ == '__main__':
    # Run the app on all interfaces in debug mode
    # debug mode will restart server is this file changes.
    app.run(host='0.0.0.0', port=22000, debug=True)
    
