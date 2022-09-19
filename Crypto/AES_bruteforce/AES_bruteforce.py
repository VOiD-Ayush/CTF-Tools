import hashlib
from Crypto.Cipher import AES
from base64 import b64decode
import re

enc = "G38zckAufW4B9A6sywz28kzgW8CCx1UWugLUTjKlo/kwV1CVesmr0tPX/JZOW0aik0TlkrcAIZZ/G0BigUtmeg=="

pattern = re.compile('.*-.*-.*-.*')

iv = b64decode(enc)[0:16]
data = b64decode(enc)[16:]

for x in range(0,9999):
	pin = "%04d" % x
	key = hashlib.md5(pin.encode("UTF-8")).digest()[0:16]
	# print(key)
	try:
		cipher = AES.new(key, AES.MODE_CBC, iv)
		clear = cipher.decrypt(data)
		if pattern.match(str(clear)):
			print(clear.decode("UTF-8"))
	except:
		pass
