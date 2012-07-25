# RSA Encryptor -blakedut2
print "Welcome to the RSA Message Encryptor (Integer Only)"
n = input("Please enter the first block of the recipient's key: ")
e = input("Please enter the second block of the recipient's key: ")
m = input("Please enter a number to encrypt: ")
c = m**e
print "Your encrypted ciphertext is: ", c