# Blake Dutton
import sys
import string
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
    def decrypt(self, c):
        if c.isupper():
            cint = string.uppercase.index(c)
            c = (cint-key)%26
            pstr = string.uppercase[c]
            return pstr
        elif c.isalpha():
            cint = string.lowercase.index(c)
            c = (cint-key)%26
            pstr = string.lowercase[c]
            return pstr
        else:
            return c
def interface():
    crypt = Encryption()
    choice = raw_input("Do you want to (e)ncrypt, (d)ecrypt or (q)uit? ")
    if choice == "e":
        cipher = ""
        plain = raw_input("Enter a string to encrypt: ")
        for char in plain:
            n = crypt.encrypt(char)
            cipher += n
        print "Your encrypted text is:",cipher
        interface()
    elif choice == "d":
        plain = ""
        cipher = raw_input("Enter a string to decrypt: ")
        for char in cipher:
            n = crypt.decrypt(char)
            plain += n
        print "Your decrypted text is:",plain
        interface()
    elif choice == "q":
        quit()
global key
if (len(sys.argv) < 2):
    print "No key was entered, TERMINATING!"
    quit()
else:
    key = int(sys.argv[1])
    interface()