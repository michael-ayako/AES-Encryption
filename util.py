import logging
import random
import io

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
def filechk(filename):
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
        temp_key = random.randint(10000,65535)
        print("[%s] - %s\n"%(x,temp_key))
        KEYS.append(temp_key)
    try:
        KEY = int(input())
        return KEYS[KEY]
    except Exception as err:
        logging.error(err)
        exit()

#Converting file to text
def file_converter_enc(BITSMATRIX):
    BIT_TEMP = []
    for x in BITSMATRIX:
        temp = ''
        for y in x:
            for z in y:
                temp += str(z)
        BIT_TEMP.append(temp)
    chars = []
    for x in BIT_TEMP:
        chars.append(chr(int(x,2)))
    with open('msg.enc','w',encoding = 'utf-8') as f:
        for x in chars:
            f.write(x)

def file_converter_dec(BITSMATRIX):
    BIT_TEMP = []
    for x in BITSMATRIX:
        temp = ''
        for y in x:
            for z in y:
                temp += str(z)
        BIT_TEMP.append(temp) 
    chars = []
    for x in BIT_TEMP:
        chars.append(chr(int(x,2)))
    with open('msg.txt','w',encoding = 'utf-8') as f:
        for x in chars:
            f.write(x)
    

#Quitting file
def quit():
    logging.info("Quitting")
    exit()
