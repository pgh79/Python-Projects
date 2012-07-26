def isPrime(n):
    for m in range(2, int(n**0.5)+1):
        if n % m == 0:
            return False
    return True

print "Welcome to PrimeFinder!"
start = input("Enter a start number: ")
end = input("Enter an end number: ")
for a in range(start, end):
    if isPrime(a):
        print a
