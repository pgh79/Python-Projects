def isPrime(n):
    for m in range(2, int(n**0.5)+1):
        if n % m == 0:
            return False
    return True
p = input("Please enter a prime number: ")
if not isPrime(p):
    print p,"is not a prime number."
    quit()
m = 2**p - 1
s = 4
for i in range(0, p - 2):
    s = ((s * s) - 2) % m
if s == 0:
    print m,"is a Mersenne Prime!"
else:
    print m,"is not a Mersenne Prime."