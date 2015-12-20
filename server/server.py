import sys
import os
from flask import Flask
from flask import request

# Move to the directory that contains the interfacing script to import it
# (I'm actually pretty proud of this line because it means I can call server.py from anywhere)
sys.path.append(os.path.join(os.path.dirname(__file__),'..','peer-mentoring-app-interface'))
import myscript


app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'

@app.route('/data', methods=['POST', 'GET'])
def data():
   # print "Welcome to data"
    if request.method == 'GET':
    #    print "Get method"
        return myscript.data()
    else:
        #print request.form['name']
        print request.form['major']
        new_major = request.form['major']
        #new_name =  request.form['name']
        y = myscript.post(new_major)
        return y 

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
    
