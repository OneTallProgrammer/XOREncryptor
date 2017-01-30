# There is a big flaw with the implementation of checking whether a file is encrypted
# Instead, a stamp is going to be pinned to the end of a file when it is encrypted and removed when it is
# deencrypted

# The stamp will be placed in settings.py




from settings import *

def createLogFile():
    try:
        file = open(passkeyLogTitle, "x")
        file.close
    except FileExistsError:
        pass

# encrypts a text file using XOR encryption
def xorEncrypt(filename, passkey):
    # read in data from file
    file = open(filename, "r")
    data = file.read();
    file.close()

    # make data into a list for easily accessed characters
    data = list(data)

    # loop through the characters in the data list and XOR against the letters in the passkey
    passkeyCounter = 0 # iterates through passkey characters
    for index in range(len(data)):
        # get ordinal value of characters, XOR them together, and turn the new value back into a character
        data[index] = chr(ord(data[index]) ^ ord(passkey[passkeyCounter]))
        passkeyCounter += 1
        if passkeyCounter == len(passkey):
            passkeyCounter = 0

    # join encrypted characters and write to file
    file = open(filename, "w")
    file.write("".join(data))
    file.close()

def reencrypt(filename, currentKey, newKey):
    xorEncrypt(filename, currentKey)
    xorEncrypt(filename, newKey)

def isEncrypted(filename):
    global delimiter
    encrypted = False

    try:
        with open(passkeyLogTitle, "r") as passkeyLog:
            for line in passkeyLog:
                data = line.split(delimiter)
                if data[0] == filename:
                    encrypted = True
                    break
    except FileNotFoundError:
        pass

    return encrypted

def addPasskeyEntry(filename, passkey):
    file = open(passkeyLogTitle, "a")
    file.writelines(filename + delimiter + passkey + "\n")
    file.close()

def remPasskeyEntry(filename):
    file = open(passkeyLogTitle, "r+")
    data = file.readlines()
    file.seek(0)

    # checks for the argument string in passkey.txt and overwrites it if found
    for line in data:                             # extract pair sets as a string
        pair = line.split(delimiter)              # parse each message and passkey pair
        if filename != pair[0]:                   # if the argument filename is contained in file
            file.write(line)                      # overwrite it
    file.truncate()                               # truncate any extra characters from the file
    file.close()

def extractPairFromFile(filename):
    file = open(passkeyLogTitle, "r")
    data = file.readlines()

    # loops through lines in passkey.txt until it finds a match for the argument filename
    for line in data:
        pair = line.split(delimiter)        # extracts the filename and passkey from passkey.txt
        if filename == pair[0]:             # if argument filename is the first member of the extracted pair
            pair[1] = pair[1].strip('\n')   # strip of newline characters
            return pair
    return None                             # returns None if argument file is not in passkey.txt

def encryptFile(filename, passkey):
    if isEncrypted(filename):
        passkeyEntry = extractPairFromFile(filename)
        if passkey == passkeyEntry[1]:                      # user wants to decrypt file
            xorEncrypt(filename, passkey)
            remPasskeyEntry(filename)
        else:                                               # user want to reencrypt with a new passkey
            reencrypt(filename, passkeyEntry[1], passkey)
            remPasskeyEntry(passkeyEntry[0])
            addPasskeyEntry(filename, passkey)

    else:
        xorEncrypt(filename, passkey)                       # user wants to encrypt unencrypted file
        addPasskeyEntry(filename, passkey)