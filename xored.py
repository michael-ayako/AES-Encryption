from util import logging,logger

def encXOR(filename,KEY):
    FILE = open(filename,'r')
    CONTENT = []
    logging.info("Reading file contents...")
    for cont in FILE:
        CONTENT = cont + cont + "\n"
    BITSTORE = []
    for x in CONTENT:
        BITSTORE.append('{0:016b}'.format(int(ord(x))))
    BITXOR = []
    for x in BITSTORE:
        xord_bytes = ''
        for bitx,bity in zip(x,KEY):
            xord_bytes += str(ord(bitx)^ord(bity))
        BITXOR.append(xord_bytes)
    return BITXOR

def decXOR(filename,KEY):
    filename