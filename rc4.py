#!/usr/bin/python
# PURPOSE : Implementing RC4
# Author  : Tushar Sharma

def rc4(msg, key):
    #Initialization
    S = []
    for i in xrange(0, 256):
        S.append(i)

    #test
    print S, '\n'

    j = 0
    for i in xrange(0, 256):
        j = (j + S[i] + ord(key[i % len(key)])) % 256
        #Swapping
        S[i] = S[i] ^ S[j]
        S[j] = S[i] ^ S[j]
        S[i] = S[i] ^ S[j]

    #test 
    print S, '\n'

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
 

msg = raw_input('Enter plaintext > ')
key = raw_input('Enter key between 1 and 256 bytes > ')
M = []

M = rc4(msg, key)
print 'Cipher is ', M

foo = []
for e in M:
    foo.append(chr(e))

#print foo

M = rc4(foo, key)

print 'Message is'
for e in M:
    print chr(e),
