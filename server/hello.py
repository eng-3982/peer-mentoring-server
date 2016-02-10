#!/usr/bin/env python

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'We is in there!'


if __name__ == '__main__':
    app.run()

