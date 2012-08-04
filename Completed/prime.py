# Blake Dutton
n = input("Please enter a number: ")
for m in range(2, int(n**0.5)+1):
    if n % m == 0: print "Composite"
print "Prime"