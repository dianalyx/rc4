#!/usr/bin/python

#Purpose : Implementing RC4

__author__ = "Tushar Sharma"

import sys, getopt, base64

def rc4(msg, key):
    #Initialization
    S = []
    for i in xrange(0, 256):
        S.append(i)

    #testing purpose
    #print S, '\n'

    j = 0
    for i in xrange(0, 256):
        j = (j + S[i] + ord(key[i % len(key)])) % 256
        #Swapping
        S[i] = S[i] ^ S[j]
        S[j] = S[i] ^ S[j]
        S[i] = S[i] ^ S[j]

    #testing purpose 
    #print S, '\n'

    i = 0
    j = 0
    M = []

    for k in xrange(0, len(msg)):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        #Swapping
        S[i] = S[i] ^ S[j]
        S[j] = S[i] ^ S[j]
        S[i] = S[i] ^ S[j]
    
        pr = S[(S[i] + S[j]) % 256]
        M.append(ord(msg[k]) ^ pr)

    return M

def encrypt():
    global M, msg, key

    M = rc4(msg, key)
    foo = ''
    for e in M:
        foo += chr(e)
    encoded = base64.b64encode(foo)
    print 'Cipher in base64 is',encoded
    data = base64.b64decode(encoded)
    bar = []
    for e in data:
        bar.append(ord(e))

def decrypt():
    global M, msg, key
    
    data = base64.b64decode(msg)
    bar = []
    for e in data:
        bar.append(ord(e))

    #print bar

    foo = []
    for e in bar:
       foo.append(chr(e))

    M = rc4(foo, key)

    tmp = ''
    for e in M:
        tmp += chr(e)
    print 'Message is', tmp


def my_error():
    print 'Usage\nrc4.py -e -m <message> -k <key>   or \nrc4.py -d -m <message> -k <key>'
    sys.exit(2)
    
def main(argv):

    mode = 2  #arbitrarily value
    global M, msg, key

    M = []
    msg = ''
    key = ''
    key_received = False
    msg_received = True

    if len(argv) < 1:
        my_error()

    try:
        opts, args = getopt.getopt(argv,"hedm:k:")
    except getopt.GetoptError:
        my_error()

    for opt, arg in opts:
        if opt == '-h':
            my_error()

        elif opt in ("-e"):
            mode = 0

        elif opt in ("-d"):
            mode = 1

        elif opt in ("-m"):
            msg = arg
            msg_received = True  #True

        elif opt in ("-k"):
            key = arg
            key_received = True  #True

    if mode == 0 and msg_received is True and key_received is True:
        encrypt()

    elif mode == 1 and msg_received is True and key_received is True:
        decrypt()

    else:
        my_error()

if __name__ == "__main__":
   main(sys.argv[1:])
