#RSA Key Gen -blakedut2
import random
import fractions
def isPrime(n):
    for m in range(2, int(n**0.5)+1):
        if n % m == 0:
            return False
    return True
print "Welcome to RSA Key Generator"
p = random.randint(1, 10)
while isPrime(p)!=True:
    p = random.randint(1, 10)
q = random.randint(1, 10)
while isPrime(q)!=True:
    q = random.randint(1, 10)
n = p*q #n is the modulus for the public and private keys
#Calculate the Euler Totient of n
x = (p-1)*(q-1)
#Generate a random coprime e for x
#e is the public key
e = random.randint(1, x)
while fractions.gcd(e, x)!=1:
    e = random.randint(1, x)
#Create the private key d
d = e ** -1
print "Please record these keys."
print "Your PUBLIC key is: (",n,", ",e,")"
print "Your PRIVATE key is: (",n,", ",d,")"
print "A file in the same directory as this has created a file storing your keys."
print "This file is called keys.txt and should be in the same directory as the \nencryption and decryption scripts"
s = open('keys.txt', 'w')
str(n)
str(e)
str(d)
s.write('%s \n'%n)
s.write('%s \n'%e)
s.write('%s \n'%d)