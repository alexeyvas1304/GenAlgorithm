import random

def binary(osob):
    c = random.randint(0,len(osob)-1)
    osob[c] = 1 - osob[c]
    return osob 
    