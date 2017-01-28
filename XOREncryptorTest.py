# pass a txt file to XOREncrypt once to encrypt it
# pass the same textfile to decrypt it


# Joseph Cauthen
# 1/27/2017

# encrypts a text file using XOR encryption
def XOREncrypt(filename, passkey):
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




filename = "message.txt"
passkey = "passkey"

XOREncrypt(filename, passkey)