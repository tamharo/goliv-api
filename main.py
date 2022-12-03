from flask import Flask, request

import json

from search3 import getPlace
from sorter import sorter

import vaex

import time

app = Flask(__name__)

start_time2 = time.time()
print("--- %s seconds before load road ---" % (time.time() - start_time2))
dv = vaex.open(r'db/road.csv.hdf5')
print("--- %s seconds after load road ---" % (time.time() - start_time2))

@app.route('/sorter', methods=['GET'])
def api_sorter():
    return sorter()

@app.route('/search', methods=['GET'])
def api_search():
    start_time = time.time()
    print("--- %s seconds before call to get place ---" % (time.time() - start_time))
    search = getPlace(request.args['city'], dv, request.args['search'].upper())
    print("--- %s seconds after call to get place ---" % (time.time() - start_time))
    return search

@app.route('/', methods=['GET'])
def say_hello():
    return "Hello, world!"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

#127.0.0.1:8080/search?search=rue%20de%20franchepre&city=54