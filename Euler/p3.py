from prime import *
n = 600851475143
factn = factors(n)
primefact = []
for n in factn:
    if isPrime(n) == True:
        primefact.append(n)
primefact.sort()
print primefact[-1]
