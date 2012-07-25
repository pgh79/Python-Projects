import random
import sys
import fractions
def isPrime(n):
    for m in range(2, int(n**0.5)+1):
        if n % m == 0:
            return False
    return True

print "Welcome to RSA Encrypt/Decrypt!"
#Enter p prime numbers
p = input ("Please enter var p: ")
#Check if p is prime
if not isPrime(p):
    print "Q was not a prime number, please start again."
    quit()
#Enter q
q = input ("Please enter var q: ")
#Check if q is prime
if not isPrime(q):
    print "P was not a prime number, please start again."
    sys.exit()
x = (p-1)*(q-1)
e = random.randint(1, x)
while fractions.gcd(e, x)!=1:
    e = random.randint(1, x)
d = e ** -1
print "Key's generated."
m = input("Enter a number to encrypt: ")
if isinstance(m, int) == False:
    print "Your entered string was not an integer, please start again."
    sys.exit()
c = m**e
print "Your encrypted number is: ", c
h = input("Enter the same number to decrypt it: ")
b = c**d
print "Your decrypted number is: ", b