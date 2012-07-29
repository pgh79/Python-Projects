#Prime Class -blakedut2
from math import sqrt
def isPrime(n):
    for m in range(2, int(n**0.5)+1):
        if n % m == 0:
            return False
    return True
def factors(n):
    fact = [1, n]
    check = 2
    rootn = sqrt(n)
    while check<rootn:
        if n % check == 0:
            fact.append(check)
            fact.append(n/check)
        check += 1
    if rootn == check:
        fact.append(check)
        fact.sort()
    return fact    
