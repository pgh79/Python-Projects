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
n = pq #n is the modulus for the public and private keys
#Calculate the Euler Totient of n
x = (p-1)*(q-1)
#Generate a random coprime e for x
#e is the public key
e = random.randint(1, x)
while fractions.gcd(e, x)!=1:
    e = random.randint(1, x)
#Create the private key d
d = e ** -1
print "Key's generated."
m = input("Enter a number to encrypt: ")
if isinstance(m, int) == False:
    print "Your entered string was not an integer, please start again."
    sys.exit()
#Use the public key e to encrypt message c
#!!!When sending a message to someone else, use THEIR public key
c = m**e
print "Your encrypted number is: ", c
h = input("Enter the same number to decrypt it: ")
#Use YOUR private key d to decrypt the message sent to you which was encrypted with YOUR public key
b = c**d
print "Your decrypted number is: ", b