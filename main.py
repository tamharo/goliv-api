from flask import Flask, request, jsonify, render_template
import csv
import os
import re
import json

from spelling import speelingAbbre

app = Flask(__name__)


def formatReg(search):

    formatedReg = search

    for sp in speelingAbbre:
        formatedReg = re.sub(sp[0], sp[1], formatedReg)

    # return search with regex or empty str
    return formatedReg


def getPlace(zone, search):
    reg = formatReg(search)

    # Open CSV file place with all road in France
    file = open('db/' + zone + '.csv')
    roads = csv.reader(file, delimiter=';')

    

    resultSearch = []

    for index, r in roads:
        if re.search(reg, r[1]) and len(resultSearch) < 10:
            resultSearch.append(r)
        if len(resultSearch) == 10:
            break

    return resultSearch

# @app.route('/search', methods=['GET'])
# def api_search():
#     search = getPlace('road', request.args['search'].upper())

#     return search

@app.route('/search', methods=['GET'])
def api_search():
    z = request.args['city'] if request.args['city'] != '' else 'road'
    search = getPlace(z, request.args['search'].upper())
    
    return render_template('index.html', roads=search)

if __name__ == '__main__':
    app.run(debug=True)