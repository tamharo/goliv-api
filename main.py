from flask import Flask, request

import json

from search2 import getPlace
from sorter import sorter

#import time

app = Flask(__name__)

@app.route('/sorter', methods=['GET'])
def api_sorter():
    return sorter()

@app.route('/search', methods=['GET'])
def api_search():
    #start_time = time.time()
    z = request.args['city'] if request.args['city'] != '' else 'road'
    search = getPlace(z, request.args['search'].upper())
    #print("--- %s seconds ---" % (time.time() - start_time))
    return search

@app.route('/', methods=['GET'])
def say_hello():
    return "Hello, world!"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)