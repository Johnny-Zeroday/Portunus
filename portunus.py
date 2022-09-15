from itertools import cycle

# Permet de chiffrer/déchiffrer des messages en utilisant un XOR et une clé de chiffrement.

key = 'Clé'
message = "Mon message (pas encore) secret"

def str_xor(s1, s2):
 return "".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(s1,cycle(s2))])

Decoded = str_xor(message, key)
decoded = str_xor(encoded, key)

print ('Encoded:', repr(encoded))
print ('Decoded:', repr(decoded))