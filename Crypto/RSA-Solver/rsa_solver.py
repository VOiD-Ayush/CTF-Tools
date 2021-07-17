#!/bin/python3

# p and q are generally huge prime mumbers
# n is the multiple of p and q

# if p and q given so n=p*q

# if n is given go to factorialdb.com and find p and q

# totient of n (also called as phi) is (p-1)*(q-1)

# plaintext is the text we want to encrypt

# ciphertext is the encrypted message

# here c =m^e (mod n) 

# m=plaintext , e=given , n = multiple
# in python we use pow(m,e,n)
# plaintext raised to power of e and n is the modulus to pass

# d is the decryption key  and can be found 
# d = e^-1(e phi)
# d = dkey , e= ekey , phi= totient

# from Crypto.Util.number import inverse
# d = inverse(e,phi) 

# m = c^d (mod n)
# in python we use pow(c,d,n)

#========================================

#!/bin/python3

from Crypto.Util.number import inverse

n = <int>
# Replace int with the value of n

e = <int>
# Replace int with the value of e

ct = <int> 
# Replace int with the value of cipher-text

p = <int>
q = <int>
# Replace int with the value of p and q
# p and q if not given , can be found using http://factordb.com/index.php


phi = (p-1)*(q-1)
# Calculating phi
print('phi is',phi)

d = inverse(e,phi)
# Calculating d (decryption-key)
print('d is',d)

pt=pow(ct,d,n)
# Getting the plaintext
print('plain-text is ',pt)

print("plaintext's hex :",hex(pt)[2:-1])
print("Decrypt it to get the plaintext !!")
h=hex(pt)[2:-1]
