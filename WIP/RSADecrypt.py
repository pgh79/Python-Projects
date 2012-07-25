#RSA Decryptor -blakedut2
print "Welcome to the RSA Message Decryptor! (Integer Only)"
s = open('keys.txt', 'r')
v = s.readlines()
n = int(v[0])
d = float(v[2].rstrip())
f = open('ciphertext.txt', 'r')
x = f.readlines()
c = int(x[0])
m = int(c**d)
print "Your decrypted message is: ", m