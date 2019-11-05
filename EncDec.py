#Getting general Imports
import os
import sys
import argparse
import logging
from tqdm import tqdm
import random
import time
import numpy as np


def logger():
    #Logging 
    logging.info("Configuring logger...")
    try:
        logging.basicConfig(filename="./chatterbot/logs%s.log"%((__file__).split(".")[0]), format='%(asctime)s %(message)s', filemode='w')   
        logger=logging.getLogger() 
        logger.setLevel(logging.DEBUG)
        logging.info("Logger configured...")
    except Exception as err:
        logging.info("Logging not configured: "+err) 

#Checking if FILE is available
def filechck(filename):
    try:
        FILE = open(filename, 'rb')
        FILE.close()
        logging.info("File %s was found"%(filename))
        return
    except Exception as err:
        logging.error(err)
        exit()

#Creating Key function
def create_key():
    print("Please select a random word from the list and share it to the reciever of this file by typing the numbers adjacent to the word")
    KEYS = []
    for x in range(6):
        temp_key = random.randint(32768,65535)
        print("[%s] - %s"%(x,int(temp_key)))
        KEYS.append(str(temp_key))
    try:
        #KEY = int(input())
        KEY = 4
        return KEYS[KEY]
    except Exception as err:
        logging.error(err)
        exit()

#XORING Function    
def XOR(filename,KEY):
    FILE = open(filename,'r')
    CONTENT = []
    logging.info("Reading file contents...")
    for cont in FILE:
        CONTENT = cont + cont + "\n"
    BITSTORE = ''
    for x in CONTENT:
        BITSTORE += '{0:b}'.format(int(ord(x)))
    BITBREAKDOWN =[]
    counter = 0
    store = ''
    for x in BITSTORE:
        if counter == 16:
            BITBREAKDOWN.append(store)
            counter = 0
            store = ''
        store += x
        counter += 1
    BITXOR = []
    for x in BITBREAKDOWN:
        xord_bytes = ''
        for bitx,bity in zip(x,KEY):
            xord_bytes += str(ord(bitx)^ord(bity))
        BITXOR.append(xord_bytes)
    return BITXOR

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
        param = ''
        for shf in shiftedMatrix:
            for j in shf:
                param += j
        FINALSHIFT.append(str(param).encode('ascii'))
    return FINALSHIFT

        


                  
     

        

#Encryption
def enc(filename):
    KEY = create_key()
    print('Share this Key %s with the message reciever'%(KEY))
    KEY = '{0:b}'.format(int((KEY)))
    logging.info("Key created")
    logging.info("Encryption has started...")
    logging.info("XORING bits")
    BITXOR = tqdm(XOR(filename,KEY))
    logging.info("Bit circulation shift")
    BITSHIFT = tqdm(SHIFTLEFT(BITXOR))
    f = open('outpute', 'wb')
    for x in BITSHIFT:
        f.write(x)
    f.close()
    
        
                
            

    

    

def dec(filename):
    logging.info("Decryption has started")
def quit():
    logging.info("Quitting")
    exit()

#Main function: Creates logging and Option parser 
def Main():
    logger()
    #Option inputs
    parser = argparse.ArgumentParser(description='Lets Encrypt and Decrypt some files', add_help=True)
    group = parser.add_mutually_exclusive_group()
    parser.add_argument("FileName",help='Input a filename')
    group.add_argument('-e','--enc',help='Select this option to encrypt the file',action = 'store_true')
    group.add_argument('-d','--dec',help='Select this option to decrypt the file',action = 'store_true')
    parser.add_argument('-q','--quit',help='Select this option to quit current proccess',action = 'store_true')
    args = parser.parse_args()

    filechck(args.FileName)    
    if args.enc:
        enc(args.FileName)
    elif args.dec:
        dec(args.FileName)

if __name__ == '__main__':
    Main()




