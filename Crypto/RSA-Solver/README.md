# RSA-soler

> Install Crypto.Util.number to excute the script

p and q are generally huge prime mumbers
n is the multiple of p and q

If p and q given --> so n=p*q

If n is given go to [factorialdb.com](http://factordb.com/index.php) and find p and q

Totient of n (also called as phi) is (p-1)*(q-1)

Plaintext is the text we want to encrypt

Ciphertext is the encrypted message

Here, c =m^e (mod n) 
```python
m=plaintext , e=given , n = multiple
in python we use pow(m,e,n)
plaintext raised to power of e and n is the modulus to pass
```
```python
d is the decryption key  and can be found 
d = e^-1(e phi)
d = dkey , e= ekey , phi= totient
```
```python
from Crypto.Util.number import inverse
d = inverse(e,phi) 

m = c^d (mod n)
in python we use pow(c,d,n)
```
