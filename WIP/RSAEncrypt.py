# RSA Encryptor -blakedut2
print "Welcome to the RSA Message Encryptor (Integer Only)"
print "Accessing keys.txt..."
s = open('keys.txt', 'r')
v = s.readlines()
n = int(v[0])
e = float(v[1].rstrip())
m = input("Please enter a number to encrypt: ")
c = int(m**e)
print "Your encrypted ciphertext is: ", c
s.close
d = open('ciphertext.txt', 'w')
d.write('%s \n'%c)
