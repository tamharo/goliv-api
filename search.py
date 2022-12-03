import csv
import re

from spelling import speelingAbbre

import time;


def formatReg(search):

    formatedReg = search

    for sp in speelingAbbre:
        formatedReg = re.sub(sp[0], sp[1], formatedReg)

    # return search with regex or empty str
    return formatedReg


def getPlace(zone, search):
    start_time = time.time()
    reg = formatReg(search)

    # Open CSV file place with all road in France
    file = open('db/' + zone + '.csv')
    roads = csv.reader(file, delimiter=';')

    resultSearch = []

    for r in roads:
        if re.search(reg, r[1]) and len(resultSearch) < 10:
            resultSearch.append(r)
        if len(resultSearch) == 10:
            break

    print(resultSearch)
    print("--- %s seconds ---" % (time.time() - start_time))

    return "resultSearch"