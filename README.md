# INTRODUCTION

This is a programming assignment for a cryptography class I am taking in Fall 2019. I am to emulate the the structure of AES encryption and how it works. You can go through the files that have been used, that have commentary on how everything in has been used

## FILE DESCRIPTION

- EncDec.py
    This is the main file that hosts the main function
- xored.py
    This file hosts the XOR function
- sbox.py 
    This file performs the sbox functionality of the program
- bitshift.py
    This file performs bit circulate shifts on the data being encrypted
- util.py
    This performs basic functions, like creating the randomg key, file creation after encryption and decryption etc.
--- TestPy.txt 
    This is our sample text for encryption
--- msg.enc
    This is our encrypted file 
--- msg.txt
    This is the outfile after the decryption is performed

# HOWTO

1. To use the file you must have your text to be encrypted in the same directory as the EncDec.py file (and just to be clear this includes xored.py, sbox.py, bitshift.py, util.py)

2. The command to Encrypt will be  
    python EncDec.py -e 'filename' 
    This will prompt for you to pick a key between 5 random numbers after which your file will be encrypted.
    NOTE: This only works with Flatfiles
3. The command to Decrypt will be
    python EncDec.py -d 'filename'
    This will prompt you to use the random number selected in step 2
    NOTE: This will only work with the correct key and the 'msg.enc' created in step 2 above 


