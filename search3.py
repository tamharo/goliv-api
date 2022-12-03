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


def getPlace(dv, search):
    start_time = time.time()
    reg = formatReg(search)
    
    val = dv[dv.rue.str.contains(search, regex=True)]
    
    return val.rue.tolist()



#python3 search3.py