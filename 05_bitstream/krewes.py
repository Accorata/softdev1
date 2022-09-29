'''
TNPG: Henry Bach, Yuki Feng
SoftDev
K05 -- <Title/Topic/Summary... (Aim for concision, brevity, CLARITY. Write to your future self...)>
2022-9-28
time spent: 1.0

DISCO:
dictionary[key] allows us to set a value of a dictionary

QCC:
What is the name of this assignment?
'''

import random as rng


def readFile() :
    file = open("krewes.txt").read() # Grabs string from file contents
    devos = file.split("@@@") # We divide the string into a list of devos
    data = {} # We create an empty dictionary
    for devo in devos :
        (key, devo_name, ducky_name) = devo.split("$$$") # We separate each devo into period, name, and ducky's name
        if key not in list(data) : # Add the period if it doesn't already exist
            data[key] = []
        data[key].append([devo_name, ducky_name]) # Add the devo to its period
    return data


def randDevo():
    krewes = readFile()
    key = rng.choice(list(krewes))
    devo = rng.choice(krewes[key])
    return key + ": " + (str)(devo)

print(randDevo())