import csv
import re
import vaex
import pandas as pd
import numpy as np

import time


from spelling import speelingAbbre

def formatReg(search):

    formatedReg = search

    for sp in speelingAbbre:
        formatedReg = re.sub(sp[0], sp[1], formatedReg)

    # return search with regex or empty str
    return formatedReg


def getPlace(search):
    start_time = time.time()
    reg = formatReg(search)
    print("--- %s seconds format reg ---" % (time.time() - start_time))
    dv = vaex.open(r'db/road.csv.hdf5')
    print("--- %s seconds open file ---" % (time.time() - start_time))
    val = dv[dv.dept == "54" and dv.rue.str.contains("RUE DE FRANCHEPRE", regex=True)]
    print("--- %s seconds search into file ---" % (time.time() - start_time))
    result = val.rue.tolist()
    #print(val)
    print("--- %s seconds convert to list ---" % (time.time() - start_time))
    
    
    
    return val.rue.tolist()

getPlace('RUE DE FRANCHE')

#python3 search3.py