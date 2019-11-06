import numpy as np
from util import logging
#Shifting Bits to the left
def SHIFTLEFT(BITS):
    FINALSHIFT = []
    for x in BITS:
        bitmatrix = []
        for y in x:
            bitmatrix.append(y)
        matrix = np.asarray(bitmatrix).reshape(4,4)
        count = 0
        newbitmatrix= []
        rw1,rw2,rw3,rw4 = [] , [] , [] , []
        for m in matrix:
            if count == 0:
                rw1 = [m[0],m[1],m[2],m[3]]
                newbitmatrix.append(rw1) 
            if count == 1:
                rw2 = [m[1],m[2],m[3],m[0]]
                newbitmatrix.append(rw2) 
            if count == 2:
                rw3 = [m[2],m[3],m[0],m[1]]
                newbitmatrix.append(rw3) 
            if count == 3:
                rw4 = [m[3],m[0],m[1],m[2]]
                newbitmatrix.append(rw4) 
            count += 1
        shiftedMatrix = np.asarray(newbitmatrix).reshape(4,4)
        FINALSHIFT.append(shiftedMatrix)
    BIT_TEMP = []
    for x in FINALSHIFT:
        temp = ''
        for y in x:
            for z in y:
                temp += str(z)
        BIT_TEMP.append(temp)
    return BIT_TEMP

def SHIFTRIGHT(BITS):
    FINALSHIFT = []
    for x in BITS:
        bitmatrix = []
        for y in x:
            bitmatrix.append(y)
        matrix = np.asarray(bitmatrix).reshape(4,4)
        count = 0
        newbitmatrix= []
        rw1,rw2,rw3,rw4 = [] , [] , [] , []
        for m in matrix:
            if count == 0:
                rw1 = [m[0],m[1],m[2],m[3]]
                newbitmatrix.append(rw1) 
            if count == 1:
                rw2 = [m[3],m[0],m[1],m[2]]
                newbitmatrix.append(rw2) 
            if count == 2:
                rw3 = [m[2],m[3],m[0],m[1]]
                newbitmatrix.append(rw3) 
            if count == 3:
                rw4 = [m[1],m[2],m[3],m[0]]
                newbitmatrix.append(rw4) 
            count += 1
        shiftedMatrix = np.asarray(newbitmatrix)
        FINALSHIFT.append(shiftedMatrix)
    BIT_TEMP = []
    for x in FINALSHIFT:
        temp = ''
        for y in x:
            for z in y:
                temp += str(z)
        BIT_TEMP.append(temp)
    return BIT_TEMP