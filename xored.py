from util import logging,logger

def encXOR(filename,KEY):
    FILE = open(filename,'r')
    CONTENT = []
    for cont in FILE:
        CONTENT = cont + cont
    BITSTORE = []
    for x in CONTENT:
        for y in x:
            BITSTORE.append('{0:016b}'.format(int(ord(y))))
    BITXOR = []
    for x in BITSTORE:
        xord_bytes = ''
        for bitx,bity in zip(x,KEY):
            xord_bytes += str(ord(bitx)^ord(bity))
        BITXOR.append(xord_bytes)
    return BITXOR

def encXORrounds(BITSTORE,KEY):
    BITXOR = []
    for x in BITSTORE:
        xord_bytes = ''
        for bitx,bity in zip(x,KEY):
            xord_bytes += str(ord(bitx)^ord(bity))
        BITXOR.append(xord_bytes)
    return BITXOR

def decXOR(BITS,KEY):
    BITXOR = []
    for x in BITS:
        xord_bytes = ''
        for bitx,bity in zip(x,KEY):
            xord_bytes += str(ord(bitx)^ord(bity))   
        BITXOR.append(xord_bytes)
    return BITXOR
    