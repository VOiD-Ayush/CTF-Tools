# Pip install gmpy2 for executing this script
import gmpy2


n = <int>
# replace <int> with the value of n

n=hex(n)

e= <int>
# replace <int> with the value of e

cipher= <int>
# replace <int> with the value of cipher text given 

 
# Let the magic begin
with gmpy2.local_context(gmpy2.context(), precision=800) as ctx:
	ctx.precision += 800
	root = gmpy2.cbrt(cipher)

try:
	print(str('%x' % + int(root)).decode('hex'))

except AttributeError:
	print(bytes.fromhex(str('%x' % + int(root))).decode('utf-8'))

# Get you get the plain-text here 