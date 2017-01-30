# pass a txt file to XOREncrypt once to encrypt it
# pass the same textfile to decrypt it

# Joseph Cauthen
# 1/27/2017

import xorEncryption
import sys
from settings import *

requiredArguments = 3
xorEncryption.createLogFile()

if len(sys.argv) == 1:
    print("GUI to come")
elif len(sys.argv) == requiredArguments:
    filename = sys.argv[1]                         # file name must be the first command line argument
    passkey = sys.argv[2]                          # passkey must be the second command line argument

    xorEncryption.encryptFile(filename, passkey)
else:
    print("Error: Invalid Command: Only two types of commands are accepted\n"
          "python xor.py [filename] [passkey] \n"
          "python xor.py")