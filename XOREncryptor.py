

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

def isEncrypted(filename, delimiter):
    encrypted = False

    try:
        with open("passkey.txt", "r") as keyLog:
            for line in keyLog:
                data = line.split(delimiter)
                if data[0] == filename:
                    encrypted = True
                    break
    except FileNotFoundError:
        pass

    return encrypted

