# Blake Dutton
n = input("Please enter a number: ")
prime = True
for m in range(2, int(n**0.5)+1):
    if n % m == 0:
        prime = False
        print "Composite"
if prime == True:
    print "Prime"
