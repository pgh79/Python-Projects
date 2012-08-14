# Blake Dutton
max = input("Number to play to: ")
for i in range(1, max+1):
    if i % 3 == 0 and i % 5 == 0: print "fizzbuzz"
    elif i % 3 == 0: print "fizz"
    elif i % 5 == 0: print "buzz"
    else: print i