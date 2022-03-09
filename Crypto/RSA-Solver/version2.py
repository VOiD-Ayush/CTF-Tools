from Crypto.Util.number import inverse,long_to_bytes


n = "change with the int value"

ct = 'cipher text int value'
# check factorialdb
e='value of e'
p = "change with the int value"
q = "change with the int value"

phi = (p-1)*(q-1)

d = inverse(e,phi)

pt = pow(ct,d,n)

print(long_to_bytes(pt))
