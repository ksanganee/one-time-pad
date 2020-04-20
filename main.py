import random
#Spaces?

ASCIILENGTH = 8

def encrypt(plaintext):
    plaintext = plaintext.upper()
    key = GenerateKey(plaintext)
    x = 0
    outlist = [None] * len(plaintext)
    bitlistcipher = [None] * (ASCIILENGTH-1)
    for letter in plaintext:
        if letter != ' ':
            bitlistletter = list(ASCIIToBits(LetterToASCII(letter)))
            bitlistkey = list(ASCIIToBits(LetterToASCII(key[x])))
            for i in range(0,ASCIILENGTH-1):
                bitlistcipher[i] = XOR(bitlistletter[i],bitlistkey[i])

            bitlistcipher[0] = 1
            bitlistcipher[2] = 1
            char = BitsToLetter(bitlistcipher)
        else:
            char = ' '

        outlist[x] = char
        x = x + 1

    ciphertext = ''
    for j in outlist:
        ciphertext = ciphertext + str(j)

    # for k in range(0,len(key)-1):
    #     print(key[k])
    # print('')
    print(ciphertext)


def decrypt(ciphertext, key):
    pass

def XOR(a,b):
    a = int(a)
    b = int(b)
    if (a and not b) or (not a and b):
        return 1
    else:
        return 0

def LetterToASCII(letter):
    ascii = ord(letter)
    return ascii

def ASCIIToLetter(ASCII):
    letter = chr(ASCII)
    return letter

def ASCIIToBits(ASCII):
    bits = bin(ASCII)
    binarylist = list(bits[2:])
    return binarylist

def BinaryToDenary(binary):
    denary = 0
    for digit in binary:
        denary = denary*2 + int(digit)
    return denary

def BitsToLetter(binarylist):
    bits = ''
    for d in range(0,ASCIILENGTH-1):
        bits = bits + str(binarylist[d])
    number = BinaryToDenary(bits)
    ASCII = chr(number)
    return ASCII


def GenerateKey(plaintext):
    length = len(plaintext)
    templist = list(plaintext)
    for i in range(0,length):
        templist[i] = random.randint(0,100)
        templist[i] = templist[i] % 26
        templist[i] = templist[i] + 65
        templist[i] = ASCIIToLetter(templist[i])
    return templist


encrypt('test')
