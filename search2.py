import csv
import re
import vaex
import pandas as pd
import numpy as np


from spelling import speelingAbbre

def formatReg(search):

    formatedReg = search

    for sp in speelingAbbre:
        formatedReg = re.sub(sp[0], sp[1], formatedReg)

    # return search with regex or empty str
    return formatedReg


def getPlace(zone, search):
    reg = formatReg(search)
    dv = vaex.open(r'db/road.csv.hdf5')
    val = dv[dv.rue.str.contains(r"^RUE\s[a-zA-Z]*\sFRANCHEPRE", regex=True)]
    
    return val.rue.tolist()