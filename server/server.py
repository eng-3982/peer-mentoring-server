import myscript
from flask import Flask
from flask import request

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
    
