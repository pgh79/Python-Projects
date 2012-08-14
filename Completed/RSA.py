#RSA Generation Classes
import random
import fractions
import sys
class RSA:
    def __init__(self):
        self.n = 0
        self.e = 0
        self.d = 0
        self.v = False
    def isPrime(self, n):
        for m in range(2, int(n**0.5)+1):
            if n % m == 0:
                return False
        return True
    def generate(self):
        s = open('keys.txt', 'w')
        p = random.randint(5, 20)
        while self.isPrime(p)!=True:
            p = random.randint(5, 20)
        q = random.randint(5, 20)
        while self.isPrime(q)!=True:
            q = random.randint(5, 20)
        self.n = p*q #n is the modulus for the public and private keys
        #Calculate the Euler Totient of n
        x = (p-1)*(q-1)
        #Generate a random coprime e for x
        #e is the public key
        self.e = random.randint(1, x)
        while fractions.gcd(self.e, x)!=1:
            self.e = random.randint(1, x)
        #Create the private key d
        self.d = self.e ** -1
        print "Your PUBLIC key is: (",self.n,", ",self.e,")"
        print "Your PRIVATE key is: (",self.n,", ",self.d,")"
        print "A file in the same directory as this has created a file storing your keys."
        print "This file is called keys.txt and should be in the same directory as the \nencryption and decryption scripts"
        nx = str(self.n)
        ex = str(self.e)
        dx = str(self.d)
        s.write('%s \n'%self.n)
        s.write('%s \n'%self.e)
        s.write('%s \n'%self.d)
        s.close()
        self.interface()
    def imp(self):
        self.s = open('keys.txt', 'r+')
        v = self.s.readlines()
        self.n = int(v[0])
        self.e = int(v[1])
        self.d = float(v[2])
    def encrypt(self):
        m = input("Please enter a number to encrypt: ")
        c = int(m**self.e)
        print "Your encrypted ciphertext is: ",c
        print "Your ciphertext has also been saved to ciphertext.txt"
        f = open('ciphertext.txt', 'w')
        f.write('%s \n'%c)
        f.close()
        self.interface()
    def decrypt(self):
        f = open('ciphertext.txt', 'r')
        b = f.readlines()
        c = int(b[0])
        m = int(c**self.d)
        print "Your decrypted ciphertext is: ",m
        f.close()
        self.interface()
    def interface(self):
        c = raw_input("Would you like to Generate, Encrypt Decrypt or Quit? ")
        if c == "Generate":
            self.generate()
            self.v = True
        elif c == "Encrypt":
            if self.v == True:
                self.encrypt()
            else:
                self.imp()
                self.encrypt()
        elif c == "Decrypt":
            if self.v == True:
                self.decrypt()
            else:
                self.imp()
                self.decrypt()
        elif c == "Quit":
            quit()
        else:
            print "You did not enter a valid option."
            self.interface()
rsa = RSA()
rsa.interface()