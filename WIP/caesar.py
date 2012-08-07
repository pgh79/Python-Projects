# Blake Dutton
import sys
import string
#Define important Var's
global key
crypt = Encryption()
cipher = ""
# NB: p is plaintext and c is ciphertext
class Encryption:
    def __init__(self):
        pass
    def encrypt(self, p):
        if p.isupper():
            pint = string.uppercase.index(p)
            c = (pint+key)%26
            cstr = string.uppercase[c]
            return cstr
        elif p.isalpha():
            pint = string.lowercase.index(p)
            c = (pint+key)%26
            cstr = string.lowercase[c]
            return cstr
        else:
            return p
if (len(sys.argv) < 2):
    print "No key was entered, TERMINATING!"
    quit()
elif sys.argv[1] < 1:
    print "The key entered was not a positive integer, TERMINATING!"
    quit()
else:
    key = int(sys.argv[1])
    plain = raw_input("Enter a string to encrypt: ")
    for char in plain:
        char = crypt.encrypt(char)
        cipher += char
    print cipher