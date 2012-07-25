#RSA Decryptor -blakedut2
print "Welcome to the RSA Message Decryptor! (Integer Only)"
n = input("Please enter the first block of your private key: ")
d = input("Please enter the second block of your private key: ")
c = input("Please enter the ciphertext to decrypt: ")
m = c**d
print "Your decrypted message is: ", m