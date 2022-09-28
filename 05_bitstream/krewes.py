'''
TNPG: Henry Bach, Yuki Feng
SoftDev
K05 -- <Title/Topic/Summary... (Aim for concision, brevity, CLARITY. Write to your future self...)>
2022-9-28
time spent: 0.1

DISCO:

QCC:

'''

import random as rng

def readFile() :
    file = open("krewes.txt").read()
    devos = file.split("@@@")
    data = {}
    for devo in devos :
        (key, devo_name, ducky_name) = devo.split("$$$")
        key = (str) key
        data[key].append([devo_name, ducky_name])
    
    print(data)

readFile()