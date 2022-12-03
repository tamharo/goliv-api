import vaex
import pandas as pd
import numpy as np
import os

from spelling import speelingAbbre


def convert_to_hdf5():
    
    #dv = vaex.from_csv("db copy/54.csv", convert=True, delimiter=";")

    #directory = 'db2'

    #for filename in os.listdir(directory):
    #    f = os.path.join(directory, filename)

    #    if os.path.isfile(f) and filename != "road.csv" and filename != "road.csv.yaml" and filename != "road.csv.hdf5":
    #        #vaex.from_csv(f, convert=True,delimiter=";", dtype={"dept": "str", "rue": "str"})
    #        ""

    return 'result'




#convert_to_hdf5()

def getPlace():
    dv = vaex.open(r'db copy/54.csv.hdf5')
    #val = dv[dv[1].str.contains("RUE DE FRANCHEP", regex=True)]

    print(dv)
    
    return ""

getPlace()

#python3 hdf5.py