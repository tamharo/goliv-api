from flask import Flask, request

from search3 import getPlace
from sorter import sorter


import time

app = Flask(__name__)

# start_time2 = time.time()
# print("--- %s seconds before load road ---" % (time.time() - start_time2))
# dv = vaex.open(r'db/road.csv.hdf5')
# print("--- %s seconds after load road ---" % (time.time() - start_time2))

@app.route('/sorter', methods=['GET'])
def api_sorter():
    return sorter()

@app.route('/search', methods=['GET'])
def api_search():
    return ""

@app.route('/', methods=['GET'])
def say_hello():
    return "Goliv api v.1.1.0 by Manhamprod"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)