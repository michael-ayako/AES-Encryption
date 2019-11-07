#Getting general Imports
import os
import sys
import argparse
from tqdm import tqdm

import time
import numpy as np
from util import logging,logger,filechk,create_key,file_converter_enc,file_converter_dec
from xored import encXOR, decXOR, encXORrounds
from bitshift import SHIFTLEFT, SHIFTRIGHT
from sbox import sbox_enc,sbox_dec,sbox_dec_rounds

#Encryption
def enc(filename):
    KEY = create_key()
    print('Share this Key %s with the message reciever'%(KEY))
    KEY = '{0:016b}'.format(int(hex(KEY),16))
    logging.info("Key created")
    logging.info("Encryption has started...")
    BITXOR = encXOR(filename,KEY)
    BITSHIFT = SHIFTLEFT(BITXOR)
    BITSBOX = sbox_enc(BITSHIFT)
    BITS = BITSBOX
    for x in tqdm(range(16)):
        BITS = encXORrounds(BITS,KEY)
        BITS = SHIFTLEFT(BITXOR)
        BITS = sbox_enc(BITSHIFT)
    file_converter_enc(BITS)

#Decrypting files
def dec(filename):
    KEY = int(input("Input the key shared to you\n"))
    KEY = '{0:016b}'.format(int(hex(KEY),16))
    logging.info("Key recieved")
    logging.info("Decryption has started...")
    INV_BITSBOX = sbox_dec(filename)
    BITSHIFT = SHIFTRIGHT(INV_BITSBOX)
    BITXNOR = decXOR(BITSHIFT,KEY)
    BITS = BITXNOR
    #Using
    for x in tqdm(range(16)):
        BITS =  sbox_dec_rounds(BITS)
        BITS = SHIFTRIGHT(INV_BITSBOX)
        BITS = decXOR(BITSHIFT,KEY)
    file_converter_dec(BITS)


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




