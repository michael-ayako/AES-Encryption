#Getting general Imports
import os
import sys
import argparse
from tqdm import tqdm

import time
import numpy as np
from util import logging,logger,filechk,create_key,file_converter
from xored import encXOR, decXOR
from bitshift import SHIFTLEFT, SHIFTRIGHT

#Encryption
def enc(filename):
    KEY = create_key()
    print('Share this Key %s with the message reciever'%(KEY))
    KEY = '{0:016b}'.format(int(hex(KEY),16))
    logging.info("Key created")
    logging.info("Encryption has started...")
    logging.info("XORING bits")
    BITXOR = tqdm(encXOR(filename,KEY))
    logging.info("Bit circulation shift")
    BITSHIFT = tqdm(SHIFTLEFT(BITXOR))
    file_converter(BITSHIFT)

    

def dec(filename):
    logging.info("Decryption has started")


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

    filechk(args.FileName)    
    if args.enc:
        enc(args.FileName)
    elif args.dec:
        dec(args.FileName)

if __name__ == '__main__':
    Main()




